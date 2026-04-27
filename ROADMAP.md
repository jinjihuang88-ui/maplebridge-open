# Roadmap

This repository is intentionally interface-first. The roadmap is organized around what should become public and reusable without crossing the MapleBridge production boundary.

## Phase 1: Public Contract Layer

Status: substantially complete

- [x] publish intent schema for bilateral buyer and supplier normalization
- [x] publish buyer-agent and seller-agent protocol contracts
- [x] publish public match-engine dimensions and explainability notes
- [x] publish notification event interface
- [x] publish a clear A2A positioning note

## Phase 2: Builder-Facing Examples

Status: in progress

- [x] add example buyer intent payloads for multiple sourcing scenarios
- [x] add example seller capability payloads for OEM, ODM, and low-MOQ cases
- [ ] add more end-to-end sample match explanations
- [ ] add connector examples for webhook, CSV, and crawler ingestion
- [x] add a local reference demo flow that never touches production systems

## Phase 3: Open Integration Surface

Status: started

- [x] publish a lightweight integration guide for partner platforms
- [x] document trust and review handoff boundaries
- [x] add versioned contract notes
- [ ] add migration guidance for future schema revisions

## Phase 4: Ecosystem Readiness

Status: planned

- publish follow-up tagged releases with example-driven changes
- maintain changelog entries for public contract changes
- enable repository discussions for builder questions
- collect issue-driven feedback on schema and protocol design

## Explicit Non-Goals

The roadmap does not include:

- opening the production MapleBridge app
- exposing live crawler sources or orchestration rules
- publishing production ranking thresholds
- exposing live customer or partner data
