"""Offline garment lifecycle REST interface."""
from datetime import date
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .sustainability import SustainabilityStore

router = APIRouter(prefix='/api/v1/wardrobe/sustainability', tags=['Wardrobe Sustainability'])

@lru_cache(maxsize=1)
def sustainability():
    return SustainabilityStore(store())

class LifecycleInput(BaseModel):
    garment_id: int = Field(gt=0)
    action: str
    event_date: date
    recipient: str = Field(default='', max_length=200)
    notes: str = Field(default='', max_length=2000)

def run(callback):
    try:
        return callback()
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc

@router.post('/events', status_code=201)
def record(body: LifecycleInput):
    return run(lambda: sustainability().record(body.garment_id, body.action, body.event_date,
                                                body.recipient, body.notes))

@router.get('/events')
def history(garment_id: int | None = Query(default=None, gt=0),
            action: str | None = None, limit: int = Query(default=100, ge=1, le=500)):
    return run(lambda: sustainability().history(garment_id, action, limit))

@router.delete('/events/{event_id}')
def delete(event_id: int):
    return {'deleted': sustainability().delete(event_id)}

@router.get('/report')
def report(year: int | None = Query(default=None, ge=1900, le=9999)):
    return run(lambda: sustainability().report(year))
