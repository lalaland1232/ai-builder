from dotenv import load_dotenv
load_dotenv()
from users.routes import user_router
from core.config import Settings
from exceptions import UserNotFound
from fastapi.responses import JSONResponse

import core.logging
from fastapi import FastAPI
  
settings =Settings()
app = FastAPI()
if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")
if not settings.JWT_SECRET:
    raise ValueError("JWT_SECRET is not set in the environment variables.")

@app.exception_handler(UserNotFound)
def user_not_found_exception(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "User not found"}
    )
app.include_router(user_router)