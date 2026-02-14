from datetime import datetime
from storage import load_notes, save_notes


def add_note(text):
    notes = load_notes()

    new_id = 1 if not notes else notes[-1]['id'] + 1

    note = {
        'id': new_id,
        'text': text,
        'status': 'To do',
        'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    save_notes(notes)

    print('Added note #{}'.format(new_id))


def list_notes() -> None:
    notes = load_notes()
    for note in notes:
        print(f'{note["id"]}: {note["text"]}|{note["status"]}|{note["createdAt"]}')


def delete_note(note_id):
    notes = load_notes()
    notes = [n for n in notes if n["id"] != note_id]
    save_notes(notes)

    print('Deleted note #{}'.format(note_id))


def find_notes(keyword):
    notes = load_notes()

    for note in notes:
        if keyword.lower() in note['text'].lower():
            print(f'{note["id"]}: {note["text"]}|{note["status"]}|{note["createdAt"]}')


def edit_note(note_id: object, text: object) -> None:
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            if text.lower() == "done":
                note['status'] = 'Done'
            else:
                note['text'] = text

    save_notes(notes)
    print('Edited note #{}'.format(note_id))
