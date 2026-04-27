# Roadmap

This repository is intentionally interface-first. The roadmap is organized around what should become public and reusable without crossing the MapleBridge production boundary.

## Phase 1: Public Contract Layer

Status: in progress

- publish intent schema for bilateral buyer and supplier normalization
- publish buyer-agent and seller-agent protocol contracts
- publish public match-engine dimensions and explainability notes
- publish notification event interface
- publish a clear A2A positioning note

## Phase 2: Builder-Facing Examples

Status: in progress

- add example buyer intent payloads for multiple sourcing scenarios
- add example seller capability payloads for OEM, ODM, and low-MOQ cases
- add end-to-end sample match explanations
- add connector examples for webhook, CSV, and crawler ingestion
- add a local reference demo flow that never touches production systems

## Phase 3: Open Integration Surface

Status: planned

- publish a lightweight integration guide for partner platforms
- document trust and review handoff boundaries
- add versioned contract notes
- add migration guidance for future schema revisions

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
