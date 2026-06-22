from fastapi import FastAPI
from notebook.route import api_router
from database import Base, engine
from notes.route import notes_api_route
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api_router)
app.include_router(notes_api_route)