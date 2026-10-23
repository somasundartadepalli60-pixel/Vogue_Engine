"""Local photo endpoints: no third-party services or API keys."""
from functools import lru_cache
from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from .photos import PhotoLibrary, MAX_BYTES

router = APIRouter(prefix='/api/v1/wardrobe/photos', tags=['Wardrobe Photos'])

@lru_cache(maxsize=1)
def library():
    return PhotoLibrary()

class CaptionUpdate(BaseModel):
    caption: str = Field(max_length=240)

@router.post('/garments/{garment_id}', status_code=201)
async def upload_photo(garment_id: int, file: UploadFile = File(...), caption: str = Form('')):
    content = await file.read(MAX_BYTES + 1)
    try:
        return library().add(garment_id, content, caption)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc

@router.get('')
def list_photos(garment_id: int | None = None):
    return library().list(garment_id)

@router.get('/{photo_id}/image')
def view_photo(photo_id: int):
    try:
        path = library().path_for(photo_id)
    except LookupError as exc:
        raise HTTPException(404, str(exc)) from exc
    if not path.is_file():
        raise HTTPException(404, 'Image file missing')
    return FileResponse(path, media_type='image/jpeg', headers={'Cache-Control':'private, max-age=3600','X-Content-Type-Options':'nosniff'})

@router.patch('/{photo_id}')
def edit_photo(photo_id: int, body: CaptionUpdate):
    photo = library().update_caption(photo_id, body.caption)
    if photo is None:
        raise HTTPException(404, 'Photo not found')
    return photo

@router.delete('/{photo_id}')
def delete_photo(photo_id: int):
    if not library().remove(photo_id):
        raise HTTPException(404, 'Photo not found')
    return {'deleted': True}
