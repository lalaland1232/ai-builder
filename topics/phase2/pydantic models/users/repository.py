import models as m
from schemas import UserCreateResponse
from sqlalchemy import select
class UserRepository:
    def create_user(self,session,request):
        user = m.User(
            
            name=request.name,
            email=request.email
        )
        session.add(user)
        return user
    
    def get_by_id(self,session,id:int):
        user = session.get(m.User,id)
        if user:
            return UserCreateResponse(
                id=user.id,
                name=user.name,
                email=user.email
            )
        return None
    
    def get_by_email(self,session,email:str):
        stmt = select(m.User).where(m.User.email==email)
        user = session.execute(stmt).scalar()
        if user:
            return UserCreateResponse(
                id=user.id,
                name=user.name,
                email=user.email
            )
        return None

         
