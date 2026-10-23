"""Stage 2 local-only wardrobe backup, filtering, and outfit calendar."""
import csv
import io
import json
import sqlite3
from datetime import date
from fastapi import APIRouter, HTTPException, Query, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel, Field
from .api import store

router = APIRouter(prefix='/api/v1/wardrobe', tags=['Wardrobe Stage 2'])

class CalendarEntry(BaseModel):
    day: date
    outfit_id: int = Field(gt=0)
    note: str = Field(default='', max_length=500)


def initialize():
    with store().connection() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS outfit_calendar (
          day TEXT PRIMARY KEY, outfit_id INTEGER NOT NULL REFERENCES outfits(id) ON DELETE CASCADE,
          note TEXT NOT NULL DEFAULT '')''')

@router.get('/search')
def search(q: str = '', category: str | None = None, sort: str = 'name', page: int = Query(1,ge=1), page_size: int = Query(20,ge=1,le=100)):
    if sort not in ('name','newest','most_worn','least_worn'):
        raise HTTPException(422,'Invalid sort')
    order = {'name':'name COLLATE NOCASE, id','newest':'id DESC','most_worn':'wears DESC, id','least_worn':'wears, id'}[sort]
    clauses=['(name LIKE ? OR color LIKE ?)']; args=[f'%{q}%',f'%{q}%']
    if category:
        clauses.append('category=?');args.append(category.lower())
    where=' AND '.join(clauses)
    with store().connection() as db:
        total=db.execute('SELECT COUNT(*) FROM garments WHERE '+where,args).fetchone()[0]
        rows=db.execute(f'SELECT * FROM garments WHERE {where} ORDER BY {order} LIMIT ? OFFSET ?', [*args,page_size,(page-1)*page_size]).fetchall()
    return {'items':[dict(row) for row in rows],'total':total,'page':page,'page_size':page_size}

@router.get('/export/json')
def export_json():
    with store().connection() as db:
        garments=[dict(r) for r in db.execute('SELECT name,category,color,season,occasion,favorite,wears FROM garments ORDER BY id')]
    return {'format':'vogue-wardrobe-v1','garments':garments}

@router.get('/export/csv')
def export_csv():
    items=export_json()['garments']; buffer=io.StringIO()
    columns=['name','category','color','season','occasion','favorite','wears']
    writer=csv.DictWriter(buffer,fieldnames=columns);writer.writeheader();writer.writerows(items)
    return StreamingResponse(iter([buffer.getvalue()]),media_type='text/csv',headers={'Content-Disposition':'attachment; filename="wardrobe.csv"'})

class ImportPayload(BaseModel):
    format: str
    garments: list[dict] = Field(max_length=1000)

@router.post('/import/json')
def import_json(payload: ImportPayload):
    if payload.format!='vogue-wardrobe-v1':raise HTTPException(422,'Unsupported backup format')
    prepared=[]
    for item in payload.garments:
        try:
            name=str(item['name']).strip();category=str(item['category']).strip().lower();color=str(item['color']).strip().lower()
            season=str(item.get('season','all')).strip().lower();occasion=str(item.get('occasion','casual')).strip().lower()
            favorite=int(item.get('favorite',0));wears=int(item.get('wears',0))
            if not all((name,category,color,season,occasion)) or len(name)>120 or any(len(v)>40 for v in (category,color,season,occasion)) or favorite not in (0,1) or wears<0:raise ValueError()
            prepared.append((name,category,color,season,occasion,favorite,wears))
        except (KeyError,TypeError,ValueError) as exc:raise HTTPException(422,'Invalid garment in backup') from exc
    with store().connection() as db:
        db.executemany('INSERT INTO garments(name,category,color,season,occasion,favorite,wears) VALUES (?,?,?,?,?,?,?)',prepared)
    return {'imported':len(prepared)}

@router.put('/calendar')
def set_calendar(entry: CalendarEntry):
    initialize()
    with store().connection() as db:
        if not db.execute('SELECT 1 FROM outfits WHERE id=?',(entry.outfit_id,)).fetchone():raise HTTPException(404,'Outfit not found')
        db.execute('INSERT INTO outfit_calendar(day,outfit_id,note) VALUES (?,?,?) ON CONFLICT(day) DO UPDATE SET outfit_id=excluded.outfit_id,note=excluded.note',(entry.day.isoformat(),entry.outfit_id,entry.note))
    return entry.model_dump(mode='json')

@router.get('/calendar')
def get_calendar(start: date | None = None, end: date | None = None):
    initialize()
    if start and end and end<start:raise HTTPException(422,'End date precedes start date')
    sql='SELECT c.day,c.outfit_id,c.note,o.name AS outfit_name FROM outfit_calendar c JOIN outfits o ON o.id=c.outfit_id WHERE 1=1';args=[]
    if start:sql+=' AND c.day>=?';args.append(start.isoformat())
    if end:sql+=' AND c.day<=?';args.append(end.isoformat())
    with store().connection() as db:return [dict(r) for r in db.execute(sql+' ORDER BY c.day',args)]

@router.delete('/calendar/{day}')
def delete_calendar(day: date):
    initialize()
    with store().connection() as db:
        deleted=db.execute('DELETE FROM outfit_calendar WHERE day=?',(day.isoformat(),)).rowcount
    if not deleted:raise HTTPException(404,'No planned outfit on that date')
    return {'deleted':True}
