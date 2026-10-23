"""Local-only lending API."""
from datetime import date
from functools import lru_cache
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .lending import LendingStore

router=APIRouter(prefix='/api/v1/wardrobe/lending',tags=['Wardrobe Lending'])
@lru_cache(maxsize=1)
def service(): return LendingStore(store())

class NewLoan(BaseModel):
    garment_id:int=Field(gt=0)
    direction:str
    contact:str=Field(min_length=1,max_length=150)
    start_date:date
    due_date:date
    notes:str=Field(default='',max_length=1000)

class ReturnLoan(BaseModel):
    returned_at:date|None=None

class ExtendLoan(BaseModel):
    due_date:date

def run(fn,*args,**kwargs):
    try: return fn(*args,**kwargs)
    except LookupError as exc: raise HTTPException(404,str(exc)) from exc
    except ValueError as exc: raise HTTPException(422,str(exc)) from exc

@router.post('/loans',status_code=201)
def create(body:NewLoan): return run(service().create,**body.model_dump(mode='json'))

@router.get('/loans')
def list_loans(direction:str|None=None,active_only:bool=False,overdue_only:bool=False):
    return run(service().list,direction,active_only,overdue_only)

@router.get('/summary')
def summary(): return service().summary()

@router.get('/loans/{loan_id}')
def get(loan_id:int):
    result=service().get(loan_id)
    if not result: raise HTTPException(404,'Loan not found')
    return result

@router.post('/loans/{loan_id}/return')
def return_loan(loan_id:int,body:ReturnLoan): return run(service().return_loan,loan_id,body.returned_at)

@router.patch('/loans/{loan_id}/due-date')
def extend(loan_id:int,body:ExtendLoan): return run(service().extend,loan_id,body.due_date)

@router.get('/loans/{loan_id}/history')
def history(loan_id:int): return run(service().history,loan_id)


@router.get('/insights', tags=['Wardrobe Lending Analytics'])
def insights(days:int=30):
    from .lending_analytics import build_lending_insights
    return run(build_lending_insights, service(), days=days)
