from fastmcp import FastMCP
# Instantiate the server
mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
return f"Hello, {name}!"
