# Security Boundary

This repository is intended to stay outside the live MapleBridge production boundary.

## Public

- intent shapes
- event names
- interface contracts
- example JSON
- explanation of fit dimensions
- demo UI boundary

## Private

- production `/app`
- production API
- production DB schema with live records
- real buyer and supplier data
- hidden ranking thresholds
- source acquisition heuristics
- anti-abuse logic
- email and notification credentials

## Rule

Nothing in this repository should require access to:

- the production database
- the production email system
- live crawler jobs
- production sessions

This is the core rule that keeps GitHub publication from affecting the current marketplace.
