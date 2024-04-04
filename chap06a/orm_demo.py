from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base() # returns a Base class
Session = sessionmaker(bind=engine) # returns Session class
sess = Session()

class User(Base):
    """Represents User table."""
    __tablename__ = 'users' # optional, not required if table and class name matches
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String[50])
    email = Column(String)


# Tables are automatically created by SQLAlchemy based on previous class
Base.metadata.create_all(engine)

# Insert data into users table
new_user = User(name="John Doe", email="john@gmail.com")
sess.add(new_user)
sess.commit()
