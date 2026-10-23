"""Offline tailoring jobs, appointments, expenses, and immutable status history."""
from datetime import date
from math import isfinite
from .storage import WardrobeStore

DDL = """
CREATE TABLE IF NOT EXISTS tailoring_jobs (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 description TEXT NOT NULL,
 tailor TEXT NOT NULL DEFAULT '',
 status TEXT NOT NULL DEFAULT 'planned' CHECK(status IN ('planned','in_progress','ready','completed','cancelled')),
 due_date TEXT,
 appointment_at TEXT,
 estimated_cost REAL NOT NULL DEFAULT 0 CHECK(estimated_cost>=0),
 actual_cost REAL CHECK(actual_cost>=0),
 notes TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_tailoring_garment ON tailoring_jobs(garment_id);
CREATE INDEX IF NOT EXISTS idx_tailoring_status_due ON tailoring_jobs(status,due_date);
CREATE TABLE IF NOT EXISTS tailoring_events (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 job_id INTEGER NOT NULL REFERENCES tailoring_jobs(id) ON DELETE CASCADE,
 from_status TEXT,
 to_status TEXT NOT NULL,
 note TEXT NOT NULL DEFAULT '',
 changed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""
STATUSES = ('planned','in_progress','ready','completed','cancelled')
TRANSITIONS = {
 'planned': {'in_progress','cancelled'},
 'in_progress': {'ready','completed','cancelled'},
 'ready': {'completed','in_progress','cancelled'},
 'completed': set(), 'cancelled': set()
}

def money(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not isfinite(value) or value<0 or value>1_000_000_000:
        raise ValueError('Cost must be a finite nonnegative amount')
    return round(float(value),2)

def date_value(value):
    return date.fromisoformat(value).isoformat() if value else None

class AlterationStore:
    def __init__(self, wardrobe:WardrobeStore):
        self.wardrobe=wardrobe
        with wardrobe.connection() as db: db.executescript(DDL)

    def get(self, job_id):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM tailoring_jobs WHERE id=?',(job_id,)).fetchone()
            return dict(row) if row else None

    def create(self, garment_id, description, tailor='', due_date=None, appointment_at=None, estimated_cost=0, notes=''):
        description=description.strip()
        if not description or len(description)>500 or len(tailor)>120 or len(notes)>1000:
            raise ValueError('Invalid tailoring details')
        due_date=date_value(due_date)
        if appointment_at:
            from datetime import datetime
            datetime.fromisoformat(appointment_at)
        estimated_cost=money(estimated_cost)
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone():
                raise LookupError('Garment not found')
            cur=db.execute('INSERT INTO tailoring_jobs(garment_id,description,tailor,due_date,appointment_at,estimated_cost,notes) VALUES (?,?,?,?,?,?,?)',
                           (garment_id,description,tailor,due_date,appointment_at,estimated_cost,notes))
            db.execute('INSERT INTO tailoring_events(job_id,from_status,to_status,note) VALUES (?,NULL,?,?)',(cur.lastrowid,'planned','Created'))
            job_id=cur.lastrowid
        return self.get(job_id)

    def list(self, garment_id=None, status=None, due_before=None):
        if status and status not in STATUSES: raise ValueError('Unknown status')
        clauses=[]; params=[]
        if garment_id is not None: clauses.append('garment_id=?');params.append(garment_id)
        if status: clauses.append('status=?');params.append(status)
        if due_before: clauses.append('due_date<=?');params.append(date_value(due_before))
        where=' WHERE '+' AND '.join(clauses) if clauses else ''
        with self.wardrobe.connection() as db:
            return [dict(r) for r in db.execute('SELECT * FROM tailoring_jobs'+where+' ORDER BY COALESCE(due_date,\'9999-12-31\'),id',params)]

    def update(self, job_id, *, tailor=None, due_date=None, appointment_at=None, estimated_cost=None, actual_cost=None, notes=None):
        changes={}
        for key,value in [('tailor',tailor),('due_date',due_date),('appointment_at',appointment_at),('estimated_cost',estimated_cost),('actual_cost',actual_cost),('notes',notes)]:
            if value is not None: changes[key]=value
        if not changes: raise ValueError('No changes supplied')
        if 'due_date' in changes: changes['due_date']=date_value(changes['due_date'])
        if 'appointment_at' in changes:
            from datetime import datetime
            datetime.fromisoformat(changes['appointment_at'])
        for key in ('estimated_cost','actual_cost'):
            if key in changes: changes[key]=money(changes[key])
        if len(changes.get('tailor',''))>120 or len(changes.get('notes',''))>1000: raise ValueError('Text too long')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM tailoring_jobs WHERE id=?',(job_id,)).fetchone(): raise LookupError('Job not found')
            db.execute('UPDATE tailoring_jobs SET '+','.join(k+'=?' for k in changes)+',updated_at=CURRENT_TIMESTAMP WHERE id=?',[*changes.values(),job_id])
        return self.get(job_id)

    def transition(self, job_id, status, note=''):
        if len(note)>500: raise ValueError('Note too long')
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT status FROM tailoring_jobs WHERE id=?',(job_id,)).fetchone()
            if row is None: raise LookupError('Job not found')
            previous=row['status']
            if status not in TRANSITIONS[previous]: raise ValueError('Invalid status transition')
            db.execute('UPDATE tailoring_jobs SET status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?',(status,job_id))
            db.execute('INSERT INTO tailoring_events(job_id,from_status,to_status,note) VALUES (?,?,?,?)',(job_id,previous,status,note))
        return self.get(job_id)

    def history(self, job_id):
        if not self.get(job_id): raise LookupError('Job not found')
        with self.wardrobe.connection() as db:
            return [dict(r) for r in db.execute('SELECT * FROM tailoring_events WHERE job_id=? ORDER BY id',(job_id,))]

    def delete(self, job_id):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM tailoring_jobs WHERE id=?',(job_id,)).rowcount)

    def summary(self):
        jobs=self.list()
        from collections import Counter
        counts=Counter(j['status'] for j in jobs)
        return {'total_jobs':len(jobs),'by_status':dict(counts),
                'estimated_total':round(sum(j['estimated_cost'] for j in jobs),2),
                'actual_total':round(sum(j['actual_cost'] or 0 for j in jobs),2),
                'overdue_open':sum(bool(j['due_date'] and j['due_date']<date.today().isoformat() and j['status'] not in ('completed','cancelled')) for j in jobs)}
