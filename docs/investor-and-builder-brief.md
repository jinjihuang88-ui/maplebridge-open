# Investor and Builder Brief

MapleBridge Open is the public protocol layer behind MapleBridge's AI-assisted China sourcing workflow.

The repository exists to make one thesis inspectable:

> B2B sourcing should not start with supplier search. It should start with a structured sourcing brief, then match buyer intent against supplier capability with explainable review logic.

## The Problem

Most small and mid-sized buyers do not begin with a clean RFQ. They usually start with something closer to:

> Need FCC-certified Bluetooth earbuds for Amazon US FBA, custom packaging, around 500 units, production in 6 weeks.

That is not yet supplier-ready. It is missing fields, risk checks, compliance detail, packaging assumptions, channel constraints, and review decisions.

Traditional sourcing platforms often push the buyer toward search results, supplier directory listings, or quote forms before the requirement is structured enough. That creates weak supplier responses, hard-to-compare quotes, and repeated back-and-forth.

## The MapleBridge Thesis

MapleBridge treats the sourcing brief as the first product surface.

The workflow is:

1. Normalize buyer demand into structured buyer intent.
2. Normalize supplier capability into comparable supplier fit signals.
3. Match both sides across product category, MOQ, compliance, packaging, export market, communication, and review risk.
4. Send uncertain or high-risk cases to human review before introduction.

This is why the project uses an A2A framing. The buyer side and supplier side do not expose the same information. They need separate agents and a shared match layer.

## Why This Repository Is Open

The live MapleBridge product remains private. This repository publishes only the public contract surface:

- buyer intent schema
- supplier capability shape
- matching dimensions
- review handoff states
- connector boundaries
- notification events
- local demo data

It does not expose:

- production app code
- real buyer or supplier data
- private crawler sources
- ranking thresholds
- credentials
- operational prompts

## Why Builders May Care

This repo is useful if you are building around:

- AI procurement agents
- B2B marketplace matching
- supplier discovery workflows
- RFQ normalization
- small-MOQ sourcing
- explainable matching systems
- human-in-the-loop review layers

The reusable part is not a database of suppliers. It is the workflow contract: how messy demand becomes structured intent, how supplier capability becomes comparable, and how a match explanation can be audited.

## Why Investors May Care

MapleBridge is not trying to become another broad supplier directory.

The wedge is narrower:

- North America buyers sourcing from China
- small and mid-sized orders
- unclear or incomplete sourcing briefs
- supplier matching before directory browsing
- bilingual buyer/supplier workflow
- human review where AI confidence is low

The open repository makes the product thesis legible without exposing production assets. It shows how the company thinks about the system boundary, not just the marketing page.

## What To Inspect First

- `README.md` for the public workflow overview.
- `schemas/intent.schema.json` for the normalized intent contract.
- `protocols/agent-protocol.md` for buyer-agent and supplier-agent handoff.
- `frameworks/match-engine.md` for matching dimensions.
- `demo/run-local-match.js` for a local workflow example.
- `docs/why-a2a.md` for the A2A reasoning.

## Current Stage

MapleBridge Open is an interface-first public scaffold. The goal is not to publish a full marketplace. The goal is to make the agent-to-agent sourcing workflow inspectable, citable, and easier for partners to reason about.

Useful links:

- Live product: https://maplebridge.io
- Open docs: https://maplebridge.io/open/
- App: https://maplebridge.io/app
- Public signals: https://maplebridge.io/maplebridge-external-signals
