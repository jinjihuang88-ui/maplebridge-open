# Webhook Integration Guide

The MapleBridge webhook allows external systems (AI agents, CRMs, sourcing platforms) to submit buyer demands programmatically and receive matched supplier results.

---

## Endpoint

```
POST https://maplebridge.io/api/v1/webhook/manus
Content-Type: application/json
```

---

## Use Cases

- **AI agent integration**: Route buyer requirements collected by AI agents (MANUS, ChatGPT plugins, custom bots) directly to MapleBridge matching
- **CRM automation**: Trigger matching when a new sourcing request is logged in your CRM
- **Multi-platform aggregation**: Collect buyer intents from Telegram, WhatsApp, web forms, and funnel them through a single integration
- **Batch processing**: Process bulk buyer inquiry files by iterating webhook calls

---

## Request Format

```json
{
  "demand": "string (required)",
  "contact_email": "string (optional)",
  "contact_phone": "string (optional)",
  "contact_wechat": "string (optional)",
  "source": "string (optional)",
  "category": "string (optional)",
  "budget_usd": "number (optional)"
}
```

### Field Details

**`demand`** *(required)*

Natural language description of what the buyer needs. The LLM parser extracts:
- Product type and specifications
- Quantity / MOQ requirements
- Target market / destination
- Certifications required
- Timeline and urgency
- Budget constraints

Write as a buyer would describe their need — no structured format required.

**`source`** *(optional)*

Identifier for the originating channel. Used for analytics. Suggested values:
- `"api"` — direct API call
- `"telegram"` — Telegram bot
- `"manus"` — MANUS AI agent
- `"web"` — web portal
- `"crm"` — CRM integration

**`category`** *(optional)*

Product category hint to improve matching speed. Use Chinese category names from the taxonomy:

| Value | Meaning |
|-------|---------|
| `消费电子` | Consumer electronics |
| `家居家具` | Home & furniture |
| `玩具礼品` | Toys & gifts |
| `服装服饰` | Apparel & accessories |
| `美妆护肤` | Beauty & personal care |
| `宠物用品` | Pet products |
| `五金工具` | Hardware & tools |
| `综合` | General / uncategorized |

If omitted, the LLM parser infers the category from the demand text.

---

## Response Format

### Success

```json
{
  "status": "ok",
  "intent_id": "INTENT_A1B2C3D4",
  "matched": 3,
  "message": "Intent received and matched"
}
```

- `intent_id`: Use this to query match details via GET `/intents/{intent_id}`
- `matched`: Number of supplier intents matched (may be 0 for very specific requirements)

### Error

```json
{
  "status": "error",
  "message": "demand field is required"
}
```

---

## Example Integrations

### Python

```python
import requests

def submit_demand(demand_text, email=None, source="api"):
    response = requests.post(
        "https://maplebridge.io/api/v1/webhook/manus",
        json={
            "demand": demand_text,
            "contact_email": email,
            "source": source,
        }
    )
    return response.json()

result = submit_demand(
    "Need 2000 units custom logo USB-C cables for Canadian market, 1m length, braided nylon",
    email="buyer@company.com"
)
print(result["intent_id"])  # INTENT_XXXXXXXX
print(result["matched"])    # e.g., 7
```

### JavaScript / Node.js

```javascript
async function submitDemand(demand, contactEmail, source = "api") {
  const response = await fetch("https://maplebridge.io/api/v1/webhook/manus", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      demand,
      contact_email: contactEmail,
      source,
    }),
  });
  return response.json();
}

const result = await submitDemand(
  "Looking for bamboo toothbrush manufacturer, 10,000 units, FSC certified, eco packaging",
  "purchasing@greenco.ca"
);
console.log(result.intent_id);
```

### MANUS Agent Integration

MapleBridge is designed to receive structured buyer demands from MANUS AI agents. Configure your MANUS agent with the webhook action:

```json
{
  "action": "http_post",
  "url": "https://maplebridge.io/api/v1/webhook/manus",
  "body": {
    "demand": "{{buyer_requirement}}",
    "contact_email": "{{buyer_email}}",
    "source": "manus"
  }
}
```

---

## Demand Writing Tips

For best matching results:

| Do | Don't |
|----|-------|
| Include quantity/MOQ | Just say "bulk" |
| Mention certifications (CE, FCC, FDA) | Omit compliance requirements |
| State the destination market | Leave market unspecified |
| Include budget range | Leave budget blank |
| Describe key specs | Use only product name |

**Good example:**
> "500 units stainless steel water bottles for Canadian retail, BPA-free, 500ml, leak-proof lid, custom logo printing, budget $8-12 per unit, need samples within 3 weeks"

**Poor example:**
> "water bottles"

---

## Idempotency

The webhook does not enforce idempotency. Submitting the same demand text twice will create two separate intents. If you need idempotency, include a unique `source` identifier and deduplicate on your end before calling the webhook.

---

## Notifications

When matches are found:
1. The buyer receives an email summary of matched suppliers (if `contact_email` provided)
2. Matched suppliers receive the anonymized buyer demand summary
3. Both parties can connect directly once match is confirmed

Notification timing: typically within 60 seconds of webhook submission.
