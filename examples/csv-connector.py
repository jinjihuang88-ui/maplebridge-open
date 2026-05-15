"""
MapleBridge CSV connector example.

This file shows how to map CSV rows to buyer or supplier intents.
It demonstrates the public connector boundary only.

What stays outside the open repository:
- Live crawler sources and credentials
- Customer data and private supplier records
- Production ranking logic and score thresholds
- Actual supplier contact information
"""
from __future__ import annotations

import csv
import json
from typing import Any


def map_csv_row_to_intent(row: dict[str, Any]) -> dict[str, Any]:
    """Map a CSV row to a buyer or supplier intent object."""
    role = row.get("role", "buyer").lower()

    base = {
        "role": role,
        "language": row.get("language", "en"),
        "product_category": row.get("product_category", ""),
        "summary": row.get("summary", ""),
        "country": row.get("country", ""),
        "moq": {
            "value": int(row.get("moq_value", 0)),
            "unit": row.get("moq_unit", "units"),
        },
        "compliance": [c.strip() for c in row.get("compliance", "").split(",") if c.strip()],
        "review_state": "needs_review",
    }

    if role == "supplier":
        base["channels"] = [c.strip() for c in row.get("channels", "").split(",") if c.strip()]

    base["fit_constraints"] = [c.strip() for c in row.get("fit_constraints", "").split(",") if c.strip()]

    return base


def process_csv_file(csv_path: str) -> list[dict[str, Any]]:
    """Read a CSV file and return a list of intent objects."""
    intents = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            intents.append(map_csv_row_to_intent(row))
    return intents


if __name__ == "__main__":
    # Sample CSV input (mock data only for documentation purposes)
    # NOTE: What stays outside the open repository:
    # - Live crawler sources and credentials
    # - Customer data and private supplier records
    # - Production ranking logic and score thresholds
    # - Actual supplier contact information
    sample_csv = '''role,language,product_category,summary,country,moq_value,moq_unit,compliance,fit_constraints,channels
buyer,en,drinkware,Low-MOQ insulated bottle order for Canada,Canada,500,units,"BPA-free, FDA food contact","custom logo, retail packaging, ship to Toronto",
supplier,en,drinkware,Shenzhen drinkware OEM with FDA/LFGB experience,China,300,units,"BPA-free, FDA food contact, LFGB","custom logo, retail packaging","OEM, private label, North America export"
'''
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(sample_csv)
        temp_path = f.name

    intents = process_csv_file(temp_path)
    print(json.dumps(intents, indent=2))