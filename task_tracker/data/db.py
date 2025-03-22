import pyodbc

def get_db_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"
            "DATABASE=TaskTracker;"
            "Trusted_Connection=yes;",
            timeout=5  # Add a timeout to avoid long hangs
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None
