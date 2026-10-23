# Stage 28 — Local Backup Dashboard

Run `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000` and open `http://127.0.0.1:8000/wardrobe/backups`.

Create, list, verify, preview, restore and delete local SQLite backups. Restore requires typing `RESTORE` and triggers an automatic recovery backup. The dashboard uses the existing Stage 27 API; it does not need API keys, `.env` files or internet services.

**Security:** Keep the server bound to `127.0.0.1`. Existing backup API endpoints are not independently authenticated. Do not expose this service to untrusted networks. SQLite snapshots do not include separate garment photo files; back those up separately.
