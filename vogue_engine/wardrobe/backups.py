"""Offline SQLite backup, verification, preview and guarded restoration."""
from __future__ import annotations
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

class BackupManager:
    def __init__(self, database_path: str, backup_dir: str | None = None):
        self.database_path = Path(database_path).resolve()
        if str(database_path) == ':memory:':
            raise ValueError('Persistent SQLite database required for backups')
        self.backup_dir = Path(backup_dir).resolve() if backup_dir else self.database_path.parent / 'wardrobe_backups'
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def _paths(self, backup_id):
        if not re.fullmatch(r'[a-f0-9]{32}', backup_id):
            raise ValueError('Invalid backup identifier')
        return self.backup_dir / f'{backup_id}.sqlite3', self.backup_dir / f'{backup_id}.json'

    @staticmethod
    def _digest(path):
        h = hashlib.sha256()
        with path.open('rb') as f:
            for block in iter(lambda: f.read(1024 * 1024), b''):
                h.update(block)
        return h.hexdigest()

    @staticmethod
    def _inspect(path):
        with sqlite3.connect(f'file:{path}?mode=ro', uri=True) as db:
            result = db.execute('PRAGMA integrity_check').fetchone()[0]
            if result != 'ok':
                raise ValueError('SQLite integrity check failed: ' + str(result))
            tables = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
            if 'garments' not in tables:
                raise ValueError('Backup does not contain a wardrobe garments table')
            counts = {t: db.execute('SELECT COUNT(*) FROM "' + t.replace('"', '""') + '"').fetchone()[0] for t in tables}
            return {'tables': tables, 'row_counts': counts}

    def create(self, label='Manual backup'):
        if not self.database_path.is_file():
            raise FileNotFoundError('Wardrobe database not found')
        backup_id = uuid4().hex
        db_path, meta_path = self._paths(backup_id)
        try:
            with sqlite3.connect(str(self.database_path)) as src, sqlite3.connect(str(db_path)) as dst:
                src.backup(dst)
            details = self._inspect(db_path)
            meta = {'id': backup_id, 'label': str(label)[:120], 'created_at': datetime.now(timezone.utc).isoformat(), 'sha256': self._digest(db_path), 'bytes': db_path.stat().st_size, **details}
            meta_path.write_text(json.dumps(meta, indent=2), encoding='utf-8')
            return meta
        except Exception:
            db_path.unlink(missing_ok=True)
            meta_path.unlink(missing_ok=True)
            raise

    def list(self):
        result = []
        for p in self.backup_dir.glob('*.json'):
            try:
                result.append(json.loads(p.read_text(encoding='utf-8')))
            except (ValueError, OSError):
                continue
        return sorted(result, key=lambda x: x.get('created_at', ''), reverse=True)

    def verify(self, backup_id):
        db_path, meta_path = self._paths(backup_id)
        if not db_path.is_file() or not meta_path.is_file():
            raise FileNotFoundError('Backup not found')
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        if meta.get('id') != backup_id or meta.get('sha256') != self._digest(db_path):
            raise ValueError('Backup checksum mismatch')
        return {'valid': True, 'backup': meta, 'contents': self._inspect(db_path)}

    def preview(self, backup_id):
        verified = self.verify(backup_id)
        current = self._inspect(self.database_path) if self.database_path.exists() else None
        return {'backup': verified['contents'], 'current': current, 'restore_will_replace_current_database': True}

    def restore(self, backup_id, confirm=False):
        if confirm is not True:
            raise ValueError('Explicit restore confirmation is required')
        self.verify(backup_id)
        db_path, _ = self._paths(backup_id)
        # Keep a recovery point before overwriting the live database.
        recovery = self.create('Automatic pre-restore recovery')
        try:
            with sqlite3.connect(str(db_path)) as src, sqlite3.connect(str(self.database_path)) as dst:
                src.backup(dst)
            self._inspect(self.database_path)
        except Exception:
            recovery_path, _ = self._paths(recovery['id'])
            with sqlite3.connect(str(recovery_path)) as src, sqlite3.connect(str(self.database_path)) as dst:
                src.backup(dst)
            raise
        return {'restored': True, 'backup_id': backup_id, 'recovery_backup_id': recovery['id']}

    def delete(self, backup_id):
        self.verify(backup_id)
        db_path, meta_path = self._paths(backup_id)
        db_path.unlink()
        meta_path.unlink()
        return {'deleted': True}
