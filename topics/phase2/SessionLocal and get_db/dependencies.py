from notebook.repository import NotebookRepository
from notebook.service import NotebookService
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from notes.repository import NotesRepository
from notes.service import NotesService
def get_notebook_repository(db:Session=Depends(get_db)):
    return NotebookRepository(db)

def get_notebook_service(repository:NotebookRepository=Depends(get_notebook_repository),db:Session=Depends(get_db)):
    return NotebookService(repository=repository,session=db)

def get_notes_repository(db:Session=Depends(get_db)):
    return NotesRepository(db)

def get_notes_service(repository:NotesRepository=Depends(get_notes_repository),db:Session=Depends(get_db)):
    return NotesService(repository=repository,session=db)