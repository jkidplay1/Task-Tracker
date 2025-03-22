import pyodbc
from task_tracker.data.db import get_db_connection

def add_task(description):
    """Adds a new task to the database."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO Tasks (description, status) VALUES (?, 'todo')", (description,))
            conn.commit()
            print("Task added successfully.")
    except Exception as e:
        print(f"Error adding task: {e}")
    finally:
        conn.close()

def list_tasks(status=None, limit=None):
    """Retrieves and displays tasks from the database with optional filters."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        with conn.cursor() as cursor:
            query = "SELECT id, description, status, created_at, updated_at FROM Tasks"
            params = []
            
            if status:
                query += " WHERE status = ?"
                params.append(status)
            
            if limit:
                query += " ORDER BY created_at DESC OFFSET 0 ROWS FETCH NEXT ? ROWS ONLY"
                params.append(limit)
            
            cursor.execute(query, params)
            tasks = cursor.fetchall()
            
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(f"[{task[0]}] {task[1]} - {task[2]} (Created: {task[3]}, Updated: {task[4]})")
    except Exception as e:
        print(f"Error retrieving tasks: {e}")
    finally:
        conn.close()

def update_task(task_id, new_description):
    """Updates the description of a task."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Tasks SET description = ?, updated_at = GETDATE() WHERE id = ?", (new_description, task_id))
            conn.commit()
            print(f"Task {task_id} updated successfully.")
    except Exception as e:
        print(f"Error updating task: {e}")
    finally:
        conn.close()

def delete_task(task_id):
    """Deletes a task from the database."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM Tasks WHERE id = ?", (task_id,))
            conn.commit()
            print(f"Task {task_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting task: {e}")
    finally:
        conn.close()

def mark_in_progress(task_id):
    """Marks a task as 'in-progress'."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Tasks SET status = 'in-progress', updated_at = GETDATE() WHERE id = ?", (task_id,))
            conn.commit()
            print(f"Task {task_id} marked as in-progress.")
    except Exception as e:
        print(f"Error updating task status: {e}")
    finally:
        conn.close()

def mark_done(task_id):
    """Marks a task as 'done'."""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database.")
        return
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE Tasks SET status = 'done', updated_at = GETDATE() WHERE id = ?", (task_id,))
            conn.commit()
            print(f"Task {task_id} marked as done.")
    except Exception as e:
        print(f"Error updating task status: {e}")
    finally:
        conn.close()
