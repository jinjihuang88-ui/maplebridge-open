# Release Process

MapleBridge Open uses lightweight semantic versioning for the public contract layer.

## Scope of a release

A public release can include:

- schema updates
- protocol documentation changes
- match framework clarifications
- connector interface changes
- notification interface changes
- open docs and demo-boundary docs

A public release must not expose:

- `maplebridge.io/app`
- production APIs
- private prompts
- live production data
- private thresholds or internal trust heuristics

## Versioning guidance

- `v0.x.y`: early public contract layer
- minor bump: new docs, new fields, new non-breaking interfaces
- patch bump: clarifications, typo fixes, examples, small corrections

## Release checklist

1. Update `CHANGELOG.md`.
2. Confirm `README.md` links are still correct.
3. Confirm new docs stay inside the public boundary.
4. Create or update a roadmap item if the release changes project direction.
5. Publish the GitHub release with clear release notes.
6. If useful, open or link a Discussions thread for follow-up questions.

## Release note pattern

Keep each release note short and operational:

- what changed
- what was added
- what stays out of scope
- where builders should start reading

## Post-release

After each release:

- update the pinned meta issue if it changes operating priorities
- route ecosystem questions into Discussions
- link the release from external channels only when the release adds meaningful public value
