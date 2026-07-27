
from fastapi import Depends
from app.db.models import *
from sqlalchemy import select
from sqlalchemy.orm import selectinload
def get_user_by_email(email: str , db):
    stmt = select(User).where(User.email == email).options(selectinload(User.artifact))
    return db.execute(stmt).scalar()

def get_user_by_id(id:int,db):
    return db.get(User,id)

def add_artifact(artifact,id,db):
    artifact = Artifact(artifact=artifact,id=id)
    db.add(artifact)

def add_refresh_token(hashed_token,db,user_id,ip,device,created_at,expire):
    refresh_token = RefreshToken(hashed_token=hashed_token,user_id=user_id,ip=ip,device=device,created_at=created_at,expire=expire,revoked_at=None)
    db.add(refresh_token)