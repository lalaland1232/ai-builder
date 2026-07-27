from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
from core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
