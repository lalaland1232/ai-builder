from fastapi import APIRouter, Depends, Request
from app.core.schemas import LoginRequest
from app.db.database import get_db
from app.db.models import User, Artifact
import bcrypt
from app.login.repository import LoginRepository
from app.login.service import LoginService


router = APIRouter()

def get_repository(db=Depends(get_db)):
    return LoginRepository(db)
def get_service(db=Depends(get_db), repository=Depends(get_repository)):
    return LoginService(db, repository)

@router.post("/login")
def login(request:LoginRequest,req:Request,service=Depends(get_service)):
    return service.login(request,req=req)
    
