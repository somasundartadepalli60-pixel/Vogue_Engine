"""Local wardrobe API; standalone router can be mounted on the existing application."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .storage import WardrobeStore
from .planner import suggest_outfits

router=APIRouter(prefix='/api/v1/wardrobe',tags=['Local Wardrobe'])

@lru_cache(maxsize=1)
def store():
    return WardrobeStore()

class GarmentCreate(BaseModel):
    name: str = Field(min_length=1,max_length=120)
    category: str = Field(min_length=1,max_length=40)
    color: str = Field(min_length=1,max_length=40)
    season: str = 'all'
    occasion: str = 'casual'

class GarmentUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    color: str | None = None
    season: str | None = None
    occasion: str | None = None
    favorite: bool | None = None
    wears: int | None = Field(default=None,ge=0)

class OutfitCreate(BaseModel):
    name: str
    garment_ids: list[int]
    occasion: str = 'casual'

@router.post('/garments',status_code=201)
def add_garment(body: GarmentCreate):
    try:return store().add(**body.model_dump())
    except ValueError as exc:raise HTTPException(422,str(exc)) from exc

@router.get('/garments')
def list_garments(category: str | None=None,season: str | None=None,occasion: str | None=None,favorites_only: bool=False):
    return store().list(category,season,occasion,favorites_only)

@router.get('/garments/{garment_id}')
def get_garment(garment_id:int):
    result=store().get(garment_id)
    if result is None:raise HTTPException(404,'Garment not found')
    return result

@router.patch('/garments/{garment_id}')
def update_garment(garment_id:int,body:GarmentUpdate):
    try:result=store().update(garment_id,**body.model_dump(exclude_unset=True))
    except ValueError as exc:raise HTTPException(422,str(exc)) from exc
    if result is None:raise HTTPException(404,'Garment not found')
    return result

@router.delete('/garments/{garment_id}')
def delete_garment(garment_id:int):
    if not store().delete(garment_id):raise HTTPException(404,'Garment not found')
    return {'deleted':True}

@router.post('/outfits',status_code=201)
def create_outfit(body:OutfitCreate):
    try:return store().create_outfit(**body.model_dump())
    except ValueError as exc:raise HTTPException(422,str(exc)) from exc

@router.get('/outfits')
def list_outfits():return store().outfits()

@router.get('/suggestions')
def suggestions(occasion:str='casual',season:str='all',limit:int=Query(10,ge=1,le=100)):
    return suggest_outfits(store().list(),occasion,season,limit)

@router.get('/statistics')
def statistics():return store().statistics()
