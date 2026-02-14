import json
import os

FILE_NAME = 'notes.json'

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_notes(notes):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)

