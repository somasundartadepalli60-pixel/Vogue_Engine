"""Stage 42: local rating, favorites and personalized outfit ranking API."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .outfit_engine import recommend_combinations
from .outfit_feedback import FeedbackStore, apply_feedback

router = APIRouter(prefix='/api/v1/wardrobe/outfit-feedback', tags=['Offline Outfit Feedback'])

@lru_cache(maxsize=1)
def feedback_store():
    return FeedbackStore(store().path)

class FeedbackInput(BaseModel):
    garment_ids: list[int] = Field(min_length=3, max_length=3)
    rating: int = Field(ge=1, le=5)
    favorite: bool = False
    notes: str = Field(default='', max_length=500)

@router.put('')
def save_feedback(body: FeedbackInput):
    try:
        ids = body.garment_ids
        if len(set(ids)) != 3 or any(i <= 0 for i in ids):
            raise ValueError('Invalid garment IDs')
        available = {g['id'] for g in store().list()}
        if not set(ids).issubset(available):
            raise HTTPException(404, 'One or more garments do not exist')
        return feedback_store().save(ids, body.rating, body.favorite, body.notes)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc

@router.get('')
def list_feedback():
    return {'feedback': feedback_store().list()}

@router.delete('')
def delete_feedback(garment_ids: list[int] = Query(...)):
    try:
        if not feedback_store().delete(garment_ids):
            raise HTTPException(404, 'Feedback not found')
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    return {'deleted': True}

@router.get('/recommendations')
def personalized_recommendations(occasion: str = Query('casual', max_length=40),
                                 season: str = Query('all', max_length=40),
                                 limit: int = Query(10, ge=1, le=100)):
    # Rank a larger candidate pool before limiting; the base engine bounds work.
    candidates = recommend_combinations(store().list(), occasion, season, 100)
    ranked = apply_feedback(candidates, feedback_store().list())
    return {'occasion': occasion, 'season': season, 'recommendations': ranked[:limit]}

@router.get('/analytics')
def feedback_analytics():
    """Aggregated, offline outfit feedback statistics."""
    entries = feedback_store().list()
    counts = {str(stars): sum(row['rating'] == stars for row in entries) for stars in range(1, 6)}
    total = len(entries)
    return {'total': total, 'favorites': sum(bool(row['favorite']) for row in entries),
            'average_rating': round(sum(row['rating'] for row in entries) / total, 2) if total else None,
            'rating_counts': counts}
