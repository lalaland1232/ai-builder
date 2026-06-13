from fastapi import Depends
from users.reposetries import UserRepository
from users.services import UserService
from exceptions import UserNotFound
from fastapi import APIRouter
user_router =APIRouter()
def get_user_service():
    repo = UserRepository()
    return UserService(repo)



@user_router.get("/users/{id}")
def get_user(id :int, user_service : UserService = Depends(get_user_service)):
    response =user_service.get_user(id)
    return response
