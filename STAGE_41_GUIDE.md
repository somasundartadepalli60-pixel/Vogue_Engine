# Stage 41 — Offline Outfit Studio

Start: `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`

Visit `http://127.0.0.1:8000/wardrobe/outfit-engine`.

The dashboard displays ranked outfits, component garments, score breakdowns, explanation text, and color comparison. Save a recommended outfit with an editable name. The server checks all three garment IDs still exist and represent a valid top/bottom/shoe combination before writing to SQLite.

No API keys, `.env` files, remote services, or paid APIs. Intended for trusted local use only. Scoring is heuristic; it does not guarantee personal style or color accuracy.
