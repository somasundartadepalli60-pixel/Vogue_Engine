# Stage 32 — Wardrobe Activity Dashboard

Run the existing FastAPI application and visit `http://127.0.0.1:8000/wardrobe/activity`.

This dashboard adds a searchable, paginated timeline, before/after comparison for update events, and monthly/action activity bars. It reads the Stage 31 activity API and stores no extra data. All rendering uses DOM text nodes rather than HTML injection, and all requests are local. Existing records remain unchanged.

Install and run from the project directory:

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Keep this app on localhost; its activity endpoints are intended for trusted local access. No API keys or `.env` files are required.
