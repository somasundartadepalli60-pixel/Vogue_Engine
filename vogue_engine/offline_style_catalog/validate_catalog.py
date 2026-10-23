"""Validate independently stored outfit recommendation examples without dependencies."""
import json
from pathlib import Path

def validate(root=None):
    root = Path(root) if root else Path(__file__).parent
    files = sorted(root.glob("scenario_*.json"))
    seen = set()
    for path in files:
        item = json.loads(path.read_text(encoding="utf-8"))
        assert item["id"] not in seen, f"Duplicate ID in {path}"
        seen.add(item["id"])
        assert item["season"] in {"spring", "summer", "autumn", "winter"}
        assert item["occasion"] in {"casual", "work", "formal", "travel", "sport"}
        assert len(item["outfit"]) == 3
        assert len({piece["category"] for piece in item["outfit"]}) == 3
        assert all(piece["color"] and piece["category"] for piece in item["outfit"])
        assert 0 <= item["score"] <= 100
    return len(files)

if __name__ == "__main__":
    print(f"Validated {validate()} offline outfit scenarios")
