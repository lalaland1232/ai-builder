from datetime import timezone,datetime

from app.core.security import authenticate_user, create_access_token,create_refresh_token
from fastapi import HTTPException
import hashlib
class LoginService:
    def __init__(self,db,repository):
        self.db = db
        self.repository = repository

    def login(self,request,req):
        user = authenticate_user(email=request.email,password=request.password,db=self.db)
        if user:
            claims={"sub":str(user.id)}
            try:
                access_token = create_access_token(claims=claims)
                refresh_token = create_refresh_token(claims=claims)
                hashed_token=hashlib.sha256(refresh_token["token"].encode("utf-8")).digest()
                self.repository.add_refresh_token(hashed_token=hashed_token,ip=req.client.host,device=req.headers.get("user-agent"),created_at=refresh_token["created_at"],expire=refresh_token["expire"],user_id=user.id)
                self.db.commit()
                return {"access_token":access_token,"refresh_token":refresh_token["token"],"type":"bearer"}
            except Exception as e:
                print(e)
                self.db.rollback()
                raise HTTPException(status_code=500,detail="Internal server error")
        raise HTTPException(status_code=401,detail="Invalid email or password")

    
    