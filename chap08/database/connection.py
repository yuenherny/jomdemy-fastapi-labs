"""This will handle connection to database"""
from sqlmodel import SQLModel, Session, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

database_file = f"../{os.getenv("DB_NAME")}"
database_connection = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False} # only for SQLite
engine_url = create_engine(database_connection, echo=True)

def conn():
    """All tables will be created"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session
