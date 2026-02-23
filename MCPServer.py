import logging
import os
import random
import sys
import requests
from mcp.server.fastmcp import FastMCP

name = "demo-mcp-server"
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(name)

port = int(os.environ.get('PORT', 8080))
mcp = FastMCP(name, logger=logger, port=port)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    logger.info(f"Tool called: add({a}, {b})")
    return a + b

@mcp.tool()
def get_secret_word() -> str:
    """Get a random secret word"""
    logger.info("Tool called: get_secret_word()")
    return random.choice(["apple", "banana", "cherry"])