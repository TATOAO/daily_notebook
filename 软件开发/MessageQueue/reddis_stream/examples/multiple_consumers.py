"""
Multiple Consumers Example

This example demonstrates:
- Multiple consumers working in the same consumer group
- Load balancing across consumers
- Different consumer types handling different tasks
- Consumer coordination and fault tolerance
"""

import sys
import os
import time
import json
import argparse
from datetime import datetime
from typing import Dict, Any, List

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.redis_client import RedisClient, get_redis_client, close_redis_client


class StockDataConsumer:
    """Base class for stock data consumers."""
    
    def __init__(self, redis_client: RedisClient, consumer_name: str, consumer_type: str):
        self.redis_client = redis_client
        self.consumer_name = consumer_name
        self.consumer_type = consumer_type
        self.stream_name = "stock_quotes"
        self.group_name = "stock_analyzers"
        self.running = False
        self.messages_processed = 0
        
    def _create_consumer_group(self):
        """Create consumer group for the stream."""
        try:
            self.redis_client.create_consumer_group(self.stream_name, self.group_name)
            print(f"✓ Consumer group '{self.group_name}' created/connected")
        except Exception as e:
            print(f"Error creating consumer group: {e}")
            raise
    
    def process_message(self, message_id: str, fields: Dict[str, Any]):
        """Process a single message. Override in subclasses."""
        raise NotImplementedError
    
    def consume_messages(self, block_time: int = 5000):
        """Consume messages from the Redis Stream."""
        print(f"Starting {self.consumer_type} consumer: {self.consumer_name}")
        print(f"Stream: {self.stream_name}")
        print(f"Group: {self.group_name}")
        print("-" * 60)
        
        # Create consumer group
        self._create_consumer_group()
        
        self.running = True
        
        try:
            while self.running:
                # Read messages from the stream
                messages = self.redis_client.read_from_group(
                    self.group_name,
                    self.consumer_name,
                    self.stream_name,
                    count=5,
                    block=block_time
                )
                
                # Process messages
                for stream, message_list in messages:
                    for message_id, fields in message_list:
                        self.process_message(message_id, fields)
                        
                        # Acknowledge the message
                        self.redis_client.acknowledge_message(
                            self.stream_name, 
                            self.group_name, 
                            message_id
                        )
                        
                        self.messages_processed += 1
                
        except KeyboardInterrupt:
            print(f"\nStopping {self.consumer_type} consumer...")
        except Exception as e:
            print(f"Error in {self.consumer_type} consumer: {e}")
        finally:
            self.running = False
            print(f"{self.consumer_type} consumer stopped. Messages processed: {self.messages_processed}")
    
    def stop(self):
        """Stop the consumer."""
        self.running = False


class PriceAlertConsumer(StockDataConsumer):
    """Consumer that focuses on price alerts and significant movements."""
    
    def __init__(self, redis_client: RedisClient, consumer_name: str):
        super().__init__(redis_client, consumer_name, "Price Alert")
        self.price_threshold = 1.5  # 1.5% price change
        self.alerts_generated = 0
    
    def process_message(self, message_id: str, fields: Dict[str, Any]):
        """Process stock quote for price alerts."""
        if 'symbol' not in fields:
            return
        
        symbol = fields['symbol']
        price_change_percent = abs(fields.get('change_percent', 0))
        
        if price_change_percent >= self.price_threshold:
            direction = "UP" if fields['change_percent'] > 0 else "DOWN"
            alert_msg = f"🚨 PRICE ALERT: {symbol} moved {direction} {price_change_percent:.2f}% to ${fields['price']:.2f}"
            print(f"[{self.consumer_name}] {alert_msg}")
            self.alerts_generated += 1
        else:
            # Just log the quote
            change_symbol = "▲" if fields['change'] >= 0 else "▼"
            print(f"[{self.consumer_name}] {symbol}: ${fields['price']:.2f} "
                  f"{change_symbol} {fields['change']:+.2f} ({fields['change_percent']:+.2f}%)")


class VolumeAnalysisConsumer(StockDataConsumer):
    """Consumer that analyzes volume patterns."""
    
    def __init__(self, redis_client: RedisClient, consumer_name: str):
        super().__init__(redis_client, consumer_name, "Volume Analysis")
        self.volume_history = {}
        self.volume_spikes = 0
    
    def process_message(self, message_id: str, fields: Dict[str, Any]):
        """Process stock quote for volume analysis."""
        if 'symbol' not in fields:
            return
        
        symbol = fields['symbol']
        volume = fields.get('volume', 0)
        
        # Track volume history
        if symbol not in self.volume_history:
            self.volume_history[symbol] = []
        
        self.volume_history[symbol].append(volume)
        
        # Keep only last 10 volumes
        if len(self.volume_history[symbol]) > 10:
            self.volume_history[symbol] = self.volume_history[symbol][-10:]
        
        # Analyze volume patterns
        if len(self.volume_history[symbol]) >= 5:
            avg_volume = sum(self.volume_history[symbol][-5:]) / 5
            current_volume = volume
            
            if current_volume > avg_volume * 2:  # 2x average volume
                print(f"[{self.consumer_name}] 📊 VOLUME SPIKE: {symbol} volume {current_volume:,} "
                      f"({current_volume/avg_volume:.1f}x average)")
                self.volume_spikes += 1
            elif current_volume < avg_volume * 0.5:  # 50% of average volume
                print(f"[{self.consumer_name}] 📉 LOW VOLUME: {symbol} volume {current_volume:,} "
                      f"({current_volume/avg_volume:.1f}x average)")
        
        # Log volume info
        print(f"[{self.consumer_name}] {symbol} Volume: {volume:,}")


class MarketEventConsumer(StockDataConsumer):
    """Consumer that processes market events and news."""
    
    def __init__(self, redis_client: RedisClient, consumer_name: str):
        super().__init__(redis_client, consumer_name, "Market Event")
        self.events_processed = 0
        self.sector_events = {}
    
    def process_message(self, message_id: str, fields: Dict[str, Any]):
        """Process market events."""
        if 'type' in fields and fields['type'] in ['market_event', 'sector_event']:
            event_type = fields['type']
            description = fields.get('description', 'Unknown event')
            
            if event_type == 'market_event':
                print(f"[{self.consumer_name}] 🌍 MARKET EVENT: {description}")
            else:
                sector = fields.get('sector', 'Unknown')
                print(f"[{self.consumer_name}] 🏢 SECTOR EVENT ({sector}): {description}")
                
                # Track sector events
                if sector not in self.sector_events:
                    self.sector_events[sector] = 0
                self.sector_events[sector] += 1
            
            self.events_processed += 1
        elif 'symbol' in fields:
            # Log stock quotes briefly
            symbol = fields['symbol']
            change_symbol = "▲" if fields['change'] >= 0 else "▼"
            print(f"[{self.consumer_name}] {symbol}: {change_symbol} {fields['change_percent']:+.2f}%")


class TechnicalAnalysisConsumer(StockDataConsumer):
    """Consumer that performs technical analysis on stock data."""
    
    def __init__(self, redis_client: RedisClient, consumer_name: str):
        super().__init__(redis_client, consumer_name, "Technical Analysis")
        self.price_history = {}
        self.analysis_count = 0
    
    def _calculate_sma(self, prices: List[float], period: int) -> float:
        """Calculate Simple Moving Average."""
        if len(prices) < period:
            return 0
        return sum(prices[-period:]) / period
    
    def _calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """Calculate Relative Strength Index."""
        if len(prices) < period + 1:
            return 50  # Neutral RSI
        
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        if len(gains) < period:
            return 50
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def process_message(self, message_id: str, fields: Dict[str, Any]):
        """Process stock quote for technical analysis."""
        if 'symbol' not in fields:
            return
        
        symbol = fields['symbol']
        price = fields['price']
        
        # Track price history
        if symbol not in self.price_history:
            self.price_history[symbol] = []
        
        self.price_history[symbol].append(price)
        
        # Keep only last 50 prices
        if len(self.price_history[symbol]) > 50:
            self.price_history[symbol] = self.price_history[symbol][-50:]
        
        # Perform technical analysis
        if len(self.price_history[symbol]) >= 20:
            prices = self.price_history[symbol]
            
            # Calculate indicators
            sma_20 = self._calculate_sma(prices, 20)
            sma_10 = self._calculate_sma(prices, 10)
            rsi = self._calculate_rsi(prices, 14)
            
            # Generate signals
            signals = []
            
            if sma_10 > sma_20:
                signals.append("BULLISH")
            elif sma_10 < sma_20:
                signals.append("BEARISH")
            
            if rsi > 70:
                signals.append("OVERBOUGHT")
            elif rsi < 30:
                signals.append("OVERSOLD")
            
            # Log analysis
            signal_str = " | ".join(signals) if signals else "NEUTRAL"
            print(f"[{self.consumer_name}] {symbol} Analysis: SMA10=${sma_10:.2f} SMA20=${sma_20:.2f} "
                  f"RSI={rsi:.1f} Signal: {signal_str}")
            
            self.analysis_count += 1
        else:
            # Just log the price
            print(f"[{self.consumer_name}] {symbol}: ${price:.2f}")


def create_consumer(consumer_type: str, consumer_name: str, redis_client: RedisClient) -> StockDataConsumer:
    """Factory function to create different types of consumers."""
    if consumer_type == "price_alert":
        return PriceAlertConsumer(redis_client, consumer_name)
    elif consumer_type == "volume_analysis":
        return VolumeAnalysisConsumer(redis_client, consumer_name)
    elif consumer_type == "market_event":
        return MarketEventConsumer(redis_client, consumer_name)
    elif consumer_type == "technical_analysis":
        return TechnicalAnalysisConsumer(redis_client, consumer_name)
    else:
        raise ValueError(f"Unknown consumer type: {consumer_type}")


def main():
    """Main function to run multiple consumers."""
    parser = argparse.ArgumentParser(description="Stock Quote Multiple Consumers")
    parser.add_argument("consumer_name", help="Name of this consumer instance")
    parser.add_argument("--type", choices=["price_alert", "volume_analysis", "market_event", "technical_analysis"],
                       default="price_alert", help="Type of consumer")
    parser.add_argument("--block-time", type=int, default=5000, help="Block time in milliseconds")
    
    args = parser.parse_args()
    
    print("Multiple Stock Quote Consumers")
    print("=" * 50)
    print(f"Consumer: {args.consumer_name}")
    print(f"Type: {args.type}")
    print()
    
    try:
        # Get Redis client
        redis_client = get_redis_client()
        print("✓ Connected to Redis")
        
        # Create consumer
        consumer = create_consumer(args.type, args.consumer_name, redis_client)
        
        # Start consuming messages
        consumer.consume_messages(block_time=args.block_time)
        
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