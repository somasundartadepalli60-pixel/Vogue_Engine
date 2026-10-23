# Stage 7 — Local Wardrobe Finance

Tracks purchase prices, vendors, purchase dates, monthly budgets, and cost per wear. Uses the existing SQLite wardrobe database; no API keys, .env files, cloud services, or network connections are needed.

## Start

```bash
pip install -e ".[test]"
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and find **Wardrobe Finance**.

Create a garment first via Wardrobe API, then PUT `/api/v1/wardrobe/finance/purchases/{garment_id}` with e.g. `{"amount":"799.00","purchased_on":"2026-10-23","vendor":"Local shop"}`. PUT `/api/v1/wardrobe/finance/budgets/2026-10` with `{"amount":"3000.00"}`. GET `/api/v1/wardrobe/finance/overview` for analytics.

Money is stored as integer paise to avoid floating-point accumulation errors. Only INR is supported. Purchase records are removed when their garments are deleted. Zero wears yields null cost-per-wear. Local endpoints are intended for a single trusted user, not public hosting.
