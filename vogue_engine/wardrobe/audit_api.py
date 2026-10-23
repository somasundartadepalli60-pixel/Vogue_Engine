"""Local inventory audit HTTP endpoints."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .audit import InventoryAuditor

router = APIRouter(prefix='/api/v1/wardrobe/audits', tags=['Wardrobe Audits'])

@lru_cache(maxsize=1)
def service():
    return InventoryAuditor(store())

class NewAudit(BaseModel):
    label: str = Field(min_length=1,max_length=120)

class Presence(BaseModel):
    present: bool = True

def execute(fn,*args,**kwargs):
    try:
        return fn(*args,**kwargs)
    except LookupError as exc:
        raise HTTPException(404,str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(422,str(exc)) from exc

@router.post('',status_code=201)
def start(body:NewAudit):
    return execute(service().start,body.label)

@router.get('')
def list_audits():
    return service().list()

@router.get('/integrity')
def integrity():
    return service().integrity()

@router.get('/{audit_id}')
def get(audit_id:int):
    return execute(service().get,audit_id)

@router.put('/{audit_id}/items/{garment_id}')
def mark(audit_id:int,garment_id:int,body:Presence):
    return execute(service().confirm,audit_id,garment_id,body.present)

@router.get('/compare/{earlier_id}/{later_id}')
def compare(earlier_id: int, later_id: int):
    return execute(service().compare, earlier_id, later_id)
