import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Rodin"))


# After initializing and connecting 'session'
tools_response = await session.list_tools()
print("Available tools:")
for tool in tools_response.tools:
    print(f" - {tool.name}: {tool.description}")
