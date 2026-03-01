# https://gofastmcp.com/getting-started/quickstart

from fastmcp import FastMCP
import math

# Instantiate the server
mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return int(a + b)

if __name__ == "__main__":
    mcp.run()
