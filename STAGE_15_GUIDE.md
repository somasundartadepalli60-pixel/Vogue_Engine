# Stage 15 — Local Image Color Analysis

This stage adds deterministic dominant-color palettes and visual color matching for garment photos. It uses Pillow, the existing photo storage, and no network requests, API keys, or .env files.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs`. Use `GET /api/v1/wardrobe/colors/photos/{photo_id}?count=5` for a photo palette and `GET /api/v1/wardrobe/colors/search?color=%23ff0000` to search similar colors. Upload garment images first through the Stage 14 photo interface.

Matching uses weighted RGB distance and quantized dominant colors. It is not semantic garment recognition and may be affected by backgrounds and lighting. All data stays local. Do not expose this development server publicly.
