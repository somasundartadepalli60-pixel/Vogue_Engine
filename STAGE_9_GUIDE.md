# Vogue Engine — Stage 9: Offline Travel Planner

Stage 9 adds persistent trip planning, wardrobe-based packing recommendations, packing checklists, and per-day outfit schedules. Existing stages are retained.

## Install and run

```bash
pip install -e '.[test]'
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and look for **Wardrobe Travel**.

## Workflow

1. Add garments and saved outfits using existing wardrobe endpoints.
2. `POST /api/v1/wardrobe/travel/trips` with `name`, `destination`, `start_date`, `end_date`, `season`, and `occasion`.
3. `GET /api/v1/wardrobe/travel/trips/{trip_id}/recommendations` for offline ranking.
4. `POST /api/v1/wardrobe/travel/trips/{trip_id}/items/{garment_id}` to add items.
5. `PUT /api/v1/wardrobe/travel/trips/{trip_id}/items/{garment_id}` with `{"packed": true}` to mark packed.
6. `PUT /api/v1/wardrobe/travel/trips/{trip_id}/outfits` with `{"day":"2026-11-02","outfit_id":1}` to schedule a saved outfit.

All records use the existing local SQLite database. No API keys, `.env` files, or external services are required. Travel recommendations are deterministic heuristics, not weather forecasts.
