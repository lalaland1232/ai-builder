from app.db.models import RefreshToken
from sqlalchemy import select
class LoginRepository:
    def __init__(self,db):
        self.db = db
    def add_refresh_token(self,hashed_token,ip,device,created_at,expire,user_id):
        refresh_token = RefreshToken(hashed_token=hashed_token,ip=ip,device=device,created_at=created_at,expire=expire,user_id=user_id)
        self.db.add(refresh_token)
    
    def revoke_refresh_token(self,id):
        stmt = select(RefreshToken).where(RefreshToken.id==id)
        return self.db.execute(stmt).scalar_one_or_none()