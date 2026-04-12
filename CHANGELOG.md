# Changelog

All notable public-facing changes to this repository should be recorded here.

This changelog covers the open contract layer only. It does not describe changes to the private MapleBridge production app.

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
