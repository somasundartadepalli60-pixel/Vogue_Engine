# Stage 37 — Offline travel wardrobe dashboard

Run `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000` and open http://127.0.0.1:8000/wardrobe/travel .

Create trips, add recommended garments, mark items packed, export CSV packing checklists, and schedule existing outfits. New API routes: GET `/api/v1/wardrobe/travel/trips/{trip_id}/summary` and GET `/api/v1/wardrobe/travel/trips/{trip_id}/checklist.csv`. Data is stored in the existing SQLite wardrobe database. No API keys, `.env` files or paid APIs. Keep server bound to localhost.
