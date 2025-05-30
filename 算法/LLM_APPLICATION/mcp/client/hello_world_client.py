#!/usr/bin/env python3
"""
A simple Hello World MCP Client example that uses LangChain with LangSmith.
This client connects to the MCP server and demonstrates tool usage with LLM.
"""

import asyncio
import json
import os
from typing import Any, Dict, Optional
from contextlib import AsyncExitStack

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, FunctionMessage
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Load environment variables
load_dotenv(override=True)


class HelloWorldMCPClient:
    def __init__(self):
        print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
        print(f"OPENAI_BASE_URL: {os.getenv('OPENAI_BASE_URL')}")
        print(f"OPENAI_MODEL: {os.getenv('OPENAI_MODEL')}")
        print(f"LANGCHAIN_TRACING_V2: {os.getenv('LANGCHAIN_TRACING_V2')}")
        print(f"LANGCHAIN_PROJECT: {os.getenv('LANGCHAIN_PROJECT')}")
        
        # Configure LangSmith tracing
        if os.getenv('LANGCHAIN_TRACING_V2') == 'true':
            os.environ["LANGCHAIN_TRACING_V2"] = "true"
            if os.getenv('LANGCHAIN_API_KEY'):
                os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
            if os.getenv('LANGCHAIN_PROJECT'):
                os.environ["LANGCHAIN_PROJECT"] = os.getenv('LANGCHAIN_PROJECT')
        
        # Initialize LangChain ChatOpenAI
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0
        )
        
        self.exit_stack = AsyncExitStack()
        self.session: Optional[ClientSession] = None
        
    async def connect_to_server(self, server_script_path: str):
        """Connect to the MCP server."""
        print("Starting MCP server...")
        
        # Determine server type and command
        is_python = server_script_path.endswith('.py')
        if not is_python:
            raise ValueError("Server script must be a .py file")
            
        # Create server parameters
        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path],
            env=None
        )
        
        print("Connecting to MCP server...")
        
        # Connect to the server via stdio
        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        read_stream, write_stream = stdio_transport
        
        # Create session
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )
        
        # Initialize the session
        await self.session.initialize()
        
        print("Connected to MCP server successfully!")
        
        # List available tools
        tools_response = await self.session.list_tools()
        tools = tools_response.tools
        print(f"Available tools: {[tool.name for tool in tools]}")
        
        print(f"Successfully connected and found {len(tools)} MCP tools")
        
        # Demo the integration
        await self.demo_integration()
                
    async def call_mcp_tool(self, tool_name: str, arguments: Dict[str, Any] = None) -> str:
        """Call a tool via MCP and return the result."""
        if not self.session:
            raise ValueError("Not connected to MCP server")
            
        if arguments is None:
            arguments = {}
            
        result = await self.session.call_tool(tool_name, arguments)
        
        # Extract text content from the result
        if result.content and len(result.content) > 0:
            return result.content[0].text
        return ""
    
    async def chat_with_langchain(self, message: str) -> str:
        """Chat using LangChain with MCP tools integration."""
        
        # Create a custom tool calling function
        async def call_mcp_function(tool_name: str, arguments: Dict[str, Any]) -> str:
            print(f"🔧 LangChain wants to call function: {tool_name} with args: {arguments}")
            result = await self.call_mcp_tool(tool_name, arguments)
            print(f"🛠️ MCP Tool result: {result}")
            return result
        
        # Get available tools from the session
        tools_response = await self.session.list_tools()
        available_tools = tools_response.tools
        
        # If no tools available, just chat normally
        if not available_tools:
            messages = [
                SystemMessage(content="You are a helpful assistant."),
                HumanMessage(content=message)
            ]
            response = await self.llm.ainvoke(messages)
            return response.content
        
        # Convert MCP tools to OpenAI function format for LangChain
        functions = []
        for tool in available_tools:
            function_def = {
                "name": tool.name,
                "description": tool.description or "",
                "parameters": tool.inputSchema if tool.inputSchema else {"type": "object", "properties": {}}
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
        """Demonstrate the integration between LangChain and MCP tools."""
        print("\n🎉 Starting Hello World MCP + LangChain Demo!")
        print("=" * 50)
        
        # Test direct tool calls
        print("\n1. Testing direct MCP tool calls:")
        
        hello_result = await self.call_mcp_tool("hello_world", {"name": "MCP Developer"})
        print(f"   Direct hello_world call: {hello_result}")
        
        time_result = await self.call_mcp_tool("get_time")
        print(f"   Direct get_time call: {time_result}")
        
        # Test LangChain integration
        print("\n2. Testing LangChain + MCP integration:")
        
        queries = [
            "Please greet me using the hello world function with my name 'Alice'",
            "What time is it right now?",
            "Can you greet 'Bob' and then tell me the current time?",
            "Just say hello to me normally without using any tools"
        ]
        
        for i, query in enumerate(queries, 1):
            print(f"\n   Query {i}: {query}")
            response = await self.chat_with_langchain(query)
            print(f"   Response: {response}")
        
        print("\n✅ Demo completed successfully!")
    
    async def cleanup(self):
        """Clean up resources."""
        await self.exit_stack.aclose()


async def main():
    """Main function to run the client."""
    print("Hello World MCP Client with LangChain Integration")
    print("=" * 50)
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("Please copy env.example to .env and add your OpenAI API key.")
        return
    
    client = HelloWorldMCPClient()
    
    try:
        await client.connect_to_server("server/hello_world_server.py")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure the MCP server is available and dependencies are installed.")
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main()) 