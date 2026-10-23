"""Offline wardrobe color analysis API."""
from fastapi import APIRouter, HTTPException, Query
from .photos_api import library
from .color_analysis import palette_for_image, search_photos

router = APIRouter(prefix="/api/v1/wardrobe/colors", tags=["Wardrobe Colors"])

@router.get("/photos/{photo_id}")
def photo_palette(photo_id: int, count: int = Query(5, ge=1, le=12)):
    try:
        path = library().path_for(photo_id)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    if not path.is_file():
        raise HTTPException(404, "Photo file missing")
    return {"photo_id": photo_id, "palette": palette_for_image(path, count)}

@router.get("/search")
def color_search(color: str, limit: int = Query(20, ge=1, le=100), garment_id: int | None = None):
    try:
        return {"query": color, "matches": search_photos(library(), color, limit, garment_id)}
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
