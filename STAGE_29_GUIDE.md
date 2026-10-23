# Stage 29: Portable Wardrobe Data

No API keys, environment files, or cloud services are required.

## Endpoints

- `GET /api/v1/wardrobe/portable/export.json`: export core wardrobe data as JSON.
- `GET /api/v1/wardrobe/portable/export.csv?table=garments`: CSV report (`garments`, `outfits`, `outfit_garments`).
- `GET /api/v1/wardrobe/portable/archive.zip`: ZIP containing JSON and CSV exports.
- `POST /api/v1/wardrobe/portable/import/preview`: raw JSON request body, validated preview.
- `POST /api/v1/wardrobe/portable/import/commit?confirm=true`: raw JSON request body, append validated garments.

The import deliberately does not overwrite existing garments or import outfit relationships. Export archives do not include photographs or every extension table. Back up the SQLite database and photo directory separately for full recovery. Keep the server bound to `127.0.0.1`; these routes are intended for trusted local use.
