from app.db.models import Role
class DeleteUserService:
    def __init__(self, repository,db):
        self.repository = repository
        self.db=db
    def delete_user(self, user_id: int,user):
        role = self.db.get(Role, user.role_id)
        if role.name =="user":
            if user.id != user_id:
                raise Exception("You do not have permission to delete this user.")
        try:
            self.repository.delete_refresh_tokens(user_id)
            self.repository.delete_artifact(user_id)
            self.repository.delete_user(user_id)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error occurred while deleting user: {e}")