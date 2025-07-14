"""
Redis client utilities for the message queue tutorial.
Provides connection management and common operations.
"""

import redis
import os
from typing import Optional, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RedisClient:
    """Redis client wrapper with connection management and error handling."""
    
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        """
        Initialize Redis client.
        
        Args:
            host: Redis server host
            port: Redis server port
            db: Redis database number
        """
        self.host = host
        self.port = port
        self.db = db
        self.client: Optional[redis.Redis] = None
        self._connect()
    
    def _connect(self):
        """Establish connection to Redis."""
        try:
            self.client = redis.Redis(
                host=self.host,
                port=self.port,
                db=self.db,
                decode_responses=True,
                socket_connect_timeout=5,
                socket_timeout=5
            )
            # Test connection
            self.client.ping()
            logger.info(f"Connected to Redis at {self.host}:{self.port}")
        except redis.ConnectionError as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error connecting to Redis: {e}")
            raise
    
    def is_connected(self) -> bool:
        """Check if Redis connection is alive."""
        try:
            return self.client.ping()
        except:
            return False
    
    def add_to_stream(self, stream_name: str, data: Dict[str, Any]) -> str:
        """
        Add a message to a Redis stream.
        
        Args:
            stream_name: Name of the stream
            data: Message data as key-value pairs
            
        Returns:
            Message ID
        """
        try:
            message_id = self.client.xadd(stream_name, data)
            logger.debug(f"Added message {message_id} to stream {stream_name}")
            return message_id
        except Exception as e:
            logger.error(f"Error adding message to stream {stream_name}: {e}")
            raise
    
    def read_from_stream(self, stream_name: str, start_id: str = '0', count: int = 10):
        """
        Read messages from a stream.
        
        Args:
            stream_name: Name of the stream
            start_id: Starting message ID ('0' for beginning, '$' for latest)
            count: Maximum number of messages to read
            
        Returns:
            List of messages
        """
        try:
            messages = self.client.xread({stream_name: start_id}, count=count)
            return messages
        except Exception as e:
            logger.error(f"Error reading from stream {stream_name}: {e}")
            raise
    
    def create_consumer_group(self, stream_name: str, group_name: str, start_id: str = '0'):
        """
        Create a consumer group for a stream.
        
        Args:
            stream_name: Name of the stream
            group_name: Name of the consumer group
            start_id: Starting message ID for the group
        """
        try:
            self.client.xgroup_create(stream_name, group_name, start_id, mkstream=True)
            logger.info(f"Created consumer group {group_name} for stream {stream_name}")
        except redis.exceptions.ResponseError as e:
            if "BUSYGROUP" in str(e):
                logger.info(f"Consumer group {group_name} already exists")
            else:
                logger.error(f"Error creating consumer group: {e}")
                raise
        except Exception as e:
            logger.error(f"Unexpected error creating consumer group: {e}")
            raise
    
    def read_from_group(self, group_name: str, consumer_name: str, stream_name: str, 
                       count: int = 10, block: int = 5000):
        """
        Read messages from a stream as part of a consumer group.
        
        Args:
            group_name: Name of the consumer group
            consumer_name: Name of the consumer
            stream_name: Name of the stream
            count: Maximum number of messages to read
            block: Block time in milliseconds (0 for non-blocking)
            
        Returns:
            List of messages
        """
        try:
            messages = self.client.xreadgroup(
                group_name, 
                consumer_name, 
                {stream_name: '>'}, 
                count=count, 
                block=block
            )
            return messages
        except Exception as e:
            logger.error(f"Error reading from group {group_name}: {e}")
            raise
    
    def acknowledge_message(self, stream_name: str, group_name: str, message_id: str):
        """
        Acknowledge a message in a consumer group.
        
        Args:
            stream_name: Name of the stream
            group_name: Name of the consumer group
            message_id: ID of the message to acknowledge
        """
        try:
            self.client.xack(stream_name, group_name, message_id)
            logger.debug(f"Acknowledged message {message_id} in group {group_name}")
        except Exception as e:
            logger.error(f"Error acknowledging message {message_id}: {e}")
            raise
    
    def get_pending_messages(self, stream_name: str, group_name: str):
        """
        Get pending messages for a consumer group.
        
        Args:
            stream_name: Name of the stream
            group_name: Name of the consumer group
            
        Returns:
            Pending messages information
        """
        try:
            pending = self.client.xpending(stream_name, group_name)
            return pending
        except Exception as e:
            logger.error(f"Error getting pending messages: {e}")
            raise
    
    def trim_stream(self, stream_name: str, maxlen: int = 1000):
        """
        Trim a stream to keep only the latest messages.
        
        Args:
            stream_name: Name of the stream
            maxlen: Maximum number of messages to keep
        """
        try:
            removed = self.client.xtrim(stream_name, maxlen=maxlen, approximate=True)
            logger.info(f"Trimmed stream {stream_name}, removed {removed} messages")
            return removed
        except Exception as e:
            logger.error(f"Error trimming stream {stream_name}: {e}")
            raise
    
    def close(self):
        """Close the Redis connection."""
        if self.client:
            self.client.close()
            logger.info("Redis connection closed")


# Global Redis client instance
_redis_client: Optional[RedisClient] = None


def get_redis_client() -> RedisClient:
    """Get or create a Redis client instance."""
    global _redis_client
    if _redis_client is None or not _redis_client.is_connected():
        _redis_client = RedisClient()
    return _redis_client


def close_redis_client():
    """Close the global Redis client."""
    global _redis_client
    if _redis_client:
        _redis_client.close()
        _redis_client = None 