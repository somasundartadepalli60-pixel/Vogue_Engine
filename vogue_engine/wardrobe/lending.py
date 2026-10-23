"""Offline garment loans with immutable events and return reminders."""
from datetime import date
from .storage import WardrobeStore

DDL = '''
CREATE TABLE IF NOT EXISTS garment_loans (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 direction TEXT NOT NULL CHECK(direction IN ('lent','borrowed')),
 contact TEXT NOT NULL,
 start_date TEXT NOT NULL,
 due_date TEXT NOT NULL,
 returned_at TEXT,
 notes TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 CHECK(due_date>=start_date),
 CHECK(returned_at IS NULL OR returned_at>=start_date)
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_one_active_loan ON garment_loans(garment_id) WHERE returned_at IS NULL;
CREATE INDEX IF NOT EXISTS idx_loans_due ON garment_loans(due_date,returned_at);
CREATE TABLE IF NOT EXISTS garment_loan_events (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 loan_id INTEGER NOT NULL REFERENCES garment_loans(id) ON DELETE CASCADE,
 event TEXT NOT NULL,
 detail TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
'''

def valid_date(value):
    return date.fromisoformat(str(value)).isoformat()

class LendingStore:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with wardrobe.connection() as db: db.executescript(DDL)

    def get(self, loan_id):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM garment_loans WHERE id=?',(loan_id,)).fetchone()
            return dict(row) if row else None

    def create(self, garment_id, direction, contact, start_date, due_date, notes=''):
        start_date,due_date=valid_date(start_date),valid_date(due_date)
        if direction not in ('lent','borrowed'): raise ValueError('Invalid loan direction')
        if due_date<start_date: raise ValueError('Due date must be on or after start date')
        if not contact.strip() or len(contact)>150 or len(notes)>1000: raise ValueError('Invalid contact or notes')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone(): raise LookupError('Garment not found')
            if db.execute('SELECT 1 FROM garment_loans WHERE garment_id=? AND returned_at IS NULL',(garment_id,)).fetchone():
                raise ValueError('Garment already has an active loan')
            cur=db.execute('INSERT INTO garment_loans(garment_id,direction,contact,start_date,due_date,notes) VALUES (?,?,?,?,?,?)',
                           (garment_id,direction,contact.strip(),start_date,due_date,notes))
            loan_id=cur.lastrowid
            db.execute('INSERT INTO garment_loan_events(loan_id,event,detail) VALUES (?,?,?)',(loan_id,'created',direction))
        return self.get(loan_id)

    def list(self, direction=None, active_only=False, overdue_only=False, today=None):
        if direction is not None and direction not in ('lent','borrowed'): raise ValueError('Invalid loan direction')
        today=valid_date(today or date.today())
        clauses=[]; args=[]
        if direction: clauses.append('direction=?');args.append(direction)
        if active_only or overdue_only: clauses.append('returned_at IS NULL')
        if overdue_only: clauses.append('due_date<?');args.append(today)
        sql='SELECT * FROM garment_loans'+(' WHERE '+' AND '.join(clauses) if clauses else '')+' ORDER BY due_date,id'
        with self.wardrobe.connection() as db: return [dict(r) for r in db.execute(sql,args)]

    def return_loan(self, loan_id, returned_at=None):
        returned_at=valid_date(returned_at or date.today())
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM garment_loans WHERE id=?',(loan_id,)).fetchone()
            if not row: raise LookupError('Loan not found')
            if row['returned_at'] is not None: raise ValueError('Loan already returned')
            if returned_at<row['start_date']: raise ValueError('Return date precedes loan')
            db.execute('UPDATE garment_loans SET returned_at=? WHERE id=?',(returned_at,loan_id))
            db.execute('INSERT INTO garment_loan_events(loan_id,event,detail) VALUES (?,?,?)',(loan_id,'returned',returned_at))
        return self.get(loan_id)

    def extend(self, loan_id, due_date):
        due_date=valid_date(due_date)
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM garment_loans WHERE id=?',(loan_id,)).fetchone()
            if not row: raise LookupError('Loan not found')
            if row['returned_at']: raise ValueError('Cannot extend returned loan')
            if due_date<row['start_date']: raise ValueError('Invalid due date')
            db.execute('UPDATE garment_loans SET due_date=? WHERE id=?',(due_date,loan_id))
            db.execute('INSERT INTO garment_loan_events(loan_id,event,detail) VALUES (?,?,?)',(loan_id,'due_date_changed',due_date))
        return self.get(loan_id)

    def history(self, loan_id):
        if not self.get(loan_id): raise LookupError('Loan not found')
        with self.wardrobe.connection() as db:
            return [dict(r) for r in db.execute('SELECT * FROM garment_loan_events WHERE loan_id=? ORDER BY id',(loan_id,))]

    def summary(self, today=None):
        today=valid_date(today or date.today())
        with self.wardrobe.connection() as db:
            row=db.execute('''SELECT COUNT(*) total, SUM(CASE WHEN returned_at IS NULL THEN 1 ELSE 0 END) active,
              SUM(CASE WHEN returned_at IS NULL AND due_date<? THEN 1 ELSE 0 END) overdue,
              SUM(CASE WHEN returned_at IS NOT NULL THEN 1 ELSE 0 END) returned
              FROM garment_loans''',(today,)).fetchone()
            return {k:int(row[k] or 0) for k in row.keys()}
