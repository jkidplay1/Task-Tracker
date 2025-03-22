import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database credentials from .env
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER")

# Define connection string using Windows Authentication
CONN_STRING = f"DRIVER={DB_DRIVER};SERVER={DB_SERVER};DATABASE={DB_NAME};Trusted_Connection=yes;"

def get_db_connection():
    """Establish a connection to the SQL Server database using Windows Authentication."""
    try:
        conn = pyodbc.connect(CONN_STRING)
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
