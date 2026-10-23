# Stage 14 — Local Garment Photos

Adds an offline garment photo gallery with JPEG/PNG/WebP uploads, safe JPEG normalization, EXIF orientation correction, thumbnails, SHA-256 deduplication, captions, gallery, deletion, and tests.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/wardrobe/photos or /docs. Add a garment before uploading.

Photos are stored in `vogue_photos/` and metadata in `vogue_wardrobe.sqlite3`. Back up both together. No keys, environment files or cloud providers required.

**Security:** This feature is intended for local, trusted use. The image endpoints are not user-authenticated; do not expose the development server publicly.
