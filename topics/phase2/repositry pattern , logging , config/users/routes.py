from users.repository import UserRepository
from users.services import UserService
from fastapi import APIRouter, Depends
import logging
user_router = APIRouter()
logger = logging.getLogger(__name__)
def get_user_repository():
    return UserRepository()

def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(user_repository)

@user_router.get("/users/{id}")
def get_user(id: int, user_service: UserService = Depends(get_user_service)):
    logger.info("request recieved")
    return user_service.get_user(id)