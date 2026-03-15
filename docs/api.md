# MapleBridge API Reference

Base URL: `https://maplebridge.io/api/v1`

All requests must include `Content-Type: application/json`.

---

## Endpoints

### POST `/webhook/manus`

Submit a buyer demand for AI parsing and matching.

**Request Body**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `demand` | string | Yes | Natural language buyer requirement (supports English and Chinese) |
| `contact_email` | string | No | Buyer contact email for match notifications |
| `contact_phone` | string | No | Buyer contact phone number |
| `contact_wechat` | string | No | Buyer WeChat ID |
| `source` | string | No | Origin identifier (e.g., `"api"`, `"telegram"`, `"web"`) |
| `category` | string | No | Product category hint (see category list) |
| `budget_usd` | number | No | Estimated order budget in USD |

**Example Request**

```bash
curl -X POST https://maplebridge.io/api/v1/webhook/manus \
  -H "Content-Type: application/json" \
  -d '{
    "demand": "I need 1000 units of wireless Bluetooth earbuds for the Canadian market, CE and FCC certified, budget around $15 per unit",
    "contact_email": "purchasing@acme.ca",
    "source": "api",
    "category": "消费电子"
  }'
```

**Example Response**

```json
{
  "status": "ok",
  "intent_id": "INTENT_A1B2C3D4",
  "matched": 5,
  "message": "Intent received and matched"
}
```

**Error Response**

```json
{
  "status": "error",
  "message": "demand field is required"
}
```

---

### GET `/intents`

List recent intents (DEMAND and SUPPLY).

**Query Parameters**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `intent_type` | string | `"DEMAND"` | Filter by `DEMAND` or `SUPPLY` |
| `category` | string | — | Filter by product category |
| `limit` | integer | `20` | Number of results (max 100) |
| `offset` | integer | `0` | Pagination offset |

**Example Request**

```bash
curl "https://maplebridge.io/api/v1/intents?intent_type=SUPPLY&category=消费电子&limit=10"
```

**Example Response**

```json
{
  "total": 42,
  "intents": [
    {
      "intent_id": "INTENT_B3C4D5E6",
      "intent_type": "SUPPLY",
      "category": "消费电子",
      "summary": "Shenzhen electronics manufacturer, MOQ 500 units, CE/FCC certified",
      "created_at": 1741910400,
      "status": "pending"
    }
  ]
}
```

---

### GET `/intents/{intent_id}`

Retrieve a single intent by ID.

**Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `intent_id` | string | Intent ID (format: `INTENT_XXXXXXXX`) |

**Example Request**

```bash
curl "https://maplebridge.io/api/v1/intents/INTENT_A1B2C3D4"
```

**Example Response**

```json
{
  "intent_id": "INTENT_A1B2C3D4",
  "intent_type": "DEMAND",
  "category": "消费电子",
  "summary": "1000 units wireless earbuds, CE/FCC, $15/unit budget",
  "payload": {
    "core_need": "1000 units wireless Bluetooth earbuds for Canadian market",
    "estimated_value_usd": 15000,
    "scarcity_level": "MEDIUM",
    "contact_email": "purchasing@acme.ca",
    "source": "api"
  },
  "status": "pending",
  "created_at": 1741910400
}
```

---

### GET `/matches`

List matched DEMAND-SUPPLY pairs.

**Query Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `intent_id` | string | Filter matches for a specific intent |
| `min_score` | float | Minimum match score (0.0 – 1.0) |
| `limit` | integer | Number of results (default 20) |

**Example Request**

```bash
curl "https://maplebridge.io/api/v1/matches?intent_id=INTENT_A1B2C3D4"
```

**Example Response**

```json
{
  "matches": [
    {
      "match_id": "MATCH_X1Y2Z3",
      "demand_intent_id": "INTENT_A1B2C3D4",
      "supply_intent_id": "INTENT_B3C4D5E6",
      "score": 0.91,
      "matched_at": 1741910500,
      "status": "notified"
    }
  ]
}
```

---

### GET `/health`

Health check endpoint.

```bash
curl "https://maplebridge.io/api/v1/health"
```

Response:
```json
{"status": "ok", "version": "1.0"}
```

---

## Rate Limits

| Tier | Requests / minute |
|------|-------------------|
| Public (unauthenticated) | 10 |
| Authenticated API key | 100 |

Rate limit headers are included in all responses:
- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `X-RateLimit-Reset`

---

## Intent ID Format

All intent IDs follow the pattern `INTENT_` + 8 uppercase hex characters:

```
INTENT_A1B2C3D4
```

Match IDs follow: `MATCH_` + 8 uppercase hex characters.

---

## Status Values

| Status | Description |
|--------|-------------|
| `pending` | Intent created, awaiting matching |
| `matched` | At least one match found |
| `notified` | Match notification sent to buyer/supplier |
| `closed` | Deal completed or expired |

---

## Error Codes

| HTTP Status | Meaning |
|-------------|---------|
| 400 | Bad request — missing or invalid fields |
| 404 | Intent not found |
| 429 | Rate limit exceeded |
| 500 | Internal server error |
