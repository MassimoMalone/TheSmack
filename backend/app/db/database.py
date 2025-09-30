# app/db/database.py

from dotenv import load_dotenv
import os
import psycopg2 # <-- NEW: Import psycopg2
from contextlib import contextmanager # <-- NEW: For managing connections safely

# load_dotenv() # Assuming this is run correctly elsewhere, maybe in main.py or at startup

DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
print("this is the url: "+DATABASE_URL)

# --- We remove SQLAlchemy components (engine, SessionLocal, Base) ---

# NEW: Define a function that manages the connection and cursor
@contextmanager
def get_db_connection():
    """Provides a managed psycopg2 database connection."""
    conn = None
    try:
        # psycopg2 connection string format is slightly different; 
        # we parse the URL to get the components
        # NOTE: If the URL has 'postgresql+psycopg2://' you need to strip the prefix for psycopg2 to understand it.
        # Simple way to parse:
        from urllib.parse import urlparse
        
        url_components = urlparse(DATABASE_URL)
        
        conn = psycopg2.connect(
            database=url_components.path.lstrip('/'),
            user=url_components.username,
            password=url_components.password,
            host=url_components.hostname,
            port=url_components.port
        )
        yield conn
        
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        # In a real app, you might raise an HTTPException here
        raise e
    finally:
        if conn:
            conn.close()

# NEW: Function to get a cursor (used for executing commands)
@contextmanager
def get_db_cursor(commit: bool = False):
    """Provides a managed psycopg2 cursor."""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            try:
                yield cursor
                if commit:
                    conn.commit()
            except Exception as e:
                conn.rollback()
                raise e

# NOTE: If you still need Base for future migration tools, you can leave it, 
# but for raw psycopg2, you don't use it.