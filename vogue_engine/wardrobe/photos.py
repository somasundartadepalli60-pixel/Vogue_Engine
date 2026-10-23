"""Offline garment image library with validation and SQLite metadata."""
from __future__ import annotations
import hashlib
import io
import sqlite3
from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

MAX_BYTES = 8 * 1024 * 1024
MAX_PIXELS = 24_000_000

class PhotoLibrary:
    def __init__(self, root='vogue_photos', database='vogue_wardrobe.sqlite3'):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.database = str(database)
        with self.connect() as db:
            db.executescript("""CREATE TABLE IF NOT EXISTS garment_photos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                garment_id INTEGER NOT NULL,
                digest TEXT NOT NULL,
                caption TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(garment_id, digest));
                CREATE INDEX IF NOT EXISTS idx_garment_photos_garment ON garment_photos(garment_id);""")

    def connect(self):
        db = sqlite3.connect(self.database)
        db.row_factory = sqlite3.Row
        return db

    def add(self, garment_id, content, caption=''):
        if not isinstance(content, bytes) or not content or len(content) > MAX_BYTES:
            raise ValueError('Image must be nonempty and no larger than 8 MiB')
        if len(caption) > 240:
            raise ValueError('Caption too long')
        with self.connect() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?', (garment_id,)).fetchone():
                raise LookupError('Garment not found')
        try:
            with Image.open(io.BytesIO(content)) as image:
                if image.width * image.height > MAX_PIXELS:
                    raise ValueError('Image dimensions exceed limit')
                if image.format not in ('PNG','JPEG','WEBP'):
                    raise ValueError('Only PNG, JPEG and WebP are supported')
                image = ImageOps.exif_transpose(image)
                image.thumbnail((1600, 1600))
                output = io.BytesIO()
                image.convert('RGB').save(output, format='JPEG', quality=85, optimize=True)
                normalized = output.getvalue()
        except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as exc:
            raise ValueError('Invalid image') from exc
        digest = hashlib.sha256(normalized).hexdigest()
        destination = self.root / (digest + '.jpg')
        with self.connect() as db:
            existing = db.execute('SELECT * FROM garment_photos WHERE garment_id=? AND digest=?', (garment_id,digest)).fetchone()
            if existing:
                return dict(existing)
            destination.write_bytes(normalized)
            cursor = db.execute('INSERT INTO garment_photos(garment_id,digest,caption) VALUES (?,?,?)', (garment_id,digest,caption))
            db.commit()
            return self.get(cursor.lastrowid)

    def get(self, photo_id):
        with self.connect() as db:
            row = db.execute('SELECT * FROM garment_photos WHERE id=?', (photo_id,)).fetchone()
            return dict(row) if row else None

    def list(self, garment_id=None):
        with self.connect() as db:
            if garment_id is None:
                rows = db.execute('SELECT * FROM garment_photos ORDER BY id DESC').fetchall()
            else:
                rows = db.execute('SELECT * FROM garment_photos WHERE garment_id=? ORDER BY id DESC', (garment_id,)).fetchall()
            return [dict(row) for row in rows]

    def update_caption(self, photo_id, caption):
        if len(caption)>240:
            raise ValueError('Caption too long')
        with self.connect() as db:
            db.execute('UPDATE garment_photos SET caption=? WHERE id=?',(caption,photo_id))
            db.commit()
        return self.get(photo_id)

    def remove(self, photo_id):
        photo = self.get(photo_id)
        if not photo:
            return False
        with self.connect() as db:
            db.execute('DELETE FROM garment_photos WHERE id=?',(photo_id,))
            db.commit()
            remaining = db.execute('SELECT 1 FROM garment_photos WHERE digest=?',(photo['digest'],)).fetchone()
        if not remaining:
            (self.root / (photo['digest']+'.jpg')).unlink(missing_ok=True)
        return True

    def path_for(self, photo_id):
        photo = self.get(photo_id)
        if photo is None:
            raise LookupError('Photo not found')
        return self.root / (photo['digest']+'.jpg')
