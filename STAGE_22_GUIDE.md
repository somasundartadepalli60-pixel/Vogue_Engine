# Vogue Engine Stage 22 — Local Tailoring Dashboard

Adds `/wardrobe/tailoring`, a browser interface for creating and updating tailoring jobs, tracking appointment dates, viewing upcoming due dates, and comparing recorded monthly expenses. The new read-only endpoint `/api/v1/wardrobe/alterations/insights` aggregates existing SQLite tailoring jobs. No external services, API keys, or `.env` files are needed.

Run from the project directory:

```sh
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/wardrobe/tailoring . Create garments in the existing wardrobe first, then use their IDs when creating tailoring jobs. Reminders are shown when you open the page; they are not background notifications. Monthly expense totals are grouped by job creation month, not payment month. For safety the server binds to localhost; do not expose it publicly without authentication.
