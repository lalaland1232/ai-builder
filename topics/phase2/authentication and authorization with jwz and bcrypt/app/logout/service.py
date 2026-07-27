from hashlib import sha256
import jwt
from app.core.config import settings
class LogoutService:
    def __init__(self,db,repo):
        self.db = db
        self.repo = repo
    def logout(self, token):
        payload=jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type")!="refresh":
            raise ValueError("Invalid token type")
        hashed_token=sha256(token.encode()).digest()
        result=self.repo.logout(hashed_token)
        self.db.commit()
        if result.rowcount==0:
            raise ValueError("Token not found or already revoked")
        return {"message":"Logout successful"}