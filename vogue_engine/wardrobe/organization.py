"""Offline organization, reusable collections, and inventory search."""
from __future__ import annotations
import sqlite3
from collections import Counter
from .storage import WardrobeStore

SCHEMA = """
CREATE TABLE IF NOT EXISTS wardrobe_collections (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE COLLATE NOCASE, description TEXT NOT NULL DEFAULT '', created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS wardrobe_collection_items (collection_id INTEGER NOT NULL REFERENCES wardrobe_collections(id) ON DELETE CASCADE, garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE, PRIMARY KEY(collection_id,garment_id));
CREATE TABLE IF NOT EXISTS wardrobe_tags (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE COLLATE NOCASE);
CREATE TABLE IF NOT EXISTS wardrobe_garment_tags (garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE, tag_id INTEGER NOT NULL REFERENCES wardrobe_tags(id) ON DELETE CASCADE, PRIMARY KEY(garment_id,tag_id));
CREATE INDEX IF NOT EXISTS idx_collection_garment ON wardrobe_collection_items(garment_id);
CREATE INDEX IF NOT EXISTS idx_tag_garment ON wardrobe_garment_tags(garment_id);
"""

class OrganizationStore:
    def __init__(self, store: WardrobeStore):
        self.store = store
        with store.connection() as db:
            db.executescript(SCHEMA)

    @staticmethod
    def clean(value: str, limit: int = 80) -> str:
        if not isinstance(value, str) or not value.strip() or len(value.strip()) > limit:
            raise ValueError(f'Value must contain 1 to {limit} characters')
        return value.strip()

    def create_collection(self, name: str, description: str = '') -> dict:
        name = self.clean(name)
        if len(description) > 500: raise ValueError('Description too long')
        with self.store.connection() as db:
            try:
                cur = db.execute('INSERT INTO wardrobe_collections(name,description) VALUES (?,?)', (name,description))
            except sqlite3.IntegrityError as exc: raise ValueError('Collection already exists') from exc
            return {'id':cur.lastrowid,'name':name,'description':description}

    def collections(self) -> list[dict]:
        with self.store.connection() as db:
            return [dict(row) for row in db.execute("""SELECT c.*, COUNT(ci.garment_id) item_count FROM wardrobe_collections c LEFT JOIN wardrobe_collection_items ci ON c.id=ci.collection_id GROUP BY c.id ORDER BY c.name COLLATE NOCASE""")]

    def delete_collection(self, collection_id: int) -> bool:
        with self.store.connection() as db:
            return bool(db.execute('DELETE FROM wardrobe_collections WHERE id=?',(collection_id,)).rowcount)

    def set_collection_items(self, collection_id: int, garment_ids: list[int]) -> dict:
        if len(garment_ids) != len(set(garment_ids)) or len(garment_ids) > 10000:
            raise ValueError('Garment IDs must be unique; maximum 10000')
        with self.store.connection() as db:
            if not db.execute('SELECT 1 FROM wardrobe_collections WHERE id=?',(collection_id,)).fetchone():
                raise LookupError('Collection not found')
            if garment_ids:
                placeholders=','.join('?' for _ in garment_ids)
                found=db.execute(f'SELECT COUNT(*) FROM garments WHERE id IN ({placeholders})',garment_ids).fetchone()[0]
                if found != len(garment_ids): raise ValueError('Unknown garment ID')
            db.execute('DELETE FROM wardrobe_collection_items WHERE collection_id=?',(collection_id,))
            db.executemany('INSERT INTO wardrobe_collection_items(collection_id,garment_id) VALUES (?,?)',[(collection_id,g) for g in garment_ids])
        return {'collection_id':collection_id,'garment_ids':garment_ids}

    def collection_items(self, collection_id: int) -> list[dict]:
        with self.store.connection() as db:
            if not db.execute('SELECT 1 FROM wardrobe_collections WHERE id=?',(collection_id,)).fetchone(): raise LookupError('Collection not found')
            return [dict(row) for row in db.execute("""SELECT g.* FROM garments g JOIN wardrobe_collection_items ci ON ci.garment_id=g.id WHERE ci.collection_id=? ORDER BY g.name COLLATE NOCASE""",(collection_id,))]

    def set_tags(self, garment_id: int, names: list[str]) -> list[str]:
        tags=list(dict.fromkeys(self.clean(n,40).lower() for n in names))
        if len(tags)>30: raise ValueError('Maximum 30 tags per garment')
        with self.store.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone(): raise LookupError('Garment not found')
            db.execute('DELETE FROM wardrobe_garment_tags WHERE garment_id=?',(garment_id,))
            for name in tags:
                db.execute('INSERT OR IGNORE INTO wardrobe_tags(name) VALUES (?)',(name,))
                tag_id=db.execute('SELECT id FROM wardrobe_tags WHERE name=?',(name,)).fetchone()[0]
                db.execute('INSERT INTO wardrobe_garment_tags(garment_id,tag_id) VALUES (?,?)',(garment_id,tag_id))
        return tags

    def tags(self) -> list[dict]:
        with self.store.connection() as db:
            return [dict(r) for r in db.execute("""SELECT t.name,COUNT(gt.garment_id) garment_count FROM wardrobe_tags t LEFT JOIN wardrobe_garment_tags gt ON t.id=gt.tag_id GROUP BY t.id HAVING garment_count>0 ORDER BY t.name""")]

    def search(self, query='', category=None, color=None, season=None, occasion=None, tag=None, collection_id=None, favorite=None, min_wears=None, max_wears=None, sort='name', descending=False, limit=50, offset=0) -> dict:
        if sort not in {'name','created_at','wears','category','color','id'}: raise ValueError('Invalid sort field')
        if not 1<=limit<=500 or offset<0: raise ValueError('Invalid pagination')
        if min_wears is not None and min_wears<0 or max_wears is not None and max_wears<0: raise ValueError('Invalid wear count')
        clauses=['1=1']; params=[]
        if query:
            clauses.append("(g.name LIKE ? ESCAPE '!' OR g.category LIKE ? ESCAPE '!' OR g.color LIKE ? ESCAPE '!')")
            pattern='%'+query.replace('!', '!!').replace('%', '!%').replace('_', '!_')+'%'
            params.extend([pattern]*3)
        for field,value in [('category',category),('color',color),('occasion',occasion)]:
            if value: clauses.append(f'g.{field}=?');params.append(value.lower())
        if season: clauses.append("(g.season=? OR g.season='all')");params.append(season.lower())
        if favorite is not None: clauses.append('g.favorite=?');params.append(int(favorite))
        if min_wears is not None: clauses.append('g.wears>=?');params.append(min_wears)
        if max_wears is not None: clauses.append('g.wears<=?');params.append(max_wears)
        if tag:
            clauses.append('EXISTS (SELECT 1 FROM wardrobe_garment_tags gt JOIN wardrobe_tags t ON t.id=gt.tag_id WHERE gt.garment_id=g.id AND t.name=?)');params.append(tag.lower())
        if collection_id is not None:
            clauses.append('EXISTS (SELECT 1 FROM wardrobe_collection_items ci WHERE ci.garment_id=g.id AND ci.collection_id=?)');params.append(collection_id)
        where=' AND '.join(clauses)
        order=f'g.{sort}'+(' DESC' if descending else ' COLLATE NOCASE' if sort in {'name','category','color'} else ' ASC')+', g.id ASC'
        with self.store.connection() as db:
            total=db.execute('SELECT COUNT(*) FROM garments g WHERE '+where,params).fetchone()[0]
            rows=[dict(r) for r in db.execute('SELECT g.* FROM garments g WHERE '+where+' ORDER BY '+order+' LIMIT ? OFFSET ?',[*params,limit,offset])]
        return {'total':total,'limit':limit,'offset':offset,'items':rows}

    def breakdown(self) -> dict:
        items=self.store.list()
        return {'total':len(items),'unworn':sum(g['wears']==0 for g in items),'favorites':sum(bool(g['favorite']) for g in items),'by_color':dict(sorted(Counter(g['color'] for g in items).items())),'by_season':dict(sorted(Counter(g['season'] for g in items).items())),'by_occasion':dict(sorted(Counter(g['occasion'] for g in items).items())),'by_category':dict(sorted(Counter(g['category'] for g in items).items()))}
