"""Local-only backup management endpoints."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .backups import BackupManager

router = APIRouter(prefix='/api/v1/wardrobe/backups', tags=['Wardrobe Backups'])

@lru_cache(maxsize=1)
def manager():
    return BackupManager(store().path)

class BackupRequest(BaseModel):
    label: str = Field(default='Manual backup', max_length=120)

class RestoreRequest(BaseModel):
    confirm: bool = False

def call(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except FileNotFoundError as exc:
        raise HTTPException(404, str(exc)) from exc
    except (ValueError, OSError) as exc:
        raise HTTPException(422, str(exc)) from exc

@router.post('', status_code=201)
def create(body: BackupRequest):
    return call(manager().create, body.label)

@router.get('')
def list_backups():
    return manager().list()

@router.get('/{backup_id}/verify')
def verify(backup_id: str):
    return call(manager().verify, backup_id)

@router.get('/{backup_id}/preview')
def preview(backup_id: str):
    return call(manager().preview, backup_id)

@router.post('/{backup_id}/restore')
def restore(backup_id: str, body: RestoreRequest):
    return call(manager().restore, backup_id, body.confirm)

@router.delete('/{backup_id}')
def delete(backup_id: str):
    return call(manager().delete, backup_id)
