from sqlalchemy import select
from app.db.models import User
class SignUpRepository:
    def __init__(self, db):
        self.db = db

    def find_user_by_email(self,email):
        stmt = select(User).filter(User.email == email)
        user =self.db.execute(stmt).scalar_one_or_none()
        return user
    
    def add_user(self,request):
        user = User(email=request.email,name=request.name)
        self.db.add(user)
        self.db.flush()  # Flush to get the user ID for artifact creation
        return user
        