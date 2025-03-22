from fastapi import FastAPI, HTTPException, Query
from task_tracker.business.task_service import (
    list_tasks, add_task, update_task, delete_task, mark_in_progress, mark_done
)
<<<<<<< HEAD
from task_tracker.api import auth_routes

app = FastAPI()

# Include authentication routes
app.include_router(auth_routes.router, prefix="/auth")

=======

app = FastAPI()

>>>>>>> 74066c0 (Add authentication, database, and API routes)
@app.get("/")
def root():
    return {"message": "Welcome to the Task Tracker API"}

@app.get("/tasks")
def get_tasks(status: str = Query(None), limit: int = Query(None)):
<<<<<<< HEAD
=======
    """
    Retrieve tasks with optional filters:
    - `status`: Filter tasks by their status (e.g., "todo", "in-progress", "done").
    - `limit`: Limit the number of returned tasks.
    """
>>>>>>> 74066c0 (Add authentication, database, and API routes)
    tasks = list_tasks(status=status, limit=limit)
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(description: str):
<<<<<<< HEAD
=======
    """
    Add a new task to the database.
    """
>>>>>>> 74066c0 (Add authentication, database, and API routes)
    task_id = add_task(description)
    return {"message": "Task added successfully", "task_id": task_id}

@app.put("/tasks/{task_id}")
def modify_task(task_id: int, new_description: str):
<<<<<<< HEAD
=======
    """
    Update an existing task's description.
    """
>>>>>>> 74066c0 (Add authentication, database, and API routes)
    success = update_task(task_id, new_description)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} updated successfully"}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
<<<<<<< HEAD
=======
    """
    Delete a task by ID.
    """
>>>>>>> 74066c0 (Add authentication, database, and API routes)
    success = delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} deleted successfully"}

@app.patch("/tasks/{task_id}/in-progress")
def set_task_in_progress(task_id: int):
<<<<<<< HEAD
=======
    """
    Mark a task as 'in-progress'.
    """
>>>>>>> 74066c0 (Add authentication, database, and API routes)
    success = mark_in_progress(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} marked as in-progress"}

@app.patch("/tasks/{task_id}/done")
def set_task_done(task_id: int):
<<<<<<< HEAD
=======
    """
    Mark a task as 'done'.
    """
>>>>>>> 74066c0 (Add authentication, database, and API routes)
    success = mark_done(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} marked as done"}
