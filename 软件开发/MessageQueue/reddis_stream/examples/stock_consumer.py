"""
Stock Quote Consumer

This example demonstrates a consumer that:
- Reads stock quotes from Redis Stream
- Processes real-time market data
- Calculates moving averages and indicators
- Triggers alerts for significant price movements
- Shows how to handle different message types
"""

import sys
import os
import time
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from collections import defaultdict, deque

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.redis_client import RedisClient, get_redis_client, close_redis_client


class StockQuoteConsumer:
    """Consumes and processes stock quotes from Redis Stream."""
    
    def __init__(self, redis_client: RedisClient, consumer_name: str = "stock_consumer"):
        self.redis_client = redis_client
        self.consumer_name = consumer_name
        self.stream_name = "stock_quotes"
        self.group_name = "stock_analyzers"
        
        # Initialize data structures for analysis
        self.price_history = defaultdict(lambda: deque(maxlen=50))  # Last 50 prices per stock
        self.volume_history = defaultdict(lambda: deque(maxlen=20))  # Last 20 volumes per stock
        self.moving_averages = defaultdict(lambda: deque(maxlen=20))  # 20-period moving average
        self.alerts = []
        self.running = False
        
        # Statistics
        self.messages_processed = 0
        self.quotes_processed = 0
        self.events_processed = 0
        
        # Alert thresholds
        self.price_change_threshold = 2.0  # 2% price change
        self.volume_spike_threshold = 3.0   # 3x average volume
        self.volatility_threshold = 5.0     # 5% volatility
        
    def _create_consumer_group(self):
        """Create consumer group for the stream."""
        try:
            self.redis_client.create_consumer_group(self.stream_name, self.group_name)
            print(f"✓ Consumer group '{self.group_name}' created/connected")
        except Exception as e:
            print(f"Error creating consumer group: {e}")
            raise
    
    def _calculate_moving_average(self, symbol: str, period: int = 20) -> Optional[float]:
        """Calculate moving average for a stock."""
        prices = list(self.price_history[symbol])
        if len(prices) >= period:
            return sum(prices[-period:]) / period
        return None
    
    def _calculate_volume_average(self, symbol: str, period: int = 10) -> Optional[float]:
        """Calculate average volume for a stock."""
        volumes = list(self.volume_history[symbol])
        if len(volumes) >= period:
            return sum(volumes[-period:]) / period
        return None
    
    def _detect_price_alert(self, symbol: str, quote: Dict[str, Any]) -> Optional[str]:
        """Detect significant price movements."""
        price_change_percent = abs(quote['change_percent'])
        
        if price_change_percent >= self.price_change_threshold:
            direction = "UP" if quote['change_percent'] > 0 else "DOWN"
            return f"PRICE ALERT: {symbol} moved {direction} {price_change_percent:.2f}% to ${quote['price']:.2f}"
        
        return None
    
    def _detect_volume_alert(self, symbol: str, quote: Dict[str, Any]) -> Optional[str]:
        """Detect unusual volume activity."""
        avg_volume = self._calculate_volume_average(symbol)
        if avg_volume:
            volume_ratio = quote['volume'] / avg_volume
            
            if volume_ratio >= self.volume_spike_threshold:
                return f"VOLUME ALERT: {symbol} volume spike {volume_ratio:.1f}x average ({quote['volume']:,} shares)"
        
        return None
    
    def _detect_volatility_alert(self, symbol: str, quote: Dict[str, Any]) -> Optional[str]:
        """Detect high volatility periods."""
        prices = list(self.price_history[symbol])
        if len(prices) >= 10:
            # Calculate recent volatility (standard deviation of returns)
            returns = []
            for i in range(1, len(prices)):
                if prices[i-1] > 0:
                    returns.append((prices[i] - prices[i-1]) / prices[i-1])
            
            if returns:
                import statistics
                volatility = statistics.stdev(returns) * 100  # Convert to percentage
                
                if volatility >= self.volatility_threshold:
                    return f"VOLATILITY ALERT: {symbol} showing {volatility:.1f}% volatility"
        
        return None
    
    def _process_stock_quote(self, quote: Dict[str, Any]):
        """Process a single stock quote."""
        symbol = quote['symbol']
        
        # Update price history
        self.price_history[symbol].append(quote['price'])
        self.volume_history[symbol].append(quote['volume'])
        
        # Calculate moving average
        ma = self._calculate_moving_average(symbol)
        if ma:
            self.moving_averages[symbol].append(ma)
        
        # Check for alerts
        alerts = []
        
        price_alert = self._detect_price_alert(symbol, quote)
        if price_alert:
            alerts.append(price_alert)
        
        volume_alert = self._detect_volume_alert(symbol, quote)
        if volume_alert:
            alerts.append(volume_alert)
        
        volatility_alert = self._detect_volatility_alert(symbol, quote)
        if volatility_alert:
            alerts.append(volatility_alert)
        
        # Store alerts
        for alert in alerts:
            self.alerts.append({
                'timestamp': quote['timestamp'],
                'datetime': quote['datetime'],
                'symbol': symbol,
                'alert': alert,
                'price': quote['price']
            })
        
        # Print quote summary
        change_symbol = "▲" if quote['change'] >= 0 else "▼"
        ma_info = f" (MA20: ${ma:.2f})" if ma else ""
        
        print(f"[{self.quotes_processed:04d}] {symbol}: ${quote['price']:.2f} "
              f"{change_symbol} {quote['change']:+.2f} ({quote['change_percent']:+.2f}%) "
              f"Vol: {quote['volume']:,}{ma_info}")
        
        # Print alerts
        for alert in alerts:
            print(f"    ⚠️  {alert}")
        
        self.quotes_processed += 1
    
    def _process_market_event(self, event: Dict[str, Any]):
        """Process a market event."""
        print(f"[EVENT] {event['description']}")
        self.events_processed += 1
    
    def _process_message(self, message_id: str, fields: Dict[str, Any]):
        """Process a single message from the stream."""
        try:
            # Determine message type
            if 'symbol' in fields:
                # This is a stock quote
                self._process_stock_quote(fields)
            elif 'type' in fields and fields['type'] in ['market_event', 'sector_event']:
                # This is a market event
                self._process_market_event(fields)
            else:
                # Unknown message type
                print(f"[UNKNOWN] Message {message_id}: {fields}")
            
            self.messages_processed += 1
            
        except Exception as e:
            print(f"Error processing message {message_id}: {e}")
    
    def _print_statistics(self):
        """Print current statistics."""
        print("\n" + "="*60)
        print("CONSUMER STATISTICS")
        print("="*60)
        print(f"Messages processed: {self.messages_processed}")
        print(f"Stock quotes processed: {self.quotes_processed}")
        print(f"Events processed: {self.events_processed}")
        print(f"Alerts generated: {len(self.alerts)}")
        
        if self.price_history:
            print(f"\nStocks being tracked: {len(self.price_history)}")
            for symbol in sorted(self.price_history.keys()):
                prices = list(self.price_history[symbol])
                if prices:
                    current_price = prices[-1]
                    ma = self._calculate_moving_average(symbol)
                    ma_info = f" (MA20: ${ma:.2f})" if ma else ""
                    print(f"  {symbol}: ${current_price:.2f}{ma_info}")
        
        if self.alerts:
            print(f"\nRecent alerts ({min(5, len(self.alerts))}):")
            for alert in self.alerts[-5:]:
                print(f"  [{alert['datetime']}] {alert['alert']}")
        
        print("="*60)
    
    def consume_messages(self, block_time: int = 5000):
        """Consume messages from the Redis Stream."""
        print(f"Starting stock quote consumer: {self.consumer_name}")
        print(f"Stream: {self.stream_name}")
        print(f"Group: {self.group_name}")
        print(f"Block time: {block_time}ms")
        print("-" * 60)
        
        # Create consumer group
        self._create_consumer_group()
        
        self.running = True
        last_stats_time = time.time()
        
        try:
            while self.running:
                # Read messages from the stream
                messages = self.redis_client.read_from_group(
                    self.group_name,
                    self.consumer_name,
                    self.stream_name,
                    count=10,
                    block=block_time
                )
                
                # Process messages
                for stream, message_list in messages:
                    for message_id, fields in message_list:
                        self._process_message(message_id, fields)
                        
                        # Acknowledge the message
                        self.redis_client.acknowledge_message(
                            self.stream_name, 
                            self.group_name, 
                            message_id
                        )
                
                # Print statistics every 30 seconds
                current_time = time.time()
                if current_time - last_stats_time >= 30:
                    self._print_statistics()
                    last_stats_time = current_time
                
        except KeyboardInterrupt:
            print("\nStopping consumer...")
        except Exception as e:
            print(f"Error in consumer: {e}")
        finally:
            self.running = False
            self._print_statistics()
            print("Consumer stopped.")
    
    def stop(self):
        """Stop the consumer."""
        self.running = False


def main():
    """Main function to run the stock quote consumer."""
    print("Stock Quote Consumer")
    print("=" * 50)
    print()
    
    try:
        # Get Redis client
        redis_client = get_redis_client()
        print("✓ Connected to Redis")
        
        # Create consumer
        consumer = StockQuoteConsumer(redis_client, "stock_analyzer_1")
        
        # Start consuming messages
        consumer.consume_messages(block_time=5000)  # 5 second block time
        
    except KeyboardInterrupt:
        print("\nConsumer stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPlease make sure Redis is running and producer is active:")
        print("  redis-server")
        print("  python examples/stock_producer.py")
    finally:
        close_redis_client()


if __name__ == "__main__":
    main() 