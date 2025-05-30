#!/usr/bin/env python3
"""
A simple Hello World MCP Server example using FastMCP.
This server provides basic tools that return greetings and time information.
"""

import datetime
from mcp.server.fastmcp import FastMCP

# Create the FastMCP server instance
mcp = FastMCP("hello-world-server")


@mcp.tool()
def hello_world(name: str = "World") -> str:
    """Returns a hello world greeting with optional name."""
    return f"Hello, {name}! Welcome to MCP (Model Context Protocol)!"


@mcp.tool()
def get_time() -> str:
    """Returns the current time."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current time is: {current_time}"


if __name__ == "__main__":
    # Run the server using stdio transport
    print("Starting Hello World MCP Server...")
    print("Server is ready to handle requests via stdio.")
    mcp.run(transport="stdio") 