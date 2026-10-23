"""SQLite-backed wardrobe repository. No network, API keys, or environment files."""
from __future__ import annotations
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

SCHEMA = """
CREATE TABLE IF NOT EXISTS garments (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL CHECK(length(trim(name)) > 0),
 category TEXT NOT NULL,
 color TEXT NOT NULL,
 season TEXT NOT NULL DEFAULT 'all',
 occasion TEXT NOT NULL DEFAULT 'casual',
 favorite INTEGER NOT NULL DEFAULT 0 CHECK(favorite IN (0,1)),
 wears INTEGER NOT NULL DEFAULT 0 CHECK(wears >= 0),
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_garments_category ON garments(category);
CREATE INDEX IF NOT EXISTS idx_garments_season ON garments(season);
CREATE TABLE IF NOT EXISTS outfits (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 occasion TEXT NOT NULL DEFAULT 'casual',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS outfit_garments (
 outfit_id INTEGER NOT NULL REFERENCES outfits(id) ON DELETE CASCADE,
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 PRIMARY KEY(outfit_id, garment_id)
);
"""

class WardrobeStore:
    def __init__(self, path: str = 'vogue_wardrobe.sqlite3'):
        self.path = str(path)
        if self.path != ':memory:':
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        with self.connection() as db:
            db.executescript(SCHEMA)

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.path)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA foreign_keys=ON')
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    def add(self, name: str, category: str, color: str, season='all', occasion='casual') -> dict:
        if not all(v.strip() for v in (name, category, color)):
            raise ValueError('Name, category and color are required')
        with self.connection() as db:
            cur = db.execute('INSERT INTO garments(name,category,color,season,occasion) VALUES (?,?,?,?,?)',
                             (name.strip(),category.strip().lower(),color.strip().lower(),season.lower(),occasion.lower()))
            return dict(db.execute('SELECT * FROM garments WHERE id=?',(cur.lastrowid,)).fetchone())

    def get(self, garment_id: int) -> Optional[dict]:
        with self.connection() as db:
            row = db.execute('SELECT * FROM garments WHERE id=?',(garment_id,)).fetchone()
            return dict(row) if row else None

    def list(self, category=None, season=None, occasion=None, favorites_only=False) -> list[dict]:
        sql = 'SELECT * FROM garments WHERE 1=1'
        args=[]
        for column, value in [('category',category),('occasion',occasion)]:
            if value:
                sql += f' AND {column}=?'; args.append(value.lower())
        if season:
            sql += " AND (season=? OR season='all')";args.append(season.lower())
        if favorites_only:
            sql += ' AND favorite=1'
        sql += ' ORDER BY favorite DESC, name COLLATE NOCASE, id'
        with self.connection() as db:
            return [dict(r) for r in db.execute(sql,args)]

    def update(self, garment_id: int, **fields) -> Optional[dict]:
        allowed={'name','category','color','season','occasion','favorite','wears'}
        if not fields or set(fields)-allowed:
            raise ValueError('Supply valid fields to update')
        if 'favorite' in fields and fields['favorite'] not in (True,False,0,1):
            raise ValueError('favorite must be boolean')
        if 'wears' in fields and fields['wears'] < 0:
            raise ValueError('wears must be nonnegative')
        with self.connection() as db:
            cur=db.execute('UPDATE garments SET '+', '.join(f'{k}=?' for k in fields)+' WHERE id=?', [*fields.values(),garment_id])
            if not cur.rowcount:return None
            return dict(db.execute('SELECT * FROM garments WHERE id=?',(garment_id,)).fetchone())

    def delete(self, garment_id: int) -> bool:
        with self.connection() as db:
            return bool(db.execute('DELETE FROM garments WHERE id=?',(garment_id,)).rowcount)

    def create_outfit(self, name: str, garment_ids: list[int], occasion='casual') -> dict:
        if not name.strip() or not garment_ids or len(set(garment_ids)) != len(garment_ids):
            raise ValueError('Outfit needs a name and unique garment IDs')
        with self.connection() as db:
            found=db.execute('SELECT COUNT(*) FROM garments WHERE id IN ('+','.join('?'*len(garment_ids))+')',garment_ids).fetchone()[0]
            if found != len(garment_ids): raise ValueError('Unknown garment ID')
            cur=db.execute('INSERT INTO outfits(name,occasion) VALUES (?,?)',(name.strip(),occasion.lower()))
            db.executemany('INSERT INTO outfit_garments(outfit_id,garment_id) VALUES (?,?)',[(cur.lastrowid,g) for g in garment_ids])
            return {'id':cur.lastrowid,'name':name.strip(),'occasion':occasion.lower(),'garment_ids':garment_ids}

    def outfits(self) -> list[dict]:
        with self.connection() as db:
            result=[]
            for row in db.execute('SELECT * FROM outfits ORDER BY id DESC').fetchall():
                outfit=dict(row)
                outfit['garments']=[dict(g) for g in db.execute('SELECT g.* FROM garments g JOIN outfit_garments og ON og.garment_id=g.id WHERE og.outfit_id=? ORDER BY g.id',(row['id'],))]
                result.append(outfit)
            return result

    def statistics(self) -> dict:
        with self.connection() as db:
            total=db.execute('SELECT COUNT(*) FROM garments').fetchone()[0]
            favorites=db.execute('SELECT COUNT(*) FROM garments WHERE favorite=1').fetchone()[0]
            wears=db.execute('SELECT COALESCE(SUM(wears),0) FROM garments').fetchone()[0]
            categories={r['category']:r['count'] for r in db.execute('SELECT category,COUNT(*) count FROM garments GROUP BY category')}
            return {'garments':total,'favorites':favorites,'total_wears':wears,'categories':categories,'outfits':db.execute('SELECT COUNT(*) FROM outfits').fetchone()[0]}
