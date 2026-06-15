from sqlalchemy import select
from schemas import UserCreateResponse
from models import User
class UserService:
    def __init__(self,session, user_repository):
        self.session = session
        self.user_repository = user_repository
        
    def create_user(self,request):
        stmt = select(User).where(User.email==request.email)
        result = self.session.execute(stmt).scalar()
        if result:
            raise Exception("User with this email already exists")
        user=self.user_repository.create_user(self.session,request)
        self.session.commit()
        return UserCreateResponse(
            id=user.id,
            name=user.name,
            email=user.email
        )
    
    def get_user_by_id(self,id:int):
        return self.user_repository.get_by_id(self.session,id)
    
    def get_user_by_email(self,email:str):
        return self.user_repository.get_by_email(self.session,email)
    