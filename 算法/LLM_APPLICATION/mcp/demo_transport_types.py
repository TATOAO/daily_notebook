#!/usr/bin/env python3
"""
Demo script showcasing different MCP transport types.
This demonstrates both stdio and HTTP/SSE transports.
"""

import asyncio
import subprocess
import time
import os
from pathlib import Path

print("🚀 MCP Transport Types Demonstration")
print("=" * 50)

async def demo_stdio_transport():
    """Demonstrate stdio transport (local subprocess)."""
    print("\n📡 1. STDIO Transport (Local Subprocess)")
    print("-" * 40)
    print("✅ Advantages:")
    print("   • Simple setup - just run a Python script")
    print("   • Fast communication via stdin/stdout")
    print("   • Automatic process management")
    print("   • Good for local tools and integrations")
    print()
    print("❌ Limitations:")
    print("   • Only works locally")
    print("   • One client per server instance")
    print("   • Server dies if client dies")
    print()
    
    # Check if the stdio server exists
    stdio_server_path = Path("server/hello_world_server.py")
    if stdio_server_path.exists():
        print("🔧 Demo: Running stdio client...")
        try:
            # Run the stdio client
            process = await asyncio.create_subprocess_exec(
                "python", "client/hello_world_client.py",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Wait for completion or timeout
            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(), 
                    timeout=30.0
                )
                
                if process.returncode == 0:
                    print("✅ Stdio demo completed successfully!")
                    # Show last few lines of output
                    output_lines = stdout.decode().split('\n')
                    print("📄 Sample output:")
                    for line in output_lines[-5:]:
                        if line.strip():
                            print(f"   {line}")
                else:
                    print(f"❌ Stdio demo failed with return code: {process.returncode}")
                    if stderr:
                        print(f"Error: {stderr.decode()}")
                        
            except asyncio.TimeoutError:
                print("⏰ Stdio demo timed out (this is normal for demo purposes)")
                process.terminate()
                
        except FileNotFoundError:
            print("❌ Python not found. Make sure Python is installed.")
        except Exception as e:
            print(f"❌ Error running stdio demo: {e}")
    else:
        print("❌ Stdio server not found at server/hello_world_server.py")


async def demo_http_transport():
    """Demonstrate HTTP/SSE transport (web service)."""
    print("\n🌐 2. HTTP/SSE Transport (Web Service)")
    print("-" * 40)
    print("✅ Advantages:")
    print("   • Remote connectivity over HTTP")
    print("   • Multiple clients can connect")
    print("   • Server runs independently")
    print("   • Web-friendly (firewalls, proxies)")
    print("   • Scalable and stateless")
    print()
    print("❌ Considerations:")
    print("   • More complex setup")
    print("   • Requires web server")
    print("   • Network latency")
    print("   • Security considerations (auth, CORS)")
    print()
    
    # Check if the HTTP server exists
    http_server_path = Path("server/http_server.py")
    if http_server_path.exists():
        print("🔧 Demo: Starting HTTP server...")
        
        # Start the HTTP server in background
        server_process = None
        try:
            server_process = await asyncio.create_subprocess_exec(
                "python", "server/http_server.py",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Wait a moment for server to start
            await asyncio.sleep(3)
            
            print("🔧 Server started, now running HTTP client...")
            
            # Run the HTTP client
            client_process = await asyncio.create_subprocess_exec(
                "python", "client/http_client.py",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Wait for client completion or timeout
            try:
                stdout, stderr = await asyncio.wait_for(
                    client_process.communicate(),
                    timeout=20.0
                )
                
                if client_process.returncode == 0:
                    print("✅ HTTP demo completed successfully!")
                    # Show last few lines of output
                    output_lines = stdout.decode().split('\n')
                    print("📄 Sample output:")
                    for line in output_lines[-5:]:
                        if line.strip():
                            print(f"   {line}")
                else:
                    print(f"❌ HTTP demo failed with return code: {client_process.returncode}")
                    if stderr:
                        print(f"Error: {stderr.decode()}")
                        
            except asyncio.TimeoutError:
                print("⏰ HTTP demo timed out")
                client_process.terminate()
                
        except Exception as e:
            print(f"❌ Error running HTTP demo: {e}")
        finally:
            # Clean up server process
            if server_process:
                server_process.terminate()
                await asyncio.sleep(1)
                if server_process.returncode is None:
                    server_process.kill()
    else:
        print("❌ HTTP server not found at server/http_server.py")


async def show_transport_comparison():
    """Show a comparison table of transport types."""
    print("\n📊 Transport Comparison")
    print("-" * 40)
    print("| Feature          | stdio        | HTTP/SSE      |")
    print("|------------------|--------------|---------------|")
    print("| Setup            | Simple       | Moderate      |")
    print("| Connectivity     | Local only   | Local/Remote  |")
    print("| Multiple clients | No           | Yes           |")
    print("| Performance      | Fast         | Good          |")
    print("| Security         | Process-level| HTTP-level    |")
    print("| Scalability      | Limited      | High          |")
    print("| Use case         | Local tools  | Web services  |")


async def show_custom_transport_info():
    """Show information about custom transports."""
    print("\n🔧 3. Custom Transports")
    print("-" * 40)
    print("MCP also supports custom transport implementations:")
    print()
    print("🔹 WebSocket transport")
    print("   • Real-time bidirectional communication")
    print("   • Lower latency than HTTP")
    print("   • Good for interactive applications")
    print()
    print("🔹 gRPC transport")
    print("   • High-performance RPC")
    print("   • Strong typing with protobuf")
    print("   • Good for microservices")
    print()
    print("🔹 TCP/Unix socket transport")
    print("   • Direct socket communication")
    print("   • Maximum performance")
    print("   • Good for system-level integration")
    print()
    print("🔹 Message queue transport (Redis, RabbitMQ)")
    print("   • Asynchronous messaging")
    print("   • Pub/sub patterns")
    print("   • Good for distributed systems")


async def main():
    """Run the complete transport demonstration."""
    
    # Check for dependencies
    try:
        import mcp
        import fastapi
        import uvicorn
        print("✅ All dependencies found")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found")
        print("Some demos may not work without an API key")
        print("Copy env.example to .env and add your key")
    
    # Run demos
    await demo_stdio_transport()
    await demo_http_transport()
    await show_transport_comparison()
    await show_custom_transport_info()
    
    print("\n🎉 Transport demonstration complete!")
    print("\nNext steps:")
    print("1. Try running: python client/hello_world_client.py")
    print("2. Try running: python server/http_server.py (in one terminal)")
    print("3. Then run: python client/http_client.py (in another terminal)")


if __name__ == "__main__":
    asyncio.run(main()) 