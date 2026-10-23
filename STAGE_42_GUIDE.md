# Stage 42 — Offline outfit feedback and personalized ranking

This stage adds SQLite-backed outfit ratings (1–5), favorite combinations, short notes, and explainable feedback-based ranking. All earlier stages remain intact.

Run `pip install -e ".[test]"`, then `python -m pytest -q` and `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`.

Open `/docs` and find **Offline Outfit Feedback**. Use `PUT /api/v1/wardrobe/outfit-feedback` with three garment IDs, rating, favorite and notes. `GET /api/v1/wardrobe/outfit-feedback` lists saved feedback; `DELETE` removes one combination; `/recommendations` applies a small rating/favorite bonus to locally generated outfit recommendations.

Scoring is heuristic, not trained AI. Ratings attach to sets of garment IDs and are not automatically deleted when garments are removed. The app is designed for trusted local use, not a public unauthenticated server. No API keys, `.env` files, paid APIs or network inference are needed.
