# Stage 18 — Offline Photo Organizer

Run `pip install -e ".[test]"` and `python -m pytest -q`, then start `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`.

Open http://127.0.0.1:8000/wardrobe/organize to browse, filter, select, compare and bulk-edit photos. Bulk endpoints: `PATCH /api/v1/wardrobe/photos/bulk/captions` and `POST /api/v1/wardrobe/photos/bulk/delete`.

All processing stays local. No API keys, environment files or cloud accounts are required. Keep the server bound to loopback; the local photo interface is not intended for public exposure.
