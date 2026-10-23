"""Offline garment lifecycle, donation and recycling ledger.

Environmental figures are deliberately not invented: this module reports item
counts and reuse rates, not unverified carbon or water savings.
"""
from __future__ import annotations
from datetime import date
from .storage import WardrobeStore

DESTINATIONS = {'donated', 'recycled', 'repaired', 'resold', 'discarded'}

class SustainabilityStore:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with wardrobe.connection() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS garment_lifecycle (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
                action TEXT NOT NULL CHECK(action IN ('donated','recycled','repaired','resold','discarded')),
                event_date TEXT NOT NULL,
                recipient TEXT NOT NULL DEFAULT '',
                notes TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS idx_lifecycle_garment ON garment_lifecycle(garment_id);
            CREATE INDEX IF NOT EXISTS idx_lifecycle_date ON garment_lifecycle(event_date);
            ''')

    def record(self, garment_id: int, action: str, event_date: date,
               recipient: str = '', notes: str = '') -> dict:
        action = action.strip().lower()
        if action not in DESTINATIONS:
            raise ValueError('Unsupported lifecycle action')
        if not self.wardrobe.get(garment_id):
            raise LookupError('Garment not found')
        if len(recipient) > 200 or len(notes) > 2000:
            raise ValueError('Recipient or notes too long')
        with self.wardrobe.connection() as db:
            cur = db.execute('''INSERT INTO garment_lifecycle
                (garment_id,action,event_date,recipient,notes) VALUES (?,?,?,?,?)''',
                (garment_id, action, event_date.isoformat(), recipient.strip(), notes.strip()))
            return dict(db.execute('SELECT * FROM garment_lifecycle WHERE id=?', (cur.lastrowid,)).fetchone())

    def history(self, garment_id: int | None = None, action: str | None = None,
                limit: int = 100) -> list[dict]:
        if not 1 <= limit <= 500:
            raise ValueError('Limit must be between 1 and 500')
        if action is not None and action not in DESTINATIONS:
            raise ValueError('Unsupported lifecycle action')
        query = '''SELECT l.*, g.name AS garment_name FROM garment_lifecycle l
            JOIN garments g ON g.id=l.garment_id WHERE 1=1'''
        args = []
        if garment_id is not None:
            query += ' AND l.garment_id=?'; args.append(garment_id)
        if action is not None:
            query += ' AND l.action=?'; args.append(action)
        query += ' ORDER BY l.event_date DESC,l.id DESC LIMIT ?'; args.append(limit)
        with self.wardrobe.connection() as db:
            return [dict(r) for r in db.execute(query, args)]

    def delete(self, event_id: int) -> bool:
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM garment_lifecycle WHERE id=?', (event_id,)).rowcount)

    def report(self, year: int | None = None) -> dict:
        if year is not None and not 1900 <= year <= 9999:
            raise ValueError('Invalid year')
        query = 'SELECT action, COUNT(*) AS total, COUNT(DISTINCT garment_id) AS garments FROM garment_lifecycle'
        args = []
        if year is not None:
            query += ' WHERE substr(event_date,1,4)=?'; args.append(str(year))
        query += ' GROUP BY action'
        with self.wardrobe.connection() as db:
            rows = [dict(r) for r in db.execute(query, args)]
            garments = db.execute('SELECT COUNT(*) FROM garments').fetchone()[0]
            by_month_query = 'SELECT substr(event_date,1,7) AS month, COUNT(*) AS events FROM garment_lifecycle'
            if year is not None:
                by_month_query += ' WHERE substr(event_date,1,4)=?'
            by_month_query += ' GROUP BY month ORDER BY month'
            months = [dict(r) for r in db.execute(by_month_query, args)]
        counts = {a: 0 for a in sorted(DESTINATIONS)}
        counts.update({r['action']: r['total'] for r in rows})
        reuse = counts['donated'] + counts['repaired'] + counts['resold']
        total = sum(counts.values())
        return {'year': year, 'wardrobe_items': garments, 'total_events': total,
                'actions': counts, 'reuse_events': reuse,
                'reuse_event_percentage': round(100 * reuse / total, 2) if total else 0.0,
                'monthly_events': months,
                'methodology': 'Counts recorded events; does not estimate environmental savings.'}
