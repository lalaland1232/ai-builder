from fastapi import FastAPI
from fastapi import HTTPException
from exceptions import UserNotFound
from users.routes import user_router
from fastapi.responses import JSONResponse as Json
app = FastAPI()
app.include_router(user_router)
@app.exception_handler(UserNotFound)
def user_not_found_handler(request, exc):
    return Json(status_code=404, content={"detail": "User not found"})


