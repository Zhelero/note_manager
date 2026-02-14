from notes import add_note, list_notes, delete_note, find_notes, edit_note

def main():
    print('Input command:')
    print('Commands: add, list, delete, find, edit, exit')

    while True:
        task = input('Enter command: ')
        if task.startswith('add '):
            text = task[4:].strip('')
            add_note(text)

        elif task == 'list':
            list_notes()

        elif task.startswith('delete '):
            print('Are you sure you want to delete this note?')
            answer = input('y/n: ')
            if answer == 'y':
                note_id = int(task.split()[1])
                delete_note(note_id)
            else:
                print('Aborted')

        elif task.startswith('find '):
            key_word = task[5:].strip('')
            find_notes(key_word)

        elif task.startswith('edit '):
            note_id = int(task.split()[1])
            parts = task.split()
            text = " ".join(parts[2:]) if len(parts) > 2 else ""
            edit_note(note_id, text)

        elif task == 'exit':
            break

        else:
            print('Invalid command')

if __name__ == '__main__':
    main()