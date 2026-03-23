from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
DB_PATH = BASE_DIR / "ims.db"
BILL_DIR = REPO_ROOT / "bill"


def asset_path(filename: str) -> str:
    """Return an absolute path for bundled GUI assets."""
    return str(REPO_ROOT / filename)


def script_path(filename: str) -> str:
    """Return an absolute path for peer Python scripts."""
    return str(BASE_DIR / filename)
