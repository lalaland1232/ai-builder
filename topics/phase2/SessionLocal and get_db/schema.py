from datetime import datetime

from pydantic import BaseModel
class GetNotebookResponse(BaseModel):
    title:str
    created_at:datetime

class GetNotesResponse(BaseModel):
    title:str
    content:str
    
    created_at:datetime

class CreateNotebookRequest(BaseModel):
    title:str

class CreateNotesRequest(BaseModel):
    title:str
    content:str
    notebook_id:int
    