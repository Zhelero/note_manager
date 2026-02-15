from models import Note
import sqlite3

DB_NAME = 'notes.db'

class NoteRepository:
    def __init__(self) -> None:
        self._init_db()

    def _connect(self):
        return sqlite3.connect(DB_NAME)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    status TEXT,
                    created_at TEXT
                )
            """)

    def load(self):
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, text, status, created_at FROM notes"
            )
            rows = cursor.fetchall()
        return [
            Note(id=row[0], text=row[1], status=row[2], created_at=row[3]) for row in rows
        ]

    def add(self, note: Note) -> None:
        with self._connect() as conn:
            conn.execute("""
            INSERT INTO notes (text, status, created_at)
            VALUES (?, ?, ?)
            """, (note.text, note.status,note.created_at))

    def delete(self, note_id) -> None:
        with self._connect() as conn:
            conn.execute("""DELETE FROM notes WHERE id = ?""", (note_id,))

    def update(self, note: Note) -> None:
        with self._connect() as conn:
            conn.execute("""
                         UPDATE notes 
                         SET text = ?, status = ?, created_at = ?
                         WHERE id = ?
                         """, (note.text, note.status, note.created_at, note.id))