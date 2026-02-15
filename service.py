from models import Note
from repository import NoteRepository

class NoteService:
    def __init__(self):
        self.repo = NoteRepository()


    def add(self, text):
        note = Note.create(0, text)
        self.repo.add(note)
        print('Added note')


    def list(self) -> None:
        return self.repo.load()


    def delete(self, note_id):
        self.repo.delete(note_id)
        print('Deleted note #{}'.format(note_id))


    def find(self, keyword):
        notes = self.repo.load()

        return [n for n in notes if keyword.lower() in n.text.lower()]


    def edit(self, note_id: object, text: object) -> None:
        notes = self.repo.load()
        for note in notes:
            if note.id == note_id:
                if text.lower() == "done":
                    note.status = 'Done'
                else:
                    note.text = text
                print(note.id, note.text, note.status, note.created_at)
                self.repo.update(note)
        print('Edited note #{}'.format(note_id))
