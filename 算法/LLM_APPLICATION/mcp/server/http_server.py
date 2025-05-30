#!/usr/bin/env python3
"""
An HTTP-based MCP Server example using FastAPI.
This server runs as a web service and can handle multiple client connections.
"""

import datetime
import asyncio
import json
from typing import Optional, Dict, Any

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app for HTTP transport
app = FastAPI(
    title="MCP HTTP Server",
    description="A Model Context Protocol server running over HTTP with SSE",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:*", "http://127.0.0.1:*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Simple in-memory storage for demo
_tools = {
    "hello_world": {
        "name": "hello_world",
        "description": "Returns a hello world greeting with optional name",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name to greet",
                    "default": "World"
                }
            }
        }
    },
    "get_time": {
        "name": "get_time", 
        "description": "Returns the current time",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    "get_server_info": {
        "name": "get_server_info",
        "description": "Returns information about this HTTP MCP server",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
}


def execute_tool(tool_name: str, arguments: Dict[str, Any] = None) -> str:
    """Execute a tool and return the result."""
    if arguments is None:
        arguments = {}
    
    if tool_name == "hello_world":
        name = arguments.get("name", "World")
        return f"Hello, {name}! Welcome to HTTP MCP (Model Context Protocol)!"
    elif tool_name == "get_time":
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Current time is: {current_time}"
    elif tool_name == "get_server_info":
        return "This is an HTTP-based MCP server running with FastAPI. It can handle multiple concurrent client connections!"
    else:
        raise ValueError(f"Unknown tool: {tool_name}")


@app.get("/")
async def root():
    """Root endpoint with server information."""
    return {
        "name": "MCP HTTP Server",
        "description": "Model Context Protocol server with HTTP transport",
        "version": "1.0.0",
        "endpoints": {
            "sse": "/sse",
            "messages": "/messages",
            "tools": "/tools",
            "call_tool": "/call_tool"
        },
        "tools": list(_tools.keys())
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}


@app.get("/tools")
async def list_tools():
    """List available tools (MCP-style)."""
    return {
        "tools": list(_tools.values())
    }


@app.post("/call_tool")
async def call_tool(request: Request):
    """Call a tool with arguments."""
    try:
        body = await request.json()
        tool_name = body.get("name")
        arguments = body.get("arguments", {})
        
        if not tool_name:
            raise HTTPException(status_code=400, detail="Tool name is required")
        
        if tool_name not in _tools:
            raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
        
        result = execute_tool(tool_name, arguments)
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": result
                }
            ]
        }
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/sse")
async def handle_sse(request: Request):
    """Handle SSE connections for MCP communication."""
    print(f"🔗 New SSE connection from: {request.client.host if request.client else 'unknown'}")
    
    # Validate Origin header for security (prevent DNS rebinding attacks)
    origin = request.headers.get("origin")
    if origin and not _is_allowed_origin(origin):
        print(f"❌ Rejected connection from unauthorized origin: {origin}")
        raise HTTPException(status_code=403, detail="Unauthorized origin")
    
    async def event_generator():
        """Generate SSE events for MCP communication."""
        try:
            # Send initial connection event
            yield "data: {\"type\": \"connection\", \"status\": \"connected\"}\n\n"
            
            # Send tools list
            tools_data = json.dumps({
                "type": "tools_list",
                "tools": list(_tools.values())
            })
            yield f"data: {tools_data}\n\n"
            
            # Keep the connection alive with periodic heartbeats
            while True:
                heartbeat_data = json.dumps({
                    "type": "heartbeat",
                    "timestamp": datetime.datetime.now().isoformat()
                })
                yield f"data: {heartbeat_data}\n\n"
                await asyncio.sleep(30)  # Heartbeat every 30 seconds
                
        except Exception as e:
            print(f"❌ SSE stream error: {e}")
            error_data = json.dumps({
                "type": "error",
                "message": str(e)
            })
            yield f"data: {error_data}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",  # Configure appropriately for production
            "Access-Control-Allow-Methods": "GET, POST",
            "Access-Control-Allow-Headers": "Content-Type",
        }
    )


@app.post("/messages")
async def handle_messages(request: Request):
    """Handle POST messages for MCP communication."""
    print(f"📨 Received message from: {request.client.host if request.client else 'unknown'}")
    
    # Validate Origin header for security
    origin = request.headers.get("origin")
    if origin and not _is_allowed_origin(origin):
        print(f"❌ Rejected message from unauthorized origin: {origin}")
        raise HTTPException(status_code=403, detail="Unauthorized origin")
    
    try:
        body = await request.json()
        print(f"📝 Message content: {body}")
        
        # For now, just acknowledge the message
        return JSONResponse(
            content={"status": "received", "message": "Message processed"},
            status_code=202
        )
    
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    except Exception as e:
        print(f"❌ Message handling error: {e}")
        raise HTTPException(status_code=500, detail="Message handling failed")


def _is_allowed_origin(origin: str) -> bool:
    """Check if the origin is allowed (security measure)."""
    # For development, allow localhost origins
    # In production, you should configure this properly
    allowed_origins = [
        "http://localhost",
        "http://127.0.0.1", 
        "https://localhost",
        "https://127.0.0.1"
    ]
    
    # Check if origin starts with any allowed origin
    return any(origin.startswith(allowed) for allowed in allowed_origins)


# python3 -m uvicorn server.http_server:app --reload
if __name__ == "__main__":
    import uvicorn
    
    print("Starting Hello World HTTP MCP Server...")
    print("This server provides MCP tools over HTTP transport.")
    print("\nAvailable tools:")
    print("- hello_world: Returns a greeting message")
    print("- get_time: Returns the current time")
    print("- get_server_info: Returns server information")
    print("\nServer endpoints:")
    print("- http://localhost:8000/ (server info)")
    print("- http://localhost:8000/sse (SSE endpoint)")
    print("- http://localhost:8000/messages (messages endpoint)")
    print("- http://localhost:8000/tools (list tools)")
    print("- http://localhost:8000/call_tool (call tool)")
    print("- http://localhost:8000/health (health check)")
    
    # Run the server
    uvicorn.run(
        app,
        host="127.0.0.1",  # Bind to localhost only for security
        port=8000,
        log_level="info"
    ) 