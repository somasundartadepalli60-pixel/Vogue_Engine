"""Stage 11 local outfit planning endpoints."""
from datetime import date
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .calendar import CalendarStore

router=APIRouter(prefix='/api/v1/wardrobe/calendar',tags=['Wardrobe Calendar'])
@lru_cache(maxsize=1)
def calendar(): return CalendarStore(store())

class ScheduleInput(BaseModel):
    day:date
    slot:str=Field(default='day',min_length=1,max_length=32)
    outfit_id:int=Field(gt=0)
    note:str=Field(default='',max_length=500)
    force:bool=False
class BlockInput(BaseModel):
    garment_id:int=Field(gt=0)
    start_date:date
    end_date:date
    reason:str=Field(min_length=1,max_length=200)

def safe(fn):
    try: return fn()
    except LookupError as exc: raise HTTPException(404,str(exc)) from exc
    except ValueError as exc: raise HTTPException(422,str(exc)) from exc

@router.post('/schedule',status_code=201)
def schedule(body:ScheduleInput):
    return safe(lambda:calendar().schedule(body.day,body.slot,body.outfit_id,body.note,body.force))
@router.delete('/schedule/{day}/{slot}')
def unschedule(day:date,slot:str): return {'deleted':calendar().unschedule(day,slot)}
@router.get('/agenda')
def agenda(start:date,end:date): return safe(lambda:calendar().agenda(start,end))
@router.get('/conflicts/{outfit_id}')
def conflicts(outfit_id:int,day:date,slot:str='day'):
    return safe(lambda:calendar().conflicts(day,outfit_id,slot))
@router.post('/blocks',status_code=201)
def block(body:BlockInput):
    return safe(lambda:calendar().block(body.garment_id,body.start_date,body.end_date,body.reason))
@router.get('/blocks')
def blocks(day:date|None=None): return calendar().blocks(day)
@router.delete('/blocks/{block_id}')
def unblock(block_id:int): return {'deleted':calendar().unblock(block_id)}
@router.get('/forecast')
def forecast(start:date,days:int=Query(default=30,ge=1,le=366)):
    return safe(lambda:calendar().forecast(start,days))
