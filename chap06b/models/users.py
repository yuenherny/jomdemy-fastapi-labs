from pydantic import EmailStr
from typing import List, Optional
from models.events import Event
from sqlmodel import SQLModel, Field, Column, String


class User(SQLModel, table=True):
    email: EmailStr = Field(sa_column=Column(String, unique=True, primary_key=True))
    title: str
    password: str


class UserSignIn(SQLModel):
    email: EmailStr
    password: str
