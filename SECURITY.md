# Security Policy

MapleBridge Open is the public contract layer only. It should not include production credentials, private customer data, private supplier records, live crawler sources, ranking thresholds, or production application code.

## Reporting

If you find a security issue in this public repository, open a GitHub issue only if the report does not include sensitive details.

If the issue involves credentials, private data, or a production system, do not post details publicly. Contact MapleBridge through the public website instead:

https://maplebridge.io

## Public Boundary

Allowed in this repository:

- public schemas
- public example payloads
- public protocol documentation
- local demos using synthetic data
- connector interface descriptions

Not allowed in this repository:

- secrets or API keys
- customer, buyer, or supplier private data
- live crawler sources
- production ranking thresholds
- production database or auth logic
