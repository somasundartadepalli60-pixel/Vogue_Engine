# Stage 19 — Measurements and Fit Comparison

This stage adds locally stored size profiles, garment measurement history, and numerical ease comparisons. It requires no API keys, `.env` files, or network services.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and find **Wardrobe Measurements**.

## Example

Create a garment with the existing wardrobe API, then PUT `/api/v1/wardrobe/measurements/profiles` with:

```json
{"name":"My measurements","size_label":"M","measurements":{"chest":95,"waist":80}}
```

POST `/api/v1/wardrobe/measurements/garments/{garment_id}` with:

```json
{"measured_on":"2026-10-23","size_label":"M","measurements":{"chest":101,"waist":85}}
```

GET `/api/v1/wardrobe/measurements/fit/{garment_id}/{profile_id}?ease_cm=2`. All measurements are centimeters. The comparison is heuristic and does not guarantee garment fit.
