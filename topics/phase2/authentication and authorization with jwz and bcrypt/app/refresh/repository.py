from sqlalchemy.orm import Session

from sqlalchemy import select
from app.db.models import RefreshToken

class RefreshRepository:
    def __init__(self, db: Session):
        self.db = db
        

    def check_token(self,hashed_token:bytes):
        stmt = select(RefreshToken).where(RefreshToken.hashed_token == hashed_token)
        return  self.db.execute(stmt).scalar_one_or_none()
        