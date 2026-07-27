from fastapi import APIRouter,Depends
from app.core.security import get_current_user
from app.db.database import get_db
delete_router=APIRouter()
from app.api.auth import required_permission
from app.delete_user.service import DeleteUserService
from app.delete_user.repository import DeleteUserRepository
def get_delete_repo(db=Depends(get_db)):
    return DeleteUserRepository(db)
def get_delete_service(repo=Depends(get_delete_repo),db=Depends(get_db)):
    return DeleteUserService(repo,db)
@delete_router.delete("/delete/{id}",dependencies=[Depends(required_permission(["delete_user","delete_own_user"]))])
def delete_user(id:int,service=Depends(get_delete_service),user=Depends(get_current_user)):
    print ("hi")
    return service.delete_user(id,user)