from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("TaskTracker")

# Simple in-memory task storage
tasks = []
task_id_counter = 1

@mcp.tool()
def add_task(title: str, description: str = "") -> dict:
    """Add a new task to the task list."""
    global task_id_counter
    
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }
    
    tasks.append(task)
    task_id_counter += 1
    
    return task

@mcp.tool()
def complete_task(task_id: int) -> dict:
    """Mark a task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            task["completed_at"] = datetime.now().isoformat()
            return task
    
    return {"error": f"Task {task_id} not found"}
