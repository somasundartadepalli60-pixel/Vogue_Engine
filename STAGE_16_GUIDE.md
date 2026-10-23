# Stage 16 — Offline garment photo metadata suggestions

This stage preserves previous project code and adds an **explainable, non-ML** metadata helper.

## New endpoint

`GET /api/v1/wardrobe/metadata/photos/{photo_id}` returns dominant color palette, photo dimensions, orientation, and optional category/season suggestions derived from the existing photo caption.

No API keys, `.env` files, model downloads, or external network requests are needed.

**Important limitation:** This is not computer-vision garment recognition. It cannot identify a shirt from pixels alone. If no useful caption is available, category is `null`. Suggestions never overwrite stored wardrobe metadata.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Visit `http://127.0.0.1:8000/docs`.
