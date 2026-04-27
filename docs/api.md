# MapleBridge API Reference

Base URL: `https://maplebridge.io/api/v1`

All requests must include `Content-Type: application/json`.

This document describes the public integration boundary exposed for buyer demand and supplier capability submission. It is separate from the production app implementation.

## POST `/webhook/manus`

Submit a buyer demand or supplier capability statement for AI parsing and background matching.

### Request Body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `core_need` | string | Yes | Natural-language buyer requirement or supplier capability statement |
| `role` | string | No | `demand` or `supply`; if omitted, MapleBridge attempts role inference |
| `contact_email` | string | No | Contact email for match notifications |
| `contact_name` | string | No | Contact person name |
| `company` | string | No | Company name |
| `country` | string | No | Country or market hint |
| `category` | string | No | Product category hint |
| `budget_usd` | number | No | Estimated order value or budget |
| `source_url` | string | No | Source record URL or integration origin |
| `manus_record_id` | string | No | Stable external record ID for deduplication on the caller side |

### Example Buyer Request

```bash
curl -X POST https://maplebridge.io/api/v1/webhook/manus \
  -H "Content-Type: application/json" \
  -d '{
    "core_need": "I need 1000 units of wireless Bluetooth earbuds for the Canadian market, CE and FCC certified, budget around USD 15 per unit.",
    "role": "demand",
    "contact_email": "purchasing@example.com",
    "source_url": "api-example",
    "category": "consumer electronics"
  }'
```

### Example Supplier Request

```bash
curl -X POST https://maplebridge.io/api/v1/webhook/manus \
  -H "Content-Type: application/json" \
  -d '{
    "core_need": "Shenzhen electronics factory producing FCC-certified Bluetooth earbuds, MOQ 300 units, OEM packaging, Amazon FBA prep available.",
    "role": "supply",
    "contact_email": "export@example.com",
    "source_url": "api-example",
    "category": "consumer electronics"
  }'
```

### Example Response

```json
{
  "status": "received",
  "role": "demand",
  "intent_id": "INTENT_A1B2C3D4",
  "message": "Demand received and background matching started"
}
```

## GET `/health`

Health check endpoint.

```bash
curl "https://maplebridge.io/api/v1/health"
```

Example response:

```json
{
  "status": "ok",
  "service": "IntentNet Alpha"
}
```

## Public Boundary

This open API reference intentionally avoids production-only details:

- private ranking thresholds
- production crawler source lists
- customer data
- production database shape
- notification credentials
- private anti-abuse rules
