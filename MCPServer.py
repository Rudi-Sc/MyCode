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