from fastapi import FastAPI
from users.route import api_route
app = FastAPI()
app.include_router(api_route)