
from fastapi import Depends, FastAPI
from app.me.route import merouter
from app.login.route import router
from app.db.database import Base,engine
from app.db.models import *
from app.signup.route import signup_router
from app.core.security import get_token
from app.refresh.route import refresh_router
from app.logout.route import logout_router
from app.delete_user.route import delete_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(merouter)
app.include_router(router)
app.include_router(refresh_router)
app.include_router(signup_router)
app.include_router(logout_router)
app.include_router(delete_router)
