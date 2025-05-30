#!/bin/bash

# FastAPI Streaming Response Tests with curl
# Make sure the server is running with: python main.py

BASE_URL="http://localhost:8000"

echo "=========================================="
echo "FastAPI Streaming Response Tests with curl"
echo "=========================================="

echo ""
echo "1. Testing basic endpoint..."
curl -s "$BASE_URL/" | jq .

echo ""
echo "2. Testing text streaming..."
echo "You should see characters appearing one by one:"
curl -s "$BASE_URL/stream/text"

echo ""
echo "3. Testing async text streaming..."
echo "You should see words appearing one by one:"
curl -s "$BASE_URL/stream/async-text"

echo ""
echo "4. Testing JSON streaming..."
echo "You should see JSON objects streaming:"
timeout 10s curl -s "$BASE_URL/stream/json"

echo ""
echo "5. Testing Server-Sent Events..."
echo "You should see SSE events (stopping after 10 seconds):"
timeout 10s curl -s -H "Accept: text/event-stream" "$BASE_URL/stream/sse"

echo ""
echo "6. Testing large data streaming..."
echo "You should see large data chunks (showing first 1000 chars):"
curl -s "$BASE_URL/stream/large-data" | head -c 1000
echo "..."

echo ""
echo "=========================================="
echo "All curl tests completed!"
echo "==========================================" 