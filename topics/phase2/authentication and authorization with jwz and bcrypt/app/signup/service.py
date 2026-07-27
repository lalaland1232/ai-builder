from app.core.security import create_artifact, create_access_token
from app.login.repository import LoginRepository
from app.login.service import LoginService
class SignUpService:
    def __init__(self, repo, db):
        self.repo = repo
        self.db = db

    def signup(self, request,req):
        if self.repo.find_user_by_email(request.email):
            raise ValueError("User with this email already exists")
        
        try:
            
            user = self.repo.add_user(request)
            create_artifact(password=request.password, id=user.id, db=self.db)
            self.db.commit()
            lr=LoginRepository(self.db)
            ls = LoginService(self.db, lr)
            return ls.login(request, req=req)
            
        except Exception as e:
            self.db.rollback()
            raise e
