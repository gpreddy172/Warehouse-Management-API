from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_NAME = "warehouse.db"

# Ensure the database file exists
if not os.path.exists(DB_NAME):
    open(DB_NAME, 'a').close()

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()