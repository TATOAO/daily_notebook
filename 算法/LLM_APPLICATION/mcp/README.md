# Model Context Protocol (MCP) Hello World Example

This repository contains a comprehensive hello world example demonstrating how to use the Model Context Protocol (MCP) with different transport types, integrated with OpenAI's API and LangChain.

## What is MCP?

Model Context Protocol (MCP) is an open standard that enables secure connections between AI applications and data sources. It allows language models to access external tools and data in a standardized way.

## Project Structure

```
mcp/
├── server/
│   ├── hello_world_server.py    # MCP server with stdio transport
│   └── http_server.py           # MCP server with HTTP/SSE transport
├── client/
│   ├── hello_world_client.py    # MCP client with stdio transport
│   └── http_client.py           # MCP client with HTTP/SSE transport
├── requirements.txt             # Python dependencies
├── env.example                  # Environment variables template
├── demo_transport_types.py      # Transport comparison demo
└── README.md                   # This file
```

## Transport Types

MCP supports multiple transport mechanisms for communication between clients and servers:

### 1. **stdio Transport** (Local Subprocess)
- **Use case**: Local tools, command-line applications, simple integrations
- **How it works**: Client launches server as subprocess, communicates via stdin/stdout
- **Advantages**: Simple setup, fast communication, automatic process management
- **Limitations**: Local only, one client per server, process dependency

**Example**: `client/hello_world_client.py` ↔ `server/hello_world_server.py`

### 2. **HTTP/SSE Transport** (Web Service)
- **Use case**: Remote services, web applications, multi-client scenarios
- **How it works**: Server runs as HTTP service, clients connect via HTTP + Server-Sent Events
- **Advantages**: Remote connectivity, multiple clients, independent server lifecycle
- **Considerations**: More complex setup, network latency, security requirements

**Example**: `client/http_client.py` ↔ `server/http_server.py`

### 3. **Custom Transports**
MCP also supports custom transport implementations like WebSocket, gRPC, TCP sockets, etc.

## Features

This example demonstrates:

1. **MCP Servers** (both transport types):
   - `hello_world`: Returns a greeting message with optional name
   - `get_time`: Returns the current time
   - `get_server_info`: Returns server information (HTTP version only)

2. **MCP Clients** (both transport types):
   - Connects to MCP servers
   - Integrates with OpenAI's API via LangChain
   - Demonstrates function calling with MCP tools
   - Shows both direct tool calls and LLM-mediated tool usage

## Setup Instructions

### 1. Install Dependencies

```bash
# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Set up Environment Variables

```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your OpenAI API key
# Get your API key from: https://platform.openai.com/api-keys
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
```

## Usage Examples

### Quick Demo (All Transport Types)

```bash
# Run the transport comparison demo
python demo_transport_types.py
```

### stdio Transport Example

```bash
# Run the stdio client (automatically starts the server)
python client/hello_world_client.py
```

### HTTP/SSE Transport Example

```bash
# Terminal 1: Start the HTTP server
python server/http_server.py

# Terminal 2: Run the HTTP client
python client/http_client.py
```

### Manual HTTP Server Testing

```bash
# Start the HTTP server
python server/http_server.py

# Test the server endpoints
curl http://localhost:8000/                    # Server info
curl http://localhost:8000/health              # Health check
curl http://localhost:8000/sse                 # SSE endpoint (requires SSE client)
```

## What the Examples Do

When you run the clients, they will:

1. **Connect to the MCP server** (via stdio or HTTP)
2. **List available tools** from the server
3. **Test direct tool calls** to demonstrate basic MCP functionality
4. **Test LangChain integration** by:
   - Sending queries to OpenAI
   - Having OpenAI decide when to use MCP tools
   - Executing tool calls via MCP
   - Returning enriched responses

## Expected Output

### stdio Transport:
```
Hello World MCP Client with LangChain Integration
==================================================
Starting MCP server...
Connecting to MCP server...
Connected to MCP server successfully!
Available tools: ['hello_world', 'get_time']

🎉 Starting Hello World MCP + LangChain Demo!
==================================================

1. Testing direct MCP tool calls:
   Direct hello_world call: Hello, MCP Developer! Welcome to MCP (Model Context Protocol)!
   Direct get_time call: Current time is: 2024-01-15 14:30:25

2. Testing LangChain + MCP integration:
   [... more examples ...]

✅ Demo completed successfully!
```

### HTTP Transport:
```
HTTP MCP Client with LangChain Integration
==================================================
Trying to connect to: http://localhost:8000/sse
Connecting to HTTP MCP server at: http://localhost:8000/sse
Connected to HTTP MCP server successfully!
Available tools: ['hello_world', 'get_time', 'get_server_info']

🎉 Starting HTTP MCP + LangChain Demo!
==================================================

1. Testing direct MCP tool calls:
   Direct hello_world call: Hello, HTTP Client! Welcome to HTTP MCP (Model Context Protocol)!
   Direct get_time call: Current time is: 2024-01-15 14:30:25

✅ HTTP Demo completed successfully!
```

## Transport Comparison

| Feature          | stdio        | HTTP/SSE      |
|------------------|--------------|---------------|
| Setup            | Simple       | Moderate      |
| Connectivity     | Local only   | Local/Remote  |
| Multiple clients | No           | Yes           |
| Performance      | Fast         | Good          |
| Security         | Process-level| HTTP-level    |
| Scalability      | Limited      | High          |
| Use case         | Local tools  | Web services  |

## Understanding the Code

### stdio Server (`server/hello_world_server.py`)
- Uses `FastMCP` with stdio transport
- Launched as subprocess by client
- Simple process-based communication

### HTTP Server (`server/http_server.py`)
- Uses `FastAPI` with `SseServerTransport`
- Runs as independent web service
- Handles multiple concurrent connections
- Includes security measures (origin validation)

### stdio Client (`client/hello_world_client.py`)
- Uses `StdioServerParameters` and `stdio_client`
- Launches server subprocess automatically
- Manages server lifecycle

### HTTP Client (`client/http_client.py`)
- Uses `sse_client` for HTTP/SSE transport
- Connects to remote server URL
- Handles connection failures gracefully

## Extending the Examples

You can extend these examples by:

1. **Adding more tools** to the servers (e.g., file operations, API calls)
2. **Using different LLM providers** (Claude, local models, etc.)
3. **Implementing resource providers** for data access
4. **Adding authentication and security** measures
5. **Creating custom transports** (WebSocket, gRPC, etc.)

## Security Considerations

### HTTP Transport Security
- **Origin validation**: Prevents DNS rebinding attacks
- **Localhost binding**: Reduces exposure when running locally
- **Authentication**: Consider adding API keys for production
- **CORS configuration**: Configure appropriately for your use case

### General Security
- Validate all inputs
- Implement proper error handling
- Use secure communication channels
- Monitor for unusual patterns

## Troubleshooting

- **Missing API key**: Make sure your `.env` file contains a valid OpenAI API key
- **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **stdio connection issues**: Check that the server starts successfully
- **HTTP connection issues**: 
  - Make sure the HTTP server is running (`python server/http_server.py`)
  - Check that port 8000 is available
  - Verify the server URL in the client configuration

## Additional Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [MCP Transport Specification](https://modelcontextprotocol.io/docs/concepts/transports)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
