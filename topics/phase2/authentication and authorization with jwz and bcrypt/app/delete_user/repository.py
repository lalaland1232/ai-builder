
from app.db.models import *


class DeleteUserRepository:
    def __init__(self, db):
        self.db = db

    def delete_user(self, user_id: int):
        self.db.query(User).filter(User.id == user_id).delete()
    def delete_refresh_tokens(self, user_id: int):
        self.db.query(RefreshToken).filter(RefreshToken.user_id == user_id).delete()
    def delete_artifact(self, user_id: int):
        self.db.query(Artifact).filter(Artifact.id == user_id).delete()