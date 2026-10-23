# Stage 31 — Offline wardrobe activity history

Adds an append-only SQLite event journal for garment create/update/delete and outfit create/delete operations. Triggers capture changes from existing code paths, including imports. Historical changes made before Stage 31 are not reconstructed.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `/docs` and look for **Wardrobe Activity**. Endpoints:

- `GET /api/v1/wardrobe/activity` — filter by entity type, ID, action, dates, pagination.
- `GET /api/v1/wardrobe/activity/summary` — totals by action and month.
- `GET /api/v1/wardrobe/activity/{activity_id}` — individual event.

The journal is local and does not use keys, `.env` files or paid APIs. It records metadata and may contain garment names; treat the database as private. Event history is append-only through the API, but users with filesystem access can modify the SQLite file. Existing API security limitations remain; bind the server to localhost.
