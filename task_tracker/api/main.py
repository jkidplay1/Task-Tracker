from fastapi import FastAPI, HTTPException, Query
from task_tracker.business.task_service import (
    list_tasks, add_task, update_task, delete_task, mark_in_progress, mark_done
)
from task_tracker.api import auth_routes

app = FastAPI()

# Include authentication routes
app.include_router(auth_routes.router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Welcome to the Task Tracker API"}

@app.get("/tasks")
def get_tasks(status: str = Query(None), limit: int = Query(None)):
    tasks = list_tasks(status=status, limit=limit)
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(description: str):
    task_id = add_task(description)
    return {"message": "Task added successfully", "task_id": task_id}

@app.put("/tasks/{task_id}")
def modify_task(task_id: int, new_description: str):
    success = update_task(task_id, new_description)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} updated successfully"}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    success = delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} deleted successfully"}

@app.patch("/tasks/{task_id}/in-progress")
def set_task_in_progress(task_id: int):
    success = mark_in_progress(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} marked as in-progress"}

@app.patch("/tasks/{task_id}/done")
def set_task_done(task_id: int):
    success = mark_done(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} marked as done"}
