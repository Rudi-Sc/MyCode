from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("TaskTracker")

# Simple in-memory task storage
tasks = []
task_id_counter = 1
