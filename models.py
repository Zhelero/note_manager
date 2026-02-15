from dataclasses import dataclass
from datetime import datetime

@dataclass
class Note:
    id: int
    text: str
    status: str
    created_at: str

    @staticmethod
    def create(note_id:int, text:str):
        return Note(
            id=note_id,
            text=text,
            status="To do",
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
