# Stage 25 — Offline wardrobe inventory audits

This stage adds immutable garment snapshots for physical inventory checks, confirmation/unconfirmation of items, missing-garment reporting, and read-only SQLite consistency diagnostics.

Run `pip install -e ".[test]"`, then `python -m pytest -q` and `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`.

Open `/docs` and find **Wardrobe Audits**. Start an audit using `POST /api/v1/wardrobe/audits` with `{"label":"Closet check"}`. Mark a garment present with `PUT /api/v1/wardrobe/audits/{audit_id}/items/{garment_id}` and `{"present":true}`. Unconfirmed items are *potentially* missing, not proof of loss. Review `GET /api/v1/wardrobe/audits/integrity` for database consistency issues. No records are automatically deleted or repaired.

All data stays in local SQLite. No API keys, `.env` files, or cloud services are needed. Bind only to loopback; existing dashboard authentication is not hardened for public hosting.
