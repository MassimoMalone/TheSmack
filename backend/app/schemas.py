from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# --- Existing User Schemas ---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        # Use from_attributes for SQLAlchemy 2.0 style
        from_attributes = True 

# --- New Smack Schemas ---

class SmackUser(BaseModel):
    username: str

    class Config:
        from_attributes = True

# 2. Schema for the Feeling info nested in a Smack response
class SmackFeeling(BaseModel):
    name: str

    class Config:
        from_attributes = True

# 3. Schema for the Smack itself (the API response)
class Smack(BaseModel):
    id: int
    blurb: str
    posted_at: datetime
    likes: int
    
    # Nested relationships
    user: SmackUser 
    feeling_rel: SmackFeeling

    class Config:
        from_attributes = True