from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta , timezone
from app.core.config import settings
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
import bcrypt
from app.api import repository

oauth2_schema=OAuth2PasswordBearer(tokenUrl="/login")

def get_token(token=Depends(oauth2_schema)):
    return token

def create_token(payload:dict):
    token=jwt.encode(payload=payload,algorithm=settings.ALGORITHM,key=settings.SECRET_KEY)
    return token

def create_access_token(claims:dict):
    payload = claims.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload["exp"] = expire
    payload["type"] = "access"
    token = create_token(payload=payload)
    return token

def create_refresh_token(claims:dict):
    payload = claims.copy()
    expire= datetime.now(timezone.utc)+timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    payload["exp"] = expire
    payload["type"] = "refresh"
    token = create_token(payload=payload)
     
    return {"token":token,"expire":expire,"created_at":expire-timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)}

def authenticate_user(email:str , password:str,db:Session):
    user = repository.get_user_by_email(email=email,db=db)
    if not user:
        return False
    artifact = user.artifact.artifact
    if bcrypt.checkpw(password.encode("utf-8"), artifact):
        return user
    return False

def get_current_user(token=Depends(get_token),db=Depends(get_db)):
    try:
        
        payload=jwt.decode(jwt=token,key=settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        print("success")
        id = int(payload.get("sub"))
        user = repository.get_user_by_id(id=id,db=db)
        if user:
            return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="Token has expired")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401,detail="Invalid token")
    if not user:
        raise HTTPException(status_code=401,detail="User not found")

def create_artifact(password:str,id:int,db:Session):
    salt = bcrypt.gensalt()
    artifact = bcrypt.hashpw(password.encode("utf-8"),salt)
    repository.add_artifact(artifact=artifact,id=id,db=db)