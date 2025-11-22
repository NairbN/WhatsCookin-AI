from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create Database URL
SQLALCHEMY_DATABASE_URL = "postgresql://ryleymao@localhost/todo_api"

# Engine manages actual connection to PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()