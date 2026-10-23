# Vogue Engine Stage 26 — Inventory audit dashboard

Start the local server using `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000` and visit http://127.0.0.1:8000/wardrobe/audits .

Create an inventory snapshot, mark garments present, filter unconfirmed garments, and compare snapshots. Unconfirmed does not necessarily mean physically missing. The integrity check is read-only. The comparison API is `GET /api/v1/wardrobe/audits/compare/{earlier_id}/{later_id}`. All features run locally without API keys or `.env` files. Do not expose the local dashboard to untrusted networks without authentication.
