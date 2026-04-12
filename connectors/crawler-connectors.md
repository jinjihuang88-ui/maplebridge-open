# Crawler Connector Abstraction

The public connector layer explains how ingestion sources should normalize into the matching workflow.

## Connector Topology

MapleBridge Open treats crawler ingestion as a layered system, not a single crawler process.

At the public boundary, that means:

- one or more source-facing crawler workers can run independently
- crawler workers can specialize by market or role
- a demand-oriented workflow can stay separate from a broader SME discovery workflow
- all crawler outputs still normalize into the same matching layer

This keeps the public contract stable even when production crawler topology changes.

## Connector Contract

Input:

- source
- connector kind
- fetch context
- raw payload

Output:

- normalized company record
- normalized role hint
- contact hints
- provenance
- freshness
- extraction confidence

## Search Connector Model

The public connector model assumes:

- a primary search connector
- an optional fallback search connector
- filtering before normalization
- normalization before match scoring

In other words, the public boundary supports a pattern like:

1. query a preferred search source
2. fall back to a secondary source if coverage is weak
3. filter out low-value or non-commercial domains
4. normalize surviving records into the shared matching workflow

The exact providers, query templates, rate limits, and block-handling rules remain private.

## Normalization Expectations

A crawler connector should be able to emit enough structured hints for downstream review:

- probable role: buyer or supplier
- probable company identity
- probable contact surface
- product or category hints
- provenance and extraction confidence

The public layer documents these expectations, not the production heuristics used to derive them.

## Why This Stays Abstract

The abstraction can be public.

The following stay private:

- production crawler topology details
- production source lists
- seed queries
- crawl cadence
- fallback-provider tuning
- domain allow/block rules
- anti-blocking strategies
- spam filtering logic
