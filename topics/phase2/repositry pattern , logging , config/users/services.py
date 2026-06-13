import logging 
from exceptions import UserNotFound
logger = logging.getLogger(__name__)
class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def get_user(self,id):
        logger.info("validating user")
        user =self.user_repository.get_user(id)
        if user is None:
            logger.warning("User not found")
            raise UserNotFound()
        else:
            logger.info("User found")
            return user