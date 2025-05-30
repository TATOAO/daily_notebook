from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json
import time
from typing import Generator, AsyncGenerator

app = FastAPI(title="FastAPI Streaming Example", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "FastAPI Streaming Examples"}

@app.get("/stream/text")
async def stream_text():
    """
    Simple text streaming endpoint that streams "Hello World" character by character
    """
    def generate_text() -> Generator[str, None, None]:
        message = "Hello World from FastAPI Streaming! This is a character-by-character stream.\n"
        for char in message:
            yield char
            time.sleep(0.1)  # Simulate some processing time
    
    return StreamingResponse(generate_text(), media_type="text/plain")

@app.get("/stream/async-text")
async def stream_async_text():
    """
    Async text streaming endpoint
    """
    async def generate_async_text() -> AsyncGenerator[str, None]:
        message = "Hello World from Async FastAPI Streaming! This message comes in chunks.\n"
        words = message.split()
        for word in words:
            yield f"{word} "
            await asyncio.sleep(0.2)  # Non-blocking sleep
    
    return StreamingResponse(generate_async_text(), media_type="text/plain")

@app.get("/stream/json")
async def stream_json():
    """
    JSON streaming endpoint that streams multiple JSON objects
    """
    async def generate_json_stream() -> AsyncGenerator[str, None]:
        for i in range(10):
            data = {
                "id": i,
                "message": f"Hello World item {i}",
                "timestamp": time.time()
            }
            yield f"data: {json.dumps(data)}\n\n"
            await asyncio.sleep(0.5)
    
    return StreamingResponse(generate_json_stream(), media_type="application/json")

@app.get("/stream/sse")
async def stream_server_sent_events():
    """
    Server-Sent Events (SSE) streaming endpoint
    """
    async def generate_sse() -> AsyncGenerator[str, None]:
        for i in range(20):
            data = {
                "count": i,
                "message": f"Hello World SSE event {i}",
                "timestamp": time.time()
            }
            yield f"data: {json.dumps(data)}\n\n"
            await asyncio.sleep(1)
    
    return StreamingResponse(
        generate_sse(), 
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*"
        }
    )

@app.get("/stream/large-data")
async def stream_large_data():
    """
    Simulates streaming large data in chunks
    """
    async def generate_large_data() -> AsyncGenerator[bytes, None]:
        chunk_size = 1024  # 1KB chunks
        total_chunks = 100
        
        for i in range(total_chunks):
            # Generate some dummy data
            chunk_data = f"Chunk {i}: " + "x" * (chunk_size - len(f"Chunk {i}: ") - 1) + "\n"
            yield chunk_data.encode()
            await asyncio.sleep(0.05)  # Small delay to simulate processing
    
    return StreamingResponse(
        generate_large_data(), 
        media_type="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=large_data.txt"}
    )

# python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 