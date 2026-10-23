# Stage 5: Personal Styling Studio

Adds persisted local preferences, season-aware recommendations, avoid-color filtering, unworn-garment priority, and seasonal coverage analytics. No API keys, `.env` files, or external services are used.

## Run

```bash
pip install -e '.[test]'
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/wardrobe/style`.

## API

- `GET /api/v1/wardrobe/preferences`
- `PUT /api/v1/wardrobe/preferences`
- `GET /api/v1/wardrobe/personalized-suggestions`
- `GET /api/v1/wardrobe/seasonal-summary`

Preference data is stored in the existing local SQLite wardrobe database. Do not expose this unauthenticated local dashboard to the public internet.
