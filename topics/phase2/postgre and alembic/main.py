from core.database import Base,engine,get_db
from core.models import User
from core.config import settings
from sqlalchemy import text
session=get_db()
db=next(session)
Base.metadata.create_all(bind=engine)