"""Offline, SQLite-backed wardrobe reminders; evaluated on demand, no scheduler."""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

KINDS = {'laundry', 'repair', 'seasonal_review', 'outfit_plan', 'custom'}

class ReminderStore:
    def __init__(self, path='vogue_wardrobe.sqlite3'):
        self.path = str(path)
        self._init()

    def _db(self):
        connection = sqlite3.connect(self.path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute('PRAGMA busy_timeout=10000')
        return connection

    def _init(self):
        with self._db() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS wardrobe_reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL, kind TEXT NOT NULL, due_at TEXT NOT NULL,
                garment_id INTEGER, notes TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TEXT NOT NULL, completed_at TEXT)''')
            db.execute('''CREATE TABLE IF NOT EXISTS wardrobe_reminder_preferences (
                id INTEGER PRIMARY KEY CHECK(id=1), enabled INTEGER NOT NULL DEFAULT 1,
                lookahead_hours INTEGER NOT NULL DEFAULT 24)''')
            db.execute('INSERT OR IGNORE INTO wardrobe_reminder_preferences(id, enabled, lookahead_hours) VALUES(1,1,24)')
            db.execute('CREATE INDEX IF NOT EXISTS idx_wardrobe_reminders_due ON wardrobe_reminders(status,due_at)')

    @staticmethod
    def _time(value):
        try:
            result = datetime.fromisoformat(value.replace('Z', '+00:00'))
            if result.tzinfo is None:
                raise ValueError('Timezone offset required')
            return result.astimezone(timezone.utc).isoformat()
        except (TypeError, AttributeError, ValueError) as exc:
            raise ValueError('due_at must be an ISO-8601 timestamp with timezone') from exc

    def create(self, title, kind, due_at, garment_id=None, notes=''):
        title = title.strip()
        if not title or len(title)>120: raise ValueError('title must contain 1–120 characters')
        if kind not in KINDS: raise ValueError('unsupported reminder kind')
        if len(notes)>1000: raise ValueError('notes exceed 1000 characters')
        if garment_id is not None and garment_id < 1: raise ValueError('garment_id must be positive')
        due = self._time(due_at)
        now = datetime.now(timezone.utc).isoformat()
        with self._db() as db:
            cursor = db.execute('INSERT INTO wardrobe_reminders(title,kind,due_at,garment_id,notes,created_at) VALUES(?,?,?,?,?,?)', (title,kind,due,garment_id,notes,now))
            identifier = cursor.lastrowid
        return self.get(identifier)

    def get(self, identifier):
        with self._db() as db:
            row = db.execute('SELECT * FROM wardrobe_reminders WHERE id=?', (identifier,)).fetchone()
        if row is None: raise LookupError('Reminder not found')
        return dict(row)

    def list(self, status=None, kind=None, limit=100, offset=0):
        if status is not None and status not in {'pending','completed','dismissed'}: raise ValueError('invalid status')
        if kind is not None and kind not in KINDS: raise ValueError('invalid kind')
        if not 1<=limit<=500 or offset<0: raise ValueError('invalid pagination')
        clauses=[]; params=[]
        if status: clauses.append('status=?'); params.append(status)
        if kind: clauses.append('kind=?'); params.append(kind)
        where = (' WHERE '+' AND '.join(clauses)) if clauses else ''
        with self._db() as db:
            rows=db.execute('SELECT * FROM wardrobe_reminders'+where+' ORDER BY due_at,id LIMIT ? OFFSET ?', (*params,limit,offset)).fetchall()
            total=db.execute('SELECT COUNT(*) FROM wardrobe_reminders'+where, params).fetchone()[0]
        return {'items':[dict(r) for r in rows], 'total':total, 'limit':limit, 'offset':offset}

    def set_status(self, identifier, status):
        if status not in {'completed','dismissed','pending'}: raise ValueError('invalid status')
        completed = datetime.now(timezone.utc).isoformat() if status=='completed' else None
        with self._db() as db:
            cursor=db.execute('UPDATE wardrobe_reminders SET status=?,completed_at=? WHERE id=?', (status,completed,identifier))
            if not cursor.rowcount: raise LookupError('Reminder not found')
        return self.get(identifier)

    def preferences(self):
        with self._db() as db:
            row=db.execute('SELECT enabled,lookahead_hours FROM wardrobe_reminder_preferences WHERE id=1').fetchone()
        return {'enabled':bool(row['enabled']), 'lookahead_hours':row['lookahead_hours']}

    def set_preferences(self, enabled, lookahead_hours):
        if not 1<=lookahead_hours<=720: raise ValueError('lookahead_hours must be 1–720')
        with self._db() as db:
            db.execute('UPDATE wardrobe_reminder_preferences SET enabled=?,lookahead_hours=? WHERE id=1', (int(enabled),lookahead_hours))
        return self.preferences()

    def notifications(self, now=None):
        from datetime import timedelta
        prefs=self.preferences()
        if not prefs['enabled']: return {'items':[], 'count':0, 'enabled':False}
        current=datetime.now(timezone.utc) if now is None else datetime.fromisoformat(self._time(now))
        until=(current+timedelta(hours=prefs['lookahead_hours'])).isoformat()
        with self._db() as db:
            rows=db.execute("SELECT * FROM wardrobe_reminders WHERE status='pending' AND due_at<=? ORDER BY due_at,id LIMIT 500", (until,)).fetchall()
        items=[]
        for row in rows:
            item=dict(row)
            item['overdue']=item['due_at']<current.isoformat()
            items.append(item)
        return {'items':items,'count':len(items),'enabled':True,'as_of':current.isoformat()}
