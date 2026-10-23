"""Read-only wardrobe integrity checks and repeatable physical inventory audits.

All checks operate on the local SQLite database. No credentials or network access.
"""
from __future__ import annotations
from datetime import datetime, timezone
from .storage import WardrobeStore

DDL = '''
CREATE TABLE IF NOT EXISTS inventory_audits (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 label TEXT NOT NULL,
 created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS inventory_audit_items (
 audit_id INTEGER NOT NULL REFERENCES inventory_audits(id) ON DELETE CASCADE,
 garment_id INTEGER NOT NULL,
 garment_name TEXT NOT NULL,
 confirmed INTEGER NOT NULL DEFAULT 0 CHECK(confirmed IN (0,1)),
 confirmed_at TEXT,
 PRIMARY KEY(audit_id,garment_id)
);
CREATE INDEX IF NOT EXISTS idx_audit_items_confirmed ON inventory_audit_items(audit_id,confirmed);
'''

class InventoryAuditor:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with self.wardrobe.connection() as db:
            db.executescript(DDL)

    def start(self, label: str):
        label = label.strip()
        if not label or len(label) > 120:
            raise ValueError('Audit label must contain 1–120 characters')
        with self.wardrobe.connection() as db:
            created = datetime.now(timezone.utc).isoformat()
            audit_id = db.execute('INSERT INTO inventory_audits(label,created_at) VALUES (?,?)', (label,created)).lastrowid
            db.execute('''INSERT INTO inventory_audit_items(audit_id,garment_id,garment_name)
                          SELECT ?,id,name FROM garments''', (audit_id,))
        return self.get(audit_id)

    def get(self, audit_id: int):
        with self.wardrobe.connection() as db:
            audit = db.execute('SELECT * FROM inventory_audits WHERE id=?',(audit_id,)).fetchone()
            if audit is None:
                raise LookupError('Inventory audit not found')
            items = [dict(r) for r in db.execute('''SELECT ai.*,g.id IS NOT NULL AS still_in_wardrobe
                FROM inventory_audit_items ai LEFT JOIN garments g ON g.id=ai.garment_id
                WHERE ai.audit_id=? ORDER BY ai.confirmed,ai.garment_name,ai.garment_id''',(audit_id,))]
            return {**dict(audit), 'total':len(items), 'confirmed':sum(i['confirmed'] for i in items),
                    'missing':sum(not i['confirmed'] for i in items), 'items':items}

    def confirm(self, audit_id: int, garment_id: int, present: bool = True):
        if not isinstance(present, bool):
            raise ValueError('present must be a boolean')
        with self.wardrobe.connection() as db:
            exists = db.execute('SELECT 1 FROM inventory_audits WHERE id=?',(audit_id,)).fetchone()
            if not exists:
                raise LookupError('Inventory audit not found')
            timestamp = datetime.now(timezone.utc).isoformat() if present else None
            changed = db.execute('''UPDATE inventory_audit_items SET confirmed=?,confirmed_at=?
                WHERE audit_id=? AND garment_id=?''',(int(present),timestamp,audit_id,garment_id)).rowcount
            if not changed:
                raise LookupError('Garment not in audit snapshot')
        return self.get(audit_id)

    def list(self):
        with self.wardrobe.connection() as db:
            return [dict(r) for r in db.execute('''SELECT a.id,a.label,a.created_at,
                COUNT(i.garment_id) AS total,COALESCE(SUM(i.confirmed),0) AS confirmed
                FROM inventory_audits a LEFT JOIN inventory_audit_items i ON i.audit_id=a.id
                GROUP BY a.id ORDER BY a.id DESC''')]

    def integrity(self):
        """Non-destructive database integrity and cross-table consistency checks."""
        issues = []
        with self.wardrobe.connection() as db:
            for row in db.execute('PRAGMA foreign_key_check'):
                issues.append({'kind':'foreign_key','table':row[0], 'row_id':row[1], 'parent':row[2]})
            for row in db.execute('PRAGMA quick_check'):
                if row[0] != 'ok':
                    issues.append({'kind':'sqlite_integrity','detail':row[0]})
            # Inspect only existing tables, supporting older project versions.
            tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if {'outfit_garments','garments'} <= tables:
                for row in db.execute('''SELECT og.outfit_id,og.garment_id FROM outfit_garments og
                    LEFT JOIN garments g ON g.id=og.garment_id WHERE g.id IS NULL'''):
                    issues.append({'kind':'orphan_outfit_garment','outfit_id':row[0],'garment_id':row[1]})
            total = db.execute('SELECT COUNT(*) FROM garments').fetchone()[0]
        return {'ok':not issues,'garment_count':total,'issue_count':len(issues),'issues':issues}

    def compare(self, earlier_id: int, later_id: int):
        """Compare immutable audit snapshots, including verification changes."""
        earlier, later = self.get(earlier_id), self.get(later_id)
        before = {i['garment_id']: i for i in earlier['items']}
        after = {i['garment_id']: i for i in later['items']}
        shared = before.keys() & after.keys()
        return {
            'earlier_id': earlier_id, 'later_id': later_id,
            'added': [after[k] for k in sorted(after.keys() - before.keys())],
            'removed': [before[k] for k in sorted(before.keys() - after.keys())],
            'newly_confirmed': [after[k] for k in sorted(shared) if not before[k]['confirmed'] and after[k]['confirmed']],
            'no_longer_confirmed': [after[k] for k in sorted(shared) if before[k]['confirmed'] and not after[k]['confirmed']],
            'earlier_total': earlier['total'], 'later_total': later['total'],
            'earlier_confirmed': earlier['confirmed'], 'later_confirmed': later['confirmed'],
        }
