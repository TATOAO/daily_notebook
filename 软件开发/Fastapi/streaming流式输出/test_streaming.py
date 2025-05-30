#!/usr/bin/env python3
"""
Test script for FastAPI streaming responses
Run this after starting the FastAPI server with: python main.py
"""

import requests
import asyncio
import aiohttp
import json
import time
from typing import AsyncGenerator

BASE_URL = "http://localhost:8001"

def test_basic_endpoint():
    """Test the basic non-streaming endpoint"""
    print("=" * 50)
    print("Testing basic endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_text_streaming():
    """Test simple text streaming"""
    print("=" * 50)
    print("Testing text streaming (character by character)...")
    
    response = requests.get(f"{BASE_URL}/stream/text", stream=True)
    print(f"Status: {response.status_code}")
    print("Streamed content:")
    
    for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
        if chunk:
            print(chunk, end='', flush=True)
            time.sleep(0.02)  # Small delay to see the streaming effect
    print("\n")

def test_async_text_streaming():
    """Test async text streaming"""
    print("=" * 50)
    print("Testing async text streaming (word by word)...")
    
    response = requests.get(f"{BASE_URL}/stream/async-text", stream=True)
    print(f"Status: {response.status_code}")
    print("Streamed content:")
    
    for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
        if chunk:
            print(chunk, end='', flush=True)
    print("\n")

def test_json_streaming():
    """Test JSON streaming"""
    print("=" * 50)
    print("Testing JSON streaming...")
    
    response = requests.get(f"{BASE_URL}/stream/json", stream=True)
    print(f"Status: {response.status_code}")
    print("Streamed JSON data:")
    
    for line in response.iter_lines(decode_unicode=True):
        if line:
            if line.startswith("data: "):
                json_data = line[6:]  # Remove "data: " prefix
                try:
                    parsed_data = json.loads(json_data)
                    print(f"Received: {parsed_data}")
                except json.JSONDecodeError:
                    print(f"Raw line: {line}")
    print()

def test_sse_streaming():
    """Test Server-Sent Events streaming"""
    print("=" * 50)
    print("Testing Server-Sent Events (first 5 events only)...")
    
    response = requests.get(f"{BASE_URL}/stream/sse", stream=True)
    print(f"Status: {response.status_code}")
    print("SSE Events:")
    
    count = 0
    for line in response.iter_lines(decode_unicode=True):
        if line:
            if line.startswith("data: "):
                json_data = line[6:]  # Remove "data: " prefix
                try:
                    parsed_data = json.loads(json_data)
                    print(f"Event {count}: {parsed_data}")
                    count += 1
                    if count >= 5:  # Only show first 5 events
                        break
                except json.JSONDecodeError:
                    print(f"Raw line: {line}")
    print()

def test_large_data_streaming():
    """Test large data streaming"""
    print("=" * 50)
    print("Testing large data streaming (first 5 chunks only)...")
    
    response = requests.get(f"{BASE_URL}/stream/large-data", stream=True)
    print(f"Status: {response.status_code}")
    print("Large data chunks:")
    
    chunk_count = 0
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            # Decode and show first part of chunk
            chunk_str = chunk.decode('utf-8')
            first_line = chunk_str.split('\n')[0]
            print(f"Chunk {chunk_count}: {first_line[:50]}...")
            chunk_count += 1
            if chunk_count >= 5:  # Only show first 5 chunks
                break
    print()

async def test_async_streaming():
    """Test streaming with aiohttp for better async support"""
    print("=" * 50)
    print("Testing async streaming with aiohttp...")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/stream/async-text") as response:
            print(f"Status: {response.status}")
            print("Async streamed content:")
            
            async for chunk in response.content.iter_any():
                if chunk:
                    print(chunk.decode('utf-8'), end='', flush=True)
    print("\n")

async def test_sse_with_aiohttp():
    """Test SSE with aiohttp"""
    print("=" * 50)
    print("Testing SSE with aiohttp (first 3 events only)...")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/stream/sse") as response:
            print(f"Status: {response.status}")
            print("SSE Events (async):")
            
            count = 0
            async for line in response.content:
                line_str = line.decode('utf-8').strip()
                if line_str.startswith("data: "):
                    json_data = line_str[6:]  # Remove "data: " prefix
                    try:
                        parsed_data = json.loads(json_data)
                        print(f"Event {count}: {parsed_data}")
                        count += 1
                        if count >= 3:  # Only show first 3 events
                            break
                    except json.JSONDecodeError:
                        continue
    print()

def main():
    """Run all tests"""
    print("FastAPI Streaming Response Tests")
    print("Make sure the server is running with: python main.py")
    print()
    
    try:
        # Test basic endpoint first
        test_basic_endpoint()
        
        # Test various streaming methods
        test_text_streaming()
        test_async_text_streaming()
        test_json_streaming()
        test_sse_streaming()
        test_large_data_streaming()
        
        # Test async methods
        print("Running async tests...")
        asyncio.run(test_async_streaming())
        asyncio.run(test_sse_with_aiohttp())
        
        print("=" * 50)
        print("All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server.")
        print("Please make sure the FastAPI server is running:")
        print("python main.py")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 