# https://gofastmcp.com/getting-started/quickstart

import fastmcp
from fastmcp import Context
import math

# Instantiate the server
mcp = fastmcp.FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

@mcp.resource("resource://greeting")
def get_greeting() -> str:
    return "Hello from Rudi's MCP Server!"

@mcp.prompt()
def ask_about_topic(topic: str) -> str:
    """Generate a user message asking for an explanation of topic."""
    return f"Can you explain the concept of '{topic}' in simple terms?"

if __name__ == "__main__":
    mcp.run()
