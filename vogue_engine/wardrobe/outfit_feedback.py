"""Local outfit feedback and explainable preference adjustments (Stage 42)."""
from __future__ import annotations
import sqlite3
from pathlib import Path

DDL = '''CREATE TABLE IF NOT EXISTS outfit_feedback (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 signature TEXT NOT NULL UNIQUE,
 rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
 favorite INTEGER NOT NULL DEFAULT 0 CHECK(favorite IN (0,1)),
 notes TEXT NOT NULL DEFAULT '',
 updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);'''


def signature(ids: list[int]) -> str:
    if len(ids) != 3 or len(set(ids)) != 3 or any(not isinstance(i, int) or isinstance(i, bool) or i <= 0 for i in ids):
        raise ValueError('Exactly three distinct positive garment IDs are required')
    return ','.join(map(str, sorted(ids)))


class FeedbackStore:
    def __init__(self, db_path: str):
        self.db_path = str(db_path)
        if self.db_path != ':memory:':
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as db:
            db.execute(DDL)

    def _connect(self):
        db = sqlite3.connect(self.db_path)
        db.row_factory = sqlite3.Row
        return db

    def save(self, ids: list[int], rating: int, favorite: bool = False, notes: str = '') -> dict:
        key = signature(ids)
        if type(rating) is not int or not 1 <= rating <= 5:
            raise ValueError('Rating must be an integer from 1 to 5')
        if type(favorite) is not bool or len(notes) > 500:
            raise ValueError('Invalid favorite or notes')
        with self._connect() as db:
            db.execute('''INSERT INTO outfit_feedback(signature,rating,favorite,notes) VALUES (?,?,?,?)
                ON CONFLICT(signature) DO UPDATE SET rating=excluded.rating, favorite=excluded.favorite,
                notes=excluded.notes, updated_at=CURRENT_TIMESTAMP''', (key, rating, int(favorite), notes))
            return dict(db.execute('SELECT * FROM outfit_feedback WHERE signature=?', (key,)).fetchone())

    def list(self) -> list[dict]:
        with self._connect() as db:
            return [dict(row) for row in db.execute('SELECT * FROM outfit_feedback ORDER BY updated_at DESC, id DESC')]

    def delete(self, ids: list[int]) -> bool:
        with self._connect() as db:
            return bool(db.execute('DELETE FROM outfit_feedback WHERE signature=?', (signature(ids),)).rowcount)


def apply_feedback(recommendations: list[dict], feedback: list[dict]) -> list[dict]:
    """Re-rank scored recommendations; never mutate the engine's original objects."""
    indexed = {item['signature']: item for item in feedback}
    result = []
    for recommendation in recommendations:
        entry = dict(recommendation)
        found = indexed.get(signature(entry['garment_ids']))
        adjustment = (found['rating'] - 3) * 4 + (10 if found['favorite'] else 0) if found else 0
        entry['base_score'] = entry['score']
        entry['feedback_adjustment'] = adjustment
        entry['score'] = max(0, min(100, entry['score'] + adjustment))
        entry['user_rating'] = found['rating'] if found else None
        entry['outfit_favorite'] = bool(found['favorite']) if found else False
        entry['reasons'] = list(entry['reasons']) + (['Adjusted using your saved outfit feedback'] if found else [])
        result.append(entry)
    return sorted(result, key=lambda r: (-r['score'], r['garment_ids']))
