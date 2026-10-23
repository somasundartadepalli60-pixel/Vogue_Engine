# Stage 27 — Offline Wardrobe Backup and Recovery

Stage 27 adds SQLite-consistent snapshots, SHA-256 integrity verification, backup inventories, restore previews, guarded restore and automatic pre-restore recovery backups.

Run `pip install -e ".[test]"`, then `python -m pytest -q`, then `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`.

Open `/docs` and find **Wardrobe Backups**. Create a backup with `POST /api/v1/wardrobe/backups`, preview using `GET /{id}/preview`, and restore with `POST /{id}/restore` and JSON `{ "confirm": true }`. Restore replaces the active wardrobe database; close other database clients before restoring. A recovery backup is made first. Backups are kept in the `wardrobe_backups` directory beside the database and are **not encrypted**. Protect the computer and backup directory, and do not expose the local API to untrusted networks. All operations are local; no API keys or `.env` files are used.
