"""Local maintenance scheduling endpoints; no external services."""
from datetime import date
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .maintenance import MaintenanceStore

router=APIRouter(prefix='/api/v1/wardrobe/maintenance',tags=['Wardrobe Maintenance'])
@lru_cache(maxsize=1)
def manager(): return MaintenanceStore(store())

class PlanInput(BaseModel):
    task:str
    interval_days:int=Field(ge=1,le=3650)
    instructions:str=Field(default='',max_length=2000)
    active:bool=True

class EventInput(BaseModel):
    task:str
    performed_on:date
    notes:str=Field(default='',max_length=1000)

def guarded(fn,*args,**kwargs):
    try: return fn(*args,**kwargs)
    except ValueError as exc: raise HTTPException(422,str(exc)) from exc
    except LookupError as exc: raise HTTPException(404,str(exc)) from exc

@router.put('/garments/{garment_id}/plans')
def set_plan(garment_id:int,body:PlanInput): return guarded(manager().plan,garment_id,**body.model_dump())

@router.get('/garments/{garment_id}/plans')
def plans(garment_id:int): return manager().plans(garment_id)

@router.post('/garments/{garment_id}/events',status_code=201)
def add_event(garment_id:int,body:EventInput): return guarded(manager().record,garment_id,body.task,body.performed_on.isoformat(),body.notes)

@router.get('/garments/{garment_id}/events')
def events(garment_id:int,limit:int=Query(100,ge=1,le=500)): return guarded(manager().history,garment_id,limit)

@router.get('/garments/{garment_id}/recommendations')
def recommendations(garment_id:int): return guarded(manager().recommendations,garment_id)

@router.get('/schedule')
def schedule(as_of:date|None=None,days:int=Query(14,ge=0,le=365)): return manager().schedule(as_of.isoformat() if as_of else None,days)
