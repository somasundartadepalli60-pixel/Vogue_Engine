# Vogue Engine — Stage 30: Import/Export Dashboard

Open `http://127.0.0.1:8000/wardrobe/portability` after starting the existing FastAPI server.

## Features
- Download JSON, CSV (garments, outfits, outfit links), or ZIP archive.
- Select a JSON wardrobe export and validate it before importing.
- Review record count and a five-row sample.
- Explicitly confirm before appending garments to the local SQLite database.
- Display validation and import errors without reloading the page.

## Start
```bash
pip install -e '.[test]'
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

## Important
Imports append garments only. Outfit links, photos, and extension tables are not imported. Use the database backup facility for recovery. Keep the server bound to localhost because the import/export routes do not have independent authentication. No API keys or `.env` files are required.
