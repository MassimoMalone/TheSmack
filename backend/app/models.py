from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Text, Boolean, ForeignKey, TIMESTAMP
from .database import Base


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    users_email: Mapped[str] = mapped_column(String, unique=True) 
    users_password: Mapped[str] = mapped_column(Text, nullable=False)

    smacks: Mapped[list["Smack"]] = relationship(back_populates="user")


class Feelings(Base):
    __tablename__ = "feelings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    smacks: Mapped[list["Smack"]] = relationship(back_populates="feeling_rel")


class Smacks(Base):
    __tablename__ = "smacks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    smack_username: Mapped[str] = mapped_column(String(15), ForeignKey("users.username"))
    feeling_id: Mapped[int] = mapped_column(Integer, ForeignKey("feelings.id"))
    feeling: Mapped[str] = mapped_column(String(20), ForeignKey("feelings.name"))
    blurb: Mapped[str] = mapped_column(String(250))
    posted_at: Mapped[str] = mapped_column(TIMESTAMP)
    likes: Mapped[int] = mapped_column(Integer, default=0)
    edited_at: Mapped[str] = mapped_column(TIMESTAMP)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship(back_populates="smacks")
    feeling_rel: Mapped["Feeling"] = relationship(back_populates="smacks")
