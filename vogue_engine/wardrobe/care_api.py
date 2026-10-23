# Local care endpoints
from functools import lru_cache
from datetime import date
from fastapi import APIRouter,HTTPException,Query
from pydantic import BaseModel,Field
from .api import store
from .care import CareStore,CONDITIONS,EVENTS

router=APIRouter(prefix='/api/v1/wardrobe/care',tags=['Wardrobe Care'])
@lru_cache(maxsize=1)
def care(): return CareStore(store())

class CareInput(BaseModel):
    condition:str='good'
    wash_interval_days:int=Field(default=7,ge=1,le=365)
    last_washed:date|None=None
    care_instructions:str=Field(default='',max_length=2000)
class EventInput(BaseModel):
    event_type:str
    event_date:date
    notes:str=Field(default='',max_length=1000)

def fail(exc): raise HTTPException(status_code=404 if isinstance(exc,LookupError) else 422,detail=str(exc)) from exc

@router.put('/garments/{garment_id}')
def configure(garment_id:int,body:CareInput):
    try: return care().configure(garment_id,body.condition,body.wash_interval_days,body.last_washed,body.care_instructions)
    except (ValueError,LookupError) as exc: fail(exc)
@router.get('/garments/{garment_id}')
def garment(garment_id:int):
    result=care().get(garment_id)
    if result is None: raise HTTPException(404,'Care profile not found')
    return result
@router.post('/garments/{garment_id}/events')
def record(garment_id:int,body:EventInput):
    try: return care().record(garment_id,body.event_type,body.event_date,body.notes)
    except (ValueError,LookupError) as exc: fail(exc)
@router.get('/garments/{garment_id}/events')
def history(garment_id:int): return care().history(garment_id)
@router.get('/reminders')
def reminders(as_of:date|None=None,days:int=Query(default=0,ge=0,le=365)):
    return care().reminders(as_of,days)
@router.get('/overview')
def overview(as_of:date|None=None): return care().overview(as_of)
