"""Stage 4: local outfit history, wardrobe insights and explainable recommendations."""
from collections import Counter
from datetime import date
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store

router = APIRouter(prefix='/api/v1/wardrobe', tags=['Wardrobe Stage 4'])


def initialize():
    with store().connection() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS wear_history (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
          worn_on TEXT NOT NULL, note TEXT NOT NULL DEFAULT '',
          created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
        db.execute('CREATE INDEX IF NOT EXISTS idx_wear_history_day ON wear_history(worn_on)')
        db.execute('CREATE INDEX IF NOT EXISTS idx_wear_history_garment ON wear_history(garment_id)')


class WearEntry(BaseModel):
    garment_id: int = Field(gt=0)
    worn_on: date
    note: str = Field(default='', max_length=500)


@router.post('/wear-history', status_code=201)
def record_wear(entry: WearEntry):
    initialize()
    with store().connection() as db:
        if not db.execute('SELECT 1 FROM garments WHERE id=?', (entry.garment_id,)).fetchone():
            raise HTTPException(404, 'Garment not found')
        cursor = db.execute('INSERT INTO wear_history(garment_id,worn_on,note) VALUES (?,?,?)',
                            (entry.garment_id, entry.worn_on.isoformat(), entry.note))
        db.execute('UPDATE garments SET wears=wears+1 WHERE id=?', (entry.garment_id,))
        return {'id': cursor.lastrowid, **entry.model_dump(mode='json')}


@router.get('/wear-history')
def list_wear_history(garment_id: int | None = Query(None, gt=0), start: date | None = None,
                      end: date | None = None, limit: int = Query(100, ge=1, le=500)):
    initialize()
    if start and end and start > end:
        raise HTTPException(422, 'Start date must not exceed end date')
    sql = '''SELECT h.id,h.garment_id,g.name AS garment_name,h.worn_on,h.note
             FROM wear_history h JOIN garments g ON g.id=h.garment_id WHERE 1=1'''
    args = []
    if garment_id is not None:
        sql += ' AND h.garment_id=?'; args.append(garment_id)
    if start:
        sql += ' AND h.worn_on>=?'; args.append(start.isoformat())
    if end:
        sql += ' AND h.worn_on<=?'; args.append(end.isoformat())
    with store().connection() as db:
        return [dict(r) for r in db.execute(sql+' ORDER BY h.worn_on DESC,h.id DESC LIMIT ?', [*args, limit])]


@router.delete('/wear-history/{history_id}')
def delete_wear_history(history_id: int):
    initialize()
    with store().connection() as db:
        row = db.execute('SELECT garment_id FROM wear_history WHERE id=?', (history_id,)).fetchone()
        if row is None:
            raise HTTPException(404, 'Wear record not found')
        db.execute('DELETE FROM wear_history WHERE id=?', (history_id,))
        db.execute('UPDATE garments SET wears=MAX(0,wears-1) WHERE id=?', (row['garment_id'],))
    return {'deleted': True}


@router.get('/insights')
def wardrobe_insights():
    initialize()
    with store().connection() as db:
        garments = [dict(r) for r in db.execute('SELECT * FROM garments')]
        history_count = db.execute('SELECT COUNT(*) FROM wear_history').fetchone()[0]
    categories = dict(sorted(Counter(g['category'] for g in garments).items()))
    colors = dict(sorted(Counter(g['color'] for g in garments).items()))
    return {
        'total_garments': len(garments),
        'total_recorded_wears': sum(g['wears'] for g in garments),
        'wear_history_entries': history_count,
        'favorites': sum(bool(g['favorite']) for g in garments),
        'never_worn': [dict(id=g['id'], name=g['name']) for g in garments if g['wears'] == 0],
        'most_worn': [dict(id=g['id'], name=g['name'], wears=g['wears'])
                      for g in sorted(garments, key=lambda g: (-g['wears'], g['id']))[:5]],
        'categories': categories, 'colors': colors,
    }


@router.get('/recommendations/explained')
def explained_recommendations(occasion: str = 'casual', season: str = 'all',
                                limit: int = Query(10, ge=1, le=50)):
    """Rank owned garments by season, occasion, favorites and low usage.

    No personal data leaves the machine; ranking is deterministic and explainable.
    """
    garments = store().list()
    results = []
    for garment in garments:
        reasons = []
        score = 0
        if garment['occasion'] == occasion.lower():
            score += 4; reasons.append('Matches requested occasion')
        elif garment['occasion'] != 'all':
            continue
        if garment['season'] in ('all', season.lower()):
            score += 3; reasons.append('Suitable for selected season')
        else:
            continue
        if garment['favorite']:
            score += 2; reasons.append('Marked as favorite')
        if garment['wears'] == 0:
            score += 2; reasons.append('Not yet worn')
        elif garment['wears'] <= 2:
            score += 1; reasons.append('Infrequently worn')
        results.append({'garment': garment, 'score': score, 'reasons': reasons})
    return sorted(results, key=lambda item: (-item['score'], item['garment']['id']))[:limit]
