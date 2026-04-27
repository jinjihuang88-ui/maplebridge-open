# Webhook Integration Guide

The MapleBridge webhook allows external systems such as AI agents, CRMs, sourcing forms, and partner tools to submit buyer demands or supplier capability statements into the public matching boundary.

This is a public integration surface. It does not expose production ranking thresholds, private crawler sources, customer records, or notification credentials.

## Endpoint

```text
POST https://maplebridge.io/api/v1/webhook/manus
Content-Type: application/json
```

## Request Format

```json
{
  "core_need": "string (required)",
  "role": "demand | supply (optional)",
  "contact_email": "string (optional)",
  "contact_name": "string (optional)",
  "company": "string (optional)",
  "country": "string (optional)",
  "source_url": "string (optional)",
  "category": "string (optional)",
  "budget_usd": 0,
  "manus_record_id": "string (optional)"
}
```

## Fields

`core_need` is the natural-language buyer requirement or supplier capability statement. It can be written in plain English or Chinese.

`role` is optional. Use `demand` for buyer requirements and `supply` for supplier capability statements. If omitted, MapleBridge attempts to infer the role from the text.

`source_url` is an optional origin hint such as `api-example`, `manus-agent`, `crm-record-123`, or a partner record URL.

`category` is an optional product category hint, such as `consumer electronics`, `home goods`, `toys`, `apparel`, `beauty`, `pet products`, `hardware`, or `general`.

## Example: Buyer Demand

```json
{
  "core_need": "Need 500 stainless steel insulated bottles for Canadian retail. 500ml, BPA-free, custom logo, leak-proof cap, retail packaging.",
  "role": "demand",
  "contact_email": "buyer@example.com",
  "country": "CA",
  "source_url": "api-example",
  "category": "drinkware",
  "budget_usd": 6000
}
```

## Example: Supplier Capability

```json
{
  "core_need": "Zhejiang pet toy factory looking for Canadian pet product importers. CE available, MOQ 300 units, OEM customization supported.",
  "role": "supply",
  "contact_email": "export@example.com",
  "country": "China",
  "source_url": "api-example",
  "category": "pet products"
}
```

## Response Format

```json
{
  "status": "received",
  "role": "demand",
  "intent_id": "INTENT_A1B2C3D4",
  "message": "Demand received and background matching started"
}
```

`intent_id` is the tracking identifier for the created intent.

`role` is the interpreted role, either `demand` or `supply`.

## Python Example

```python
import requests

def submit_demand(core_need, email=None, source_url="api-example"):
    response = requests.post(
        "https://maplebridge.io/api/v1/webhook/manus",
        json={
            "core_need": core_need,
            "role": "demand",
            "contact_email": email,
            "source_url": source_url,
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()

result = submit_demand(
    "Need 2000 units custom logo USB-C cables for Canada, 1m length, braided nylon.",
    email="buyer@example.com",
)
print(result["intent_id"])
```

## JavaScript Example

```javascript
async function submitDemand(coreNeed, contactEmail, sourceUrl = "api-example") {
  const response = await fetch("https://maplebridge.io/api/v1/webhook/manus", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      core_need: coreNeed,
      role: "demand",
      contact_email: contactEmail,
      source_url: sourceUrl,
    }),
  });
  return response.json();
}
```

## Demand Writing Tips

Good buyer demand examples include product type, quantity, compliance requirements, target market, budget range, and delivery constraints.

Good supplier capability examples include product category, MOQ, compliance support, OEM/ODM/private-label capability, export market experience, and packaging or logistics limits.

## Idempotency

The webhook does not enforce idempotency. If your integration may submit the same record more than once, include a stable `manus_record_id` or deduplicate in your own system before calling the webhook.
