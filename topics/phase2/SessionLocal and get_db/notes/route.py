from fastapi import APIRouter, Depends
from dependencies import get_notes_service
from notes.service import NotesService
from schema import CreateNotesRequest
from schema import CreateNotesRequest
notes_api_route= APIRouter()
@notes_api_route.post("/notes")
def create_notes(request:CreateNotesRequest,service:NotesService=Depends(get_notes_service)):
    return service.create_notes(request)

@notes_api_route.get("/notes/{id}")
def get_notes(id:int,service:NotesService=Depends(get_notes_service)):
    return service.get_notes(id)

@notes_api_route.delete("/notes/{id}")
def delete_notes(id:int,service:NotesService=Depends(get_notes_service)):
    return service.delete_notes(id)
