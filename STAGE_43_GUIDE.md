# Vogue Engine Stage 43 — Outfit Feedback Studio

Run `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`, then visit `http://127.0.0.1:8000/wardrobe/outfit-feedback`.

Features: personalized recommendation cards, 1–5 star ratings, favorite toggles, notes, saved feedback gallery, delete confirmation, rating distribution, and aggregate statistics.

API: `GET /api/v1/wardrobe/outfit-feedback/analytics` returns total ratings, favorite count, average rating and 1–5 star distribution. All processing is local and rule-based. No API keys, `.env` files or paid APIs. Bind to localhost because endpoints have no authentication.
