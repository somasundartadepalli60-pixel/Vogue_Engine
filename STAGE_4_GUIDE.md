# Stage 4 — Wear history and wardrobe analytics

This stage preserves Stage 1–3 and adds local-only outfit wear logging, undo, month-by-month usage analytics, garment rotation and a dedicated insights dashboard.

## Run

```bash
pip install -e ".[test]"
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/wardrobe/insights

Endpoints: POST/GET `/api/v1/wardrobe/wear-log`, DELETE `/api/v1/wardrobe/wear-log/{entry_id}`, GET `/api/v1/wardrobe/analytics`.

No API keys, `.env` files or paid integrations. Wear records are stored in the existing local SQLite database. Do not expose this development server to untrusted networks: wardrobe endpoints do not enforce user-level authentication.
