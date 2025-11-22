from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collections.abc import Generator

from app.core.config import settings

DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI

# El check_same_thread es necesario para SQLite
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()