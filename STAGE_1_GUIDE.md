# Stage 1 — Offline wardrobe management

This update preserves the original engine and adds SQLite inventory, CRUD endpoints, persistent outfit collections, outfit suggestions, and wardrobe statistics. No API keys or `.env` files are required. The SQLite database is created automatically on first use.

## Run

```bash
python -m pip install -e ".[test]"
python -m uvicorn vogue_engine.dashboards.router:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive local API documentation.

## Example

```bash
curl -X POST http://127.0.0.1:8000/api/v1/wardrobe/garments -H "Content-Type: application/json" -d '{"name":"White shirt","category":"top","color":"white"}'
```

Then add `bottom` and `shoes` items and call `/api/v1/wardrobe/suggestions`. Run tests with `python -m pytest`.

## Important security note

The existing administrative token system has a hardcoded fallback signing secret and issues admin tokens through the analysis endpoint by default. This pre-existing design is **not safe for public deployment**. Keep the server bound to localhost until an authentication redesign is completed. No new API keys or secrets were introduced in Stage 1.

## Future stages

Stage 2: wardrobe import/export, outfit calendar, advanced filters and accessible local UI. Stage 3: privacy controls, hardened authorization, report persistence. Stage 4: expanded styling rules, performance and integration tests. A 500,000-line target should be achieved only if justified by useful modules, not filler.
