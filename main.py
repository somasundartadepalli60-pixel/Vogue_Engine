"""Vogue Engine local application entry point.

Run: python main.py --host 127.0.0.1 --port 8000
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Run the Vogue Engine FastAPI application")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    try:
        import uvicorn
    except ImportError as exc:
        raise SystemExit("Missing dependencies. Install with: python -m pip install -r requirements.lock") from exc
    uvicorn.run("vogue_engine.dashboards.router:app", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
