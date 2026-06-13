from fastapi import Depends
from users.reposetries import UserRepository
from exceptions import UserNotFound


class UserService:
    def __init__(self ,user_repo):
        self.user_reposetory = user_repo
    def get_user(self , id):
        print("called1")
        response = self.user_reposetory.get_user(id)
        print(response)
        if response == None:
            raise UserNotFound()
        return response