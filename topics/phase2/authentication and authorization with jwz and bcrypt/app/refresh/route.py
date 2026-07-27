

from fastapi import APIRouter, Depends,Request
refresh_router = APIRouter()
from app.core.security import get_token
from app.refresh.service import RefreshService
from app.refresh.repository import RefreshRepository
from app.db.database import get_db

def get_repo(db = Depends(get_db)):
    print("repo")
    return RefreshRepository(db)
def get_service(db = Depends(get_db), repo = Depends(get_repo)):
    print("service")
    return RefreshService(db, repo)

@refresh_router.post("/refresh")
def refresh(req: Request,token = Depends(get_token),service: RefreshService = Depends(get_service)):
    return service.refresh(token=token,req=req)