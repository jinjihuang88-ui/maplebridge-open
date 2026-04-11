# MapleBridge Open

**Public protocol and framework layer for AI-assisted bilateral B2B matching.**

**A2A-ready buyer-agent + seller-agent contracts for sourcing and matching workflows.**

MapleBridge Open defines the reusable contract surface behind a workflow where:

- a **buyer agent** normalizes demand
- a **seller agent** normalizes supply
- a shared **match engine** scores bilateral fit
- **connector** layers ingest external signals
- **notification** events trigger introductions, reminders, and review handoffs

In this repository, `A2A` means an agent-to-agent workflow where specialized buyer-side and seller-side agents exchange normalized state through a shared matching and review layer.

This repository is intentionally separate from the live MapleBridge production app at [https://maplebridge.io/app](https://maplebridge.io/app).

Canonical public pages:

- Overview: [https://maplebridge.io/open/](https://maplebridge.io/open/)
- Intent Schema: [https://maplebridge.io/open/intent-schema](https://maplebridge.io/open/intent-schema)
- Agent Protocol: [https://maplebridge.io/open/agent-protocol](https://maplebridge.io/open/agent-protocol)
- Match Engine: [https://maplebridge.io/open/match-engine](https://maplebridge.io/open/match-engine)
- Crawler Connectors: [https://maplebridge.io/open/crawler-connectors](https://maplebridge.io/open/crawler-connectors)
- Notification Interface: [https://maplebridge.io/open/notification-interface](https://maplebridge.io/open/notification-interface)
- Local Demo UI Boundary: [https://maplebridge.io/open/local-demo-ui](https://maplebridge.io/open/local-demo-ui)
- Why A2A: [https://maplebridge.io/open/why-a2a](https://maplebridge.io/open/why-a2a)

## Why This Exists

Most B2B sourcing systems publish either:

- a supplier directory
- a lead capture form
- a CRM workflow

MapleBridge Open focuses on a different layer:

**bilateral matching infrastructure**

That means publishing the public contracts for:

1. how buyer demand should be normalized
2. how supplier capability should be normalized
3. how both sides should flow into a shared scoring engine
4. where review, trust, and notifications should sit in the system

## What This Repository Contains

- `schemas/`
  Public intent schema and example JSON for buyer and supplier normalization.
- `protocols/`
  Buyer-agent and seller-agent handoff contract.
- `frameworks/`
  Public match scoring dimensions and explainability boundary.
- `connectors/`
  Public ingestion abstraction for crawler, webhook, and dataset connectors.
- `notifications/`
  Public event contract for reminders, introductions, and review hooks.
- `demo/`
  Reference boundary for a local demo UI.
- `docs/`
  Positioning, security boundary, launch, and repository metadata notes.

## What This Repository Does Not Contain

This is not a public copy of the live marketplace.

It does **not** include:

- the production MapleBridge `/app` implementation
- production FastAPI routes
- production Streamlit UI
- production databases
- real buyer or supplier data
- real match thresholds or ranking weights
- production crawler seeds or source lists
- outbound notification credentials
- private prompt and anti-abuse logic

## Repository Structure

```text
maplebridge-open/
|- schemas/
|- protocols/
|- frameworks/
|- connectors/
|- notifications/
|- demo/
`- docs/
```

## Public vs Private Boundary

**Public**

- schema shapes
- protocol contracts
- scoring dimensions
- notification event names
- demo UI boundaries
- integration-facing documentation

**Private**

- live marketplace logic
- live customer data
- production orchestration
- trust heuristics
- real crawler operations
- production follow-up flows

See:

- [docs/positioning.md](docs/positioning.md)
- [docs/why-a2a.md](docs/why-a2a.md)
- [docs/security-boundary.md](docs/security-boundary.md)
- [docs/github-metadata.md](docs/github-metadata.md)

## Recommended First Read

- [schemas/intent-schema.md](schemas/intent-schema.md)
- [protocols/agent-protocol.md](protocols/agent-protocol.md)
- [frameworks/match-engine.md](frameworks/match-engine.md)

## Status

This repository is currently an **interface-first public scaffold** with an Apache-2.0 license.

Suggested launch copy and positioning notes are in:

- [docs/github-metadata.md](docs/github-metadata.md)
- [docs/license-status.md](docs/license-status.md)

## Production Relationship

The live MapleBridge website and application remain separate:

- website: [https://maplebridge.io](https://maplebridge.io)
- production app: [https://maplebridge.io/app](https://maplebridge.io/app)

This repository should stay outside the production runtime boundary.
