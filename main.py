from service import NoteService

service = NoteService()

def main():
    print('Note manager')
    print('Commands: add, list, delete, find, edit, exit')

    while True:
        task = input('Enter command: ').strip()

        if task.startswith('add '):
            text = task[4:]
            service.add(text)

        elif task == 'list':
            notes = service.list()
            for n in notes:
                print(f'{n.id}|{n.text}|{n.status}|{n.created_at}')

        elif task.startswith('delete '):
            print('Are you sure you want to delete this note?')
            answer = input('y/n: ')
            if answer == 'y':
                service.delete(int(task.split()[1]))
            else:
                print('Aborted')

        elif task.startswith('find '):
            keyword = task[5:].strip('')
            results = service.find(keyword)
            for n in results:
                print(f'{n.id}|{n.text}|{n.status}|{n.created_at}')

        elif task.startswith('edit '):
            note_id = int(task.split()[1])
            parts = task.split()
            text = " ".join(parts[2:]) if len(parts) > 2 else ""
            service.edit(note_id, text)

        elif task == 'exit':
            break

        else:
            print('Invalid command')

if __name__ == '__main__':
    main()