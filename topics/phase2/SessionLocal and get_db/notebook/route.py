from fastapi import APIRouter, Depends
from dependencies import get_notebook_service
from notebook.service import NotebookService
from schema import CreateNotebookRequest


api_router=APIRouter()
@api_router.get("/notebook/{id}")
def get_notebook(id:int,service:NotebookService=Depends(get_notebook_service)):
    return service.get_notebook(id)

@api_router.post("/notebook")
def post_notebook(request:CreateNotebookRequest,service:NotebookService=Depends(get_notebook_service)):
    return service.create_notebook(request)

@api_router.get("/notebook/{id}/notes")
def get_notebook_notes(id:int,service:NotebookService=Depends(get_notebook_service)):
    return service.get_notebook_notes(id)

@api_router.delete("/notebook/{id}")
def delete_notebook(id:int,service:NotebookService=Depends(get_notebook_service)):
    return service.delete_notebook(id)

@api_router.get("/notebooks")
def get_all_notebooks(service:NotebookService=Depends(get_notebook_service)):
    return service.get_all_notebooks()

@api_router.get("/notebooks/with-notes")
def get_notebooks_with_their_notes(service:NotebookService=Depends(get_notebook_service)):
    return service.get_notebooks_with_their_notes()