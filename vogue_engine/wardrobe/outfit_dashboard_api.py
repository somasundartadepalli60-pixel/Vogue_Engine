"""Stage 41: save a recommended combination only after server-side validation."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .api import store
from .outfit_engine import recommend_combinations

router = APIRouter(prefix='/api/v1/wardrobe/outfit-engine', tags=['Offline Outfit Engine'])

class SaveRecommendation(BaseModel):
    garment_ids: list[int] = Field(min_length=3, max_length=3)
    name: str = Field(min_length=1, max_length=120)
    occasion: str = Field(default='casual', max_length=40)
    season: str = Field(default='all', max_length=40)

@router.post('/save', status_code=201)
def save_recommendation(body: SaveRecommendation):
    if len(set(body.garment_ids)) != 3:
        raise HTTPException(422, 'Select three distinct garments')
    garments = store().list()
    selected = [g for g in garments if g['id'] in body.garment_ids]
    if len(selected) != 3:
        raise HTTPException(404, 'One or more garments no longer exist')
    # Validate that the chosen trio is a real recommendation under the requested filters.
    candidates = recommend_combinations(selected, body.occasion, body.season, limit=1)
    if not candidates or set(candidates[0]['garment_ids']) != set(body.garment_ids):
        raise HTTPException(422, 'Garments are not a compatible top, bottom, and footwear set')
    try:
        return store().create_outfit(name=body.name.strip(), garment_ids=body.garment_ids, occasion=body.occasion)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
