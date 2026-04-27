#!/bin/bash
# Example: Submit buyer demand or supplier capability via webhook
# MapleBridge API - POST /api/v1/webhook/manus

BASE_URL="https://maplebridge.io/api/v1"

# Example 1: Electronics buyer (Canada)
echo "=== Example 1: Electronics Buyer ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "core_need": "Looking for a Chinese manufacturer of wireless Bluetooth earbuds. Need 1000 units minimum, CE and FCC certified, custom logo and packaging, budget USD 12-18 per unit. Shipping to Toronto, Canada.",
    "contact_email": "purchasing@techretail.ca",
    "contact_phone": "+1-416-555-0100",
    "source_url": "api-example",
    "role": "demand",
    "category": "consumer electronics",
    "budget_usd": 18000
  }' | python3 -m json.tool

echo ""

# Example 2: Home goods buyer (UK)
echo "=== Example 2: Home Goods Buyer (UK) ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "core_need": "UK importer looking for bamboo kitchenware sets: cutting boards, utensils, serving trays. Minimum 500 sets per SKU. FSC certified, EU food safety compliant. Wholesale price target GBP 8-15 per set.",
    "contact_email": "imports@homestyle.co.uk",
    "source_url": "api-example",
    "role": "demand",
    "category": "home goods"
  }' | python3 -m json.tool

echo ""

# Example 3: Toy buyer (Australia)
echo "=== Example 3: Toy Buyer (Australia) ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "core_need": "Australian wholesale toy distributor sourcing STEM educational toys for ages 6-12. Need EN71 and AS/NZS certified. Minimum 200 units per item, looking for 10 SKUs. Budget AUD 15-40 per unit.",
    "contact_email": "buy@toysdownunder.com.au",
    "contact_wechat": "toysau_buying",
    "source_url": "api-example",
    "role": "demand",
    "category": "toys",
    "budget_usd": 50000
  }' | python3 -m json.tool

echo ""

# Example 4: Supplier capability
echo "=== Example 4: Supplier Capability ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "core_need": "Zhejiang pet toy factory looking for Canadian pet product importers. CE available, MOQ 300 units, OEM customization supported. Main products: cat scratchers, interactive toys, chew toys.",
    "contact_email": "export@zhepet.com",
    "contact_wechat": "zhepet_alice",
    "source_url": "api-example",
    "role": "supply",
    "category": "pet products"
  }' | python3 -m json.tool
