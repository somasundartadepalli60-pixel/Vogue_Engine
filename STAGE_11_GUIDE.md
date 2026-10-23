# Vogue Engine Stage 11 — Offline Outfit Calendar

Adds a persistent calendar for saved outfits, garment availability blocks (laundry, repairs, loans), conflict detection, and planned-wear forecasting. Existing Stage 1–10 code remains intact.

## Start

```bash
pip install -e '.[test]'
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/docs and locate **Wardrobe Calendar**.

Create garments and outfits using the existing Wardrobe endpoints, then schedule them with `POST /api/v1/wardrobe/calendar/schedule`. `GET /agenda` lists scheduled outfits; `POST /blocks` marks garments unavailable; `GET /forecast` counts upcoming planned garment wears. Conflicts return HTTP 422 unless `force` is true.

All storage is local SQLite. No API keys, `.env` files, cloud services, or paid APIs are needed. Do not expose the development server publicly without additional authentication and security review.
