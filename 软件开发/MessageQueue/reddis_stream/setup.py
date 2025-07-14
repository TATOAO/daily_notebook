#!/usr/bin/env python3
"""
Setup script for Redis Streams Message Queue Tutorial

This script helps you set up the project environment and dependencies.
"""

import os
import sys
import subprocess
import platform


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def check_redis():
    """Check if Redis is installed and running."""
    print("🔍 Checking Redis installation...")
    
    # Check if redis-server is available
    try:
        result = subprocess.run(['redis-server', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✅ Redis server found: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Redis server not found")
        return False


def install_redis():
    """Install Redis based on the operating system."""
    system = platform.system().lower()
    
    if system == "darwin":  # macOS
        print("🍎 Installing Redis on macOS...")
        return run_command("brew install redis", "Installing Redis via Homebrew")
    
    elif system == "linux":
        print("🐧 Installing Redis on Linux...")
        # Try different package managers
        if run_command("which apt-get", "Checking for apt-get"):
            return run_command("sudo apt-get update && sudo apt-get install -y redis-server", 
                             "Installing Redis via apt-get")
        elif run_command("which yum", "Checking for yum"):
            return run_command("sudo yum install -y redis", "Installing Redis via yum")
        else:
            print("❌ No supported package manager found. Please install Redis manually.")
            return False
    
    elif system == "windows":
        print("🪟 Installing Redis on Windows...")
        print("Please install Redis manually from: https://redis.io/download")
        print("Or use WSL (Windows Subsystem for Linux)")
        return False
    
    else:
        print(f"❌ Unsupported operating system: {system}")
        return False


def start_redis():
    """Start Redis server."""
    print("🚀 Starting Redis server...")
    
    # Check if Redis is already running
    try:
        result = subprocess.run(['redis-cli', 'ping'], 
                              capture_output=True, text=True, check=True)
        if result.stdout.strip() == "PONG":
            print("✅ Redis is already running")
            return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    
    # Start Redis server
    try:
        # Start Redis in background
        subprocess.Popen(['redis-server'], 
                        stdout=subprocess.DEVNULL, 
                        stderr=subprocess.DEVNULL)
        
        # Wait a moment for Redis to start
        import time
        time.sleep(2)
        
        # Test connection
        result = subprocess.run(['redis-cli', 'ping'], 
                              capture_output=True, text=True, check=True)
        if result.stdout.strip() == "PONG":
            print("✅ Redis server started successfully")
            return True
        else:
            print("❌ Redis server failed to start")
            return False
            
    except Exception as e:
        print(f"❌ Failed to start Redis: {e}")
        return False


def setup_python_environment():
    """Set up Python virtual environment and install dependencies."""
    print("🐍 Setting up Python environment...")
    
    # Check if Python is available
    if not run_command("python --version", "Checking Python installation"):
        print("❌ Python not found. Please install Python 3.7+")
        return False
    
    # Create virtual environment
    if not run_command("python -m venv .venv", "Creating virtual environment"):
        return False
    
    # Activate virtual environment and install dependencies
    if platform.system().lower() == "windows":
        activate_cmd = ".venv\\Scripts\\activate"
        pip_cmd = ".venv\\Scripts\\pip"
    else:
        activate_cmd = "source .venv/bin/activate"
        pip_cmd = ".venv/bin/pip"
    
    # Install dependencies
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing Python dependencies"):
        return False
    
    print("✅ Python environment setup completed")
    return True


def run_tests():
    """Run the test suite to verify everything works."""
    print("🧪 Running tests...")
    
    if platform.system().lower() == "windows":
        python_cmd = ".venv\\Scripts\\python"
    else:
        python_cmd = ".venv/bin/python"
    
    if run_command(f"{python_cmd} -m pytest tests/ -v", "Running test suite"):
        print("✅ All tests passed!")
        return True
    else:
        print("❌ Some tests failed. Please check the output above.")
        return False


def print_next_steps():
    """Print next steps for the user."""
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETED!")
    print("="*60)
    print("\nNext steps:")
    print("1. Activate the virtual environment:")
    if platform.system().lower() == "windows":
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")
    
    print("\n2. Start Redis (if not already running):")
    print("   redis-server")
    
    print("\n3. Run the basic example:")
    print("   python examples/basic_stream.py")
    
    print("\n4. Run the stock market example:")
    print("   # Terminal 1: python examples/stock_producer.py")
    print("   # Terminal 2: python examples/stock_consumer.py")
    
    print("\n5. Read the tutorial:")
    print("   open reddis_stream.md")
    
    print("\n6. Run tests:")
    print("   python -m pytest tests/ -v")
    
    print("\nHappy learning! 🚀")


def main():
    """Main setup function."""
    print("Redis Streams Message Queue Tutorial - Setup")
    print("=" * 50)
    print()
    
    # Check Redis
    if not check_redis():
        print("\nRedis not found. Attempting to install...")
        if not install_redis():
            print("\n❌ Failed to install Redis. Please install it manually.")
            print("Visit: https://redis.io/download")
            return False
    
    # Start Redis
    if not start_redis():
        print("\n❌ Failed to start Redis. Please start it manually:")
        print("redis-server")
        return False
    
    # Setup Python environment
    if not setup_python_environment():
        print("\n❌ Failed to setup Python environment.")
        return False
    
    # Run tests
    print("\nRunning tests to verify setup...")
    run_tests()
    
    # Print next steps
    print_next_steps()
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 