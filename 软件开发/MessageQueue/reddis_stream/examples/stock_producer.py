"""
Stock Quote Producer

This example simulates a real-time stock quote producer that:
- Generates realistic stock price movements
- Publishes quotes to Redis Stream
- Includes price, volume, timestamp, and other market data
- Demonstrates real-time data streaming
"""

import sys
import os
import time
import random
import json
from datetime import datetime, timedelta
from typing import Dict, Any, List

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.redis_client import RedisClient, get_redis_client, close_redis_client


class StockQuoteProducer:
    """Simulates a stock quote producer that generates realistic market data."""
    
    def __init__(self, redis_client: RedisClient):
        self.redis_client = redis_client
        self.stream_name = "stock_quotes"
        self.stocks = self._initialize_stocks()
        self.running = False
        
    def _initialize_stocks(self) -> Dict[str, Dict[str, Any]]:
        """Initialize stock data with realistic starting prices."""
        return {
            'AAPL': {
                'name': 'Apple Inc.',
                'current_price': 150.00,
                'base_volume': 50000000,
                'volatility': 0.02,  # 2% daily volatility
                'sector': 'Technology'
            },
            'GOOGL': {
                'name': 'Alphabet Inc.',
                'current_price': 2800.00,
                'base_volume': 20000000,
                'volatility': 0.025,
                'sector': 'Technology'
            },
            'MSFT': {
                'name': 'Microsoft Corporation',
                'current_price': 300.00,
                'base_volume': 30000000,
                'volatility': 0.018,
                'sector': 'Technology'
            },
            'TSLA': {
                'name': 'Tesla Inc.',
                'current_price': 800.00,
                'base_volume': 40000000,
                'volatility': 0.04,
                'sector': 'Automotive'
            },
            'AMZN': {
                'name': 'Amazon.com Inc.',
                'current_price': 3200.00,
                'base_volume': 25000000,
                'volatility': 0.022,
                'sector': 'E-commerce'
            },
            'NVDA': {
                'name': 'NVIDIA Corporation',
                'current_price': 500.00,
                'base_volume': 35000000,
                'volatility': 0.035,
                'sector': 'Technology'
            },
            'JPM': {
                'name': 'JPMorgan Chase & Co.',
                'current_price': 140.00,
                'base_volume': 15000000,
                'volatility': 0.015,
                'sector': 'Financial'
            },
            'JNJ': {
                'name': 'Johnson & Johnson',
                'current_price': 160.00,
                'base_volume': 10000000,
                'volatility': 0.012,
                'sector': 'Healthcare'
            }
        }
    
    def _generate_price_movement(self, stock_data: Dict[str, Any]) -> float:
        """Generate realistic price movement using random walk with mean reversion."""
        current_price = stock_data['current_price']
        volatility = stock_data['volatility']
        
        # Random walk with small drift
        daily_return = random.gauss(0, volatility / 252)  # Daily volatility
        price_change = current_price * daily_return
        
        # Add some mean reversion (tendency to return to a "fair" price)
        mean_reversion_strength = 0.1
        fair_price = current_price  # In a real system, this would be calculated from fundamentals
        mean_reversion = (fair_price - current_price) * mean_reversion_strength * 0.01
        
        new_price = current_price + price_change + mean_reversion
        
        # Ensure price doesn't go negative
        return max(new_price, 0.01)
    
    def _generate_volume(self, stock_data: Dict[str, Any], price_change: float) -> int:
        """Generate realistic trading volume based on price movement."""
        base_volume = stock_data['base_volume']
        
        # Volume tends to be higher when there's significant price movement
        volume_multiplier = 1.0 + abs(price_change) / stock_data['current_price'] * 10
        
        # Add some randomness
        volume_multiplier *= random.uniform(0.8, 1.2)
        
        # Ensure reasonable volume range
        volume = int(base_volume * volume_multiplier)
        return max(volume, 1000000)  # Minimum 1M shares
    
    def _generate_quote(self, symbol: str, stock_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a complete stock quote."""
        old_price = stock_data['current_price']
        new_price = self._generate_price_movement(stock_data)
        price_change = new_price - old_price
        price_change_percent = (price_change / old_price) * 100
        
        # Update the stock data
        stock_data['current_price'] = new_price
        
        # Generate volume
        volume = self._generate_volume(stock_data, price_change)
        
        # Generate bid/ask spread
        spread_percent = random.uniform(0.01, 0.05)  # 0.01% to 0.05%
        bid_price = new_price * (1 - spread_percent / 2)
        ask_price = new_price * (1 + spread_percent / 2)
        
        # Generate high/low for the day (simplified)
        daily_high = max(new_price, old_price * 1.02)
        daily_low = min(new_price, old_price * 0.98)
        
        quote = {
            'symbol': symbol,
            'name': stock_data['name'],
            'price': round(new_price, 2),
            'change': round(price_change, 2),
            'change_percent': round(price_change_percent, 2),
            'volume': volume,
            'bid': round(bid_price, 2),
            'ask': round(ask_price, 2),
            'high': round(daily_high, 2),
            'low': round(daily_low, 2),
            'sector': stock_data['sector'],
            'timestamp': int(time.time()),
            'datetime': datetime.now().isoformat(),
            'quote_type': 'real_time'
        }
        
        return quote
    
    def _add_market_events(self, quotes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Add market events that affect multiple stocks."""
        events = []
        
        # Market-wide events (affect all stocks)
        if random.random() < 0.1:  # 10% chance of market event
            event_types = [
                'market_open',
                'market_close', 
                'fed_announcement',
                'earnings_season',
                'economic_data_release'
            ]
            event_type = random.choice(event_types)
            
            events.append({
                'type': 'market_event',
                'event': event_type,
                'timestamp': int(time.time()),
                'datetime': datetime.now().isoformat(),
                'description': f'Market event: {event_type}'
            })
        
        # Sector-specific events
        sectors = set(quote['sector'] for quote in quotes)
        for sector in sectors:
            if random.random() < 0.05:  # 5% chance per sector
                sector_events = {
                    'Technology': ['tech_earnings', 'product_launch', 'regulatory_news'],
                    'Financial': ['rate_change', 'banking_news', 'regulatory_announcement'],
                    'Healthcare': ['fda_approval', 'clinical_trial_results', 'drug_news'],
                    'Automotive': ['sales_data', 'ev_adoption', 'supply_chain_news'],
                    'E-commerce': ['holiday_sales', 'logistics_update', 'competition_news']
                }
                
                if sector in sector_events:
                    event = random.choice(sector_events[sector])
                    events.append({
                        'type': 'sector_event',
                        'sector': sector,
                        'event': event,
                        'timestamp': int(time.time()),
                        'datetime': datetime.now().isoformat(),
                        'description': f'{sector} sector event: {event}'
                    })
        
        return events
    
    def publish_quotes(self, interval: float = 1.0):
        """Publish stock quotes to Redis Stream at specified interval."""
        print(f"Starting stock quote producer...")
        print(f"Publishing quotes every {interval} seconds")
        print(f"Stream: {self.stream_name}")
        print(f"Stocks: {', '.join(self.stocks.keys())}")
        print("-" * 60)
        
        self.running = True
        message_count = 0
        
        try:
            while self.running:
                start_time = time.time()
                
                # Generate quotes for all stocks
                quotes = []
                for symbol, stock_data in self.stocks.items():
                    quote = self._generate_quote(symbol, stock_data)
                    quotes.append(quote)
                
                # Add market events
                events = self._add_market_events(quotes)
                
                # Publish quotes to Redis Stream
                for quote in quotes:
                    message_id = self.redis_client.add_to_stream(self.stream_name, quote)
                    message_count += 1
                    
                    # Print quote info
                    change_symbol = "▲" if quote['change'] >= 0 else "▼"
                    print(f"[{message_count:04d}] {quote['symbol']}: ${quote['price']:.2f} "
                          f"{change_symbol} {quote['change']:+.2f} ({quote['change_percent']:+.2f}%) "
                          f"Vol: {quote['volume']:,}")
                
                # Publish market events
                for event in events:
                    message_id = self.redis_client.add_to_stream(self.stream_name, event)
                    print(f"[{message_count:04d}] EVENT: {event['description']}")
                
                # Calculate sleep time to maintain interval
                elapsed = time.time() - start_time
                sleep_time = max(0, interval - elapsed)
                
                if sleep_time > 0:
                    time.sleep(sleep_time)
                
        except KeyboardInterrupt:
            print("\nStopping stock quote producer...")
        except Exception as e:
            print(f"Error in producer: {e}")
        finally:
            self.running = False
            print(f"Producer stopped. Total messages published: {message_count}")
    
    def stop(self):
        """Stop the producer."""
        self.running = False


def main():
    """Main function to run the stock quote producer."""
    print("Stock Quote Producer")
    print("=" * 50)
    print()
    
    try:
        # Get Redis client
        redis_client = get_redis_client()
        print("✓ Connected to Redis")
        
        # Create producer
        producer = StockQuoteProducer(redis_client)
        
        # Start publishing quotes
        producer.publish_quotes(interval=1.0)  # 1 quote per second
        
    except KeyboardInterrupt:
        print("\nProducer stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPlease make sure Redis is running:")
        print("  redis-server")
    finally:
        close_redis_client()


if __name__ == "__main__":
    main() 