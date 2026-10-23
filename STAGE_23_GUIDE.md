# Stage 23 — Garment Lending and Borrowing

Offline garment lending, borrowing, return history, due-date extensions and overdue reminders.

## Run

```bash
pip install -e '.[test]'
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs`, then **Wardrobe Lending**.

Create a garment first, then create a loan using its garment ID. Active loans are unique per garment. Returns and due-date changes are logged as history events. Overdue status is computed on demand (no external notifications).

No API keys, `.env` files, cloud services, or paid APIs are required. This local development server is not intended for public exposure.
