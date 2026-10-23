"""Local SQLite persistence for reports; no remote services or credentials."""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from vogue_engine.core.engine.schemas.style_payload import MasterVogueStyleReport

DEFAULT_PATH = Path.home() / '.vogue_engine' / 'reports.sqlite3'

class ReportStore:
    def __init__(self, path=None):
        self.path = Path(path) if path else DEFAULT_PATH
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS reports (id TEXT PRIMARY KEY, payload TEXT NOT NULL, created_at TEXT NOT NULL)')

    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        return db

    def save(self, report):
        with self.connect() as db:
            db.execute('INSERT OR REPLACE INTO reports VALUES (?,?,?)',
                       (report.report_uuid, report.model_dump_json(), datetime.now(timezone.utc).isoformat()))

    def get(self, report_id):
        with self.connect() as db:
            row = db.execute('SELECT payload FROM reports WHERE id=?', (report_id,)).fetchone()
        return MasterVogueStyleReport.model_validate_json(row['payload']) if row else None

    def list(self, limit=50):
        with self.connect() as db:
            return [dict(row) for row in db.execute('SELECT id,created_at FROM reports ORDER BY created_at DESC LIMIT ?', (limit,))]

    def delete(self, report_id):
        with self.connect() as db:
            return bool(db.execute('DELETE FROM reports WHERE id=?', (report_id,)).rowcount)

    def clear(self):
        with self.connect() as db:
            count = db.execute('SELECT COUNT(*) FROM reports').fetchone()[0]
            db.execute('DELETE FROM reports')
            return count
