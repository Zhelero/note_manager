import json
import os
from models import Note

FILE_NAME = 'notes.json'

class NoteRepository:
    def load(self):
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Note(**item) for item in data]

    def save(self, notes):
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([note.__dict__ for note in notes], file,
                      ensure_ascii=False, indent=2)

