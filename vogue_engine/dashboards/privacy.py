"""Local-only privacy management protected by a passphrase stored as a salted hash."""
import hashlib
import hmac
import os
import sqlite3
from pathlib import Path
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, Field
from .report_store import ReportStore
from .user import REPORT_CACHE

router = APIRouter(prefix='/api/v1/privacy', tags=['Local Privacy'])
SETTINGS_PATH = Path.home() / '.vogue_engine' / 'privacy.sqlite3'

class Passphrase(BaseModel):
    passphrase: str = Field(min_length=12, max_length=256)

def database():
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(SETTINGS_PATH)
    db.execute('CREATE TABLE IF NOT EXISTS local_auth (id INTEGER PRIMARY KEY CHECK(id=1), salt BLOB NOT NULL, digest BLOB NOT NULL)')
    return db

def require_auth(passphrase):
    if not passphrase:
        raise HTTPException(401, 'Passphrase required in X-Local-Passphrase header')
    with database() as db:
        row = db.execute('SELECT salt,digest FROM local_auth WHERE id=1').fetchone()
    if not row:
        raise HTTPException(403, 'Set up local privacy passphrase first')
    digest = hashlib.scrypt(passphrase.encode(), salt=row[0], n=2**14, r=8, p=1)
    if not hmac.compare_digest(digest, row[1]):
        raise HTTPException(401, 'Invalid passphrase')

@router.post('/setup', status_code=201)
def setup(body: Passphrase):
    salt = os.urandom(16)
    digest = hashlib.scrypt(body.passphrase.encode(), salt=salt, n=2**14, r=8, p=1)
    with database() as db:
        if db.execute('SELECT 1 FROM local_auth WHERE id=1').fetchone():
            raise HTTPException(409, 'Already configured')
        db.execute('INSERT INTO local_auth VALUES (1,?,?)', (salt,digest))
    return {'configured': True}

@router.get('/reports')
def reports(x_local_passphrase: str | None = Header(default=None)):
    require_auth(x_local_passphrase)
    return ReportStore().list()

@router.delete('/reports/{report_id}')
def delete_report(report_id: str, x_local_passphrase: str | None = Header(default=None)):
    require_auth(x_local_passphrase)
    deleted = ReportStore().delete(report_id)
    REPORT_CACHE.pop(report_id, None)
    if not deleted:
        raise HTTPException(404, 'Report not found')
    return {'deleted': True}

@router.delete('/reports')
def clear_reports(x_local_passphrase: str | None = Header(default=None)):
    require_auth(x_local_passphrase)
    count = ReportStore().clear()
    REPORT_CACHE.clear()
    return {'deleted_reports': count}
