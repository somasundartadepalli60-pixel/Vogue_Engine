"""Local organization endpoints; no remote services or secrets."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .organization import OrganizationStore

router=APIRouter(prefix='/api/v1/wardrobe/organize',tags=['Wardrobe Organization'])
@lru_cache(maxsize=1)
def organization(): return OrganizationStore(store())

class CollectionInput(BaseModel):
    name: str = Field(min_length=1,max_length=80)
    description: str = Field(default='',max_length=500)
class ItemsInput(BaseModel):
    garment_ids: list[int] = Field(max_length=10000)
class TagsInput(BaseModel):
    tags: list[str] = Field(max_length=30)

def handle(exc):
    if isinstance(exc,LookupError): raise HTTPException(404,str(exc)) from exc
    raise HTTPException(422,str(exc)) from exc

@router.post('/collections',status_code=201)
def create_collection(body:CollectionInput):
    try: return organization().create_collection(body.name,body.description)
    except ValueError as exc: handle(exc)
@router.get('/collections')
def collections(): return organization().collections()
@router.delete('/collections/{collection_id}')
def delete_collection(collection_id:int):
    if not organization().delete_collection(collection_id): raise HTTPException(404,'Collection not found')
    return {'deleted':True}
@router.put('/collections/{collection_id}/items')
def set_items(collection_id:int,body:ItemsInput):
    try: return organization().set_collection_items(collection_id,body.garment_ids)
    except (ValueError,LookupError) as exc: handle(exc)
@router.get('/collections/{collection_id}/items')
def collection_items(collection_id:int):
    try: return organization().collection_items(collection_id)
    except LookupError as exc: handle(exc)
@router.put('/garments/{garment_id}/tags')
def set_tags(garment_id:int,body:TagsInput):
    try: return {'tags':organization().set_tags(garment_id,body.tags)}
    except (ValueError,LookupError) as exc: handle(exc)
@router.get('/tags')
def tags(): return organization().tags()
@router.get('/search')
def search(q:str='',category:str|None=None,color:str|None=None,season:str|None=None,occasion:str|None=None,tag:str|None=None,collection_id:int|None=None,favorite:bool|None=None,min_wears:int|None=None,max_wears:int|None=None,sort:str='name',descending:bool=False,limit:int=Query(50,ge=1,le=500),offset:int=Query(0,ge=0)):
    try:return organization().search(q,category,color,season,occasion,tag,collection_id,favorite,min_wears,max_wears,sort,descending,limit,offset)
    except ValueError as exc: handle(exc)
@router.get('/breakdown')
def breakdown(): return organization().breakdown()
