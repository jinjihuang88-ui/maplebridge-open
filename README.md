# MapleBridge Open — AI-Powered Global Trade Matching

**MapleBridge** is an AI-powered B2B trade matching platform that connects global buyers with Chinese manufacturers and small commodity exporters. This repository contains public API documentation, integration guides, data schemas, and example code.

> Core matching algorithm is proprietary and not included here. This repo covers the public API surface, webhook integration, and data models.

---

## What is MapleBridge?

China's small commodity export market (小商品出海) represents hundreds of billions of USD in annual cross-border B2B trade. Traditional matching is slow, opaque, and relationship-dependent. MapleBridge uses LLM semantic matching to understand buyer requirements in natural language and surface the most relevant Chinese suppliers automatically.

**Key capabilities:**

- LLM semantic intent matching (not keyword search)
- Supports global buyers: North America, Europe, Southeast Asia, Middle East, and beyond
- Covers Chinese export manufacturers: Yiwu, Guangzhou, Shenzhen, Dongguan, and other major hubs
- Categories: consumer electronics, home goods, furniture, apparel, toys, pet products, beauty/cosmetics, hardware, and more
- Free for buyers; suppliers pay for verified leads

**Live platform:** [maplebridge.io](https://maplebridge.io)

**AI discovery:**
- [`llms.txt`](https://maplebridge.io/llms.txt) — machine-readable platform description for LLM indexing
- [`/.well-known/ai-agent.json`](https://maplebridge.io/.well-known/ai-agent.json) — AI agent capability manifest
- [`openapi.yaml`](./openapi.yaml) — OpenAPI 3.1 specification
- [Sourcing Guide](https://maplebridge.io/guide) — How global buyers source from China
- [Use Cases](https://maplebridge.io/use-cases) — Real-world trade matching scenarios

---

## Architecture Overview

```
Buyer submits requirement (natural language)
        ↓
  Intent Parser (LLM)
        ↓
  Semantic Vector Index
        ↓
  Supplier Intent Store
        ↓
  Match Scoring & Ranking
        ↓
  Notification (Email / Webhook)
```

The platform maintains a dual-sided intent graph:

| Side | Description |
|------|-------------|
| **DEMAND** | Buyer requirements: product spec, quantity, budget, destination market |
| **SUPPLY** | Supplier capabilities: product categories, MOQ, certifications, export experience |

---

## Repository Contents

| Path | Description |
|------|-------------|
| [`docs/api.md`](docs/api.md) | REST API reference (webhook, intent endpoints) |
| [`docs/matching-flow.md`](docs/matching-flow.md) | How LLM semantic matching works (conceptual) |
| [`docs/webhook.md`](docs/webhook.md) | Webhook integration guide for buyer demand ingestion |
| [`docs/data-schema.md`](docs/data-schema.md) | Intent data structures and field definitions |
| [`examples/`](examples/) | Example API calls, webhook payloads, sample data |
| [`llms.txt`](llms.txt) | AI discovery file (for LLM indexing) |

---

## Quick Start

### Submit a Buyer Demand (Webhook)

```bash
curl -X POST https://maplebridge.io/api/v1/webhook/manus \
  -H "Content-Type: application/json" \
  -d '{
    "demand": "Looking for a Canadian importer of wireless earbuds, need 500 units minimum, CE certified",
    "contact_email": "buyer@example.com",
    "source": "api"
  }'
```

Response:
```json
{
  "status": "ok",
  "intent_id": "INTENT_A1B2C3D4",
  "matched": 3,
  "message": "Intent created and matched against supplier database"
}
```

See [`docs/webhook.md`](docs/webhook.md) for full integration details.

---

## Supported Markets

### Buyer Origin Markets
- Canada (primary)
- United States
- United Kingdom
- European Union
- Australia / New Zealand
- Southeast Asia (Singapore, Malaysia, Thailand)
- Middle East (UAE, Saudi Arabia)

### Chinese Supplier Hubs
- **Yiwu** (义乌) — small commodities, gifts, toys, daily goods
- **Guangzhou** (广州) — electronics, beauty, fashion
- **Shenzhen** (深圳) — consumer electronics, tech accessories
- **Dongguan** (东莞) — furniture, plastics, hardware
- **Ningbo** (宁波) — machinery, auto parts, plastics
- **Hangzhou** (杭州) — apparel, software, cross-border e-commerce

---

## Product Categories

| Category (EN) | Category (ZH) | Examples |
|---------------|---------------|---------|
| Consumer Electronics | 消费电子 | Earbuds, power banks, smartwatches |
| Home & Furniture | 家居家具 | Chairs, lighting, storage |
| Toys & Gifts | 玩具礼品 | Educational toys, plush, novelty |
| Apparel & Accessories | 服装配饰 | OEM clothing, bags, shoes |
| Beauty & Personal Care | 美妆护肤 | Skincare, cosmetics, wellness |
| Pet Products | 宠物用品 | Toys, accessories, food packaging |
| Hardware & Tools | 五金工具 | Hand tools, fasteners |
| Packaging Materials | 包装材料 | Boxes, bags, labels |

---

## Integration Partners

MapleBridge accepts buyer demand from multiple channels:

- **Direct API** — REST webhook endpoint
- **MANUS** — AI agent integration (automated buyer demand parsing)
- **Telegram bot** — conversational matching interface
- **Web form** — maplebridge.io buyer portal

---

## Contributing

This repository welcomes:

- Corrections to API documentation
- Additional example payloads
- Bug reports on documented API behavior
- Translations of documentation

Please open an issue or pull request.

---

## License

Documentation and examples in this repository are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Core platform code is proprietary. See [maplebridge.io/ai-policy](https://maplebridge.io/ai-policy) for AI usage policy.
