# Redis Streams Message Queue Tutorial

## Introduction

Welcome to this comprehensive tutorial on Redis Streams and message queues! This guide will teach you everything you need to know about building message queues using Redis Streams, with practical examples focused on stock market data processing.

## What is a Message Queue?

A message queue is a communication pattern that enables asynchronous processing between different parts of a system. Think of it like a post office:

- **Producers** (senders) put messages in the queue
- **Consumers** (receivers) pick up and process messages
- Messages are stored temporarily until processed
- Multiple consumers can work in parallel
- If a consumer fails, messages aren't lost

### Why Use Message Queues?

1. **Decoupling**: Producers and consumers don't need to know about each other
2. **Scalability**: Add more consumers to handle increased load
3. **Reliability**: Messages persist even if consumers are down
4. **Asynchronous Processing**: Non-blocking operations
5. **Load Balancing**: Distribute work across multiple workers

## Redis Streams vs Traditional Message Queues

### Traditional Message Queues (RabbitMQ, Apache Kafka)
- **Pros**: Feature-rich, mature, enterprise-ready
- **Cons**: Complex setup, separate infrastructure, higher overhead

### Redis Streams
- **Pros**: Simple, built into Redis, easy to learn, great for real-time data
- **Cons**: Fewer advanced features, limited to Redis ecosystem

**For learning and small to medium applications, Redis Streams is perfect!**

## Core Concepts

### 1. Stream
A stream is like a log file that only grows:
- Messages are appended to the end
- Each message has a unique ID
- Messages are immutable (cannot be modified)
- Messages can be read from any position

### 2. Message ID
- Format: `timestamp-sequence` (e.g., `1640995200000-0`)
- Timestamp is in milliseconds since Unix epoch
- Sequence number handles multiple messages in same millisecond

### 3. Consumer Group
- A group of consumers that share the work
- Each message is delivered to only one consumer in the group
- Provides load balancing and fault tolerance
- Messages can be re-delivered if consumer fails

### 4. Pending Messages
- Messages that have been delivered but not acknowledged
- Can be re-delivered if consumer fails
- Important for reliability

## Basic Operations

### Adding Messages
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Add a message to a stream
message_id = r.xadd('mystream', {
    'field1': 'value1', 
    'field2': 'value2'
})
print(f"Message added with ID: {message_id}")
```

### Reading Messages
```python
# Read all messages from a stream
messages = r.xread({'mystream': '0'})
for stream, message_list in messages:
    for message_id, fields in message_list:
        print(f"ID: {message_id}, Fields: {fields}")
```

### Consumer Groups
```python
# Create a consumer group
try:
    r.xgroup_create('mystream', 'mygroup', '0', mkstream=True)
except redis.exceptions.ResponseError:
    print("Group already exists")

# Read messages as a consumer in a group
messages = r.xreadgroup('mygroup', 'consumer1', {'mystream': '>'})
```

## Stock Market Example

Let's build a complete stock market data processing system:

### Architecture
```
[Stock Data Source] → [Producer] → [Redis Stream] → [Consumers]
                                                      ├── [Price Alert Consumer]
                                                      ├── [Volume Analysis Consumer]
                                                      ├── [Technical Analysis Consumer]
                                                      └── [Market Event Consumer]
```

### 1. Stock Quote Producer
The producer simulates real-time stock data:

```python
class StockQuoteProducer:
    def __init__(self, redis_client):
        self.redis_client = redis_client
        self.stream_name = "stock_quotes"
        self.stocks = self._initialize_stocks()
    
    def _generate_quote(self, symbol, stock_data):
        # Generate realistic price movement
        new_price = self._generate_price_movement(stock_data)
        volume = self._generate_volume(stock_data, price_change)
        
        quote = {
            'symbol': symbol,
            'price': new_price,
            'volume': volume,
            'timestamp': int(time.time()),
            'datetime': datetime.now().isoformat()
        }
        
        return quote
    
    def publish_quotes(self, interval=1.0):
        while self.running:
            for symbol, stock_data in self.stocks.items():
                quote = self._generate_quote(symbol, stock_data)
                self.redis_client.add_to_stream(self.stream_name, quote)
            time.sleep(interval)
```

### 2. Stock Quote Consumer
The consumer processes incoming stock data:

```python
class StockQuoteConsumer:
    def __init__(self, redis_client, consumer_name):
        self.redis_client = redis_client
        self.consumer_name = consumer_name
        self.stream_name = "stock_quotes"
        self.group_name = "stock_analyzers"
        self.price_history = defaultdict(lambda: deque(maxlen=50))
    
    def _detect_price_alert(self, symbol, quote):
        price_change_percent = abs(quote['change_percent'])
        if price_change_percent >= 2.0:  # 2% threshold
            return f"PRICE ALERT: {symbol} moved {price_change_percent:.2f}%"
        return None
    
    def consume_messages(self):
        while self.running:
            messages = self.redis_client.read_from_group(
                self.group_name, 
                self.consumer_name, 
                self.stream_name
            )
            
            for stream, message_list in messages:
                for message_id, fields in message_list:
                    self._process_message(message_id, fields)
                    self.redis_client.acknowledge_message(
                        self.stream_name, 
                        self.group_name, 
                        message_id
                    )
```

### 3. Multiple Consumers
Different consumers handle different tasks:

```python
# Price Alert Consumer
class PriceAlertConsumer(StockDataConsumer):
    def process_message(self, message_id, fields):
        if abs(fields['change_percent']) >= 1.5:
            print(f"🚨 PRICE ALERT: {fields['symbol']}")

# Volume Analysis Consumer  
class VolumeAnalysisConsumer(StockDataConsumer):
    def process_message(self, message_id, fields):
        # Analyze volume patterns
        pass

# Technical Analysis Consumer
class TechnicalAnalysisConsumer(StockDataConsumer):
    def process_message(self, message_id, fields):
        # Calculate moving averages, RSI, etc.
        pass
```

## Advanced Features

### 1. Message Acknowledgment
Always acknowledge processed messages to prevent re-delivery:

```python
# Acknowledge a message
r.xack('mystream', 'mygroup', message_id)
```

### 2. Pending Messages
Check for unacknowledged messages:

```python
# Check pending messages
pending = r.xpending('mystream', 'mygroup')
print(f"Pending messages: {pending}")
```

### 3. Stream Trimming
Keep streams from growing indefinitely:

```python
# Keep only last 1000 messages
r.xtrim('mystream', maxlen=1000, approximate=True)
```

### 4. Blocking Reads
Wait for new messages:

```python
# Wait for new messages (block for 5 seconds)
messages = r.xread({'mystream': '$'}, block=5000)
```

## Running the Examples

### 1. Start Redis
```bash
redis-server
```

### 2. Install Dependencies
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install redis
```

### 3. Run Basic Example
```bash
python examples/basic_stream.py
```

### 4. Run Stock Market Example
```bash
# Terminal 1: Start producer
python examples/stock_producer.py

# Terminal 2: Start consumer
python examples/stock_consumer.py
```

### 5. Run Multiple Consumers
```bash
# Terminal 1: Start producer
python examples/stock_producer.py

# Terminal 2: Start price alert consumer
python examples/multiple_consumers.py price_alert_consumer --type price_alert

# Terminal 3: Start volume analysis consumer
python examples/multiple_consumers.py volume_consumer --type volume_analysis

# Terminal 4: Start technical analysis consumer
python examples/multiple_consumers.py tech_consumer --type technical_analysis
```

## Best Practices

### 1. Error Handling
Always handle Redis connection errors:

```python
try:
    redis_client = get_redis_client()
    # Your code here
except redis.ConnectionError as e:
    print(f"Redis connection failed: {e}")
    # Handle reconnection
```

### 2. Message Acknowledgment
Always acknowledge processed messages:

```python
try:
    # Process message
    process_message(fields)
    # Acknowledge only after successful processing
    redis_client.acknowledge_message(stream_name, group_name, message_id)
except Exception as e:
    # Don't acknowledge if processing failed
    print(f"Processing failed: {e}")
```

### 3. Consumer Groups
Use consumer groups for reliability:

```python
# Create consumer group
redis_client.create_consumer_group(stream_name, group_name)

# Read from group
messages = redis_client.read_from_group(group_name, consumer_name, stream_name)
```

### 4. Stream Trimming
Regularly trim old messages:

```python
# Trim streams periodically
redis_client.trim_stream(stream_name, maxlen=1000)
```

### 5. Monitoring
Monitor your message queue:

```python
# Check pending messages
pending = redis_client.get_pending_messages(stream_name, group_name)
if pending['pending'] > 100:
    print("Warning: High number of pending messages")
```

## Real-World Applications

### 1. Stock Trading Platform
- Real-time price feeds
- Order processing
- Risk management
- Portfolio updates

### 2. E-commerce
- Order processing
- Inventory updates
- Payment processing
- Email notifications

### 3. IoT Data Processing
- Sensor data collection
- Device monitoring
- Alert generation
- Data analytics

### 4. Social Media
- User activity feeds
- Content moderation
- Notification delivery
- Analytics processing

### 5. Log Processing
- Centralized logging
- Error tracking
- Performance monitoring
- Security analysis

## Integration with Your Stock Website

Here's how you can integrate this with your stock website:

### 1. WebSocket Integration
```python
import asyncio
import websockets
import json

async def stock_websocket_handler(websocket, path):
    # Subscribe to stock quotes
    redis_client = get_redis_client()
    
    while True:
        # Read latest stock quotes
        messages = redis_client.read_from_stream("stock_quotes", start_id='$')
        
        for stream, message_list in messages:
            for message_id, fields in message_list:
                # Send to connected clients
                await websocket.send(json.dumps(fields))
        
        await asyncio.sleep(1)

# Start WebSocket server
start_server = websockets.serve(stock_websocket_handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
```

### 2. REST API Integration
```python
from flask import Flask, jsonify
from utils.redis_client import get_redis_client

app = Flask(__name__)

@app.route('/api/stocks/<symbol>')
def get_stock_quote(symbol):
    redis_client = get_redis_client()
    
    # Get latest quote for symbol
    messages = redis_client.read_from_stream("stock_quotes", start_id='$')
    
    for stream, message_list in messages:
        for message_id, fields in message_list:
            if fields.get('symbol') == symbol:
                return jsonify(fields)
    
    return jsonify({'error': 'Stock not found'}), 404
```

### 3. Database Integration
```python
import sqlite3

class StockDataProcessor:
    def __init__(self, redis_client, db_path):
        self.redis_client = redis_client
        self.db_path = db_path
    
    def process_and_store(self, quote):
        # Store in database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO stock_quotes (symbol, price, volume, timestamp)
            VALUES (?, ?, ?, ?)
        """, (quote['symbol'], quote['price'], quote['volume'], quote['timestamp']))
        
        conn.commit()
        conn.close()
```

## Testing

Run the unit tests to verify everything works:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_streams.py::TestRedisClient::test_connection -v
```

## Troubleshooting

### Common Issues

1. **Redis Connection Failed**
   - Make sure Redis is running: `redis-server`
   - Check Redis is listening on correct port: `redis-cli ping`

2. **Consumer Not Receiving Messages**
   - Check consumer group exists
   - Verify message acknowledgment
   - Check for pending messages

3. **High Memory Usage**
   - Trim old messages regularly
   - Monitor stream length
   - Use appropriate maxlen settings

4. **Messages Not Being Processed**
   - Check consumer is running
   - Verify consumer group configuration
   - Look for error logs

### Debugging Commands

```bash
# Check Redis info
redis-cli info

# Monitor Redis commands
redis-cli monitor

# Check stream info
redis-cli xinfo stream stock_quotes

# Check consumer group info
redis-cli xinfo groups stock_quotes
```

## Next Steps

1. **Run the Examples**: Start with basic_stream.py to understand fundamentals
2. **Modify for Your Needs**: Adapt the stock examples for your specific use case
3. **Add Error Handling**: Implement robust error handling and monitoring
4. **Scale Up**: Add more consumers and producers as needed
5. **Integrate**: Connect to your stock website or application

## Resources

- [Redis Streams Documentation](https://redis.io/docs/data-types/streams/)
- [Redis Python Client](https://redis-py.readthedocs.io/)
- [Message Queue Patterns](https://martinfowler.com/articles/microservices.html#MessageQueues)
- [Redis Commands Reference](https://redis.io/commands/)

## Conclusion

Redis Streams provide a powerful and simple way to build message queues. They're perfect for learning message queue concepts and for real-time data processing applications like stock market data.

The examples in this tutorial demonstrate:
- Basic stream operations
- Consumer groups and load balancing
- Real-time data processing
- Multiple consumer types
- Error handling and monitoring

Start with the basic examples, then gradually add complexity as you build your stock website. Remember to always acknowledge messages and handle errors gracefully!

Happy coding! 🚀
