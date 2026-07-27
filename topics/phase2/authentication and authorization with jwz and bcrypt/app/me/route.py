from fastapi import APIRouter,Depends
from app.core.security import get_current_user

merouter = APIRouter()
@merouter.get("/me")
def me(current_user=Depends(get_current_user)):
    return current_user