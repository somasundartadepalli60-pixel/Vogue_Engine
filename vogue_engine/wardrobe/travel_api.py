"""Local-only trip and packing endpoints."""
from datetime import date
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .travel import TravelStore

router=APIRouter(prefix='/api/v1/wardrobe/travel',tags=['Wardrobe Travel'])
@lru_cache(maxsize=1)
def travel(): return TravelStore(store())

class TripInput(BaseModel):
    name:str=Field(min_length=1,max_length=120)
    destination:str=Field(min_length=1,max_length=120)
    start_date:date
    end_date:date
    season:str='all'
    occasion:str='casual'
class PackedInput(BaseModel):
    packed:bool
class OutfitDay(BaseModel):
    day:date
    outfit_id:int=Field(gt=0)

def run(action):
    try: return action()
    except LookupError as exc: raise HTTPException(404,str(exc)) from exc
    except ValueError as exc: raise HTTPException(422,str(exc)) from exc

@router.post('/trips',status_code=201)
def create(body:TripInput):
    return run(lambda:travel().create(body.name,body.destination,body.start_date,body.end_date,body.season,body.occasion))
@router.get('/trips')
def trips(): return travel().list()
@router.get('/trips/{trip_id}')
def trip(trip_id:int):
    result=travel().get(trip_id)
    if not result: raise HTTPException(404,'Trip not found')
    return result
@router.delete('/trips/{trip_id}')
def delete(trip_id:int): return {'deleted':travel().delete(trip_id)}
@router.post('/trips/{trip_id}/items/{garment_id}')
def add(trip_id:int,garment_id:int): return run(lambda:travel().add_item(trip_id,garment_id))
@router.delete('/trips/{trip_id}/items/{garment_id}')
def remove(trip_id:int,garment_id:int): return {'removed':travel().remove_item(trip_id,garment_id)}
@router.put('/trips/{trip_id}/items/{garment_id}')
def pack(trip_id:int,garment_id:int,body:PackedInput): return run(lambda:travel().set_packed(trip_id,garment_id,body.packed))
@router.get('/trips/{trip_id}/checklist')
def checklist(trip_id:int): return run(lambda:travel().checklist(trip_id))
@router.get('/trips/{trip_id}/recommendations')
def recommendations(trip_id:int,limit:int=Query(default=20,ge=1,le=100)):
    return run(lambda:travel().recommendations(trip_id,limit))
@router.put('/trips/{trip_id}/outfits')
def outfit(trip_id:int,body:OutfitDay): return run(lambda:travel().schedule_outfit(trip_id,body.day,body.outfit_id))
@router.get('/trips/{trip_id}/outfits')
def outfits(trip_id:int): return run(lambda:travel().outfit_schedule(trip_id))


@router.get('/trips/{trip_id}/summary')
def summary(trip_id:int):
    return run(lambda:travel().packing_summary(trip_id))

@router.get('/trips/{trip_id}/checklist.csv')
def checklist_csv(trip_id:int):
    from fastapi.responses import Response
    content=run(lambda:travel().packing_csv(trip_id))
    return Response(content=content,media_type='text/csv; charset=utf-8',
                    headers={'Content-Disposition':f'attachment; filename="trip-{trip_id}-packing.csv"'})

# Stage 38: reusable packing templates and weather-independent seasonal suggestions.
class TemplateInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)

@router.get('/templates')
def templates(): return travel().list_templates()

@router.post('/trips/{trip_id}/templates', status_code=201)
def save_template(trip_id:int, body:TemplateInput):
    return run(lambda: travel().save_template(body.name, trip_id))

@router.post('/trips/{trip_id}/templates/{template_id}/apply')
def apply_template(trip_id:int, template_id:int):
    return run(lambda: travel().apply_template(trip_id, template_id))

@router.delete('/templates/{template_id}')
def delete_template(template_id:int):
    return {'deleted': travel().delete_template(template_id)}

@router.get('/trips/{trip_id}/seasonal-plan')
def seasonal_plan(trip_id:int, limit:int=Query(default=30,ge=1,le=100)):
    return run(lambda: travel().seasonal_plan(trip_id, limit))

# Stage 39: side-by-side comparison for the interactive template dashboard.
@router.get('/trips/{first_id}/compare/{second_id}')
def compare_trips(first_id:int, second_id:int):
    return run(lambda: travel().compare_trips(first_id, second_id))
