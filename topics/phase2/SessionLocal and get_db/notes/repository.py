from models import Notes

class NotesRepository:
    def __init__(self,session):
        self.session=session
    
    def create_notes(self,request):
        notes =Notes(
            title=request.title,
            content=request.content,
            notebook_id=request.notebook_id
        )
        self.session.add(notes)

    def get_notes(self,id):
        return self.session.get(Notes,id)