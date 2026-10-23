"""Offline outfit wear diary and wardrobe analytics."""
import sqlite3
from datetime import date
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store

router = APIRouter(prefix="/api/v1/wardrobe", tags=["Wardrobe Analytics"])

class WearEntry(BaseModel):
    outfit_id: int = Field(gt=0)
    day: date
    note: str = Field(default="", max_length=500)

def initialize():
    with store().connection() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS outfit_wear_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            outfit_id INTEGER NOT NULL REFERENCES outfits(id) ON DELETE CASCADE,
            day TEXT NOT NULL, note TEXT NOT NULL DEFAULT '',
            UNIQUE(outfit_id,day))""")
        db.execute('CREATE INDEX IF NOT EXISTS idx_outfit_wear_day ON outfit_wear_log(day)')

@router.post('/wear-log', status_code=201)
def log_wear(entry: WearEntry):
    initialize()
    with store().connection() as db:
        if not db.execute('SELECT 1 FROM outfits WHERE id=?',(entry.outfit_id,)).fetchone():
            raise HTTPException(404,'Outfit not found')
        try:
            cur=db.execute('INSERT INTO outfit_wear_log(outfit_id,day,note) VALUES (?,?,?)',
                (entry.outfit_id,entry.day.isoformat(),entry.note))
        except sqlite3.IntegrityError as exc:
            raise HTTPException(409,'Outfit already logged for this day') from exc
        db.execute("UPDATE garments SET wears=wears+1 WHERE id IN (SELECT garment_id FROM outfit_garments WHERE outfit_id=?)",(entry.outfit_id,))
        return {'id':cur.lastrowid,**entry.model_dump(mode='json')}

@router.get('/wear-log')
def wear_log(start:date|None=None,end:date|None=None,limit:int=Query(100,ge=1,le=500)):
    initialize()
    if start and end and start>end:raise HTTPException(422,'Invalid date range')
    sql="SELECT w.id,w.outfit_id,w.day,w.note,o.name AS outfit_name FROM outfit_wear_log w JOIN outfits o ON o.id=w.outfit_id WHERE 1=1"
    args=[]
    if start:sql+=' AND w.day>=?';args.append(start.isoformat())
    if end:sql+=' AND w.day<=?';args.append(end.isoformat())
    with store().connection() as db:
        return [dict(r) for r in db.execute(sql+' ORDER BY w.day DESC,w.id DESC LIMIT ?',(*args,limit))]

@router.delete('/wear-log/{entry_id}')
def undo_wear(entry_id:int):
    initialize()
    with store().connection() as db:
        row=db.execute('SELECT outfit_id FROM outfit_wear_log WHERE id=?',(entry_id,)).fetchone()
        if not row:raise HTTPException(404,'Wear entry not found')
        db.execute("UPDATE garments SET wears=MAX(0,wears-1) WHERE id IN (SELECT garment_id FROM outfit_garments WHERE outfit_id=?)",(row['outfit_id'],))
        db.execute('DELETE FROM outfit_wear_log WHERE id=?',(entry_id,))
    return {'deleted':True}

@router.get('/analytics')
def analytics():
    initialize()
    with store().connection() as db:
        total=db.execute('SELECT COUNT(*) FROM outfit_wear_log').fetchone()[0]
        monthly=[dict(r) for r in db.execute("SELECT substr(day,1,7) month,COUNT(*) wears FROM outfit_wear_log GROUP BY substr(day,1,7) ORDER BY month DESC LIMIT 12")]
        most=[dict(r) for r in db.execute("SELECT id,name,category,color,wears FROM garments ORDER BY wears DESC,id LIMIT 10")]
        least=[dict(r) for r in db.execute("SELECT id,name,category,color,wears FROM garments ORDER BY wears,id LIMIT 10")]
        outfits=[dict(r) for r in db.execute("SELECT o.id,o.name,COUNT(w.id) times_worn FROM outfits o LEFT JOIN outfit_wear_log w ON w.outfit_id=o.id GROUP BY o.id ORDER BY times_worn DESC,o.id LIMIT 10")]
    return {'logged_outfit_wears':total,'monthly':monthly,'most_worn':most,
            'least_worn':least,'outfit_rotation':outfits}
