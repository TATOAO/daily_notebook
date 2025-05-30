#!/usr/bin/env python3
"""
An HTTP-based MCP Client example that connects to a remote MCP server via HTTP.
This demonstrates an alternative to the stdio transport for remote server communication.
"""

import asyncio
import json
import os
import aiohttp
from typing import Any, Dict, Optional, List

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, FunctionMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)


class HttpMCPClient:
    def __init__(self):
        print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
        print(f"OPENAI_BASE_URL: {os.getenv('OPENAI_BASE_URL')}")
        print(f"OPENAI_MODEL: {os.getenv('OPENAI_MODEL')}")
        
        # Initialize LangChain ChatOpenAI
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0
        )
        
        self.session: Optional[aiohttp.ClientSession] = None
        self.server_url: Optional[str] = None
        self.tools: List[Dict[str, Any]] = []
        
    async def connect_to_http_server(self, server_url: str):
        """Connect to a remote MCP server via HTTP."""
        self.server_url = server_url.rstrip('/sse').rstrip('/')  # Remove /sse suffix if present
        print(f"Connecting to HTTP MCP server at: {self.server_url}")
        
        try:
            # Create HTTP session
            self.session = aiohttp.ClientSession()
            
            # Test connection by getting server info
            async with self.session.get(f"{self.server_url}/") as response:
                if response.status == 200:
                    server_info = await response.json()
                    print(f"Connected to: {server_info.get('name', 'Unknown Server')}")
                else:
                    raise Exception(f"Server returned status {response.status}")
            
            # Get available tools
            await self._load_tools()
            
            print("Connected to HTTP MCP server successfully!")
            print(f"Available tools: {[tool['name'] for tool in self.tools]}")
            print(f"Successfully connected and found {len(self.tools)} MCP tools")
            
            # Demo the integration
            await self.demo_integration()
            
        except Exception as e:
            print(f"Failed to connect to HTTP server: {e}")
            print("Make sure the HTTP MCP server is running and accessible")
            await self.cleanup()
            raise
    
    async def _load_tools(self):
        """Load available tools from the server."""
        if not self.session or not self.server_url:
            return
        
        try:
            async with self.session.get(f"{self.server_url}/tools") as response:
                if response.status == 200:
                    tools_response = await response.json()
                    self.tools = tools_response.get("tools", [])
                else:
                    print(f"Failed to load tools: HTTP {response.status}")
                    self.tools = []
        except Exception as e:
            print(f"Error loading tools: {e}")
            self.tools = []
                
    async def call_mcp_tool(self, tool_name: str, arguments: Dict[str, Any] = None) -> str:
        """Call a tool via HTTP and return the result."""
        if not self.session or not self.server_url:
            raise ValueError("Not connected to MCP server")
            
        if arguments is None:
            arguments = {}
        
        try:
            payload = {
                "name": tool_name,
                "arguments": arguments
            }
            
            async with self.session.post(
                f"{self.server_url}/call_tool",
                json=payload,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    # Extract text content from the result
                    content = result.get("content", [])
                    if content and len(content) > 0:
                        return content[0].get("text", "")
                    return ""
                else:
                    error_text = await response.text()
                    raise Exception(f"Tool call failed: HTTP {response.status} - {error_text}")
                    
        except Exception as e:
            raise Exception(f"Error calling tool {tool_name}: {e}")
    
    async def chat_with_langchain(self, message: str) -> str:
        """Chat using LangChain with MCP tools integration."""
        
        # Create a custom tool calling function
        async def call_mcp_function(tool_name: str, arguments: Dict[str, Any]) -> str:
            print(f"🔧 LangChain wants to call function: {tool_name} with args: {arguments}")
            result = await self.call_mcp_tool(tool_name, arguments)
            print(f"🛠️ MCP Tool result: {result}")
            return result
        
        # If no tools available, just chat normally
        if not self.tools:
            messages = [
                SystemMessage(content="You are a helpful assistant."),
                HumanMessage(content=message)
            ]
            response = await self.llm.ainvoke(messages)
            return response.content
        
        # Convert MCP tools to OpenAI function format for LangChain
        functions = []
        for tool in self.tools:
            function_def = {
                "name": tool["name"],
                "description": tool.get("description", ""),
                "parameters": tool.get("inputSchema", {"type": "object", "properties": {}})
            }
            functions.append(function_def)
        
        # Create messages
        messages = [
            SystemMessage(content="You are a helpful assistant that can use MCP tools. When appropriate, use the available functions to help answer user questions."),
            HumanMessage(content=message)
        ]
        
        # Use LangChain's function calling
        llm_with_functions = self.llm.bind_functions(functions)
        response = await llm_with_functions.ainvoke(messages)
        
        # Check if the response includes function calls
        if hasattr(response, 'additional_kwargs') and 'function_call' in response.additional_kwargs:
            function_call = response.additional_kwargs['function_call']
            function_name = function_call['name']
            function_args = json.loads(function_call['arguments'])
            
            # Call the MCP tool
            tool_result = await call_mcp_function(function_name, function_args)
            
            # Create follow-up conversation with function result
            messages.extend([
                AIMessage(content="", additional_kwargs={"function_call": function_call}),
                FunctionMessage(name=function_name, content=tool_result)
            ])
            
            # Get final response
            final_response = await self.llm.ainvoke(messages)
            return final_response.content
        
        return response.content
    
    async def demo_integration(self):
        """Demonstrate the integration between LangChain and HTTP MCP tools."""
        print("\n🎉 Starting HTTP MCP + LangChain Demo!")
        print("=" * 50)
        
        # Test direct tool calls
        print("\n1. Testing direct MCP tool calls:")
        
        try:
            hello_result = await self.call_mcp_tool("hello_world", {"name": "HTTP Client"})
            print(f"   Direct hello_world call: {hello_result}")
        except Exception as e:
            print(f"   Error calling hello_world: {e}")
        
        try:
            time_result = await self.call_mcp_tool("get_time")
            print(f"   Direct get_time call: {time_result}")
        except Exception as e:
            print(f"   Error calling get_time: {e}")
        
        try:
            info_result = await self.call_mcp_tool("get_server_info")
            print(f"   Direct get_server_info call: {info_result}")
        except Exception as e:
            print(f"   Error calling get_server_info: {e}")
        
        # Test LangChain integration
        print("\n2. Testing LangChain + HTTP MCP integration:")
        
        queries = [
            "Please greet me using the hello world function with my name 'HTTP User'",
            "What time is it right now?",
            "Can you tell me about the server and what time it is?",
        ]
        
        for i, query in enumerate(queries, 1):
            print(f"\n   Query {i}: {query}")
            try:
                response = await self.chat_with_langchain(query)
                print(f"   Response: {response}")
            except Exception as e:
                print(f"   Error: {e}")
        
        print("\n✅ HTTP Demo completed successfully!")
    
    async def cleanup(self):
        """Clean up resources."""
        if self.session:
            await self.session.close()


async def main():
    """Main function to run the HTTP client."""
    print("HTTP MCP Client with LangChain Integration")
    print("=" * 50)
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("Please copy env.example to .env and add your OpenAI API key.")
        return
    
    client = HttpMCPClient()
    
    try:
        # Example HTTP MCP server URLs
        # Replace with your actual HTTP MCP server URL
        server_urls = [
            "http://localhost:8000",  # Local HTTP server
            # "https://your-mcp-server.com",  # Remote server
        ]
        
        # Try to connect to available servers
        for server_url in server_urls:
            print(f"\nTrying to connect to: {server_url}")
            try:
                await client.connect_to_http_server(server_url)
                break  # Successfully connected
            except Exception as e:
                print(f"❌ Failed to connect to {server_url}: {e}")
                continue
        else:
            print("\n❌ Could not connect to any HTTP MCP servers.")
            print("\nTo use this client, you need to:")
            print("1. Run an HTTP MCP server (see server/http_server.py)")
            print("2. Make sure it's accessible at one of the URLs above")
            print("3. Update the server_urls list with your server's URL")
    
    finally:
        await client.cleanup()


# python -m client.http_client
if __name__ == "__main__":
    asyncio.run(main()) 