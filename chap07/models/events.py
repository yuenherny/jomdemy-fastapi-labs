from sqlmodel import SQLModel, Field, Column, JSON
from typing import List, Optional


class Event(SQLModel, table=True):
    """For data validation and DB operation"""
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        pk_with_sequence = True # auto increment


class EventUpdate(SQLModel):
    """For data validation only"""
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]] = Field(sa_column=Column(JSON))
    location: Optional[str]