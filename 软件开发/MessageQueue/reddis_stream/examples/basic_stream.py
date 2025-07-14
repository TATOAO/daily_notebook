"""
Basic Redis Stream Operations Example

This example demonstrates the fundamental operations of Redis Streams:
- Creating streams
- Adding messages
- Reading messages
- Consumer groups
- Message acknowledgment
"""

import sys
import os
import time
import random
from typing import Dict, Any

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.redis_client import RedisClient, get_redis_client, close_redis_client


def demonstrate_basic_operations():
    """Demonstrate basic Redis Stream operations."""
    print("=== Basic Redis Stream Operations ===\n")
    
    # Get Redis client
    redis_client = get_redis_client()
    stream_name = "basic_stream"
    
    try:
        # 1. Add messages to stream
        print("1. Adding messages to stream...")
        for i in range(5):
            message_data = {
                'message_number': str(i + 1),
                'timestamp': str(int(time.time())),
                'content': f'This is message number {i + 1}',
                'random_value': str(random.randint(1, 100))
            }
            message_id = redis_client.add_to_stream(stream_name, message_data)
            print(f"   Added message {i + 1} with ID: {message_id}")
        
        print()
        
        # 2. Read all messages from stream
        print("2. Reading all messages from stream...")
        messages = redis_client.read_from_stream(stream_name, start_id='0')
        
        for stream, message_list in messages:
            print(f"   Stream: {stream}")
            for message_id, fields in message_list:
                print(f"   - ID: {message_id}")
                print(f"     Fields: {fields}")
                print()
        
        # 3. Create consumer group
        print("3. Creating consumer group...")
        group_name = "basic_group"
        redis_client.create_consumer_group(stream_name, group_name)
        
        # 4. Read messages as part of consumer group
        print("4. Reading messages as consumer in group...")
        consumer_name = "consumer1"
        messages = redis_client.read_from_group(group_name, consumer_name, stream_name, count=3)
        
        for stream, message_list in messages:
            print(f"   Stream: {stream}")
            for message_id, fields in message_list:
                print(f"   - ID: {message_id}")
                print(f"     Fields: {fields}")
                
                # Acknowledge the message
                redis_client.acknowledge_message(stream_name, group_name, message_id)
                print(f"     ✓ Acknowledged")
                print()
        
        # 5. Check pending messages
        print("5. Checking pending messages...")
        pending = redis_client.get_pending_messages(stream_name, group_name)
        print(f"   Pending messages: {pending}")
        
        # 6. Read remaining messages
        print("\n6. Reading remaining messages...")
        messages = redis_client.read_from_group(group_name, consumer_name, stream_name, count=10)
        
        for stream, message_list in messages:
            for message_id, fields in message_list:
                print(f"   - ID: {message_id}")
                print(f"     Fields: {fields}")
                
                # Acknowledge the message
                redis_client.acknowledge_message(stream_name, group_name, message_id)
                print(f"     ✓ Acknowledged")
                print()
        
        # 7. Demonstrate blocking read
        print("7. Demonstrating blocking read (waiting for new messages)...")
        print("   (This will wait for 5 seconds for new messages)")
        
        # Add a new message in a separate thread to demonstrate blocking
        import threading
        
        def add_delayed_message():
            time.sleep(2)
            message_data = {
                'message_type': 'delayed',
                'timestamp': str(int(time.time())),
                'content': 'This message was added after a delay'
            }
            redis_client.add_to_stream(stream_name, message_data)
            print("   ✓ Added delayed message")
        
        thread = threading.Thread(target=add_delayed_message)
        thread.start()
        
        # Blocking read
        messages = redis_client.read_from_group(group_name, consumer_name, stream_name, 
                                               count=1, block=5000)
        
        for stream, message_list in messages:
            for message_id, fields in message_list:
                print(f"   - Received: {message_id}")
                print(f"     Fields: {fields}")
                redis_client.acknowledge_message(stream_name, group_name, message_id)
                print(f"     ✓ Acknowledged")
        
        thread.join()
        
        # 8. Stream trimming
        print("\n8. Trimming stream to keep only last 3 messages...")
        removed = redis_client.trim_stream(stream_name, maxlen=3)
        print(f"   Removed {removed} messages")
        
        # Show remaining messages
        messages = redis_client.read_from_stream(stream_name, start_id='0')
        print("   Remaining messages:")
        for stream, message_list in messages:
            for message_id, fields in message_list:
                print(f"   - ID: {message_id}")
                print(f"     Fields: {fields}")
                print()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up
        close_redis_client()


def demonstrate_stream_operations():
    """Demonstrate more advanced stream operations."""
    print("=== Advanced Stream Operations ===\n")
    
    redis_client = get_redis_client()
    stream_name = "advanced_stream"
    
    try:
        # Add messages with different data types
        print("1. Adding messages with various data types...")
        
        messages_data = [
            {'type': 'user_event', 'user_id': '123', 'action': 'login', 'timestamp': str(int(time.time()))},
            {'type': 'system_event', 'level': 'info', 'message': 'Server started', 'timestamp': str(int(time.time()))},
            {'type': 'data_update', 'table': 'users', 'operation': 'insert', 'record_id': '456', 'timestamp': str(int(time.time()))},
            {'type': 'error', 'code': '500', 'message': 'Database connection failed', 'timestamp': str(int(time.time()))},
            {'type': 'metric', 'name': 'cpu_usage', 'value': '75.5', 'unit': '%', 'timestamp': str(int(time.time()))}
        ]
        
        for i, data in enumerate(messages_data):
            message_id = redis_client.add_to_stream(stream_name, data)
            print(f"   Added message {i + 1}: {data['type']} - ID: {message_id}")
        
        print()
        
        # Read messages by type
        print("2. Reading messages and filtering by type...")
        messages = redis_client.read_from_stream(stream_name, start_id='0')
        
        user_events = []
        system_events = []
        errors = []
        
        for stream, message_list in messages:
            for message_id, fields in message_list:
                event_type = fields.get('type', 'unknown')
                if event_type == 'user_event':
                    user_events.append((message_id, fields))
                elif event_type == 'system_event':
                    system_events.append((message_id, fields))
                elif event_type == 'error':
                    errors.append((message_id, fields))
        
        print(f"   User events: {len(user_events)}")
        print(f"   System events: {len(system_events)}")
        print(f"   Errors: {len(errors)}")
        
        # Show errors
        if errors:
            print("\n   Error messages:")
            for message_id, fields in errors:
                print(f"   - {message_id}: {fields['message']} (Code: {fields['code']})")
        
        print()
        
        # Demonstrate consumer group with multiple consumers
        print("3. Demonstrating consumer group with multiple consumers...")
        group_name = "advanced_group"
        redis_client.create_consumer_group(stream_name, group_name)
        
        # Simulate multiple consumers
        consumers = ['consumer1', 'consumer2', 'consumer3']
        
        for consumer in consumers:
            print(f"   {consumer} reading messages...")
            messages = redis_client.read_from_group(group_name, consumer, stream_name, count=2)
            
            for stream, message_list in messages:
                for message_id, fields in message_list:
                    print(f"     - {consumer} processing: {message_id}")
                    print(f"       Type: {fields.get('type', 'unknown')}")
                    
                    # Simulate processing time
                    time.sleep(0.1)
                    
                    # Acknowledge
                    redis_client.acknowledge_message(stream_name, group_name, message_id)
                    print(f"       ✓ Acknowledged")
        
        print()
        
        # Check final pending messages
        print("4. Final pending messages check...")
        pending = redis_client.get_pending_messages(stream_name, group_name)
        print(f"   Pending: {pending}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        close_redis_client()


# python examples/basic_stream.py
if __name__ == "__main__":
    print("Redis Streams Basic Operations Tutorial")
    print("=" * 50)
    print()
    
    try:
        # Test Redis connection first
        redis_client = get_redis_client()
        print("✓ Redis connection successful")
        print()
        
        # Run demonstrations
        demonstrate_basic_operations()
        print("\n" + "=" * 50 + "\n")
        demonstrate_stream_operations()
        
    except Exception as e:
        print(f"❌ Failed to connect to Redis: {e}")
        print("\nPlease make sure Redis is running:")
        print("  redis-server")
        print("\nOr install Redis if not already installed:")
        print("  # macOS: brew install redis")
        print("  # Ubuntu: sudo apt-get install redis-server") 