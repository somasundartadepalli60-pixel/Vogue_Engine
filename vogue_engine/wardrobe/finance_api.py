"""Local-only financial tracking endpoints."""
from functools import lru_cache
from datetime import date
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .finance import FinanceStore

router=APIRouter(prefix='/api/v1/wardrobe/finance',tags=['Wardrobe Finance'])

@lru_cache(maxsize=1)
def finance(): return FinanceStore(store())

class PurchaseInput(BaseModel):
    amount: str = Field(pattern=r'^\d+(\.\d{1,2})?$',max_length=16)
    purchased_on: date
    vendor: str = Field(default='',max_length=120)
    notes: str = Field(default='',max_length=1000)
    currency: str = 'INR'

class BudgetInput(BaseModel):
    amount: str = Field(pattern=r'^\d+(\.\d{1,2})?$',max_length=16)
    currency: str = 'INR'

def error(exc):
    raise HTTPException(404 if isinstance(exc,LookupError) else 422,str(exc)) from exc

@router.put('/purchases/{garment_id}')
def set_purchase(garment_id:int,body:PurchaseInput):
    try: return finance().set_purchase(garment_id,body.amount,body.purchased_on.isoformat(),body.vendor,body.notes,body.currency)
    except (ValueError,LookupError) as exc: error(exc)

@router.get('/purchases')
def purchases(month:str|None=None):
    try: return finance().purchases(month)
    except ValueError as exc: error(exc)

@router.get('/purchases/{garment_id}')
def purchase(garment_id:int):
    item=finance().get_purchase(garment_id)
    if item is None: raise HTTPException(404,'Purchase not found')
    return item

@router.put('/budgets/{month}')
def budget(month:str,body:BudgetInput):
    try: return finance().set_budget(month,body.amount,body.currency)
    except ValueError as exc: error(exc)

@router.get('/budgets/{month}')
def monthly(month:str):
    try: return finance().monthly_summary(month)
    except ValueError as exc: error(exc)

@router.get('/overview')
def overview(): return finance().overview()
