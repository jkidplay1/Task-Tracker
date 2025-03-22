import bcrypt
from task_tracker.data.database import get_db_connection
from task_tracker.data.user_model import User
import pyodbc

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def register_user(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Hash password
        hashed_password = hash_password(user.password)

        # Insert user into database
        cursor.execute(
            "INSERT INTO Users (username, email, password_hash) VALUES (?, ?, ?)",
            (user.username, user.email, hashed_password)
        )
        conn.commit()
        return {"message": "User registered successfully"}
    except pyodbc.Error as e:
        return {"error": str(e)}
    finally:
        conn.close()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login_user(email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT password_hash FROM Users WHERE email=?", (email,))
        result = cursor.fetchone()

        if not result:
            return {"error": "User not found"}

        stored_password_hash = result[0]
        if verify_password(password, stored_password_hash):
            return {"message": "Login successful"}
        else:
            return {"error": "Invalid password"}
    except pyodbc.Error as e:
        return {"error": str(e)}
    finally:
        conn.close()
