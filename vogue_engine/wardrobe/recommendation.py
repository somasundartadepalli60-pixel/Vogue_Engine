"""Stage 12: explainable, offline outfit ranking and feedback learning."""
from __future__ import annotations

import sqlite3
from collections import Counter
from datetime import datetime, timezone
from itertools import product

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from .api import store
from .planner import COMPLEMENTARY
from .personalization import read_preferences

router = APIRouter(prefix='/api/v1/wardrobe/recommendation', tags=['Outfit Recommendation V2'])
GROUPS = ({'top', 'shirt', 'tshirt', 'blouse'},
          {'bottom', 'pants', 'trousers', 'skirt', 'jeans'},
          {'shoes', 'footwear', 'sneakers', 'boots'})
VALID_FEEDBACK = {'liked', 'disliked', 'worn'}


class Feedback(BaseModel):
    garment_ids: list[int] = Field(min_length=3, max_length=3)
    reaction: str
    note: str = Field(default='', max_length=500)


def _connect():
    db = sqlite3.connect(store().path)
    db.row_factory = sqlite3.Row
    db.execute('''CREATE TABLE IF NOT EXISTS recommendation_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        garment_signature TEXT NOT NULL,
        reaction TEXT NOT NULL CHECK(reaction IN ('liked','disliked','worn')),
        note TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL)''')
    db.execute('CREATE INDEX IF NOT EXISTS idx_recommendation_signature ON recommendation_feedback(garment_signature)')
    return db


def signature(ids):
    if len(ids) != 3 or len(set(ids)) != 3 or any(not isinstance(i, int) or isinstance(i, bool) or i < 1 for i in ids):
        raise ValueError('Provide three distinct positive garment IDs')
    return ','.join(map(str, sorted(ids)))


def save_feedback(ids, reaction, note=''):
    key = signature(ids)
    if reaction not in VALID_FEEDBACK:
        raise ValueError('Reaction must be liked, disliked, or worn')
    existing = {g['id'] for g in store().list()}
    if not set(ids).issubset(existing):
        raise ValueError('One or more garments do not exist')
    with _connect() as db:
        cur = db.execute('INSERT INTO recommendation_feedback(garment_signature,reaction,note,created_at) VALUES (?,?,?,?)',
                         (key, reaction, note[:500], datetime.now(timezone.utc).isoformat()))
        db.commit()
        return {'id': cur.lastrowid, 'garment_ids': sorted(ids), 'reaction': reaction, 'note': note[:500]}


def feedback_counts():
    with _connect() as db:
        rows = db.execute('SELECT garment_signature,reaction,COUNT(*) AS count FROM recommendation_feedback GROUP BY garment_signature,reaction').fetchall()
    result = {}
    for row in rows:
        result.setdefault(row['garment_signature'], Counter())[row['reaction']] = row['count']
    return result


def rank_outfits(garments, preferences, feedback, occasion='casual', season='all', limit=10):
    """Bound candidate combinations to avoid excessive CPU and memory usage."""
    if not 1 <= limit <= 100:
        raise ValueError('limit must be between 1 and 100')
    if season not in {'all', 'spring', 'summer', 'autumn', 'winter'}:
        raise ValueError('Invalid season')
    avoided = set(preferences.get('avoided_colors', []))
    eligible = [g for g in garments if g.get('color', '').lower() not in avoided
                and g.get('season', 'all') in ('all', season)
                and g.get('occasion', 'casual') in (occasion, 'all', 'casual')]
    groups = []
    for categories in GROUPS:
        group = [g for g in eligible if g.get('category', '').lower() in categories]
        group.sort(key=lambda g: (int(g.get('wears', 0)), g['id']))
        groups.append(group[:30])
    preferred = set(preferences.get('preferred_colors', []))
    preferred_categories = set(preferences.get('preferred_categories', []))
    results = []
    for trio in product(*groups):
        ids = [g['id'] for g in trio]
        colors = [g['color'].lower() for g in trio]
        components = {'base': 40, 'color': 0, 'preferences': 0, 'rotation': 0, 'feedback': 0, 'occasion': 0}
        reasons = []
        for a, b in ((0, 1), (0, 2), (1, 2)):
            if colors[b] in COMPLEMENTARY.get(colors[a], set()) or colors[a] in COMPLEMENTARY.get(colors[b], set()):
                components['color'] += 10
        if components['color']:
            reasons.append('Complementary garment colors')
        components['preferences'] += sum(6 for g in trio if g['color'].lower() in preferred)
        components['preferences'] += sum(3 for g in trio if g['category'].lower() in preferred_categories)
        if preferences.get('prefer_favorites', True):
            components['preferences'] += sum(4 for g in trio if g.get('favorite'))
        if components['preferences']:
            reasons.append('Matches your saved style preferences')
        if preferences.get('prioritize_unworn', True):
            components['rotation'] = sum(5 if int(g.get('wears', 0)) == 0 else -min(5, int(g.get('wears', 0))) for g in trio)
            reasons.append('Considers garment wear history')
        components['occasion'] = sum(3 for g in trio if g.get('occasion') == occasion)
        reactions = feedback.get(signature(ids), {})
        components['feedback'] = min(15, reactions.get('liked', 0) * 5 + reactions.get('worn', 0) * 3) - min(30, reactions.get('disliked', 0) * 10)
        if components['feedback']:
            reasons.append('Adjusted using your previous feedback')
        raw = sum(components.values())
        results.append({'garment_ids': ids, 'garments': list(trio), 'score': max(0, min(100, raw)),
                        'score_breakdown': components, 'reasons': reasons or ['Suitable garment combination']})
    results.sort(key=lambda x: (-x['score'], x['garment_ids']))
    return results[:limit]


@router.get('/suggestions')
def suggestions(occasion: str = 'casual', season: str = 'all', limit: int = Query(10, ge=1, le=100)):
    try:
        return rank_outfits(store().list(), read_preferences(), feedback_counts(), occasion, season, limit)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc


@router.post('/feedback', status_code=201)
def create_feedback(body: Feedback):
    try:
        return save_feedback(body.garment_ids, body.reaction, body.note)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc


@router.get('/feedback')
def list_feedback(limit: int = Query(50, ge=1, le=500)):
    with _connect() as db:
        rows = db.execute('SELECT * FROM recommendation_feedback ORDER BY id DESC LIMIT ?', (limit,)).fetchall()
    return [{**dict(row), 'garment_ids': [int(v) for v in row['garment_signature'].split(',')]} for row in rows]


@router.delete('/feedback/{feedback_id}')
def delete_feedback(feedback_id: int):
    with _connect() as db:
        deleted = db.execute('DELETE FROM recommendation_feedback WHERE id=?', (feedback_id,)).rowcount
        db.commit()
    if not deleted:
        raise HTTPException(404, 'Feedback not found')
    return {'deleted': True}
