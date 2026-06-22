from models import Notebook
from sqlalchemy import select
from sqlalchemy.orm import joinedload
class NotebookRepository():
    def __init__(self,session):
        self.session=session

    
    def get_notebook(self,id):
        notebook = self.session.get(Notebook, id)
        return notebook
    
    def create_notebook(self,request):
        notebook=Notebook(
            title=request.title,
        )
        self.session.add(notebook)

    def get_notebook_notes(self,id):
        notebook=self.session.get(Notebook, id)
        return notebook.notes
    
    def delete_notebook(self,id):
        self.session.query(Notebook).filter(Notebook.id==id).delete()

    def get_all_notebooks(self):
        stmt = select(Notebook)
        notebooks=self.session.execute(stmt)
        return notebooks.scalars().all()
    def get_notebooks_with_their_notes(self):
        stmt = select(Notebook).options(joinedload(Notebook.notes))
        notes =self.session.execute(stmt)
        return notes.scalars().unique().all()