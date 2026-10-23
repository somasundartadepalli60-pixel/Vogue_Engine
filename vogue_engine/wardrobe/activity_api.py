"""Read-only activity reporting endpoints for the local wardrobe."""
from functools import lru_cache
from fastapi import APIRouter, HTTPException, Query
from .api import store
from .activity import ActivityJournal

router = APIRouter(prefix='/api/v1/wardrobe/activity',tags=['Wardrobe Activity'])

@lru_cache(maxsize=1)
def journal():
    return ActivityJournal(store().path)

@router.get('')
def activity_list(entity_type: str | None = None, entity_id: int | None = None, action: str | None = None, since: str | None = None, until: str | None = None, limit: int = Query(100,ge=1,le=500), offset: int = Query(0,ge=0)):
    return journal().list(entity_type=entity_type,entity_id=entity_id,action=action,since=since,until=until,limit=limit,offset=offset)

@router.get('/summary')
def activity_summary():
    return journal().summary()

@router.get('/{activity_id}')
def activity_detail(activity_id: int):
    try:
        return journal().get(activity_id)
    except LookupError as exc:
        raise HTTPException(404,str(exc)) from exc
