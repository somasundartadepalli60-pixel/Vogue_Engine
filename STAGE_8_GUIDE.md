# Vogue Engine — Stage 8: Offline garment care

This stage adds garment condition profiles, configurable laundry intervals, dated care events, overdue reminders and care analytics. It preserves all earlier wardrobe data and routes. No API keys, `.env` files, cloud services or network calls are required by these features.

## Start

```bash
pip install -e ".[test]"
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/docs and select **Wardrobe Care**.

1. Create a garment with the Wardrobe API.
2. PUT `/api/v1/wardrobe/care/garments/{garment_id}` with `{"condition":"good","wash_interval_days":7,"last_washed":"2026-10-01"}`.
3. POST `/api/v1/wardrobe/care/garments/{garment_id}/events` with `{"event_type":"wash","event_date":"2026-10-10"}`.
4. GET `/api/v1/wardrobe/care/reminders?as_of=2026-10-20` to see due garments.
5. GET `/api/v1/wardrobe/care/overview` for aggregate counts.

Care reminders are computed when queried; this stage does not send push notifications. This is a local development service and must not be exposed publicly without an authentication/security review.
