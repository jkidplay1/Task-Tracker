from fastapi import FastAPI, HTTPException, Query
from task_tracker.business.task_service import (
    list_tasks, add_task, update_task, delete_task, mark_in_progress, mark_done
)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Task Tracker API"}

@app.get("/tasks")
def get_tasks(status: str = Query(None), limit: int = Query(None)):
    """
    Retrieve tasks with optional filters:
    - `status`: Filter tasks by their status (e.g., "todo", "in-progress", "done").
    - `limit`: Limit the number of returned tasks.
    """
    tasks = list_tasks(status=status, limit=limit)
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(description: str):
    """
    Add a new task to the database.
    """
    task_id = add_task(description)
    return {"message": "Task added successfully", "task_id": task_id}

@app.put("/tasks/{task_id}")
def modify_task(task_id: int, new_description: str):
    """
    Update an existing task's description.
    """
    success = update_task(task_id, new_description)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} updated successfully"}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    """
    Delete a task by ID.
    """
    success = delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} deleted successfully"}

@app.patch("/tasks/{task_id}/in-progress")
def set_task_in_progress(task_id: int):
    """
    Mark a task as 'in-progress'.
    """
    success = mark_in_progress(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} marked as in-progress"}

@app.patch("/tasks/{task_id}/done")
def set_task_done(task_id: int):
    """
    Mark a task as 'done'.
    """
    success = mark_done(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} marked as done"}
