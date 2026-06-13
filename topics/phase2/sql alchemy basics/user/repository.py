from models import User
from sqlalchemy import select 

class UserRepository:
    def __init__(self, session):
        self.session = session
    
    def create_user(self , user : User):
        self.session.add(user)

    def get_by_id(self , id:int):
        return self.session.get(User,id)
    
    def get_by_email(self,email:str):
        stmt = select(User).where(
            User.email == email
        )
        user= self.session.execute(stmt).scalar().first()
        if user:
            return user
        return None