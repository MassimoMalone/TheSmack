from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(15), unique=True, nullable=False)
    users_email = Column(String(250), unique=True)
    users_password = Column(Text, nullable=False)

    smacks = relationship("Smack", back_populates="user")

class Feeling(Base):
    __tablename__ = "feelings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, nullable=False)

    smacks = relationship("Smack", back_populates="feeling_obj")

class Smack(Base):
    __tablename__ = "smacks"
    id = Column(Integer, primary_key=True, index=True)
    smack_username = Column(String(15), ForeignKey("users.username"))
    feeling_id = Column(Integer, ForeignKey("feelings.id"))
    blurb = Column(String(250))
    posted_at = Column(TIMESTAMP)
    likes = Column(Integer, default=0)
    edited_at = Column(TIMESTAMP)
    is_deleted = Column(Boolean, default=False)

    user = relationship("User", back_populates="smacks")
    feeling_obj = relationship("Feeling", back_populates="smacks")
