# Offline outfit planner quickstart

No API keys, network connection, or third-party packages are required for this component.

From the project root:

```bash
python -m vogue_engine.wardrobe.offline_cli examples/wardrobe.json --season summer --occasion casual --limit 5
python -m unittest tests.test_offline_planner -v
```

The JSON input is an array of garments with `name`, `category` (`top`, `bottom`, `shoes`), and `color`.
Optional `seasons` and `occasions` are arrays of strings. The output contains scores and the garments in each ranked outfit.

The full FastAPI and image-analysis application has separate optional dependencies described in `pyproject.toml`.
