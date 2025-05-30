# FastAPI Streaming Response Examples

This project demonstrates various ways to implement streaming responses in FastAPI, including text streaming, JSON streaming, and Server-Sent Events (SSE).

## Features

- **Text Streaming**: Character-by-character and word-by-word streaming
- **JSON Streaming**: Streaming multiple JSON objects
- **Server-Sent Events**: Real-time event streaming with proper SSE format
- **Large Data Streaming**: Efficient streaming of large datasets
- **Async Support**: Both synchronous and asynchronous streaming implementations

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Start the FastAPI Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

### 2. Test the Endpoints

#### Option A: Use the Python Test Script
```bash
python test_streaming.py
```

#### Option B: Use curl Commands
```bash
chmod +x test_curl.sh
./test_curl.sh
```

#### Option C: Manual Testing with curl

**Basic endpoint:**
```bash
curl http://localhost:8000/
```

**Text streaming:**
```bash
curl http://localhost:8000/stream/text
```

**Async text streaming:**
```bash
curl http://localhost:8000/stream/async-text
```

**JSON streaming:**
```bash
curl http://localhost:8000/stream/json
```

**Server-Sent Events:**
```bash
curl -H "Accept: text/event-stream" http://localhost:8000/stream/sse
```

**Large data streaming:**
```bash
curl http://localhost:8000/stream/large-data
```

### 3. View API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Basic health check endpoint |
| `/stream/text` | GET | Character-by-character text streaming |
| `/stream/async-text` | GET | Word-by-word async text streaming |
| `/stream/json` | GET | JSON object streaming |
| `/stream/sse` | GET | Server-Sent Events streaming |
| `/stream/large-data` | GET | Large data chunk streaming |

## Key Concepts

### StreamingResponse

FastAPI's `StreamingResponse` is used to stream content to the client. It accepts:
- A generator or async generator function
- Media type (content-type)
- Optional headers

### Generator vs AsyncGenerator

- **Generator**: Use for CPU-bound operations or when you don't need async capabilities
- **AsyncGenerator**: Use for I/O-bound operations or when you need to perform async operations

### Server-Sent Events (SSE)

SSE is perfect for real-time updates from server to client. Key points:
- Content-Type: `text/event-stream`
- Data format: `data: {content}\n\n`
- Proper headers for browser compatibility

### Large Data Streaming

For large datasets:
- Stream in chunks to avoid memory issues
- Use appropriate chunk sizes (1KB - 64KB typically)
- Consider using bytes for binary data

## Implementation Examples

### Basic Text Streaming
```python
def generate_text():
    for char in "Hello World":
        yield char
        time.sleep(0.1)

return StreamingResponse(generate_text(), media_type="text/plain")
```

### Async Streaming
```python
async def generate_async_text():
    for word in ["Hello", "World"]:
        yield f"{word} "
        await asyncio.sleep(0.2)

return StreamingResponse(generate_async_text(), media_type="text/plain")
```

### JSON Streaming
```python
async def generate_json():
    for i in range(10):
        data = {"id": i, "message": f"Item {i}"}
        yield f"data: {json.dumps(data)}\n\n"
        await asyncio.sleep(0.5)

return StreamingResponse(generate_json(), media_type="application/json")
```

## Testing with Different Clients

### Python requests
```python
response = requests.get("http://localhost:8000/stream/text", stream=True)
for chunk in response.iter_content(chunk_size=1):
    print(chunk.decode(), end='')
```

### Python aiohttp
```python
async with aiohttp.ClientSession() as session:
    async with session.get("http://localhost:8000/stream/text") as response:
        async for chunk in response.content.iter_any():
            print(chunk.decode(), end='')
```

### JavaScript (Browser)
```javascript
fetch('http://localhost:8000/stream/sse')
  .then(response => {
    const reader = response.body.getReader();
    return reader.read().then(function processText({done, value}) {
      if (done) return;
      console.log(new TextDecoder().decode(value));
      return reader.read().then(processText);
    });
  });
```

## Use Cases

- **Real-time data feeds**: Stock prices, sensor data, logs
- **Large file downloads**: CSV exports, reports, backups
- **Chat applications**: Real-time messaging
- **Progress updates**: Long-running task status
- **Live data visualization**: Charts, dashboards

## Performance Tips

1. **Chunk Size**: Choose appropriate chunk sizes based on your data
2. **Memory Management**: Use generators to avoid loading everything into memory
3. **Connection Management**: Set proper timeouts and connection limits
4. **Error Handling**: Implement proper error handling in your generators
5. **Client Buffering**: Be aware of client-side buffering behavior

## Troubleshooting

- **Connection Timeout**: Increase client timeout settings for long-running streams
- **Buffering Issues**: Some proxies/browsers may buffer streaming responses
- **Memory Usage**: Monitor memory usage with large datasets
- **Connection Drops**: Implement retry logic on the client side

## License

This project is for educational purposes. Feel free to use and modify as needed. 