"""Summarize local Git evidence without mislabeling merges as pull requests."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    commits = git("rev-list", "--count", "HEAD")
    merges = git("rev-list", "--count", "--merges", "HEAD")
    print(f"Local commits: {commits}")
    print(f"Local merge commits: {merges}")
    print("Hosted pull requests: not verifiable from local Git history")
    print("Review CONTRIBUTING.md for the genuine hosted PR workflow")

if __name__ == "__main__":
    main()
