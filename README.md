# MapleBridge Open

[![Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Live Platform](https://img.shields.io/badge/platform-maplebridge.io-orange.svg)](https://maplebridge.io)
[![Open Docs](https://img.shields.io/badge/docs-open%20docs-green.svg)](https://maplebridge.io/open/)
[![GitHub Stars](https://img.shields.io/github/stars/jinjihuang88-ui/maplebridge-open?style=social)](https://github.com/jinjihuang88-ui/maplebridge-open)

MapleBridge Open is the public protocol layer behind MapleBridge, a sourcing workflow for North American buyers who need a clearer way to find and evaluate Chinese manufacturers.

It is not the production marketplace code. It is the open contract surface: buyer intent, supplier capability, matching signals, connector boundaries, and review handoffs.

## Who This Is For

- Builders working on AI agents for sourcing, procurement, B2B marketplaces, or supplier discovery.
- Buyers who want to understand how MapleBridge structures a sourcing brief before supplier search starts.
- Suppliers and partners who want a clean integration boundary without access to private production systems.
- Researchers comparing agent-to-agent workflows for bilateral matching.

## What It Shows

Most sourcing tools begin with supplier search. MapleBridge begins with the brief.

This repository shows a public version of that workflow:

1. A buyer agent normalizes the buyer's demand.
2. A supplier agent normalizes supplier capability.
3. A match layer compares category, MOQ, compliance, market fit, and review risk.
4. A human review layer decides whether an introduction should happen.

## Quick Demo

Run the local example without touching MapleBridge production systems:

```bash
npm run demo
```

Expected output:

```text
Buyer intent: Low-MOQ insulated bottle order for Canada
Best supplier: Shenzhen drinkware OEM with FDA/LFGB experience
Match score: 0.91
Why it matched: category fit, MOQ fit, compliance fit, North America export fit
Review state: human_review_recommended
```

## Repository Map

| Path | Purpose |
| --- | --- |
| `schemas/intent.schema.json` | Public JSON Schema for normalized buyer and supplier intents |
| `protocols/agent-protocol.md` | Buyer-agent and seller-agent handoff contract |
| `frameworks/match-engine.md` | Public matching dimensions and explainability boundary |
| `connectors/crawler-connectors.md` | Connector abstraction for external supply and demand signals |
| `notifications/notification-interface.md` | Event model for introductions, reminders, and review handoffs |
| `examples/` | Concrete buyer, supplier, and match examples |
| `demo/run-local-match.js` | Small local demo that makes the workflow visible |
| `docs/promotion-playbook.md` | Non-spam launch and visibility playbook |
| `docs/github-visibility-plan.md` | GitHub discovery, issue cleanup, and outreach sequence |
| `llms.txt` | AI crawler summary for LLM and answer-engine discovery |

## Example Objects

Buyer intent:

```json
{
  "intent_id": "buyer-low-moq-bottle-ca",
  "role": "buyer",
  "language": "en",
  "product_category": "drinkware",
  "summary": "Low-MOQ insulated bottle order for Canada",
  "country": "Canada",
  "moq": { "value": 500, "unit": "units" },
  "compliance": ["BPA-free", "FDA food contact"],
  "fit_constraints": ["custom logo", "retail packaging", "ship to Toronto"],
  "confidence": 0.86,
  "review_state": "needs_review"
}
```

Supplier capability:

```json
{
  "intent_id": "supplier-shenzhen-drinkware-oem",
  "role": "supplier",
  "language": "en",
  "product_category": "drinkware",
  "summary": "Shenzhen drinkware OEM with FDA/LFGB experience",
  "country": "China",
  "moq": { "value": 300, "unit": "units" },
  "compliance": ["BPA-free", "FDA food contact", "LFGB"],
  "channels": ["OEM", "private label", "North America export"],
  "fit_constraints": ["custom logo", "retail packaging"],
  "confidence": 0.9,
  "review_state": "machine_ready"
}
```

## Public Boundary

Open in this repository:

- protocol shape
- schema examples
- matching dimensions
- connector boundary
- review handoff notes
- local demo data

Not open in this repository:

- production application code
- customer data
- live crawler sources
- private ranking thresholds
- production credentials
- private supplier or buyer records

## Useful Links

- Live website: [maplebridge.io](https://maplebridge.io)
- Public open docs: [maplebridge.io/open/](https://maplebridge.io/open/)
- Why A2A matters: [docs/why-a2a.md](docs/why-a2a.md)
- Security boundary: [docs/security-boundary.md](docs/security-boundary.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- GitHub visibility plan: [docs/github-visibility-plan.md](docs/github-visibility-plan.md)

## How To Help

Useful contributions are narrow and practical:

- Add better sample buyer intents for real sourcing categories.
- Add supplier capability examples for OEM, ODM, private label, or low-MOQ cases.
- Improve schema naming and compatibility notes.
- Add connector examples that do not expose production data.
- Improve match explanations so humans can audit why a recommendation happened.

If this is useful, star the repo or open a small issue with the sourcing workflow you want represented.
