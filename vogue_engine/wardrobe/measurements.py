"""Local garment measurements, size profiles, and transparent fit comparisons."""
from __future__ import annotations
from datetime import date
from math import isfinite
from .storage import WardrobeStore

MEASURES = ('chest', 'waist', 'hip', 'shoulder', 'sleeve', 'inseam', 'length')
DDL = """
CREATE TABLE IF NOT EXISTS fit_profiles (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL UNIQUE,
 size_label TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS fit_profile_values (
 profile_id INTEGER NOT NULL REFERENCES fit_profiles(id) ON DELETE CASCADE,
 dimension TEXT NOT NULL,
 cm REAL NOT NULL CHECK(cm>0 AND cm<=400),
 PRIMARY KEY(profile_id,dimension)
);
CREATE TABLE IF NOT EXISTS garment_measurement_events (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 garment_id INTEGER NOT NULL REFERENCES garments(id) ON DELETE CASCADE,
 measured_on TEXT NOT NULL,
 size_label TEXT NOT NULL DEFAULT '',
 note TEXT NOT NULL DEFAULT '',
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS garment_measurement_values (
 event_id INTEGER NOT NULL REFERENCES garment_measurement_events(id) ON DELETE CASCADE,
 dimension TEXT NOT NULL,
 cm REAL NOT NULL CHECK(cm>0 AND cm<=400),
 PRIMARY KEY(event_id,dimension)
);
CREATE INDEX IF NOT EXISTS idx_measurement_garment_date ON garment_measurement_events(garment_id,measured_on DESC,id DESC);
"""

def validated(values):
    if not isinstance(values,dict) or not values:
        raise ValueError('At least one measurement is required')
    result={}
    for key,value in values.items():
        if key not in MEASURES: raise ValueError('Unknown measurement: '+str(key))
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not isfinite(value) or not 0<value<=400:
            raise ValueError('Measurements must be finite centimeters between 0 and 400')
        result[key]=round(float(value),2)
    return result

class MeasurementStore:
    def __init__(self, wardrobe:WardrobeStore):
        self.wardrobe=wardrobe
        with wardrobe.connection() as db: db.executescript(DDL)

    def profile(self, name, measurements, size_label=''):
        name=name.strip()
        if not name or len(name)>80 or len(size_label)>40: raise ValueError('Invalid profile name or size')
        values=validated(measurements)
        with self.wardrobe.connection() as db:
            db.execute('INSERT INTO fit_profiles(name,size_label) VALUES (?,?) ON CONFLICT(name) DO UPDATE SET size_label=excluded.size_label',(name,size_label))
            profile_id=db.execute('SELECT id FROM fit_profiles WHERE name=?',(name,)).fetchone()['id']
            db.execute('DELETE FROM fit_profile_values WHERE profile_id=?',(profile_id,))
            db.executemany('INSERT INTO fit_profile_values(profile_id,dimension,cm) VALUES (?,?,?)',[(profile_id,k,v) for k,v in values.items()])
        return self.get_profile(profile_id)

    def get_profile(self, profile_id):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM fit_profiles WHERE id=?',(profile_id,)).fetchone()
            if row is None: return None
            result=dict(row)
            result['measurements']={r['dimension']:r['cm'] for r in db.execute('SELECT dimension,cm FROM fit_profile_values WHERE profile_id=?',(profile_id,))}
            return result

    def profiles(self):
        with self.wardrobe.connection() as db:
            ids=[r['id'] for r in db.execute('SELECT id FROM fit_profiles ORDER BY name COLLATE NOCASE')]
        return [self.get_profile(i) for i in ids]

    def delete_profile(self, profile_id):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM fit_profiles WHERE id=?',(profile_id,)).rowcount)

    def record(self, garment_id, measurements, measured_on, size_label='', note=''):
        values=validated(measurements)
        measured_on=date.fromisoformat(measured_on).isoformat()
        if len(size_label)>40 or len(note)>500: raise ValueError('Size or note too long')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone():
                raise LookupError('Garment not found')
            event_id=db.execute('INSERT INTO garment_measurement_events(garment_id,measured_on,size_label,note) VALUES (?,?,?,?)',(garment_id,measured_on,size_label,note)).lastrowid
            db.executemany('INSERT INTO garment_measurement_values(event_id,dimension,cm) VALUES (?,?,?)',[(event_id,k,v) for k,v in values.items()])
        return self.event(event_id)

    def event(self, event_id):
        with self.wardrobe.connection() as db:
            row=db.execute('SELECT * FROM garment_measurement_events WHERE id=?',(event_id,)).fetchone()
            if row is None: return None
            result=dict(row)
            result['measurements']={r['dimension']:r['cm'] for r in db.execute('SELECT dimension,cm FROM garment_measurement_values WHERE event_id=?',(event_id,))}
            return result

    def history(self, garment_id):
        with self.wardrobe.connection() as db:
            ids=[r['id'] for r in db.execute('SELECT id FROM garment_measurement_events WHERE garment_id=? ORDER BY measured_on DESC,id DESC',(garment_id,))]
        return [self.event(i) for i in ids]

    def delete_event(self,event_id):
        with self.wardrobe.connection() as db:
            return bool(db.execute('DELETE FROM garment_measurement_events WHERE id=?',(event_id,)).rowcount)

    def compare(self, garment_id, profile_id, ease_cm=2.0):
        if isinstance(ease_cm,bool) or not isinstance(ease_cm,(int,float)) or not isfinite(ease_cm) or not -20<=ease_cm<=30:
            raise ValueError('Ease must be between -20 and 30 cm')
        profile=self.get_profile(profile_id)
        if profile is None: raise LookupError('Profile not found')
        history=self.history(garment_id)
        if not history: raise LookupError('No garment measurements recorded')
        garment=history[0]
        shared=sorted(set(profile['measurements']) & set(garment['measurements']))
        details=[]
        for dimension in shared:
            body=profile['measurements'][dimension]
            actual=garment['measurements'][dimension]
            delta=round(actual-body,2)
            details.append({'dimension':dimension,'profile_cm':body,'garment_cm':actual,'difference_cm':delta,'meets_ease':delta>=ease_cm})
        if not shared: status='insufficient_data'
        elif all(x['meets_ease'] for x in details): status='meets_requested_ease'
        else: status='below_requested_ease'
        return {'garment_id':garment_id,'profile_id':profile_id,'measurement_event_id':garment['id'], 'status':status,'requested_ease_cm':ease_cm,'dimensions':details,'disclaimer':'A numerical comparison only; cut, stretch, fabric, measurement method, and personal comfort affect actual fit.'}
