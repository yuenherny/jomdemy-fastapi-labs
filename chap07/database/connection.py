"""This will handle connection to database"""
from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "planner.db"
database_connection = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False} # only for SQLite
engine_url = create_engine(database_connection, echo=True)

def conn():
    """All tables will be created"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session
