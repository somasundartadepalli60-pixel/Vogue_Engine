# Vogue Engine — Stage 40: Offline Outfit Combination Engine

Stage 40 adds a deterministic and explainable outfit scoring engine using existing wardrobe garments.

## Features

- Top, bottom and footwear combinations, with category aliases.
- Symmetric color compatibility and neutral-color scoring.
- Occasion matching, favorites and wear rotation in the final score.
- Season filters and garment exclusions.
- Stable ranking with an upper bound on candidate combinations.
- JSON explanations for each suggestion.

## API

- `GET /api/v1/wardrobe/outfit-engine/recommendations?occasion=casual&season=all&limit=10`
- `GET /api/v1/wardrobe/outfit-engine/colors?first=navy&second=white`

Run locally with `python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000` and browse `/docs`.

No API keys, `.env` files, external APIs, or network calls are required. Scores are simple heuristics, not personal styling guarantees. Keep the API local unless access control is added.
