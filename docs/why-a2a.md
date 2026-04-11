# Why A2A

MapleBridge Open uses an **A2A-ready** framing because bilateral B2B matching is not a single-agent task.

It is a coordination problem across three layers:

1. a buyer-side agent that normalizes demand
2. a seller-side agent that normalizes supply
3. a shared match and review layer that scores bilateral fit

In this repository, `A2A` means **agent-to-agent workflow**:

- buyer-side and seller-side agents publish different but compatible state
- the match engine evaluates both sides through a shared scoring surface
- notification and review events move the workflow forward when data is missing or confidence is low

## Why This Matters

Most sourcing tools flatten everything into one CRM record, one directory listing, or one lead form.

That misses the real asymmetry:

- buyers expose constraints, specs, timelines, MOQ targets, packaging needs, and compliance gaps
- suppliers expose capability, export readiness, throughput, category fit, trust, and responsiveness

A shared match engine only works well if these two sides are modeled separately first.

## What This Does Not Mean

The A2A framing here does **not** mean:

- the live MapleBridge marketplace is fully autonomous
- the public repository contains production orchestration
- the repository exposes real crawler seeds, private prompts, or production thresholds

This repository publishes interface and workflow boundaries, not the private runtime behind [https://maplebridge.io/app](https://maplebridge.io/app).
