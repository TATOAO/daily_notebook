"""
Unit tests for Redis Stream operations.

These tests verify the functionality of the Redis client wrapper
and basic stream operations.
"""

import sys
import os
import time
import pytest
from unittest.mock import Mock, patch

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.redis_client import RedisClient, get_redis_client, close_redis_client


class TestRedisClient:
    """Test cases for RedisClient class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.redis_client = RedisClient(host='localhost', port=6379, db=0)
    
    def teardown_method(self):
        """Clean up after tests."""
        if self.redis_client:
            self.redis_client.close()
    
    def test_connection(self):
        """Test Redis connection."""
        assert self.redis_client.is_connected()
    
    def test_add_to_stream(self):
        """Test adding messages to a stream."""
        stream_name = "test_stream"
        data = {"field1": "value1", "field2": "value2"}
        
        message_id = self.redis_client.add_to_stream(stream_name, data)
        assert message_id is not None
        assert isinstance(message_id, str)
        
        # Clean up
        self.redis_client.client.delete(stream_name)
    
    def test_read_from_stream(self):
        """Test reading messages from a stream."""
        stream_name = "test_read_stream"
        data = {"test_field": "test_value"}
        
        # Add a message
        message_id = self.redis_client.add_to_stream(stream_name, data)
        
        # Read messages
        messages = self.redis_client.read_from_stream(stream_name, start_id='0')
        
        assert len(messages) > 0
        assert stream_name in [stream for stream, _ in messages]
        
        # Verify message content
        for stream, message_list in messages:
            if stream == stream_name:
                assert len(message_list) > 0
                for msg_id, fields in message_list:
                    assert fields['test_field'] == 'test_value'
        
        # Clean up
        self.redis_client.client.delete(stream_name)
    
    def test_consumer_group_operations(self):
        """Test consumer group operations."""
        stream_name = "test_group_stream"
        group_name = "test_group"
        
        # Create consumer group
        self.redis_client.create_consumer_group(stream_name, group_name)
        
        # Add a message
        data = {"test": "data"}
        message_id = self.redis_client.add_to_stream(stream_name, data)
        
        # Read from group
        messages = self.redis_client.read_from_group(
            group_name, "test_consumer", stream_name, count=1
        )
        
        assert len(messages) > 0
        
        # Acknowledge message
        for stream, message_list in messages:
            for msg_id, fields in message_list:
                self.redis_client.acknowledge_message(stream_name, group_name, msg_id)
        
        # Check pending messages
        pending = self.redis_client.get_pending_messages(stream_name, group_name)
        assert pending is not None
        
        # Clean up
        self.redis_client.client.delete(stream_name)
    
    def test_stream_trimming(self):
        """Test stream trimming functionality."""
        stream_name = "test_trim_stream"
        
        # Add multiple messages
        for i in range(10):
            data = {"message_number": str(i)}
            self.redis_client.add_to_stream(stream_name, data)
        
        # Trim to keep only last 3 messages
        removed = self.redis_client.trim_stream(stream_name, maxlen=3)
        assert removed >= 0
        
        # Verify only 3 messages remain
        messages = self.redis_client.read_from_stream(stream_name, start_id='0')
        total_messages = sum(len(message_list) for _, message_list in messages)
        assert total_messages <= 3
        
        # Clean up
        self.redis_client.client.delete(stream_name)


class TestStockQuoteProducer:
    """Test cases for stock quote producer functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.redis_client = RedisClient(host='localhost', port=6379, db=0)
    
    def teardown_method(self):
        """Clean up after tests."""
        if self.redis_client:
            self.redis_client.close()
    
    def test_stock_quote_structure(self):
        """Test that stock quotes have the expected structure."""
        from examples.stock_producer import StockQuoteProducer
        
        producer = StockQuoteProducer(self.redis_client)
        
        # Test stock initialization
        assert 'AAPL' in producer.stocks
        assert 'GOOGL' in producer.stocks
        
        apple_data = producer.stocks['AAPL']
        assert 'name' in apple_data
        assert 'current_price' in apple_data
        assert 'volatility' in apple_data
        assert 'sector' in apple_data
        
        # Test quote generation
        quote = producer._generate_quote('AAPL', apple_data.copy())
        
        required_fields = [
            'symbol', 'name', 'price', 'change', 'change_percent',
            'volume', 'bid', 'ask', 'high', 'low', 'sector',
            'timestamp', 'datetime', 'quote_type'
        ]
        
        for field in required_fields:
            assert field in quote
        
        assert quote['symbol'] == 'AAPL'
        assert quote['price'] > 0
        assert quote['volume'] > 0
        assert quote['bid'] <= quote['ask']
    
    def test_price_movement_generation(self):
        """Test price movement generation."""
        from examples.stock_producer import StockQuoteProducer
        
        producer = StockQuoteProducer(self.redis_client)
        stock_data = producer.stocks['AAPL'].copy()
        original_price = stock_data['current_price']
        
        # Generate multiple price movements
        prices = []
        for _ in range(10):
            new_price = producer._generate_price_movement(stock_data)
            prices.append(new_price)
            stock_data['current_price'] = new_price
        
        # Verify prices are reasonable
        for price in prices:
            assert price > 0
            assert price < original_price * 2  # Shouldn't double in 10 steps
            assert price > original_price * 0.5  # Shouldn't halve in 10 steps
    
    def test_volume_generation(self):
        """Test volume generation."""
        from examples.stock_producer import StockQuoteProducer
        
        producer = StockQuoteProducer(self.redis_client)
        stock_data = producer.stocks['AAPL'].copy()
        
        # Test volume generation
        volume = producer._generate_volume(stock_data, 1.0)  # $1 price change
        
        assert volume > 0
        assert volume >= 1000000  # Minimum volume
        assert volume <= stock_data['base_volume'] * 5  # Reasonable maximum


class TestStockQuoteConsumer:
    """Test cases for stock quote consumer functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.redis_client = RedisClient(host='localhost', port=6379, db=0)
    
    def teardown_method(self):
        """Clean up after tests."""
        if self.redis_client:
            self.redis_client.close()
    
    def test_consumer_initialization(self):
        """Test consumer initialization."""
        from examples.stock_consumer import StockQuoteConsumer
        
        consumer = StockQuoteConsumer(self.redis_client, "test_consumer")
        
        assert consumer.consumer_name == "test_consumer"
        assert consumer.stream_name == "stock_quotes"
        assert consumer.group_name == "stock_analyzers"
        assert consumer.messages_processed == 0
        assert consumer.quotes_processed == 0
        assert consumer.events_processed == 0
    
    def test_moving_average_calculation(self):
        """Test moving average calculation."""
        from examples.stock_consumer import StockQuoteConsumer
        
        consumer = StockQuoteConsumer(self.redis_client, "test_consumer")
        
        # Add some price history
        symbol = "AAPL"
        prices = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        
        for price in prices:
            consumer.price_history[symbol].append(price)
        
        # Test 5-period moving average
        ma5 = consumer._calculate_moving_average(symbol, 5)
        expected_ma5 = sum(prices[-5:]) / 5
        assert abs(ma5 - expected_ma5) < 0.01
        
        # Test 10-period moving average
        ma10 = consumer._calculate_moving_average(symbol, 10)
        expected_ma10 = sum(prices[-10:]) / 10
        assert abs(ma10 - expected_ma10) < 0.01
    
    def test_alert_detection(self):
        """Test alert detection functionality."""
        from examples.stock_consumer import StockQuoteConsumer
        
        consumer = StockQuoteConsumer(self.redis_client, "test_consumer")
        
        # Test price alert
        quote = {
            'symbol': 'AAPL',
            'price': 150.0,
            'change': 3.0,
            'change_percent': 2.1,  # Above 2% threshold
            'volume': 50000000
        }
        
        alert = consumer._detect_price_alert('AAPL', quote)
        assert alert is not None
        assert "PRICE ALERT" in alert
        assert "AAPL" in alert
        
        # Test no alert for small change
        quote['change_percent'] = 1.0  # Below threshold
        alert = consumer._detect_price_alert('AAPL', quote)
        assert alert is None


def test_redis_connection():
    """Test basic Redis connection."""
    try:
        redis_client = get_redis_client()
        assert redis_client.is_connected()
        close_redis_client()
    except Exception as e:
        pytest.skip(f"Redis not available: {e}")


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"]) 