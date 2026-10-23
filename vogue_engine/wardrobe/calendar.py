"""Offline outfit calendar with conflict detection and usage forecasts."""
from __future__ import annotations
from datetime import date, timedelta
from .storage import WardrobeStore

class CalendarStore:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with wardrobe.connection() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS outfit_calendar (
                day TEXT NOT NULL, slot TEXT NOT NULL, outfit_id INTEGER NOT NULL
                REFERENCES outfits(id) ON DELETE CASCADE,
                note TEXT NOT NULL DEFAULT '', PRIMARY KEY(day,slot));
            CREATE TABLE IF NOT EXISTS garment_blocks (
                id INTEGER PRIMARY KEY, garment_id INTEGER NOT NULL
                REFERENCES garments(id) ON DELETE CASCADE,
                start_date TEXT NOT NULL, end_date TEXT NOT NULL,
                reason TEXT NOT NULL, CHECK(end_date >= start_date));
            CREATE INDEX IF NOT EXISTS idx_blocks_dates ON garment_blocks(start_date,end_date);
            ''')

    def block(self, garment_id:int, start:date, end:date, reason:str):
        if end < start or (end-start).days > 366: raise ValueError('Invalid availability range')
        if not reason.strip(): raise ValueError('Reason is required')
        if not self.wardrobe.get(garment_id): raise LookupError('Garment not found')
        with self.wardrobe.connection() as db:
            cursor=db.execute('INSERT INTO garment_blocks(garment_id,start_date,end_date,reason) VALUES(?,?,?,?)',
                (garment_id,start.isoformat(),end.isoformat(),reason.strip()))
            return dict(db.execute('SELECT * FROM garment_blocks WHERE id=?',(cursor.lastrowid,)).fetchone())

    def unblock(self, block_id:int):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM garment_blocks WHERE id=?',(block_id,)).rowcount)

    def blocks(self, day:date|None=None):
        with self.wardrobe.connection() as db:
            if day:
                rows=db.execute('SELECT * FROM garment_blocks WHERE start_date<=? AND end_date>=? ORDER BY garment_id,id',(day.isoformat(),day.isoformat()))
            else: rows=db.execute('SELECT * FROM garment_blocks ORDER BY start_date,id')
            return [dict(r) for r in rows]

    def outfit_garments(self,outfit_id:int):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT id FROM outfits WHERE id=?',(outfit_id,)).fetchone()
            if not row: raise LookupError('Outfit not found')
            return [r[0] for r in db.execute('SELECT garment_id FROM outfit_garments WHERE outfit_id=?',(outfit_id,))]

    def conflicts(self, day:date, outfit_id:int, slot:str='day'):
        garment_ids=self.outfit_garments(outfit_id)
        blocked={r['garment_id']:r['reason'] for r in self.blocks(day)}
        with self.wardrobe.connection() as db:
            other=db.execute('''SELECT c.slot,og.garment_id FROM outfit_calendar c
                JOIN outfit_garments og ON og.outfit_id=c.outfit_id
                WHERE c.day=? AND c.slot<>?''',(day.isoformat(),slot)).fetchall()
        conflicts=[{'garment_id':g,'reason':'Unavailable: '+blocked[g]} for g in garment_ids if g in blocked]
        conflicts.extend({'garment_id':r['garment_id'],'reason':'Already scheduled for '+r['slot']}
                         for r in other if r['garment_id'] in garment_ids)
        return conflicts

    def schedule(self, day:date, slot:str, outfit_id:int, note:str='', force:bool=False):
        if not slot.strip() or len(slot)>32: raise ValueError('Invalid slot')
        if len(note)>500: raise ValueError('Note too long')
        conflicts=self.conflicts(day,outfit_id,slot)
        if conflicts and not force: raise ValueError('Outfit conflicts: '+str(conflicts))
        with self.wardrobe.connection() as db:
            db.execute('''INSERT INTO outfit_calendar(day,slot,outfit_id,note) VALUES(?,?,?,?)
                ON CONFLICT(day,slot) DO UPDATE SET outfit_id=excluded.outfit_id,note=excluded.note''',
                (day.isoformat(),slot.strip(),outfit_id,note))
        return {'day':day.isoformat(),'slot':slot,'outfit_id':outfit_id,'note':note,'conflicts':conflicts}

    def unschedule(self, day:date, slot:str):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM outfit_calendar WHERE day=? AND slot=?',(day.isoformat(),slot)).rowcount)

    def agenda(self,start:date,end:date):
        if end<start or (end-start).days>366: raise ValueError('Date range must be 0-366 days')
        with self.wardrobe.connection() as db:
            rows=db.execute('''SELECT c.day,c.slot,c.outfit_id,o.name AS outfit_name,c.note
                FROM outfit_calendar c JOIN outfits o ON o.id=c.outfit_id
                WHERE c.day BETWEEN ? AND ? ORDER BY c.day,c.slot''',(start.isoformat(),end.isoformat()))
            return [dict(r) for r in rows]

    def forecast(self,start:date,days:int=30):
        if not 1<=days<=366: raise ValueError('Days must be between 1 and 366')
        end=start+timedelta(days=days-1)
        agenda=self.agenda(start,end)
        counts={}
        for entry in agenda:
            for garment in self.outfit_garments(entry['outfit_id']):
                counts[garment]=counts.get(garment,0)+1
        return {'start':start.isoformat(),'end':end.isoformat(),'scheduled_outfits':len(agenda),
                'days_with_outfits':len({entry['day'] for entry in agenda}),
                'garment_usage':[{'garment_id':k,'planned_wears':v} for k,v in sorted(counts.items(),key=lambda item:(-item[1],item[0]))]}
