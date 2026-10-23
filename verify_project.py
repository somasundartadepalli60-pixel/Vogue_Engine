"""Validate the project structure and source compilation without cloud access."""
from pathlib import Path
import ast
import sys
ROOT = Path(__file__).resolve().parent
files = list((ROOT / "vogue_engine").rglob("*.py"))
errors = []
for path in files:
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeError) as exc:
        errors.append(f"{path}: {exc}")
print(f"Validated {len(files)} Python modules; errors={len(errors)}")
for error in errors[:20]:
    print(error, file=sys.stderr)
if not (ROOT / "vogue_engine/dashboards/router.py").exists():
    print("Missing FastAPI application entrypoint", file=sys.stderr)
    errors.append("missing entrypoint")
sys.exit(bool(errors))
