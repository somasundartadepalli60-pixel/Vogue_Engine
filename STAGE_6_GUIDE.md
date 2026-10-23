# Vogue Engine — Stage 6: Wardrobe Organization

Preserves the Stage 1–5 code and adds SQLite-backed named collections, garment tags, searchable and paginated inventory, and inventory breakdowns. No API keys, `.env` files, paid services, or network integrations were added.

## Run

```bash
pip install -e ".[test]"
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Visit http://127.0.0.1:8000/docs and look under **Wardrobe Organization**. The existing wardrobe interfaces remain available.

## New endpoints

- `POST/GET /api/v1/wardrobe/organize/collections` — create/list named collections
- `DELETE /api/v1/wardrobe/organize/collections/{id}` — delete a collection (not its garments)
- `PUT/GET /api/v1/wardrobe/organize/collections/{id}/items` — replace/list membership
- `PUT /api/v1/wardrobe/organize/garments/{id}/tags` — replace tags
- `GET /api/v1/wardrobe/organize/tags` — tag usage counts
- `GET /api/v1/wardrobe/organize/search` — search, filter, sort and paginate
- `GET /api/v1/wardrobe/organize/breakdown` — category/color/season/occasion summaries

These endpoints are intended for trusted local use, not public deployment.
