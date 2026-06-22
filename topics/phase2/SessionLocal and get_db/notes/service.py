
from schema import GetNotesResponse
class NotesService:
    def __init__(self,repository,session):
        self.repository=repository
        self.session=session

    def create_notes(self,request):
        try:
            self.repository.create_notes(request)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def get_notes(self,id):
        notes = self.repository.get_notes(id)
        response_notes= GetNotesResponse(
            title=notes.title,
            content=notes.content,
            created_at=notes.created_at
        )
        return response_notes
        