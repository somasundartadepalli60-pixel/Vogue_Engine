# Stage 2 — Local wardrobe dashboard and planning

Preserves Stage 1 and original Vogue Engine code. Adds an accessible local HTML dashboard, paginated garment search, sorting, JSON/CSV exports, validated transactional JSON import, and persistent outfit calendar.

## Start

```bash
python -m pip install -e '.[test]'
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000 --reload
```

Open **http://127.0.0.1:8000/wardrobe** for the dashboard or **http://127.0.0.1:8000/docs** for API docs. Create a saved outfit through `/api/v1/wardrobe/outfits` before planning it on the calendar.

## New endpoints

- `GET /wardrobe`: browser UI
- `GET /api/v1/wardrobe/search`: `q`, `category`, `sort`, `page`, `page_size`
- `GET /api/v1/wardrobe/export/json` and `/export/csv`: backup files
- `POST /api/v1/wardrobe/import/json`: import `{"format":"vogue-wardrobe-v1","garments":[...]}`; appends up to 1000 garments per request
- `PUT /api/v1/wardrobe/calendar`: schedule an existing saved outfit by ISO date
- `GET /api/v1/wardrobe/calendar`: optional `start`, `end` filters
- `DELETE /api/v1/wardrobe/calendar/{day}`: remove schedule entry

## Notes

The app uses SQLite on disk. No API keys, `.env` files, or external calls are required for Stage 2 features. The original admin token design remains unsuitable for exposing the server publicly; keep it bound to `127.0.0.1`. Backups include garment records, not saved outfit relationships or calendar entries. Import appends and does not deduplicate. Run `python -m pytest` for tests.
