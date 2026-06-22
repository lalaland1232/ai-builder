from schema import GetNotebookResponse
class NotebookService:
    def __init__(self,repository,session):
        self.repository=repository
        self.session=session
    
    def create_notebook(self,request):
        try:
            self.repository.create_notebook(request)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get_notebook(self,id):
        try :
            notebook = self.repository.get_notebook(id)
            notebook_response = GetNotebookResponse(
                title=notebook.title,
                created_at=notebook.created_at
            )
            return notebook_response
        except Exception as e:
            self.session.rollback()
            raise e
        
    def create_notebook(self,request):
        try:
            self.repository.create_notebook(request)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    def get_notebook_notes(self,id):
        try:
            notes = self.repository.get_notebook_notes(id)
            return notes
        except Exception as e:
            self.session.rollback()
            raise e
    def delete_notebook(self,id):
        try:
            self.repository.delete_notebook(id)
            self.session.commit()
            return {"message":"Notebook deleted successfully"}
        except Exception as e:
            self.session.rollback()
            raise e
    def get_all_notebooks(self):
        
            notebooks = self.repository.get_all_notebooks()
            return notebooks
        
    def get_notebooks_with_their_notes(self):
        return self.repository.get_notebooks_with_their_notes()