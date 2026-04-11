# Partner Integration Guide

This guide explains how partners should approach MapleBridge Open without relying on MapleBridge production systems.

## What partners can build against

Partners should treat MapleBridge Open as a public contract layer for:

- buyer intent normalization
- seller capability normalization
- bilateral matching explanations
- connector abstraction boundaries
- notification triggers

## Recommended integration path

1. Start with `schemas/intent.schema.json`.
2. Read `protocols/agent-protocol.md`.
3. Read `frameworks/match-engine.md`.
4. Use `connectors/crawler-connectors.md` only as an abstraction reference.
5. Keep your own credentials, data sources, prompts, and thresholds private.

## Suggested partner architecture

- one buyer-side adapter
- one seller-side adapter
- one normalization layer
- one local matching layer
- one notification layer

MapleBridge Open is designed to describe boundaries, not to replace a partner's production controls.

## Boundary rules

Partners should not expect:

- MapleBridge production data access
- MapleBridge production matching scores
- MapleBridge production email systems
- MapleBridge private enrichment pipelines
- MapleBridge internal sourcing heuristics

## Good first integration targets

- intake form normalization
- supplier profile normalization
- explainable match summaries
- partner-side notification triggers

## When to use Discussions

Use GitHub Discussions for:

- contract interpretation questions
- partner integration questions
- schema extension ideas
- example payload requests

Do not use Discussions for:

- production support for `maplebridge.io/app`
- private data requests
- private threshold questions
