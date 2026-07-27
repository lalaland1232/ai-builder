from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.core.security import get_token
from app.logout.repository import LogoutRepository
from app.logout.service import LogoutService
logout_router = APIRouter()
def get_repo(db=Depends(get_db)):
    return LogoutRepository(db)
def get_service(db=Depends(get_db), repo=Depends(get_repo)):
    return LogoutService(db, repo)
@logout_router.post("/logout")
def logout(token=Depends(get_token), service: LogoutService = Depends(get_service)):
    return service.logout(token)