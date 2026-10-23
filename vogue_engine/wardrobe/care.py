# Local garment care ledger
from __future__ import annotations
from datetime import date, timedelta
from .storage import WardrobeStore

SCHEMA = '''
CREATE TABLE IF NOT EXISTS garment_care (
 garment_id INTEGER PRIMARY KEY REFERENCES garments(id) ON DELETE CASCADE,
 condition TEXT NOT NULL DEFAULT 'good',
 wash_interval_days INTEGER NOT NULL DEFAULT 7 CHECK(wash_interval_days BETWEEN 1 AND 365),
 last_washed TEXT,
 next_wash TEXT,
 care_instructions TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS care_events (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 event_type TEXT NOT NULL,
 event_date TEXT NOT NULL,
 notes TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_care_events_garment ON care_events(garment_id,event_date);
CREATE INDEX IF NOT EXISTS idx_care_next_wash ON garment_care(next_wash);
'''
CONDITIONS={'new','excellent','good','fair','needs_repair','retired'}
EVENTS={'wash','dry_clean','repair','inspection','iron'}

def iso(value):
    try: return date.fromisoformat(str(value)).isoformat()
    except (ValueError,TypeError) as exc: raise ValueError('Date must be YYYY-MM-DD') from exc

class CareStore:
    def __init__(self, wardrobe:WardrobeStore):
        self.wardrobe=wardrobe
        with wardrobe.connection() as db: db.executescript(SCHEMA)

    def configure(self,garment_id,condition='good',wash_interval_days=7,last_washed=None,care_instructions=''):
        if condition not in CONDITIONS: raise ValueError('Invalid garment condition')
        if not isinstance(wash_interval_days,int) or not 1<=wash_interval_days<=365: raise ValueError('Interval must be 1 to 365 days')
        if len(care_instructions)>2000: raise ValueError('Instructions too long')
        last=iso(last_washed) if last_washed else None
        next_wash=(date.fromisoformat(last)+timedelta(days=wash_interval_days)).isoformat() if last else None
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone(): raise LookupError('Garment not found')
            db.execute('''INSERT INTO garment_care(garment_id,condition,wash_interval_days,last_washed,next_wash,care_instructions)
            VALUES(?,?,?,?,?,?) ON CONFLICT(garment_id) DO UPDATE SET condition=excluded.condition,
            wash_interval_days=excluded.wash_interval_days,last_washed=excluded.last_washed,
            next_wash=excluded.next_wash,care_instructions=excluded.care_instructions''',
            (garment_id,condition,wash_interval_days,last,next_wash,care_instructions))
        return self.get(garment_id)

    def get(self,garment_id):
        with self.wardrobe.connection() as db:
            row=db.execute('''SELECT c.*,g.name,g.category FROM garment_care c JOIN garments g ON g.id=c.garment_id WHERE garment_id=?''',(garment_id,)).fetchone()
            return dict(row) if row else None

    def record(self,garment_id,event_type,event_date,notes=''):
        if event_type not in EVENTS: raise ValueError('Invalid care event')
        when=iso(event_date)
        if len(notes)>1000: raise ValueError('Notes too long')
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM garment_care WHERE garment_id=?',(garment_id,)).fetchone()
            if not row: raise LookupError('Configure garment care first')
            cursor=db.execute('INSERT INTO care_events(garment_id,event_type,event_date,notes) VALUES(?,?,?,?)',(garment_id,event_type,when,notes))
            if event_type in {'wash','dry_clean'}:
                newest=db.execute("SELECT MAX(event_date) FROM care_events WHERE garment_id=? AND event_type IN ('wash','dry_clean')",(garment_id,)).fetchone()[0]
                next_wash=(date.fromisoformat(newest)+timedelta(days=row['wash_interval_days'])).isoformat()
                db.execute('UPDATE garment_care SET last_washed=?,next_wash=? WHERE garment_id=?',(newest,next_wash,garment_id))
            event_id=cursor.lastrowid
        return self.event(event_id)

    def event(self,event_id):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM care_events WHERE id=?',(event_id,)).fetchone()
            return dict(row) if row else None

    def history(self,garment_id):
        with self.wardrobe.connection() as db:
            return [dict(row) for row in db.execute('SELECT * FROM care_events WHERE garment_id=? ORDER BY event_date DESC,id DESC',(garment_id,))]

    def reminders(self,as_of=None,include_upcoming_days=0):
        today=date.fromisoformat(iso(as_of)) if as_of else date.today()
        if not isinstance(include_upcoming_days,int) or not 0<=include_upcoming_days<=365: raise ValueError('Invalid reminder window')
        cutoff=(today+timedelta(days=include_upcoming_days)).isoformat()
        with self.wardrobe.connection() as db:
            rows=db.execute('''SELECT c.*,g.name FROM garment_care c JOIN garments g ON g.id=c.garment_id
                WHERE c.next_wash IS NOT NULL AND c.next_wash<=? ORDER BY c.next_wash,c.garment_id''',(cutoff,)).fetchall()
        return [{**dict(row),'overdue':row['next_wash']<today.isoformat()} for row in rows]

    def overview(self,as_of=None):
        with self.wardrobe.connection() as db:
            conditions=[dict(row) for row in db.execute('SELECT condition,COUNT(*) AS count FROM garment_care GROUP BY condition ORDER BY condition')]
            events=db.execute('SELECT COUNT(*) FROM care_events').fetchone()[0]
            configured=db.execute('SELECT COUNT(*) FROM garment_care').fetchone()[0]
        due=self.reminders(as_of)
        return {'configured_garments':configured,'care_events':events,'conditions':conditions,'due_for_wash':len(due),'overdue':sum(x['overdue'] for x in due)}
