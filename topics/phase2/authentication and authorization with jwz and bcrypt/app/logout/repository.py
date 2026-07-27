from sqlalchemy import update
from datetime import datetime , timezone
from app.db.models import RefreshToken
class LogoutRepository:
    def __init__(self, db):
        self.db = db

    def logout(self, token):
        stmt = update(RefreshToken).where(RefreshToken.hashed_token == token).values(revoked_at=datetime.now(timezone.utc))
        return self.db.execute(stmt)