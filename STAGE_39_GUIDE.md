# Stage 39 — Interactive travel packing templates

The offline dashboard is at `http://127.0.0.1:8000/wardrobe/travel/templates`.

Features: save packing checklists as reusable templates, apply templates without duplicate garments, delete templates with confirmation, see local seasonal recommendations, add suggested garments, and compare two trips side by side (shared, first-only, second-only garments).

New read-only API: `GET /api/v1/wardrobe/travel/trips/{first_id}/compare/{second_id}`.

Run: `pip install -e ".[test]"` then `python -m pytest -q` and `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`.

No API keys, `.env`, paid services, or weather integration. Keep this unauthenticated local app bound to loopback.
