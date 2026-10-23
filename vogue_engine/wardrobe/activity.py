"""Stage 31: append-only local wardrobe activity journal and inventory change history."""
from __future__ import annotations
import json
import sqlite3
from datetime import datetime, timezone

SCHEMA = '''
CREATE TABLE IF NOT EXISTS wardrobe_activity (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 occurred_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
 entity_type TEXT NOT NULL,
 entity_id INTEGER,
 action TEXT NOT NULL,
 details TEXT NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS idx_activity_time ON wardrobe_activity(occurred_at DESC, id DESC);
CREATE INDEX IF NOT EXISTS idx_activity_entity ON wardrobe_activity(entity_type, entity_id);
CREATE TRIGGER IF NOT EXISTS activity_garment_insert AFTER INSERT ON garments BEGIN
 INSERT INTO wardrobe_activity(entity_type,entity_id,action,details)
 VALUES('garment',NEW.id,'created',json_object('name',NEW.name,'category',NEW.category,'color',NEW.color));
END;
CREATE TRIGGER IF NOT EXISTS activity_garment_update AFTER UPDATE ON garments BEGIN
 INSERT INTO wardrobe_activity(entity_type,entity_id,action,details)
 VALUES('garment',NEW.id,'updated',json_object('before',json_object('name',OLD.name,'category',OLD.category,'color',OLD.color,'wears',OLD.wears,'favorite',OLD.favorite),'after',json_object('name',NEW.name,'category',NEW.category,'color',NEW.color,'wears',NEW.wears,'favorite',NEW.favorite)));
END;
CREATE TRIGGER IF NOT EXISTS activity_garment_delete AFTER DELETE ON garments BEGIN
 INSERT INTO wardrobe_activity(entity_type,entity_id,action,details)
 VALUES('garment',OLD.id,'deleted',json_object('name',OLD.name));
END;
CREATE TRIGGER IF NOT EXISTS activity_outfit_insert AFTER INSERT ON outfits BEGIN
 INSERT INTO wardrobe_activity(entity_type,entity_id,action,details)
 VALUES('outfit',NEW.id,'created',json_object('name',NEW.name));
END;
CREATE TRIGGER IF NOT EXISTS activity_outfit_delete AFTER DELETE ON outfits BEGIN
 INSERT INTO wardrobe_activity(entity_type,entity_id,action,details)
 VALUES('outfit',OLD.id,'deleted',json_object('name',OLD.name));
END;
'''

class ActivityJournal:
    def __init__(self, path: str):
        self.path = str(path)
        with self._connect() as db:
            db.executescript(SCHEMA)

    def _connect(self):
        db = sqlite3.connect(self.path)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA foreign_keys=ON')
        return db

    def record(self, entity_type: str, action: str, *, entity_id: int | None = None, details: dict | None = None):
        if entity_type not in {'garment','outfit','inventory','system'}:
            raise ValueError('Unsupported entity type')
        if not action or len(action) > 60 or not action.replace('_','').isalnum():
            raise ValueError('Invalid action')
        serialized = json.dumps(details or {}, ensure_ascii=False)
        if len(serialized) > 10000:
            raise ValueError('Activity details too large')
        with self._connect() as db:
            cursor = db.execute('INSERT INTO wardrobe_activity(entity_type,entity_id,action,details) VALUES(?,?,?,?)', (entity_type,entity_id,action,serialized))
            db.commit()
            return self.get(cursor.lastrowid)

    def get(self, activity_id: int):
        with self._connect() as db:
            row = db.execute('SELECT * FROM wardrobe_activity WHERE id=?', (activity_id,)).fetchone()
        if row is None:
            raise LookupError('Activity not found')
        item = dict(row)
        item['details'] = json.loads(item['details'])
        return item

    def list(self, *, entity_type: str | None = None, entity_id: int | None = None, action: str | None = None, since: str | None = None, until: str | None = None, limit: int = 100, offset: int = 0):
        if not 1 <= limit <= 500 or offset < 0:
            raise ValueError('Invalid pagination')
        sql = 'SELECT * FROM wardrobe_activity WHERE 1=1'
        args = []
        for field, value in [('entity_type',entity_type),('entity_id',entity_id),('action',action)]:
            if value is not None:
                sql += f' AND {field}=?'
                args.append(value)
        if since:
            sql += ' AND occurred_at>=?'; args.append(since)
        if until:
            sql += ' AND occurred_at<=?'; args.append(until)
        sql += ' ORDER BY occurred_at DESC,id DESC LIMIT ? OFFSET ?'
        args.extend([limit,offset])
        with self._connect() as db:
            rows = [dict(r) for r in db.execute(sql,args)]
        for item in rows:
            item['details'] = json.loads(item['details'])
        return rows

    def summary(self):
        with self._connect() as db:
            total = db.execute('SELECT COUNT(*) FROM wardrobe_activity').fetchone()[0]
            actions = [dict(r) for r in db.execute('SELECT entity_type,action,COUNT(*) AS count FROM wardrobe_activity GROUP BY entity_type,action ORDER BY count DESC,entity_type,action')]
            months = [dict(r) for r in db.execute("SELECT substr(occurred_at,1,7) AS month, COUNT(*) AS count FROM wardrobe_activity GROUP BY month ORDER BY month DESC LIMIT 24")]
        return {'total':total,'by_action':actions,'by_month':months}
