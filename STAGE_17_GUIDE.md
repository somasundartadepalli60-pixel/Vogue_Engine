# Vogue Engine — Stage 17

Adds offline image similarity and potential duplicate photo discovery. Existing photos, garments, and features are preserved.

## Run

```bash
pip install -e '.[test]'
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Visit http://127.0.0.1:8000/docs.

## Endpoints

- `GET /api/v1/wardrobe/visual/similar/{photo_id}?limit=10&minimum=0.7`
- `GET /api/v1/wardrobe/visual/duplicates?minimum=0.95&limit=100`

The comparison uses a 64-bit perceptual difference hash (60%) and a 48-bin RGB color histogram (40%). Results are heuristic visual similarities, not proof that garments are identical. Duplicate discovery is quadratic in the number of photos, intended for modest local collections. Images remain on disk; no external calls, keys, or .env files are required.
