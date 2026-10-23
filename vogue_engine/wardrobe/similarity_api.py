"""Offline garment image similarity and duplicate candidate endpoints."""
from fastapi import APIRouter, HTTPException, Query
from .photos_api import library
from .similarity import SimilaritySearch

router = APIRouter(prefix='/api/v1/wardrobe/visual', tags=['Wardrobe Visual Search'])

@router.get('/similar/{photo_id}')
def similar_photos(photo_id: int, limit: int = Query(10, ge=1, le=100),
                   minimum: float = Query(0.0, ge=0, le=1),
                   include_same_garment: bool = True):
    try:
        return SimilaritySearch(library()).search(photo_id, limit, minimum, include_same_garment)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    except (ValueError, OSError) as exc:
        raise HTTPException(422, str(exc)) from exc

@router.get('/duplicates')
def duplicate_candidates(minimum: float = Query(0.95, ge=0, le=1),
                         limit: int = Query(100, ge=1, le=100)):
    return SimilaritySearch(library()).duplicate_candidates(minimum, limit)
