"""Offline metadata suggestions API. Does not silently change wardrobe records."""
from fastapi import APIRouter, HTTPException
from .photos_api import library
from .image_metadata import suggest_photo

router = APIRouter(prefix="/api/v1/wardrobe/metadata", tags=["Wardrobe Metadata Suggestions"])

@router.get("/photos/{photo_id}")
def suggest_metadata(photo_id: int):
    photos = library()
    record = photos.get(photo_id)
    if record is None:
        raise HTTPException(404, "Photo not found")
    path = photos.path_for(photo_id)
    if not path.is_file():
        raise HTTPException(404, "Photo file missing")
    try:
        return {"photo_id": photo_id, "garment_id": record["garment_id"],
                **suggest_photo(path, record.get("caption", ""))}
    except (OSError, ValueError) as exc:
        raise HTTPException(422, "Photo could not be analyzed") from exc
