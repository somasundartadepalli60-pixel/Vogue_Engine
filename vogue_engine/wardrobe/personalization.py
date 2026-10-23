"""Offline personal style preferences and explainable, seasonal outfit rankings."""
from __future__ import annotations
import json
import sqlite3
from pathlib import Path
from typing import Any
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .api import store
from .planner import suggest_outfits

router = APIRouter(prefix='/api/v1/wardrobe', tags=['Personal Styling'])
SEASONS = {'all', 'spring', 'summer', 'autumn', 'winter'}

class Preferences(BaseModel):
    preferred_colors: list[str] = Field(default_factory=list, max_length=30)
    avoided_colors: list[str] = Field(default_factory=list, max_length=30)
    preferred_categories: list[str] = Field(default_factory=list, max_length=30)
    season: str = 'all'
    prefer_favorites: bool = True
    prioritize_unworn: bool = True

    def normalized(self):
        data = self.model_dump()
        for field in ('preferred_colors', 'avoided_colors', 'preferred_categories'):
            data[field] = list(dict.fromkeys(v.strip().lower() for v in data[field] if v.strip()))
        data['season'] = data['season'].strip().lower()
        if data['season'] not in SEASONS:
            raise ValueError('Unknown season')
        if set(data['preferred_colors']) & set(data['avoided_colors']):
            raise ValueError('Preferred and avoided colors cannot overlap')
        return data


def _db():
    db = sqlite3.connect(store().path)
    db.execute('CREATE TABLE IF NOT EXISTS styling_preferences (id INTEGER PRIMARY KEY CHECK(id=1), data TEXT NOT NULL)')
    return db


def read_preferences() -> dict[str, Any]:
    with _db() as db:
        row = db.execute('SELECT data FROM styling_preferences WHERE id=1').fetchone()
    return json.loads(row[0]) if row else Preferences().normalized()


def save_preferences(body: Preferences) -> dict[str, Any]:
    data = body.normalized()
    with _db() as db:
        db.execute('INSERT INTO styling_preferences(id,data) VALUES (1,?) ON CONFLICT(id) DO UPDATE SET data=excluded.data', (json.dumps(data),))
    return data


def personalized_suggestions(garments: list[dict], preferences: dict, occasion='casual', season='all', limit=10):
    if not 1 <= limit <= 100:
        raise ValueError('limit must be between 1 and 100')
    effective_season = season if season != 'all' else preferences['season']
    if effective_season not in SEASONS:
        raise ValueError('Unknown season')
    avoided = set(preferences['avoided_colors'])
    eligible = [g for g in garments if g['color'].lower() not in avoided]
    # Rank a bounded number of candidates to prevent exponential expansion on large wardrobes.
    candidates = suggest_outfits(eligible, occasion, effective_season, min(100, max(limit * 5, 20)))
    preferred = set(preferences['preferred_colors'])
    categories = set(preferences['preferred_categories'])
    result = []
    for outfit in candidates:
        score = outfit['score']
        reasons = []
        color_matches = sum(g['color'].lower() in preferred for g in outfit['garments'])
        category_matches = sum(g['category'].lower() in categories for g in outfit['garments'])
        if color_matches:
            score += color_matches * 7
            reasons.append(f'{color_matches} preferred color match(es)')
        if category_matches:
            score += category_matches * 3
            reasons.append(f'{category_matches} preferred category match(es)')
        if preferences['prefer_favorites']:
            count = sum(bool(g.get('favorite')) for g in outfit['garments'])
            score += count * 4
            if count: reasons.append('Includes favorites')
        if preferences['prioritize_unworn']:
            count = sum(int(g.get('wears', 0)) == 0 for g in outfit['garments'])
            score += count * 5
            if count: reasons.append('Encourages unworn garments')
        result.append({**outfit, 'score': max(0, min(100, score)), 'reasons': reasons or ['Coordinated colors and outfit compatibility']})
    return sorted(result, key=lambda item: (-item['score'], item['garment_ids']))[:limit]


@router.get('/preferences')
def get_preferences():
    return read_preferences()


@router.put('/preferences')
def put_preferences(body: Preferences):
    try:
        return save_preferences(body)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc


@router.get('/personalized-suggestions')
def get_personalized_suggestions(occasion: str = 'casual', season: str = 'all', limit: int = Query(10, ge=1, le=100)):
    try:
        return personalized_suggestions(store().list(), read_preferences(), occasion, season, limit)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc


@router.get('/seasonal-summary')
def seasonal_summary():
    garments = store().list()
    return {
        'total': len(garments),
        'by_season': {s: sum(g['season'] in (s, 'all') for g in garments) for s in ('spring', 'summer', 'autumn', 'winter')},
        'all_season': sum(g['season'] == 'all' for g in garments),
        'unworn': sum(int(g.get('wears', 0)) == 0 for g in garments),
    }
