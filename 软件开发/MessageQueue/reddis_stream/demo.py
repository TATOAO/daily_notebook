#!/usr/bin/env python3
"""
Redis Streams Message Queue Demo

This script demonstrates the complete message queue system with:
- Stock quote producer
- Multiple consumers
- Real-time data processing
- Load balancing
"""

import sys
import os
import time
import threading
import signal
from datetime import datetime

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.redis_client import get_redis_client, close_redis_client
from examples.stock_producer import StockQuoteProducer
from examples.multiple_consumers import (
    PriceAlertConsumer, 
    VolumeAnalysisConsumer, 
    TechnicalAnalysisConsumer,
    MarketEventConsumer
)


class MessageQueueDemo:
    """Demo class that runs the complete message queue system."""
    
    def __init__(self):
        self.redis_client = get_redis_client()
        self.running = False
        self.threads = []
        
        # Initialize components
        self.producer = StockQuoteProducer(self.redis_client)
        self.consumers = {
            'price_alert': PriceAlertConsumer(self.redis_client, 'price_alert_demo'),
            'volume_analysis': VolumeAnalysisConsumer(self.redis_client, 'volume_demo'),
            'technical_analysis': TechnicalAnalysisConsumer(self.redis_client, 'tech_demo'),
            'market_event': MarketEventConsumer(self.redis_client, 'event_demo')
        }
    
    def start_producer(self):
        """Start the stock quote producer in a separate thread."""
        def producer_worker():
            print("📈 Starting stock quote producer...")
            self.producer.publish_quotes(interval=0.5)  # 2 quotes per second
        
        producer_thread = threading.Thread(target=producer_worker, daemon=True)
        producer_thread.start()
        self.threads.append(producer_thread)
        return producer_thread
    
    def start_consumer(self, consumer_type, consumer):
        """Start a consumer in a separate thread."""
        def consumer_worker():
            print(f"🔄 Starting {consumer_type} consumer...")
            consumer.consume_messages(block_time=1000)
        
        consumer_thread = threading.Thread(target=consumer_worker, daemon=True)
        consumer_thread.start()
        self.threads.append(consumer_thread)
        return consumer_thread
    
    def start_all_consumers(self):
        """Start all consumers."""
        for consumer_type, consumer in self.consumers.items():
            self.start_consumer(consumer_type, consumer)
    
    def print_statistics(self):
        """Print statistics about the running system."""
        while self.running:
            time.sleep(10)  # Print stats every 10 seconds
            
            print("\n" + "="*60)
            print("📊 SYSTEM STATISTICS")
            print("="*60)
            print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Print consumer statistics
            for consumer_type, consumer in self.consumers.items():
                print(f"{consumer_type}: {consumer.messages_processed} messages processed")
                
                if hasattr(consumer, 'alerts_generated'):
                    print(f"  - Alerts generated: {consumer.alerts_generated}")
                if hasattr(consumer, 'volume_spikes'):
                    print(f"  - Volume spikes detected: {consumer.volume_spikes}")
                if hasattr(consumer, 'analysis_count'):
                    print(f"  - Technical analyses: {consumer.analysis_count}")
                if hasattr(consumer, 'events_processed'):
                    print(f"  - Events processed: {consumer.events_processed}")
            
            # Check Redis stream info
            try:
                stream_info = self.redis_client.client.xinfo_stream("stock_quotes")
                print(f"\nStream info:")
                print(f"  - Total messages: {stream_info['length']}")
                print(f"  - First message ID: {stream_info['first-entry'][0] if stream_info['first-entry'] else 'None'}")
                print(f"  - Last message ID: {stream_info['last-entry'][0] if stream_info['last-entry'] else 'None'}")
            except Exception as e:
                print(f"  - Error getting stream info: {e}")
            
            print("="*60)
    
    def run_demo(self, duration=60):
        """Run the complete demo for a specified duration."""
        print("🚀 Redis Streams Message Queue Demo")
        print("=" * 50)
        print(f"Running for {duration} seconds...")
        print("Press Ctrl+C to stop early")
        print()
        
        self.running = True
        
        try:
            # Start producer
            self.start_producer()
            time.sleep(2)  # Give producer time to start
            
            # Start all consumers
            self.start_all_consumers()
            time.sleep(2)  # Give consumers time to start
            
            # Start statistics thread
            stats_thread = threading.Thread(target=self.print_statistics, daemon=True)
            stats_thread.start()
            
            # Run for specified duration
            print(f"✅ Demo running! All components started.")
            print("📈 Producer: Generating stock quotes")
            print("🔄 Consumers: Processing messages")
            print("📊 Statistics: Updated every 10 seconds")
            print()
            
            time.sleep(duration)
            
        except KeyboardInterrupt:
            print("\n⏹️  Stopping demo...")
        finally:
            self.stop_demo()
    
    def stop_demo(self):
        """Stop all components."""
        print("🛑 Stopping all components...")
        
        self.running = False
        
        # Stop producer
        self.producer.stop()
        
        # Stop consumers
        for consumer in self.consumers.values():
            consumer.stop()
        
        # Wait for threads to finish
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=5)
        
        print("✅ Demo stopped.")
    
    def cleanup(self):
        """Clean up resources."""
        close_redis_client()


def signal_handler(signum, frame):
    """Handle interrupt signals."""
    print("\n⏹️  Received interrupt signal. Stopping demo...")
    if hasattr(signal_handler, 'demo'):
        signal_handler.demo.stop_demo()
        signal_handler.demo.cleanup()
    sys.exit(0)


def main():
    """Main function to run the demo."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Redis Streams Message Queue Demo")
    parser.add_argument("--duration", type=int, default=60, 
                       help="Demo duration in seconds (default: 60)")
    parser.add_argument("--quick", action="store_true",
                       help="Run a quick 30-second demo")
    
    args = parser.parse_args()
    
    # Set up signal handling
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Create and run demo
        demo = MessageQueueDemo()
        signal_handler.demo = demo  # Store reference for signal handler
        
        duration = 30 if args.quick else args.duration
        demo.run_demo(duration=duration)
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        print("\nPlease make sure Redis is running:")
        print("  redis-server")
        return 1
    finally:
        if 'demo' in locals():
            demo.cleanup()
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 