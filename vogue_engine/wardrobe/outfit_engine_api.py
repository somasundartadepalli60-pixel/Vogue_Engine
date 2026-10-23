"""Stage 40 offline outfit scoring endpoints."""
from fastapi import APIRouter, HTTPException, Query
from .api import store
from .outfit_engine import color_compatibility, recommend_combinations

router = APIRouter(prefix='/api/v1/wardrobe/outfit-engine', tags=['Offline Outfit Engine'])

@router.get('/recommendations')
def recommendations(occasion: str = Query('casual', max_length=40),
                    season: str = Query('all', max_length=40),
                    limit: int = Query(10, ge=1, le=100),
                    exclude_ids: list[int] | None = Query(None)):
    if exclude_ids and len(exclude_ids) > 500:
        raise HTTPException(422, 'Too many excluded garment IDs')
    return {'occasion': occasion, 'season': season,
            'recommendations': recommend_combinations(store().list(), occasion, season, limit, exclude_ids)}

@router.get('/colors')
def compare_colors(first: str = Query(min_length=1, max_length=40),
                   second: str = Query(min_length=1, max_length=40)):
    score, explanation = color_compatibility(first, second)
    return {'first': first, 'second': second, 'score': score, 'explanation': explanation}
