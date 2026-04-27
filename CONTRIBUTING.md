# Contributing

MapleBridge Open accepts contributions to the public contract layer.

## Good Contribution Targets

- schema clarity
- protocol naming and field consistency
- documentation fixes
- example payload improvements
- explainability and integration notes

## Good First Contributions

Good first contributions should be small enough to review quickly:

- one buyer intent example for a real category
- one supplier capability example for OEM, ODM, private label, or low-MOQ supply
- one match explanation that makes a scoring decision easier to audit
- one wording improvement that makes the public/private boundary clearer

Useful categories include packaging, drinkware, pet products, apparel, home goods, electronics accessories, and ecommerce-ready private label products.

## Out of Scope

Do not propose changes that require:

- access to the private MapleBridge production app
- production data
- production crawler operations
- private ranking thresholds
- live notification credentials

## Contribution Rules

1. Keep changes inside the open contract boundary.
2. Prefer documentation and example-first pull requests.
3. Explain whether a proposed change affects schema compatibility.
4. Do not include secrets, customer data, or production-only logic.

## Before Opening a Pull Request

- read [README.md](README.md)
- read [docs/security-boundary.md](docs/security-boundary.md)
- check [ROADMAP.md](ROADMAP.md) for current priorities
- run `npm run demo`
- run `npm run check:json`
- add a changelog note if the public interface changed

## Issue Guidance

Use issues for:

- schema questions
- protocol gaps
- match-engine explainability suggestions
- connector interface requests

Use discussions, when enabled, for:

- design questions
- ecosystem ideas
- integration concepts
