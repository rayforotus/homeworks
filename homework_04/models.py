"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    "postgresql+asyncpg://user:password@localhost/otus",
    echo=True,
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Session = scoped_session(async_session)

Session = async_scoped_session(async_session, scopefunc=asyncio.current_task)

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String(32), unique=True)
    phone = Column(String(32))
    website = Column(String(256))

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    title = Column(String)
    body = Column(String)

    user = relationship("User", back_populates="posts")
