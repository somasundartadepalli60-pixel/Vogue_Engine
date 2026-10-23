"""Stage 35: offline garment maintenance plans, history and rule-based suggestions."""
from __future__ import annotations
from datetime import date, timedelta
from .storage import WardrobeStore

TASKS = {'wash', 'dry_clean', 'repair', 'inspect', 'iron', 'store'}
SCHEMA = '''
CREATE TABLE IF NOT EXISTS maintenance_plans (
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 task TEXT NOT NULL, interval_days INTEGER NOT NULL CHECK(interval_days BETWEEN 1 AND 3650),
 instructions TEXT NOT NULL DEFAULT '', active INTEGER NOT NULL DEFAULT 1,
 PRIMARY KEY (garment_id, task));
CREATE TABLE IF NOT EXISTS maintenance_events (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 task TEXT NOT NULL, performed_on TEXT NOT NULL, notes TEXT NOT NULL DEFAULT '');
CREATE INDEX IF NOT EXISTS idx_maintenance_events ON maintenance_events(garment_id,task,performed_on);
'''

def valid_day(value):
    try: return date.fromisoformat(str(value)).isoformat()
    except (ValueError, TypeError) as exc: raise ValueError('Date must be YYYY-MM-DD') from exc

class MaintenanceStore:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with wardrobe.connection() as db: db.executescript(SCHEMA)

    def plan(self, garment_id:int, task:str, interval_days:int, instructions:str='', active:bool=True):
        if task not in TASKS: raise ValueError('Unsupported maintenance task')
        if not isinstance(interval_days,int) or not 1 <= interval_days <= 3650: raise ValueError('Interval must be 1–3650 days')
        if len(instructions)>2000: raise ValueError('Instructions too long')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone(): raise LookupError('Garment not found')
            db.execute('''INSERT INTO maintenance_plans VALUES(?,?,?,?,?)
            ON CONFLICT(garment_id,task) DO UPDATE SET interval_days=excluded.interval_days,
            instructions=excluded.instructions,active=excluded.active''',
            (garment_id,task,interval_days,instructions,int(bool(active))))
        return self.plans(garment_id)[0] if len(self.plans(garment_id)) == 1 else next(p for p in self.plans(garment_id) if p['task']==task)

    def plans(self, garment_id:int|None=None):
        with self.wardrobe.connection() as db:
            sql='''SELECT p.*,g.name FROM maintenance_plans p JOIN garments g ON g.id=p.garment_id'''
            args=() if garment_id is None else (garment_id,)
            if garment_id is not None: sql+=' WHERE p.garment_id=?'
            return [dict(r) for r in db.execute(sql+' ORDER BY p.garment_id,p.task',args)]

    def record(self, garment_id:int, task:str, performed_on:str, notes:str=''):
        if task not in TASKS: raise ValueError('Unsupported maintenance task')
        day=valid_day(performed_on)
        if len(notes)>1000: raise ValueError('Notes too long')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone(): raise LookupError('Garment not found')
            cur=db.execute('INSERT INTO maintenance_events(garment_id,task,performed_on,notes) VALUES(?,?,?,?)',(garment_id,task,day,notes))
            return dict(db.execute('SELECT * FROM maintenance_events WHERE id=?',(cur.lastrowid,)).fetchone())

    def history(self,garment_id:int,limit:int=100):
        if not 1<=limit<=500: raise ValueError('Invalid limit')
        with self.wardrobe.connection() as db:
            return [dict(r) for r in db.execute('SELECT * FROM maintenance_events WHERE garment_id=? ORDER BY performed_on DESC,id DESC LIMIT ?', (garment_id,limit))]

    def schedule(self,as_of:str|None=None,days:int=14):
        today=date.fromisoformat(valid_day(as_of)) if as_of else date.today()
        if not isinstance(days,int) or not 0<=days<=365: raise ValueError('Invalid schedule window')
        cutoff=today+timedelta(days=days)
        with self.wardrobe.connection() as db:
            rows=db.execute('''SELECT p.*,g.name,MAX(e.performed_on) AS last_performed
            FROM maintenance_plans p JOIN garments g ON g.id=p.garment_id
            LEFT JOIN maintenance_events e ON e.garment_id=p.garment_id AND e.task=p.task
            WHERE p.active=1 GROUP BY p.garment_id,p.task ORDER BY p.garment_id,p.task''').fetchall()
        result=[]
        for row in rows:
            # No previous event means the task has not been performed and is due now.
            due=date.fromisoformat(row['last_performed'])+timedelta(days=row['interval_days']) if row['last_performed'] else today
            if due<=cutoff:
                result.append({**dict(row),'due_on':due.isoformat(),'overdue':due<today,'days_until_due':(due-today).days})
        return sorted(result,key=lambda r:(r['due_on'],r['garment_id'],r['task']))

    def recommendations(self,garment_id:int):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM garments WHERE id=?',(garment_id,)).fetchone()
            if not row: raise LookupError('Garment not found')
            existing={r['task'] for r in db.execute('SELECT task FROM maintenance_plans WHERE garment_id=?',(garment_id,))}
        category=row['category'].lower()
        rules=[('inspect',90,'Inspect seams, buttons and signs of wear')]
        if any(x in category for x in ('coat','jacket','suit','blazer')):
            rules.append(('dry_clean',180,'Check the care label before professional cleaning'))
        elif any(x in category for x in ('shoe','boot','sneaker')):
            rules.append(('inspect',30,'Check soles and clean according to material'))
        else:
            rules.append(('wash',14,'Follow the garment care label; adjust interval to actual wear'))
        return [{'task':task,'suggested_interval_days':interval,'reason':reason} for task,interval,reason in rules if task not in existing]
