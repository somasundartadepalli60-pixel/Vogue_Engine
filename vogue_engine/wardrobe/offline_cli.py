"""Command-line outfit recommendations from local JSON inventory."""
import argparse
import json
from pathlib import Path
from .offline_planner import Garment, recommend


def run(argv=None):
    parser = argparse.ArgumentParser(description="Rank outfits from a local wardrobe JSON file")
    parser.add_argument("inventory", type=Path)
    parser.add_argument("--season", default="")
    parser.add_argument("--occasion", default="")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)
    records = json.loads(args.inventory.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        parser.error("Inventory must be a JSON array")
    garments = [Garment(name=entry["name"], category=entry["category"],
                        color=entry["color"], seasons=tuple(entry.get("seasons", ())),
                        occasions=tuple(entry.get("occasions", ()))) for entry in records]
    result = [{"score": score, "items": [{"name": g.name, "category": g.category,
                "color": g.color} for g in items]} for score, items in recommend(
                    garments, args.season, args.occasion, args.limit)]
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(run())
