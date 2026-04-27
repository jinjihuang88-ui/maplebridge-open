"""
MapleBridge webhook example.

This file shows the public integration shape only. It is not required for the
local demo and does not include production credentials.
"""

from __future__ import annotations

import requests


BASE_URL = "https://maplebridge.io/api/v1"


def submit_demand(demand: str, **kwargs: object) -> dict:
    """Submit a buyer demand to the public webhook boundary."""
    payload = {"demand": demand, **kwargs}
    response = requests.post(
        f"{BASE_URL}/webhook/manus",
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = submit_demand(
        demand=(
            "Need 500 stainless steel insulated bottles for Canadian retail. "
            "500ml, BPA-free, custom logo, leak-proof cap, retail packaging."
        ),
        contact_email="buyer@example.com",
        source="api",
        category="drinkware",
        budget_usd=6000,
    )
    print("Intent created:", result.get("intent_id"))
