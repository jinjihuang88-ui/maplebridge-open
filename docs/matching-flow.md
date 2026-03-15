# How MapleBridge Matching Works

This document explains the conceptual flow of MapleBridge's AI-powered B2B matching system. The core algorithm is proprietary, but this guide describes the approach at an architectural level.

---

## Overview

Traditional B2B sourcing relies on keyword search, trade show contacts, and personal introductions. MapleBridge replaces this with **semantic intent matching**: both buyer requirements and supplier capabilities are represented as structured semantic intents, then matched using LLM-based scoring.

```
Buyer Requirement (natural language)
         ↓
    Intent Parsing
         ↓
  Structured Intent (DEMAND)
         ↓
  Semantic Matching Engine
         ↓
  Ranked Supplier Intents (SUPPLY)
         ↓
    Match Notification
```

---

## Step 1: Intent Parsing

When a buyer submits a requirement like:

> "I need 500 units of bamboo cutting boards for Canadian retail, FSC certified, delivery by Q3"

The LLM parser extracts structured fields:

```json
{
  "product": "bamboo cutting board",
  "quantity": 500,
  "market": "Canada",
  "certifications": ["FSC"],
  "deadline": "Q3",
  "intent_type": "DEMAND",
  "category": "家居家具"
}
```

The parser handles:
- English and Chinese input
- Ambiguous or partial requirements
- Multiple product types in one message
- Budget ranges and quantity ranges

---

## Step 2: Intent Storage

Each parsed intent is stored in the **Intent Graph** — a dual-sided store of buyer demands (DEMAND) and supplier capabilities (SUPPLY).

**DEMAND intents** come from:
- Buyer webhook submissions
- MANUS AI agent integrations
- Web portal form submissions
- Telegram bot conversations

**SUPPLY intents** come from:
- Verified supplier onboarding
- Automated crawler (supplier websites, trade directories)
- Manual supplier registration

---

## Step 3: Semantic Matching

The matching engine compares DEMAND intents against SUPPLY intents using multiple signals:

### Category Alignment
Hard filter: demand category must overlap with supply category. MapleBridge uses a hierarchical category taxonomy (e.g., `消费电子 > 无线耳机`).

### Semantic Similarity
LLM-generated embeddings capture the meaning of `core_need` fields beyond keyword overlap. A buyer asking for "wireless audio accessories" matches a supplier describing "Bluetooth headphones and earbuds" even without exact keyword matches.

### Structural Compatibility
The engine checks compatibility of:
- Quantity vs. Minimum Order Quantity (MOQ)
- Budget vs. unit price range
- Destination market vs. supplier export certifications
- Delivery timeline vs. production lead time

### Scarcity Weighting
Rare supply-demand combinations are weighted higher to surface unique matches that wouldn't appear in commodity searches.

---

## Step 4: Match Scoring

Each potential DEMAND-SUPPLY pair receives a composite score (0.0 – 1.0):

| Component | Weight | Description |
|-----------|--------|-------------|
| Category match | 30% | Exact vs. parent-level category overlap |
| Semantic similarity | 40% | Embedding cosine similarity of `core_need` fields |
| Structural compatibility | 20% | Quantity, budget, timeline fit |
| Supplier quality score | 10% | Verification status, past match success rate |

Pairs with score ≥ 0.7 are surfaced as matches.

---

## Step 5: Notification

Matched pairs trigger notifications:
- **Buyer**: email with supplier summary and contact info
- **Supplier**: email with buyer requirement summary
- **Telegram relay**: optional real-time push to Telegram channel

Match records are stored in the `matched_pairs` table with score, timestamp, and notification status.

---

## Supported Languages

The matching engine handles input in:
- English
- Simplified Chinese (简体中文)
- Traditional Chinese (繁體中文)

Mixed-language input (Chinglish) is also handled gracefully.

---

## Key Design Principles

### No Keyword Lock-in
Buyers do not need to know the right search terms. "I want something to hold my coffee" can match a supplier of ceramic mugs, insulated tumblers, or travel cups depending on context.

### Asymmetric Privacy
Buyer contact information is not exposed to suppliers until a confirmed match. Suppliers see only the anonymized demand summary until both parties indicate interest.

### Continuous Learning
Match outcomes (confirmed deals, rejections) feed back into supplier quality scores over time.

---

## Limitations

- Minimum viable demand description: ~20 words
- Highly specialized industrial products (custom machinery, medical devices) may return fewer matches due to limited supplier coverage in those verticals
- Lead time and certification validation requires manual confirmation for high-value orders

---

## Comparison: Keyword Search vs. Semantic Matching

| Scenario | Keyword Search | MapleBridge Semantic |
|----------|---------------|----------------------|
| "bamboo kitchenware" | Finds exact phrase | Also finds: eco kitchen products, sustainable cookware, FSC wood accessories |
| "礼品批发" | Chinese only | Matches English "gift wholesale" queries |
| "500 units MOQ" | Not searchable | Structural filter applied automatically |
| Partial requirements | No results | Best-effort match with confidence score |
