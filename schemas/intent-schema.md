# Intent Schema

The public intent schema defines a shared structure for buyer demand and supplier supply.

## Core Objects

- `BuyerIntent`
- `SupplierIntent`
- `FitConstraint`
- `ReviewState`

## Public Fields

- intent id
- role
- language
- product category
- summary
- country
- moq
- compliance
- channels
- fit constraints
- confidence
- review state

## Design Goal

The schema should be stable across:

- multiple agents
- multiple connectors
- local demos
- partner integrations

It should not expose private enrichment or live customer identifiers.
