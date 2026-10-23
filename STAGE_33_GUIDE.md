# Stage 33 — Offline Wardrobe Reminders

This stage adds local SQLite reminder storage, configurable reminder preferences, on-demand notifications and reminder history. No API keys, `.env`, paid services, push service, external assets or background scheduler are used.

## Run

```bash
pip install -e '.[test]'
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and find **Wardrobe Reminders**.

Create a reminder using `POST /api/v1/wardrobe/reminders` with JSON such as:

```json
{"title":"Wash winter jacket","kind":"laundry","due_at":"2026-11-01T09:00:00+05:30","garment_id":1,"notes":"Gentle cycle"}
```

Kinds: `laundry`, `repair`, `seasonal_review`, `outfit_plan`, `custom`.

`GET /api/v1/wardrobe/reminders/notifications` returns pending reminders due within the configured lookahead window, including overdue reminders. Notifications are returned when requested; this stage does **not** send operating-system alerts, emails or push notifications. `PATCH /api/v1/wardrobe/reminders/{id}/status` supports `pending`, `completed`, `dismissed`. `GET` and `PUT /preferences` control local notifications and lookahead hours (1–720).

**Security:** These local endpoints are not authenticated. Bind the server to `127.0.0.1`, not a public interface.
