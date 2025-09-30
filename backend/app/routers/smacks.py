# app/routers/smacks.py

from fastapi import APIRouter, HTTPException
# Remove SQLAlchemy imports
# from sqlalchemy.orm import Session 
# from sqlalchemy import select 
# from ..models import Smacks # <-- REMOVE
from ..db.database import get_db_cursor # <-- NEW: Import our raw connection function
from ..schemas import Smack # We still need the Pydantic schema!

router = APIRouter()

# Dependency to get a DB cursor - simplified
# We no longer need the get_db dependency function

@router.get("/smacks", response_model=list[Smack])
def read_smacks():
    
    # Raw SQL query
    query = """
    SELECT 
        s.id, s.blurb, s.posted_at, s.likes, 
        u.username AS author_name, 
        f.name AS feeling_name
    FROM smacks s
    JOIN users u ON s.smack_username = u.username
    JOIN feelings f ON s.feeling_id = f.id
    WHERE s.is_deleted = FALSE
    ORDER BY s.posted_at DESC;
    """

    try:
        with get_db_cursor() as cursor:
            # Execute the query
            cursor.execute(query)
            
            # Get the column names from the cursor description
            column_names = [desc[0] for desc in cursor.description]
            
            # Fetch all results
            results = cursor.fetchall()

            smacks_list = []
            for row in results:
                # Create a dictionary mapping column names to values
                smack_data = dict(zip(column_names, row))
                
                # Manually structure the data to match the Pydantic schema's nested fields
                structured_smack = {
                    "id": smack_data["id"],
                    "blurb": smack_data["blurb"],
                    "posted_at": smack_data["posted_at"],
                    "likes": smack_data["likes"],
                    "user": {"username": smack_data["author_name"]},
                    "feeling_rel": {"name": smack_data["feeling_name"]},
                }
                
                # Validate and convert the dictionary using the Pydantic model
                smack = Smack(**structured_smack)
                smacks_list.append(smack)
            
            return smacks_list

    except Exception as e:
        # If any database error occurs, return a server error to the client
        raise HTTPException(status_code=500, detail=f"Database query failed: {e}")