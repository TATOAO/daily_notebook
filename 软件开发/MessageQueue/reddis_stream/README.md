# Redis Streams Message Queue Tutorial

## What is a Message Queue?

A message queue is a communication pattern where:
- **Producers** send messages to a queue
- **Consumers** receive and process messages from the queue
- Messages are stored temporarily until processed
- Multiple consumers can process messages in parallel
- Provides decoupling between producers and consumers

### Why Use Message Queues?

1. **Decoupling**: Producers don't need to know about consumers
2. **Scalability**: Add more consumers to handle increased load
3. **Reliability**: Messages persist even if consumers are down
4. **Asynchronous Processing**: Non-blocking operations
5. **Load Balancing**: Distribute work across multiple workers

## Redis Streams vs Traditional Message Queues

### Traditional Message Queues (RabbitMQ, Apache Kafka)
- Complex setup and configuration
- Separate infrastructure to maintain
- More features but higher overhead

### Redis Streams
- Built into Redis (no additional infrastructure)
- Simple to use and understand
- Perfect for learning and small to medium applications
- Great for real-time data like stock quotes

## Project Structure

```
reddis_stream/
├── README.md                 # This tutorial
├── requirements.txt          # Python dependencies
├── examples/
│   ├── basic_stream.py      # Basic Redis Stream operations
│   ├── stock_producer.py    # Stock quote producer
│   ├── stock_consumer.py    # Stock quote consumer
│   └── multiple_consumers.py # Multiple consumers example
├── utils/
│   └── redis_client.py      # Redis connection utilities
└── tests/
    └── test_streams.py      # Unit tests
```

## Installation and Setup

1. Install Redis (if not already installed):
   ```bash
   # macOS
   brew install redis
   
   # Ubuntu
   sudo apt-get install redis-server
   ```

2. Start Redis:
   ```bash
   redis-server
   ```

3. Install Python dependencies:
   ```bash
   # Create virtual environment
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install dependencies
   pip install redis
   ```

## Core Concepts

### 1. Stream
- A log-like data structure in Redis
- Messages are appended to the end
- Each message has a unique ID
- Messages are immutable (cannot be modified)

### 2. Consumer Group
- A group of consumers that share the work
- Each message is delivered to only one consumer in the group
- Provides load balancing and fault tolerance

### 3. Message ID
- Unique identifier for each message
- Format: `timestamp-sequence`
- Example: `1640995200000-0`

### 4. Pending Messages
- Messages that have been delivered but not acknowledged
- Can be re-delivered if consumer fails

## Basic Operations

### Creating a Stream
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Add a message to a stream
message_id = r.xadd('mystream', {'field1': 'value1', 'field2': 'value2'})
print(f"Message added with ID: {message_id}")
```

### Reading from a Stream
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

## Stock Quote Example

Let's build a complete example using stock quotes:

### 1. Stock Quote Producer
- Simulates real-time stock data
- Publishes quotes to Redis Stream
- Includes price, volume, timestamp

### 2. Stock Quote Consumer
- Processes incoming stock quotes
- Calculates moving averages
- Triggers alerts for significant price changes

### 3. Multiple Consumers
- Shows load balancing
- Different consumers handle different tasks

## Running the Examples

1. **Basic Stream Operations**:
   ```bash
   python examples/basic_stream.py
   ```

2. **Stock Quote System**:
   ```bash
   # Terminal 1: Start producer
   python examples/stock_producer.py
   
   # Terminal 2: Start consumer
   python examples/stock_consumer.py
   ```

3. **Multiple Consumers**:
   ```bash
   # Terminal 1: Start producer
   python examples/stock_producer.py
   
   # Terminal 2: Start consumer 1
   python examples/multiple_consumers.py consumer1
   
   # Terminal 3: Start consumer 2
   python examples/multiple_consumers.py consumer2
   ```

## Advanced Features

### 1. Message Acknowledgment
```python
# Acknowledge processed messages
r.xack('mystream', 'mygroup', message_id)
```

### 2. Pending Messages
```python
# Check pending messages
pending = r.xpending('mystream', 'mygroup')
print(f"Pending messages: {pending}")
```

### 3. Stream Trimming
```python
# Keep only last 1000 messages
r.xtrim('mystream', maxlen=1000, approximate=True)
```

### 4. Blocking Reads
```python
# Wait for new messages (block for 5 seconds)
messages = r.xread({'mystream': '$'}, block=5000)
```

## Best Practices

1. **Error Handling**: Always handle Redis connection errors
2. **Message Acknowledgment**: Always acknowledge processed messages
3. **Consumer Groups**: Use consumer groups for reliability
4. **Stream Trimming**: Trim old messages to prevent memory issues
5. **Monitoring**: Monitor pending messages and consumer lag

## Common Use Cases

1. **Real-time Analytics**: Process user events, clicks, etc.
2. **Log Processing**: Centralized log collection and processing
3. **IoT Data**: Sensor data processing
4. **Stock Trading**: Real-time market data processing
5. **Chat Applications**: Message delivery and history

## Next Steps

1. Run the basic examples to understand the concepts
2. Modify the stock quote example for your specific needs
3. Add error handling and monitoring
4. Scale up with multiple consumers
5. Integrate with your stock website

## Resources

- [Redis Streams Documentation](https://redis.io/docs/data-types/streams/)
- [Redis Python Client](https://redis-py.readthedocs.io/)
- [Message Queue Patterns](https://martinfowler.com/articles/microservices.html#MessageQueues) 