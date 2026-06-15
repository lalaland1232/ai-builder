from fastapi import APIRouter, Depends
from models import session
from users.repository import UserRepository
from users.service import UserService
from schemas import UserCreateRequest
api_route = APIRouter()
def get_repository():
    return UserRepository()
def get_service(user_repo=Depends(get_repository)):
    return UserService(session=session, user_repository=user_repo)

@api_route.post("/users")
def create_user(request: UserCreateRequest, user_service: UserService = Depends(get_service)):
    return user_service.create_user(request)
    
@api_route.get("/users/{id}")
def get_user_by_id(id:int,user_service:UserService = Depends(get_service)):
    user= user_service.get_user_by_id(id)
    if user:
        return user
    return {"message":"User not found"}
@api_route.get("/users/email/{email}")
def get_user_by_email(email:str,user_service:UserService = Depends(get_service)):
    user= user_service.get_user_by_email(email)
    if user:
        return user
    return {"message":"User not found"}