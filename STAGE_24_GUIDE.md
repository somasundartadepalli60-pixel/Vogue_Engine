# Vogue Engine — Stage 24

Adds an offline lending dashboard at `http://127.0.0.1:8000/wardrobe/lending` and lending analytics at `/api/v1/wardrobe/lending/insights?days=30`.

Features: local loan creation, return actions, due-date calendar, overdue reminders on page load, monthly activity, and contact counts. No API keys, `.env` files, third-party services or CDN resources are required.

Run: `pip install -e ".[test]"`, then `python -m pytest -q`, then `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`.

Security: intended for trusted local use; do not expose the dashboard or contact records to the public internet without authentication and access control.
