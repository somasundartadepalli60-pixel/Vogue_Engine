# Vogue Engine Stage 3 — Offline privacy and report persistence

Stage 1 and 2 remain available. Stage 3 adds SQLite-backed report persistence,
passphrase-protected report listing/deletion, and removes the hardcoded HMAC signing secret.
No API keys, `.env` files, paid APIs or cloud services are required.

## Start

```bash
pip install -e ".[test]"
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/docs. Set a local passphrase (12+ characters) once
with `POST /api/v1/privacy/setup`. For protected routes supply the
`X-Local-Passphrase` HTTP header. Report data is stored locally in
`~/.vogue_engine/reports.sqlite3`; salted scrypt verifier in
`~/.vogue_engine/privacy.sqlite3`.

**Security limitations:** Existing user report URLs remain accessible to anyone
who knows the report UUID; existing admin token-in-URL behavior remains for
compatibility. Admin tokens now use a fresh random key on each process start,
so previously issued admin links stop working after restart. Privacy endpoints
are for local use; do not expose this development server to the public internet.
Deleted rows may remain in SQLite journal/backups; secure deletion of backups
and underlying storage is outside this application's scope.
