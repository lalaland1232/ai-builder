

from fastapi import APIRouter, Depends, Request
from app.signup.service import SignUpService
from app.signup.repository import SignUpRepository
from app.core.schemas import SignUpRequest
from app.db.database import get_db
signup_router = APIRouter()
def get_repo(db=Depends(get_db)):
    return SignUpRepository(db)
def get_service(repo=Depends(get_repo),db=Depends(get_db)):
    return SignUpService(repo,db)
@signup_router.post("/signup")
def signup(request: SignUpRequest, req: Request, service=Depends(get_service)):

    return service.signup(request,req)