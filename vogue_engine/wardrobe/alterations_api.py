"""Local alteration and tailoring API."""
from functools import lru_cache
from datetime import date, datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .alterations import AlterationStore

router=APIRouter(prefix='/api/v1/wardrobe/alterations',tags=['Wardrobe Alterations'])
@lru_cache(maxsize=1)
def service(): return AlterationStore(store())

class CreateJob(BaseModel):
    garment_id:int=Field(gt=0)
    description:str=Field(min_length=1,max_length=500)
    tailor:str=Field(default='',max_length=120)
    due_date:date|None=None
    appointment_at:datetime|None=None
    estimated_cost:float=Field(default=0,ge=0,le=1e9)
    notes:str=Field(default='',max_length=1000)

class UpdateJob(BaseModel):
    tailor:str|None=Field(default=None,max_length=120)
    due_date:date|None=None
    appointment_at:datetime|None=None
    estimated_cost:float|None=Field(default=None,ge=0,le=1e9)
    actual_cost:float|None=Field(default=None,ge=0,le=1e9)
    notes:str|None=Field(default=None,max_length=1000)

class StatusChange(BaseModel):
    status:str
    note:str=Field(default='',max_length=500)

def run(fn,*args,**kwargs):
    try: return fn(*args,**kwargs)
    except LookupError as exc: raise HTTPException(404,str(exc)) from exc
    except ValueError as exc: raise HTTPException(422,str(exc)) from exc

@router.post('/jobs',status_code=201)
def create(body:CreateJob):
    values=body.model_dump(mode='json')
    return run(service().create,**values)

@router.get('/jobs')
def jobs(garment_id:int|None=None,status:str|None=None,due_before:date|None=None):
    return run(service().list,garment_id,status,due_before.isoformat() if due_before else None)

@router.get('/summary')
def summary(): return service().summary()

@router.get('/jobs/{job_id}')
def get(job_id:int):
    result=service().get(job_id)
    if not result: raise HTTPException(404,'Job not found')
    return result

@router.patch('/jobs/{job_id}')
def update(job_id:int,body:UpdateJob):
    return run(service().update,job_id,**body.model_dump(exclude_unset=True,mode='json'))

@router.post('/jobs/{job_id}/status')
def status(job_id:int,body:StatusChange): return run(service().transition,job_id,body.status,body.note)

@router.get('/jobs/{job_id}/history')
def history(job_id:int): return run(service().history,job_id)

@router.delete('/jobs/{job_id}')
def delete(job_id:int):
    if not service().delete(job_id): raise HTTPException(404,'Job not found')
    return {'deleted':True}

@router.get('/insights')
def insights():
    """Local monthly expenses, upcoming appointments, and due-date reminders."""
    from .tailoring_insights import build_insights
    return build_insights(service().list())
