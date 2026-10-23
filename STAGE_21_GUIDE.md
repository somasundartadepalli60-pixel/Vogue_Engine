# Vogue Engine — Stage 21: Tailoring and Alterations

New offline features: tailoring jobs, appointments, estimated/actual repair costs, workflow status transitions, audit history, due-date filtering, and cost summaries.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Browse `http://127.0.0.1:8000/docs` and open **Wardrobe Alterations**.

Create a garment using `/api/v1/wardrobe/garments`, then create a tailoring job using `/api/v1/wardrobe/alterations/jobs`.

Sample payload:
```json
{"garment_id":1,"description":"Shorten sleeves","tailor":"Neighborhood tailor","due_date":"2026-11-15","appointment_at":"2026-11-01T10:30:00","estimated_cost":500}
```

Move a job through `planned → in_progress → ready → completed`, or cancel an unfinished job. Use `PATCH /jobs/{job_id}` to enter actual cost and reschedule appointments. View `/summary` for local statistics.

All information stays in local SQLite storage. No API keys, `.env` files, cloud integrations, or paid APIs are required. Run on localhost; existing project endpoints may need additional authentication before public deployment.
