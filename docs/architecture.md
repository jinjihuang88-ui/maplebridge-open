# MapleBridge Open Architecture

MapleBridge Open documents the public contract layer for AI-assisted bilateral B2B matching. The live marketplace and production app stay outside this repository.

```mermaid
flowchart TB
  subgraph Demand["Buyer side"]
    Brief["Raw sourcing brief"]
    BuyerIntent["BuyerIntent schema"]
  end

  subgraph Supply["Supplier side"]
    Capability["Supplier capability statement"]
    SupplierIntent["SupplierIntent schema"]
  end

  subgraph PublicLayer["Public open layer"]
    Protocol["Agent protocol"]
    Engine["Match engine framework"]
    Explanation["Match explanation"]
    Events["Notification interface"]
  end

  subgraph PrivateRuntime["Private MapleBridge runtime"]
    Review["Human review"]
    App["Production /app"]
    Data["Private buyer and supplier records"]
  end

  Brief --> BuyerIntent
  Capability --> SupplierIntent
  BuyerIntent --> Protocol
  SupplierIntent --> Protocol
  Protocol --> Engine
  Engine --> Explanation
  Explanation --> Events
  Events --> Review
  Review --> App
  App --> Data
```

## Public

- Intent shapes
- Agent handoff events
- Match dimensions
- Explanation fields
- Connector and notification boundaries
- Sample payloads and local demo data

## Private

- Production application code
- Live buyer and supplier records
- Production ranking weights
- Crawler seeds and source lists
- Credentials, prompts, and anti-abuse rules

## Canonical Web Pages

- Overview: https://maplebridge.io/open/
- Intent schema: https://maplebridge.io/open/intent-schema
- Agent protocol: https://maplebridge.io/open/agent-protocol
- Match engine: https://maplebridge.io/open/match-engine
- Sample payloads: https://maplebridge.io/open/sample-payloads
