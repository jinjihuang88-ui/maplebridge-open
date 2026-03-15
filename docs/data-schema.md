# Data Schema Reference

This document describes the data structures used in the MapleBridge intent matching system.

---

## Intent Object

The core data unit in MapleBridge. Represents either a buyer demand (DEMAND) or a supplier capability (SUPPLY).

```json
{
  "intent_id": "INTENT_A1B2C3D4",
  "intent_type": "DEMAND",
  "issuer_node": "NODE_12345678",
  "category": "消费电子",
  "summary": "1000 units wireless earbuds, CE/FCC certified",
  "status": "pending",
  "estimated_value_usd": 15000,
  "scarcity_level": "MEDIUM",
  "created_at": 1741910400,
  "payload": { ... }
}
```

### Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `intent_id` | string | Unique identifier (`INTENT_` + 8 hex chars) |
| `intent_type` | enum | `"DEMAND"` or `"SUPPLY"` |
| `issuer_node` | string | Node ID of the submitting user/agent |
| `category` | string | Product category (see Category Taxonomy) |
| `summary` | string | 50-character summary for display |
| `status` | enum | `pending`, `matched`, `notified`, `closed` |
| `estimated_value_usd` | number | Estimated order value in USD (0 if unknown) |
| `scarcity_level` | enum | `LOW`, `MEDIUM`, `HIGH` |
| `created_at` | unix timestamp | Creation time |
| `payload` | object | Full intent details (see Payload Schema) |

---

## Payload Schema

The `payload` field contains the full structured intent data extracted by the LLM parser.

### DEMAND Payload

```json
{
  "core_need": "1000 units wireless Bluetooth earbuds for Canadian market, CE and FCC certified",
  "category": "消费电子",
  "intent_type": "DEMAND",
  "estimated_value_usd": 15000,
  "scarcity_level": "MEDIUM",
  "summary": "1000 units wireless earbuds",
  "summary_en": "1000 units wireless Bluetooth earbuds, CE/FCC certified, Canada",
  "role": "demand",
  "contact_email": "buyer@company.com",
  "contact_phone": "+1-416-555-0100",
  "contact_wechat": "",
  "source": "api",
  "budget_usd": 15000,
  "quantity": 1000,
  "destination_market": "Canada",
  "certifications": ["CE", "FCC"],
  "timeline": ""
}
```

### SUPPLY Payload

```json
{
  "core_need": "[Shenzhen AudioTech Co.] OEM/ODM wireless earbuds manufacturer, MOQ 500 units, CE/FCC/RoHS certified",
  "category": "消费电子",
  "intent_type": "SUPPLY",
  "estimated_value_usd": 0,
  "scarcity_level": "MEDIUM",
  "summary": "Wireless earbuds OEM manufacturer",
  "summary_en": "Shenzhen-based wireless earbuds OEM/ODM, MOQ 500, exports to North America, CE/FCC certified",
  "role": "supply",
  "contact_email": "sales@auditech-sz.com",
  "contact_phone": "+86-755-1234-5678",
  "contact_wechat": "audiotech_sales",
  "company": "Shenzhen AudioTech Co.",
  "source_url": "https://auditech-sz.com",
  "source": "CRAWLER_SUPPLY",
  "supply_type": "manufacturer",
  "moq": 500,
  "certifications": ["CE", "FCC", "RoHS"],
  "export_markets": ["North America", "Europe"]
}
```

### Payload Field Reference

| Field | DEMAND | SUPPLY | Description |
|-------|--------|--------|-------------|
| `core_need` | ✓ | ✓ | Primary text used for semantic matching |
| `category` | ✓ | ✓ | Product category (Chinese label) |
| `intent_type` | ✓ | ✓ | `"DEMAND"` or `"SUPPLY"` |
| `summary` | ✓ | ✓ | 50-char display summary |
| `summary_en` | ✓ | ✓ | English summary (up to 100 chars) |
| `role` | ✓ | ✓ | `"demand"` or `"supply"` |
| `contact_email` | ✓ | ✓ | Contact email |
| `contact_phone` | ✓ | ✓ | Contact phone |
| `contact_wechat` | ✓ | ✓ | WeChat ID |
| `source` | ✓ | ✓ | Originating channel |
| `estimated_value_usd` | ✓ | — | Estimated deal value |
| `budget_usd` | ✓ | — | Buyer budget |
| `quantity` | ✓ | — | Required quantity |
| `destination_market` | ✓ | — | Target market |
| `certifications` | ✓ | ✓ | Required / available certifications |
| `timeline` | ✓ | — | Delivery deadline |
| `company` | — | ✓ | Supplier company name |
| `source_url` | — | ✓ | Supplier website URL |
| `supply_type` | — | ✓ | `manufacturer`, `wholesaler`, `trader`, `distributor` |
| `moq` | — | ✓ | Minimum order quantity |
| `export_markets` | — | ✓ | Markets the supplier serves |

---

## Match Object

A matched DEMAND-SUPPLY pair.

```json
{
  "match_id": "MATCH_X1Y2Z3W4",
  "demand_intent_id": "INTENT_A1B2C3D4",
  "supply_intent_id": "INTENT_B3C4D5E6",
  "score": 0.91,
  "score_breakdown": {
    "category": 0.30,
    "semantic": 0.38,
    "structural": 0.16,
    "supplier_quality": 0.07
  },
  "matched_at": 1741910500,
  "status": "notified"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `match_id` | string | Unique match identifier |
| `demand_intent_id` | string | Buyer intent ID |
| `supply_intent_id` | string | Supplier intent ID |
| `score` | float | Composite match score (0.0–1.0) |
| `score_breakdown` | object | Per-component score details |
| `matched_at` | unix timestamp | When match was created |
| `status` | enum | `pending`, `notified`, `confirmed`, `rejected` |

---

## Category Taxonomy

```
综合 (General)
消费电子 (Consumer Electronics)
  ├── 无线耳机 (Wireless Audio)
  ├── 智能手表 (Smartwatches)
  ├── 移动电源 (Power Banks)
  └── 数据线配件 (Cables & Accessories)
家居家具 (Home & Furniture)
  ├── 照明灯具 (Lighting)
  ├── 收纳储物 (Storage)
  └── 厨房用品 (Kitchen)
玩具礼品 (Toys & Gifts)
  ├── 益智玩具 (Educational Toys)
  ├── 毛绒玩具 (Plush)
  └── 节日礼品 (Seasonal Gifts)
服装服饰 (Apparel & Accessories)
  ├── OEM服装 (OEM Clothing)
  ├── 箱包 (Bags)
  └── 鞋类 (Footwear)
美妆护肤 (Beauty & Personal Care)
宠物用品 (Pet Products)
五金工具 (Hardware & Tools)
包装材料 (Packaging Materials)
```

---

## Scarcity Levels

| Level | Meaning | Typical Scenario |
|-------|---------|-----------------|
| `LOW` | Abundant supply/demand | Generic commodity products |
| `MEDIUM` | Moderate competition | Certified products, specific specs |
| `HIGH` | Rare match opportunity | Niche products, unusual certifications, very large orders |

High-scarcity intents receive priority in matching and notification.

---

## Supply Types

| Value | Description |
|-------|-------------|
| `manufacturer` | Direct production facility |
| `wholesaler` | Bulk reseller, does not manufacture |
| `trader` | Export trading company, aggregates multiple manufacturers |
| `distributor` | Regional distribution rights holder |
| `oem_odm` | OEM/ODM specialist, makes custom-branded products |
