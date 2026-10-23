# Stage 13 — Offline Recommendation Studio

This stage adds a local browser interface for the Stage 12 recommendation engine.

## Run

```bash
pip install -e ".[test]"
python -m pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/wardrobe/recommendations.

## Features

- Choose season, occasion and recommendation count.
- View outfit garments, ranking scores and explanations.
- Compare up to three outfits by score breakdown.
- Record liked, disliked and worn feedback locally.
- Browse and delete saved feedback history.

Uses the existing SQLite database and Stage 12 recommendation API. No API keys, .env files or cloud services are needed.
