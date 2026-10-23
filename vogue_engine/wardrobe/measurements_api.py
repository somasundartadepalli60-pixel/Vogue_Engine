"""Stage 19: offline garment sizing API."""
from functools import lru_cache
from datetime import date
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .measurements import MeasurementStore

router=APIRouter(prefix='/api/v1/wardrobe/measurements',tags=['Wardrobe Measurements'])
@lru_cache(maxsize=1)
def service(): return MeasurementStore(store())

class ProfileInput(BaseModel):
    name:str=Field(min_length=1,max_length=80)
    size_label:str=Field(default='',max_length=40)
    measurements:dict[str,float]

class EventInput(BaseModel):
    measured_on:date
    size_label:str=Field(default='',max_length=40)
    note:str=Field(default='',max_length=500)
    measurements:dict[str,float]

def handle(exc):
    raise HTTPException(status_code=404 if isinstance(exc,LookupError) else 422,detail=str(exc)) from exc

@router.put('/profiles')
def upsert_profile(body:ProfileInput):
    try: return service().profile(body.name,body.measurements,body.size_label)
    except ValueError as exc: handle(exc)

@router.get('/profiles')
def list_profiles(): return service().profiles()

@router.get('/profiles/{profile_id}')
def get_profile(profile_id:int):
    item=service().get_profile(profile_id)
    if item is None: raise HTTPException(404,'Profile not found')
    return item

@router.delete('/profiles/{profile_id}')
def delete_profile(profile_id:int):
    if not service().delete_profile(profile_id): raise HTTPException(404,'Profile not found')
    return {'deleted':True}

@router.post('/garments/{garment_id}')
def record(garment_id:int,body:EventInput):
    try: return service().record(garment_id,body.measurements,body.measured_on.isoformat(),body.size_label,body.note)
    except (ValueError,LookupError) as exc: handle(exc)

@router.get('/garments/{garment_id}')
def history(garment_id:int): return service().history(garment_id)

@router.delete('/events/{event_id}')
def delete_event(event_id:int):
    if not service().delete_event(event_id): raise HTTPException(404,'Measurement event not found')
    return {'deleted':True}

@router.get('/fit/{garment_id}/{profile_id}')
def fit(garment_id:int,profile_id:int,ease_cm:float=2.0):
    try: return service().compare(garment_id,profile_id,ease_cm)
    except (ValueError,LookupError) as exc: handle(exc)

# Stage 20: data for the interactive local measurement charts.
from .measurement_trends import summarize_history

@router.get('/garments/{garment_id}/trends')
def measurement_trends(garment_id:int):
    return summarize_history(service().history(garment_id))
