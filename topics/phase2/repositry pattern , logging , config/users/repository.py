import logging
logger = logging.getLogger(__name__)

class UserRepository:
    def get_user(self,id):
        logger.info("fetching user")
        if id == 1:
            logger.info("user found")
            return {"id":1,"name":"BaBa"}
        elif id == 2:
            logger.info("user found")
            return {"id":2,"name":"Tony"}
        logger.warning("user not found")
        return None