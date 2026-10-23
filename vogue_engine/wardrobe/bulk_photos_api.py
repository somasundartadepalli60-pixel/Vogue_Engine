"""Bulk operations for the local photo library."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from .photos_api import library
from .bulk_photos import BulkPhotoService

router = APIRouter(prefix='/api/v1/wardrobe/photos/bulk', tags=['Wardrobe Photo Organization'])

class PhotoSelection(BaseModel):
    photo_ids: list[int] = Field(min_length=1, max_length=100)

class CaptionSelection(PhotoSelection):
    caption: str = Field(max_length=240)

@router.patch('/captions')
def update_captions(payload: CaptionSelection):
    try:
        return BulkPhotoService(library()).update_captions(payload.photo_ids, payload.caption)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc

@router.post('/delete')
def delete_photos(payload: PhotoSelection):
    try:
        return BulkPhotoService(library()).delete(payload.photo_ids)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
