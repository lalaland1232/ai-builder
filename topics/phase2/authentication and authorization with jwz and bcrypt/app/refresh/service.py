from sqlalchemy.orm import Session
from app.core.config import settings
from fastapi import HTTPException
from hashlib import sha256
from app.refresh.repository import RefreshRepository
from app.core.security import create_access_token, create_refresh_token
from app.api.repository import  add_refresh_token
import jwt
from datetime import datetime, timezone
class RefreshService():
    def __init__(self,db:Session,repo:RefreshRepository):
        self.db = db
        self.repository = repo
       
    def refresh(self,token:str,req):
       print("hihello")
       payload=jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
       if payload.get("type") != "refresh":
              raise HTTPException(status_code=400, detail="Invalid token type")

       hashed_token=sha256(token.encode()).digest()
       current_token = self.repository.check_token(hashed_token=hashed_token)
       if current_token is None or current_token.revoked_at is not None :
              raise HTTPException(status_code=400, detail="Invalid token or token has been revoked")
       try:
            claims={
                 "sub": payload.get("sub"),

            }
            
            new_refresh_token_dict= create_refresh_token(claims=claims)
            new_refresh_token = new_refresh_token_dict["token"]
            new_access_token = create_access_token(claims=claims)
            current_token.revoked_at = datetime.now(timezone.utc)
            new_hashed_token=sha256(new_refresh_token.encode()).digest()
            add_refresh_token(hashed_token=new_hashed_token,
                                db=self.db,
                                user_id=payload.get("sub"),
                                ip=req.client.host,
                                device=req.headers.get("User-Agent"),
                                created_at=new_refresh_token_dict["created_at"],
                                expire=new_refresh_token_dict["expire"]            )
            self.db.commit()
            return {"access_token": new_access_token, "refresh_token": new_refresh_token}
       except Exception as e:
            self.db.rollback()
            print(e)
            raise HTTPException(status_code=400, detail="Token refresh failed")