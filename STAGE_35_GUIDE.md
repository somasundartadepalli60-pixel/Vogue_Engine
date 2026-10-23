# Vogue Engine — Stage 35: Offline Maintenance Tracking

Stage 35 adds local maintenance plans, care-event history, upcoming and overdue tasks, and category-based suggestions. Existing garment care endpoints remain unchanged.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Browse `http://127.0.0.1:8000/docs` and expand **Wardrobe Maintenance**.

Set a task schedule with `PUT /api/v1/wardrobe/maintenance/garments/{garment_id}/plans`, record completed work with `POST /api/v1/wardrobe/maintenance/garments/{garment_id}/events`, and check `GET /api/v1/wardrobe/maintenance/schedule?days=14`. Use the recommendations endpoint for local category-based suggestions. Suggested intervals are illustrative, not manufacturer-approved; always check garment labels.

This stage uses SQLite only. No API keys, `.env` files, external assets, background schedulers, or paid services. Bind to 127.0.0.1 because endpoints have no standalone authentication.
