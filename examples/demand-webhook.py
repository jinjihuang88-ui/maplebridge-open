"""
MapleBridge Webhook Integration Examples
POST /api/v1/webhook/manus

Demonstrates buyer demand submission from Python.
"""

import requests

BASE_URL = "https://maplebridge.io/api/v1"


def submit_demand(demand: str, **kwargs) -> dict:
    """Submit a buyer demand to MapleBridge matching engine."""
    payload = {"demand": demand, **kwargs}
    response = requests.post(
        f"{BASE_URL}/webhook/manus",
        json=payload,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def get_intent(intent_id: str) -> dict:
    """Retrieve intent details by ID."""
    response = requests.get(f"{BASE_URL}/intents/{intent_id}", timeout=15)
    response.raise_for_status()
    return response.json()


def get_matches(intent_id: str) -> list:
    """Get matched suppliers for a demand intent."""
    response = requests.get(
        f"{BASE_URL}/matches",
        params={"intent_id": intent_id},
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("matches", [])


# ── Example 1: Simple buyer demand ──────────────────────────────────────────
result = submit_demand(
    demand="Need 500 units stainless steel vacuum water bottles for Canadian retail. 500ml, BPA-free, custom logo, leak-proof. Budget $8-12 USD per unit.",
    contact_email="buyer@retailco.ca",
    source="api",
    category="家居家具",
    budget_usd=6000,
)
print("Intent created:", result["intent_id"])
print("Suppliers matched:", result["matched"])

intent_id = result["intent_id"]

# ── Example 2: Retrieve intent details ──────────────────────────────────────
intent = get_intent(intent_id)
print("\nIntent status:", intent["status"])
print("Summary:", intent["summary"])

# ── Example 3: Get match results ─────────────────────────────────────────────
matches = get_matches(intent_id)
for match in matches:
    print(f"\nMatch: {match['match_id']} | Score: {match['score']:.2f}")
    print(f"  Supply intent: {match['supply_intent_id']}")
    print(f"  Status: {match['status']}")

# ── Example 4: Batch processing from a list ──────────────────────────────────
buyer_demands = [
    {
        "demand": "1000 units custom printed tote bags for Canadian eco brand, GOTS certified cotton, 40x35cm",
        "contact_email": "ops@ecobrand.ca",
        "category": "服装服饰",
    },
    {
        "demand": "Pet grooming kit set: brush, nail clipper, comb. 300 sets MOQ. For UK market.",
        "contact_email": "sourcing@petshop.co.uk",
        "category": "宠物用品",
    },
    {
        "demand": "Seeking Yiwu small goods exporter: keychains, fridge magnets, souvenir items. Min 5000 pcs. Australia.",
        "contact_email": "wholesale@giftco.com.au",
        "category": "玩具礼品",
    },
]

print("\n=== Batch Submission ===")
for item in buyer_demands:
    r = submit_demand(**item, source="batch_api")
    print(f"✓ {r['intent_id']} | matched={r['matched']} | {item['demand'][:50]}...")
