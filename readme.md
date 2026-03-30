# Note Manager

A console application for managing notes, built with Python and SQLite.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-built--in-lightgrey?style=flat-square)

---

## About

A pet project for learning layered architecture in Python. Implements a classic
three-layer structure — model, repository, service — applied to a simple CLI app.

---

## Features

- Add, edit, delete notes
- Mark a note as Done
- Search notes by keyword
- Confirmation prompt before deletion
- Data stored in SQLite

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Database | SQLite (stdlib `sqlite3`) |
| Model | `dataclasses` |
| Interface | CLI (stdin/stdout) |

No external dependencies — runs with the standard library only.

---

## Project Structure

```
note_manager/
├── models.py       # Note dataclass + factory method
├── repository.py   # NoteRepository — all SQL queries
├── service.py      # NoteService — business logic
└── main.py         # CLI interface
```

---

## Installation

```bash
git clone https://github.com/Zhelero/note_manager
cd note_manager
python main.py
```

No `pip install` needed — zero external dependencies.

---

## Usage

```
Note manager
Commands: add, list, delete, find, edit, exit
```

| Command | Description |
|---|---|
| `add <text>` | Add a new note |
| `list` | Show all notes |
| `delete <id>` | Delete a note (with confirmation) |
| `find <keyword>` | Search notes by keyword |
| `edit <id> <text>` | Edit note text |
| `edit <id> done` | Mark note as Done |
| `exit` | Exit the program |

### Example session

```
Enter command: add Read Clean Code
Added note

Enter command: add Write tests
Added note

Enter command: list
1|Read Clean Code|To do|2026-03-30 14:45
2|Write tests|To do|2026-03-30 14:46

Enter command: edit 1 done
Edited note #1

Enter command: list
1|Read Clean Code|Done|2026-03-30 14:45
2|Write tests|To do|2026-03-30 14:46

Enter command: find test
2|Write tests|To do|2026-03-30 14:46

Enter command: delete 2
Are you sure you want to delete this note?
y/n: y
Deleted note #2
```

---

## Architecture

The project follows a three-layer structure:

```
main.py  →  NoteService  →  NoteRepository  →  SQLite
  CLI         business          data access      storage
              logic
```

This separation makes it easy to swap out the storage layer (e.g. replace SQLite
with PostgreSQL) without touching the business logic or CLI code.

---

## License

MIT
