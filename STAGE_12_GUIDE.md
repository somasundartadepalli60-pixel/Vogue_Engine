# Vogue Engine Stage 12 — Offline recommendation scoring

This stage preserves all previous modules and adds explainable outfit ranking with saved feedback.

## New endpoints

- `GET /api/v1/wardrobe/recommendation/suggestions?occasion=casual&season=all&limit=10`
- `POST /api/v1/wardrobe/recommendation/feedback` with JSON `{"garment_ids":[1,2,3],"reaction":"liked","note":"Great match"}`
- `GET /api/v1/wardrobe/recommendation/feedback`
- `DELETE /api/v1/wardrobe/recommendation/feedback/{feedback_id}`

The scoring combines color coordination, preferred colors/categories, favorites, wear rotation, occasion fit, and previous reactions. Each suggestion provides a component breakdown and explanations. Candidates are capped to 30 items per garment group (27,000 combinations maximum) for predictable offline performance.

Feedback is stored in the existing local SQLite database. There are no API keys, `.env` files, remote inference, or paid services.

## Run

```bash
pip install -e '.[test]'
pytest -q
python -m uvicorn vogue_engine.dashboards.router:app --host 127.0.0.1 --port 8000
```

Visit `http://127.0.0.1:8000/docs`.

## Note

This is a deterministic ranking algorithm, not a trained AI model. Feedback is local and can be deleted. The existing application authentication and public deployment limitations still apply.
