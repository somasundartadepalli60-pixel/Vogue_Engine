"""Local reminder API; polling is performed by the client, not a background daemon."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .reminders import ReminderStore, KINDS

router=APIRouter(prefix='/api/v1/wardrobe/reminders',tags=['Wardrobe Reminders'])

@lru_cache(maxsize=1)
def manager(): return ReminderStore(store().path)

class ReminderCreate(BaseModel):
    title: str = Field(min_length=1,max_length=120)
    kind: str
    due_at: str
    garment_id: int | None = Field(default=None,ge=1)
    notes: str = Field(default='',max_length=1000)

class StatusUpdate(BaseModel):
    status: str

class PreferenceUpdate(BaseModel):
    enabled: bool = True
    lookahead_hours: int = Field(default=24,ge=1,le=720)

def guarded(fn,*args,**kwargs):
    try: return fn(*args,**kwargs)
    except ValueError as exc: raise HTTPException(422,str(exc)) from exc
    except LookupError as exc: raise HTTPException(404,str(exc)) from exc

@router.post('',status_code=201)
def create_reminder(body:ReminderCreate): return guarded(manager().create,**body.model_dump())

@router.get('')
def list_reminders(status:str|None=None,kind:str|None=None,limit:int=Query(100,ge=1,le=500),offset:int=Query(0,ge=0)):
    return guarded(manager().list,status,kind,limit,offset)

@router.get('/notifications')
def current_notifications(): return manager().notifications()

@router.get('/preferences')
def get_preferences(): return manager().preferences()

@router.put('/preferences')
def update_preferences(body:PreferenceUpdate): return guarded(manager().set_preferences,**body.model_dump())

@router.get('/{reminder_id}')
def reminder_detail(reminder_id:int): return guarded(manager().get,reminder_id)

@router.patch('/{reminder_id}/status')
def change_reminder_status(reminder_id:int,body:StatusUpdate): return guarded(manager().set_status,reminder_id,body.status)
