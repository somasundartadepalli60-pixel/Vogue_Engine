"""Local portable export and validated import endpoints."""
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from .api import store
from . import portability

router = APIRouter(prefix='/api/v1/wardrobe/portable', tags=['Wardrobe Portability'])

@router.get('/export.json')
def export_json():
    return Response(portability.json_bytes(store().path), media_type='application/json',
                    headers={'Content-Disposition': 'attachment; filename="wardrobe.json"'})

@router.get('/export.csv')
def export_csv(table: str = 'garments'):
    try:
        content = portability.csv_bytes(store().path, table)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    return Response(content, media_type='text/csv; charset=utf-8',
                    headers={'Content-Disposition': f'attachment; filename="{table}.csv"'})

@router.get('/archive.zip')
def export_archive():
    return Response(portability.archive_bytes(store().path), media_type='application/zip',
                    headers={'Content-Disposition': 'attachment; filename="wardrobe-archive.zip"'})

async def read_limited(request: Request) -> bytes:
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > portability.MAX_IMPORT_BYTES:
            raise HTTPException(413, 'Import exceeds 5 MiB limit')
    return bytes(body)

@router.post('/import/preview')
async def import_preview(request: Request):
    try:
        return portability.preview_import(await read_limited(request))
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc

@router.post('/import/commit')
async def import_commit(request: Request, confirm: bool = False):
    try:
        return portability.import_garments(store().path, await read_limited(request), confirm=confirm)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
