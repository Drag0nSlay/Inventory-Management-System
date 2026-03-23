from pathlib import Path
import sys

PROJECT_DIR = Path(__file__).resolve().parents[1] / ".vscode" / "project"
sys.path.insert(0, str(PROJECT_DIR))

from inventory_utils import inventory_counts, parse_non_negative_number, validate_product_form


def test_parse_non_negative_number_accepts_valid_values():
    assert parse_non_negative_number("12", "Quantity") == 12
    assert parse_non_negative_number("12.50", "Price", allow_float=True) == 12.5


def test_parse_non_negative_number_rejects_invalid_values():
    for value in ("", "-1"):
        try:
            parse_non_negative_number(value, "Quantity")
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")


def test_validate_product_form_rejects_missing_inputs():
    try:
        validate_product_form("Select", "Acme", "Widget", "10", "5")
    except ValueError as exc:
        assert "Category" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_inventory_counts_reports_totals():
    counts = inventory_counts(
        [
            {"qty": "10"},
            {"qty": "5"},
            {"qty": "0"},
        ]
    )
    assert counts == {"total": 3, "low_stock": 1, "out_of_stock": 1}
