from models import Note
from repository import NoteRepository

class NoteService:
    def __init__(self):
        self.repo = NoteRepository()

    def add(self, text):
        notes = self.repo.load()
        new_id = 1 if not notes else notes[-1].id+1
        note = Note.create(new_id, text)

        notes.append(note)
        self.repo.save(notes)

        print('Added note #{}'.format(new_id))


    def list(self) -> None:
        return self.repo.load()

    def delete(self, note_id):
        notes = self.repo.load()
        notes = [n for n in notes if n.id != note_id]
        self.repo.save(notes)

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

        self.repo.save(notes)
        print('Edited note #{}'.format(note_id))
