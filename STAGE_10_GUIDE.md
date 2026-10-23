# Vogue Engine Stage 10 — Garment Lifecycle & Sustainability

This stage adds a local SQLite ledger for donations, repairs, resales, recycling, and discards. Original wardrobe data and earlier stages are retained.

## Run

```bash
pip install -e '.[test]'
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and use **Wardrobe Sustainability**.

## Endpoints

- `POST /api/v1/wardrobe/sustainability/events` — record a lifecycle event
- `GET /api/v1/wardrobe/sustainability/events` — filter event history
- `DELETE /api/v1/wardrobe/sustainability/events/{event_id}` — undo an event
- `GET /api/v1/wardrobe/sustainability/report?year=2026` — event totals, monthly counts, and reuse ratio

Example event body:

```json
{"garment_id":1,"action":"donated","event_date":"2026-10-23","recipient":"Local charity","notes":"Good condition"}
```

All data remains local. No API keys, `.env` files, paid services, or network requests are required by these features. Reports deliberately avoid invented carbon and water savings. Lifecycle events are not physical garment disposal commands; deleting a garment removes its related event history through database cascading, so export any required records first.

## Tests

```bash
python -m pytest -q
```
