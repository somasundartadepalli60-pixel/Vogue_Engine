"""Portable, local-only wardrobe exports and validated garment imports."""
from __future__ import annotations
import csv
import io
import json
import sqlite3
import zipfile
from datetime import datetime, timezone
from pathlib import Path

MAX_IMPORT_BYTES = 5 * 1024 * 1024
EXPORT_TABLES = ('garments', 'outfits', 'outfit_garments')
IMPORT_FIELDS = ('name', 'category', 'color', 'season', 'occasion')


def snapshot(db_path: str) -> dict:
    """Export consistent copies of the core wardrobe tables."""
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        db.execute('BEGIN')
        tables = {}
        for table in EXPORT_TABLES:
            tables[table] = [dict(row) for row in db.execute(f'SELECT * FROM {table} ORDER BY 1')]
        db.rollback()
    return {'format': 'vogue-wardrobe-v1', 'exported_at': datetime.now(timezone.utc).isoformat(), 'tables': tables}


def json_bytes(db_path: str) -> bytes:
    return json.dumps(snapshot(db_path), indent=2, ensure_ascii=False).encode('utf-8')


def csv_bytes(db_path: str, table: str = 'garments') -> bytes:
    if table not in EXPORT_TABLES:
        raise ValueError('Unknown export table')
    records = snapshot(db_path)['tables'][table]
    fields = {'garments': ('id','name','category','color','season','occasion','favorite','wears','created_at'),
              'outfits': ('id','name','occasion','created_at'),
              'outfit_garments': ('outfit_id','garment_id')}[table]
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=fields, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(records)
    return output.getvalue().encode('utf-8-sig')


def archive_bytes(db_path: str) -> bytes:
    """ZIP of a portable JSON snapshot and three CSV reports; excludes private photos."""
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('wardrobe.json', json_bytes(db_path))
        for table in EXPORT_TABLES:
            archive.writestr(f'{table}.csv', csv_bytes(db_path, table))
    return out.getvalue()


def validate_import(data: bytes) -> list[dict]:
    if len(data) > MAX_IMPORT_BYTES:
        raise ValueError('Import exceeds 5 MiB limit')
    try:
        document = json.loads(data.decode('utf-8-sig'))
    except (ValueError, UnicodeError) as exc:
        raise ValueError('Invalid UTF-8 JSON') from exc
    if not isinstance(document, dict) or document.get('format') != 'vogue-wardrobe-v1':
        raise ValueError('Unsupported wardrobe format')
    tables = document.get('tables')
    if not isinstance(tables, dict) or not isinstance(tables.get('garments'), list):
        raise ValueError('Missing garments list')
    garments = tables['garments']
    if len(garments) > 10000:
        raise ValueError('Too many garments')
    cleaned = []
    for index, garment in enumerate(garments):
        if not isinstance(garment, dict):
            raise ValueError(f'Garment {index} must be an object')
        entry = {}
        for field in IMPORT_FIELDS:
            value = garment.get(field, 'all' if field == 'season' else 'casual' if field == 'occasion' else '')
            if not isinstance(value, str) or not value.strip() or len(value) > 200:
                raise ValueError(f'Invalid {field} at garment {index}')
            entry[field] = value.strip()
        cleaned.append(entry)
    return cleaned


def preview_import(data: bytes) -> dict:
    garments = validate_import(data)
    return {'valid': True, 'garment_count': len(garments), 'sample': garments[:5],
            'import_mode': 'append garments only; outfit relationships are not imported'}


def import_garments(db_path: str, data: bytes, *, confirm: bool = False) -> dict:
    if not confirm:
        raise ValueError('Explicit confirmation is required')
    garments = validate_import(data)
    with sqlite3.connect(db_path) as db:
        db.execute('BEGIN IMMEDIATE')
        for garment in garments:
            db.execute('INSERT INTO garments (name,category,color,season,occasion) VALUES (?,?,?,?,?)',
                       tuple(garment[field] for field in IMPORT_FIELDS))
        db.commit()
    return {'imported': len(garments), 'mode': 'append'}
