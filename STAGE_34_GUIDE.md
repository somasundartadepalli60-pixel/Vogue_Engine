# Vogue Engine — Stage 34

Offline reminder dashboard with notification center, browser-based reminder creation, a local-time monthly calendar, status management, pagination and filters, and reminder preferences.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Visit http://127.0.0.1:8000/wardrobe/reminders.

## Notes

All reminder data remains in the local SQLite database. The browser polls the notifications endpoint once a minute while the page is open. No push service, background scheduler, external API, API key, or `.env` is used. This interface is intended for trusted local access; reminder endpoints have no independent authentication. Calendar display is based on the browser's local time zone. For large histories, the calendar fetches paginated records; it is not optimized for very large databases.
