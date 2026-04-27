# Changelog

All notable public-facing changes to this repository should be recorded here.

This changelog covers the open contract layer only. It does not describe changes to the private MapleBridge production app.

## Unreleased

### Added

- local matching demo under `demo/run-local-match.js`
- readable buyer intent, supplier capability, and match explanation examples
- platform-safe promotion playbook for GitHub and external visibility
- share kit for LinkedIn, Product Hunt, Reddit, Quora, and GitHub directory copy
- pull request template and security policy for clearer public contribution boundaries

### Changed

- reworked README around audience, quick demo, public boundary, and contribution paths
- replaced mojibake example text with English examples for better reader and AI crawler comprehension
- strengthened README, `llms.txt`, and package metadata around China sourcing, small-MOQ, OEM/ODM, and supplier matching discovery terms

## 2026-04-11

### Added

- initial public repository positioning for MapleBridge Open
- intent schema documentation and JSON schema
- buyer-agent and seller-agent protocol documentation
- public match-engine framework notes
- crawler connector abstraction notes
- notification interface notes
- local demo UI boundary notes
- A2A positioning note
- Apache-2.0 license
- roadmap and contribution guidance

### Changed

- clarified that crawler ingestion can run as multiple specialized workers instead of a single crawler path
- clarified the public search-connector model as primary search plus optional fallback search
- clarified that filtering and normalization boundaries are public, while concrete query strategies and provider tuning remain private
