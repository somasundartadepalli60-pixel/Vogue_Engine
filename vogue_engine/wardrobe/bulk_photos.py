"""Atomic, local photo metadata updates and validated bulk deletion."""
from __future__ import annotations
from .photos import PhotoLibrary

class BulkPhotoService:
    def __init__(self, library: PhotoLibrary):
        self.library = library

    def validate_ids(self, photo_ids):
        if not photo_ids or len(photo_ids) > 100 or len(set(photo_ids)) != len(photo_ids):
            raise ValueError('Select 1 to 100 distinct photos')
        if any(not isinstance(i, int) or isinstance(i, bool) or i < 1 for i in photo_ids):
            raise ValueError('Invalid photo identifier')
        with self.library.connect() as db:
            placeholders = ','.join('?' for _ in photo_ids)
            rows = db.execute(f'SELECT id FROM garment_photos WHERE id IN ({placeholders})', photo_ids).fetchall()
        if len(rows) != len(photo_ids):
            raise LookupError('One or more photos do not exist')

    def update_captions(self, photo_ids, caption):
        self.validate_ids(photo_ids)
        if not isinstance(caption, str) or len(caption) > 240:
            raise ValueError('Caption must contain at most 240 characters')
        with self.library.connect() as db:
            db.executemany('UPDATE garment_photos SET caption=? WHERE id=?', [(caption, i) for i in photo_ids])
            db.commit()
        return {'updated': len(photo_ids)}

    def delete(self, photo_ids):
        self.validate_ids(photo_ids)
        # Database deletion is atomic; shared image files are removed only after commit.
        with self.library.connect() as db:
            placeholders = ','.join('?' for _ in photo_ids)
            digests = [row['digest'] for row in db.execute(f'SELECT digest FROM garment_photos WHERE id IN ({placeholders})', photo_ids)]
            db.executemany('DELETE FROM garment_photos WHERE id=?', [(i,) for i in photo_ids])
            db.commit()
            orphaned = [digest for digest in set(digests) if not db.execute('SELECT 1 FROM garment_photos WHERE digest=? LIMIT 1', (digest,)).fetchone()]
        for digest in orphaned:
            (self.library.root / (digest + '.jpg')).unlink(missing_ok=True)
        return {'deleted': len(photo_ids)}
