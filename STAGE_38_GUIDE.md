# Vogue Engine Stage 38 — Offline travel planning enhancements

New capabilities: save a trip checklist as a named reusable template, list/delete templates, apply a template to another trip without duplicate garments, and request season/occasion-based packing suggestions without weather services.

Run `python -m pytest -q` and `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000`. Open `/docs` and find **Wardrobe Travel**.

Endpoints:
- `GET /api/v1/wardrobe/travel/templates`
- `POST /api/v1/wardrobe/travel/trips/{trip_id}/templates` body `{"name":"Weekend"}`
- `POST /api/v1/wardrobe/travel/trips/{trip_id}/templates/{template_id}/apply`
- `DELETE /api/v1/wardrobe/travel/templates/{template_id}`
- `GET /api/v1/wardrobe/travel/trips/{trip_id}/seasonal-plan`

No API keys, `.env` files, paid services or live weather lookups. Seasonal recommendations are heuristics, not weather forecasts. Run locally on 127.0.0.1 because APIs do not provide authentication.
