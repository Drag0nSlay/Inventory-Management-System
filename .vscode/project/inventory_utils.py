from __future__ import annotations

from typing import Iterable, Mapping, Any


LOW_STOCK_THRESHOLD = 5


def parse_non_negative_number(value: str, field_name: str, *, allow_float: bool = False) -> float | int:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} is required")

    number = float(cleaned) if allow_float else int(cleaned)
    if number < 0:
        raise ValueError(f"{field_name} cannot be negative")
    return number



def validate_product_form(category: str, supplier: str, name: str, price: str, quantity: str) -> None:
    if category in {"", "Select", "Empty"}:
        raise ValueError("Category is required")
    if supplier in {"", "Select", "Empty"}:
        raise ValueError("Supplier is required")
    if not name.strip():
        raise ValueError("Name is required")

    parse_non_negative_number(price, "Price", allow_float=True)
    parse_non_negative_number(quantity, "Quantity")



def inventory_counts(products: Iterable[Mapping[str, Any]], low_stock_threshold: int = LOW_STOCK_THRESHOLD) -> dict[str, int]:
    counts = {"total": 0, "low_stock": 0, "out_of_stock": 0}
    for product in products:
        counts["total"] += 1
        qty = int(product.get("qty", 0) or 0)
        if qty <= 0:
            counts["out_of_stock"] += 1
        elif qty <= low_stock_threshold:
            counts["low_stock"] += 1
    return counts
