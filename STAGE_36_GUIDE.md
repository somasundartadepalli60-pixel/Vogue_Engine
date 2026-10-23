# Stage 36 — Garment care dashboard

The dashboard at `http://127.0.0.1:8000/wardrobe/maintenance` is a local, offline UI for the Stage 35 maintenance APIs.

Run from this project folder:

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Features: garment selection, create/update care plans, record cleaning and repair events, view event history, task-count bars, upcoming/overdue schedules, monthly calendar, and local rule-based suggestions.

The calendar displays due tasks in the selected forward schedule window, not an infinite recurrence projection. Events are recorded when explicitly submitted; no background scheduling or operating-system alerts are provided. Always follow the actual garment care label. Keep this unauthenticated local dashboard on `127.0.0.1`.

No API keys, `.env` files, or paid services are needed.
