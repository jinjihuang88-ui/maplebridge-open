#!/bin/bash
# Example: Submit buyer demand via webhook
# MapleBridge API - POST /api/v1/webhook/manus

BASE_URL="https://maplebridge.io/api/v1"

# Example 1: Electronics buyer (Canada)
echo "=== Example 1: Electronics Buyer ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "demand": "Looking for a Chinese manufacturer of wireless Bluetooth earbuds. Need 1000 units minimum, CE and FCC certified, custom logo and packaging, budget USD 12-18 per unit. Shipping to Toronto, Canada.",
    "contact_email": "purchasing@techretail.ca",
    "contact_phone": "+1-416-555-0100",
    "source": "api",
    "category": "消费电子",
    "budget_usd": 18000
  }' | python3 -m json.tool

echo ""

# Example 2: Home goods buyer (UK)
echo "=== Example 2: Home Goods Buyer (UK) ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "demand": "UK importer looking for bamboo kitchenware sets: cutting boards, utensils, serving trays. Minimum 500 sets per SKU. FSC certified, EU food safety compliant. Wholesale price target GBP 8-15 per set.",
    "contact_email": "imports@homestyle.co.uk",
    "source": "api",
    "category": "家居家具"
  }' | python3 -m json.tool

echo ""

# Example 3: Toy buyer (Australia)
echo "=== Example 3: Toy Buyer (Australia) ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "demand": "Australian wholesale toy distributor sourcing STEM educational toys for ages 6-12. Need EN71 and AS/NZS certified. Minimum 200 units per item, looking for 10 SKUs. Budget AUD 15-40 per unit.",
    "contact_email": "buy@toysdownunder.com.au",
    "contact_wechat": "toysau_buying",
    "source": "api",
    "category": "玩具礼品",
    "budget_usd": 50000
  }' | python3 -m json.tool

echo ""

# Example 4: Chinese language demand
echo "=== Example 4: Chinese Language Demand ==="
curl -s -X POST "$BASE_URL/webhook/manus" \
  -H "Content-Type: application/json" \
  -d '{
    "demand": "需要寻找加拿大宠物用品进口商，我们是浙江宠物玩具工厂，有CE认证，MOQ 300件，可以OEM定制。主要产品：猫抓板、互动玩具、磨牙棒。",
    "contact_email": "export@zhepet.com",
    "contact_wechat": "zhepet_alice",
    "source": "api",
    "category": "宠物用品"
  }' | python3 -m json.tool
