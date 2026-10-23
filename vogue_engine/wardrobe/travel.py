"""Offline trip packing planner backed by the wardrobe SQLite database."""
from __future__ import annotations
from datetime import date
from .storage import WardrobeStore

class TravelStore:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with self.wardrobe.connection() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS trips (id INTEGER PRIMARY KEY, name TEXT NOT NULL,
                destination TEXT NOT NULL, start_date TEXT NOT NULL, end_date TEXT NOT NULL,
                season TEXT NOT NULL DEFAULT 'all', occasion TEXT NOT NULL DEFAULT 'casual',
                CHECK(end_date >= start_date));
            CREATE TABLE IF NOT EXISTS trip_items (trip_id INTEGER NOT NULL REFERENCES trips(id) ON DELETE CASCADE,
                garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
                packed INTEGER NOT NULL DEFAULT 0 CHECK(packed IN (0,1)),
                PRIMARY KEY(trip_id, garment_id));
            CREATE TABLE IF NOT EXISTS trip_outfits (trip_id INTEGER NOT NULL REFERENCES trips(id) ON DELETE CASCADE,
                day TEXT NOT NULL, outfit_id INTEGER NOT NULL REFERENCES outfits(id) ON DELETE CASCADE,
                PRIMARY KEY(trip_id, day));
            ''')

    def create(self, name: str, destination: str, start: date, end: date, season='all', occasion='casual'):
        if not name.strip() or not destination.strip() or end < start:
            raise ValueError('Trip name, destination and valid date range required')
        if (end-start).days > 365:
            raise ValueError('Trips may not exceed 366 days')
        with self.wardrobe.connection() as db:
            cur=db.execute('INSERT INTO trips(name,destination,start_date,end_date,season,occasion) VALUES(?,?,?,?,?,?)',
                           (name.strip(),destination.strip(),start.isoformat(),end.isoformat(),season.lower(),occasion.lower()))
            trip_id=cur.lastrowid
        return self.get(trip_id)

    def get(self, trip_id):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM trips WHERE id=?',(trip_id,)).fetchone()
            return dict(row) if row else None

    def list(self):
        with self.wardrobe.connection() as db:
            return [dict(row) for row in db.execute('SELECT * FROM trips ORDER BY start_date DESC,id DESC')]

    def delete(self, trip_id):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM trips WHERE id=?',(trip_id,)).rowcount)

    def add_item(self, trip_id, garment_id):
        if not self.get(trip_id): raise LookupError('Trip not found')
        if not self.wardrobe.get(garment_id): raise LookupError('Garment not found')
        with self.wardrobe.connection() as db:
            db.execute('INSERT OR IGNORE INTO trip_items(trip_id,garment_id) VALUES(?,?)',(trip_id,garment_id))
        return self.checklist(trip_id)

    def remove_item(self, trip_id, garment_id):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM trip_items WHERE trip_id=? AND garment_id=?',(trip_id,garment_id)).rowcount)

    def set_packed(self, trip_id, garment_id, packed):
        with self.wardrobe.connection() as db:
            result=db.execute('UPDATE trip_items SET packed=? WHERE trip_id=? AND garment_id=?',
                              (int(packed),trip_id,garment_id))
            if not result.rowcount: raise LookupError('Trip item not found')
        return self.checklist(trip_id)

    def checklist(self, trip_id):
        if not self.get(trip_id): raise LookupError('Trip not found')
        with self.wardrobe.connection() as db:
            items=[dict(row) for row in db.execute('''SELECT g.id,g.name,g.category,g.color,g.season,g.occasion,t.packed
                FROM trip_items t JOIN garments g ON g.id=t.garment_id WHERE t.trip_id=?
                ORDER BY t.packed,g.category,g.name''',(trip_id,))]
        return {'trip_id':trip_id,'items':items,'total':len(items),'packed':sum(i['packed'] for i in items)}

    def recommendations(self, trip_id, limit=20):
        trip=self.get(trip_id)
        if not trip: raise LookupError('Trip not found')
        included={item['id'] for item in self.checklist(trip_id)['items']}
        candidates=self.wardrobe.list()
        def score(g):
            return (3 if g['season'] in ('all',trip['season']) else 0) + (3 if g['occasion']==trip['occasion'] else 0) + (2 if g['favorite'] else 0) - min(g['wears'],10)*0.1
        return [{'garment':g,'score':round(score(g),2)} for g in sorted(candidates,key=lambda g:(-score(g),g['id'])) if g['id'] not in included][:limit]

    def schedule_outfit(self, trip_id, day:date, outfit_id:int):
        trip=self.get(trip_id)
        if not trip: raise LookupError('Trip not found')
        if not trip['start_date'] <= day.isoformat() <= trip['end_date']:
            raise ValueError('Day must be within trip dates')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM outfits WHERE id=?',(outfit_id,)).fetchone():
                raise LookupError('Outfit not found')
            db.execute('INSERT INTO trip_outfits(trip_id,day,outfit_id) VALUES(?,?,?) ON CONFLICT(trip_id,day) DO UPDATE SET outfit_id=excluded.outfit_id',
                       (trip_id,day.isoformat(),outfit_id))
        return self.outfit_schedule(trip_id)

    def outfit_schedule(self,trip_id):
        if not self.get(trip_id): raise LookupError('Trip not found')
        with self.wardrobe.connection() as db:
            return [dict(row) for row in db.execute('''SELECT t.day,o.id AS outfit_id,o.name AS outfit_name
                FROM trip_outfits t JOIN outfits o ON o.id=t.outfit_id WHERE t.trip_id=? ORDER BY t.day''',(trip_id,))]


    def packing_summary(self, trip_id):
        """Summarize packing progress and category coverage for an existing trip."""
        trip=self.get(trip_id)
        if not trip: raise LookupError('Trip not found')
        checklist=self.checklist(trip_id)
        categories={}
        for item in checklist['items']:
            group=categories.setdefault(item['category'], {'total':0,'packed':0})
            group['total']+=1
            group['packed']+=int(item['packed'])
        days=(date.fromisoformat(trip['end_date'])-date.fromisoformat(trip['start_date'])).days+1
        return {'trip':trip,'days':days,'total':checklist['total'],
                'packed':checklist['packed'],'remaining':checklist['total']-checklist['packed'],
                'percent_packed':round(100*checklist['packed']/checklist['total'],1) if checklist['total'] else 0,
                'categories':categories}

    def packing_csv(self, trip_id):
        """Produce an Excel-compatible, offline CSV packing checklist."""
        import csv
        import io
        checklist=self.checklist(trip_id)
        output=io.StringIO(newline='')
        writer=csv.writer(output)
        writer.writerow(['garment_id','name','category','color','packed'])
        for item in checklist['items']:
            writer.writerow([item['id'],item['name'],item['category'],item['color'],
                             'yes' if item['packed'] else 'no'])
        return output.getvalue()

    def save_template(self, name: str, trip_id: int):
        """Save garment references as a reusable, local packing template."""
        if not name.strip() or len(name) > 120:
            raise ValueError('Template name must contain 1–120 characters')
        items = self.checklist(trip_id)['items']
        with self.wardrobe.connection() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS packing_templates
                (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
            db.execute('''CREATE TABLE IF NOT EXISTS packing_template_items
                (template_id INTEGER NOT NULL REFERENCES packing_templates(id) ON DELETE CASCADE,
                 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
                 PRIMARY KEY(template_id, garment_id))''')
            try:
                cur = db.execute('INSERT INTO packing_templates(name) VALUES(?)', (name.strip(),))
            except __import__('sqlite3').IntegrityError as exc:
                raise ValueError('Template name already exists') from exc
            db.executemany('INSERT INTO packing_template_items(template_id, garment_id) VALUES(?,?)',
                           [(cur.lastrowid, item['id']) for item in items])
            return {'id': cur.lastrowid, 'name': name.strip(), 'items': len(items)}

    def list_templates(self):
        with self.wardrobe.connection() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS packing_templates
                (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
            db.execute('''CREATE TABLE IF NOT EXISTS packing_template_items
                (template_id INTEGER NOT NULL REFERENCES packing_templates(id) ON DELETE CASCADE,
                 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
                 PRIMARY KEY(template_id, garment_id))''')
            return [dict(row) for row in db.execute('''SELECT t.id,t.name,t.created_at,
                COUNT(i.garment_id) AS items FROM packing_templates t
                LEFT JOIN packing_template_items i ON i.template_id=t.id
                GROUP BY t.id ORDER BY t.id DESC''')]

    def apply_template(self, trip_id: int, template_id: int):
        if not self.get(trip_id): raise LookupError('Trip not found')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM packing_templates WHERE id=?', (template_id,)).fetchone():
                raise LookupError('Template not found')
            db.execute('''INSERT OR IGNORE INTO trip_items(trip_id,garment_id)
                SELECT ?,garment_id FROM packing_template_items WHERE template_id=?''', (trip_id,template_id))
        return self.checklist(trip_id)

    def delete_template(self, template_id: int):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM packing_templates WHERE id=?',(template_id,)).rowcount)

    def seasonal_plan(self, trip_id: int, limit: int = 30):
        """Offline heuristic; does not fetch or imply live destination weather."""
        trip = self.get(trip_id)
        if not trip: raise LookupError('Trip not found')
        if not 1 <= limit <= 100: raise ValueError('Limit must be 1–100')
        days = (date.fromisoformat(trip['end_date'])-date.fromisoformat(trip['start_date'])).days + 1
        candidates = self.recommendations(trip_id, 100)
        preferred = {'tops': min(days, 5), 'bottoms': min((days+1)//2, 4), 'shoes': 2, 'outerwear': 1}
        counts = {}
        selected = []
        for item in candidates:
            garment = item['garment']
            category = garment['category'].lower()
            cap = preferred.get(category, 2)
            if counts.get(category, 0) >= cap: continue
            counts[category] = counts.get(category, 0) + 1
            selected.append({'garment': garment, 'score': item['score'],
                             'reason': 'Season and occasion matching; verify destination conditions yourself'})
            if len(selected) >= limit: break
        return {'trip_id': trip_id, 'days': days, 'season': trip['season'],
                'weather_source': 'none (offline seasonal rules)', 'suggestions': selected}

    def compare_trips(self, first_id: int, second_id: int):
        """Compare two trip packing lists without modifying either trip."""
        first, second = self.get(first_id), self.get(second_id)
        if not first or not second:
            raise LookupError('Trip not found')
        a, b = self.checklist(first_id), self.checklist(second_id)
        left = {item['id']: item for item in a['items']}
        right = {item['id']: item for item in b['items']}
        return {
            'first': {'trip': first, 'total': a['total'], 'packed': a['packed']},
            'second': {'trip': second, 'total': b['total'], 'packed': b['packed']},
            'shared': [left[k] for k in sorted(left.keys() & right.keys())],
            'first_only': [left[k] for k in sorted(left.keys() - right.keys())],
            'second_only': [right[k] for k in sorted(right.keys() - left.keys())],
        }
