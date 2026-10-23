# Stage 20 — Fit Studio

Offline browser dashboard for size profiles, garment measurement history, interactive SVG trends and numerical fit comparisons.

## Run

```bash
pip install -e '.[test]'
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/wardrobe/measurements .

Add garments using the existing wardrobe API/dashboard first, then enter the garment ID in Fit Studio. Save a size profile and at least one garment measurement to compare them. Trend charts show recorded values in chronological order. The dashboard uses local HTML/CSS/JavaScript, inline SVG, FastAPI and SQLite. No API keys, `.env` files or CDN resources are needed.

**Security:** Local development use only; do not expose the service to the public internet without access controls. Fit results are numerical estimates, not assurances of actual fit.
