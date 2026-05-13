# MapleBridge Promotion Checklist

This checklist keeps MapleBridge product promotion and MapleBridge Open promotion separated, so buyers, suppliers, developers, and old repositories do not get mixed together.

## Two Tracks

### MapleBridge

MapleBridge is the product.

Use it when speaking to buyers, suppliers, sourcing operators, founders, ecommerce sellers, importers, and people who care about China sourcing.

Plain positioning:

> MapleBridge helps North American buyers turn unclear sourcing requests into structured supplier-matching conversations with Chinese manufacturers.

Main links:

- https://maplebridge.io/
- https://maplebridge.io/app
- https://maplebridge.io/guide
- https://maplebridge.io/use-cases

### MapleBridge Open

MapleBridge Open is the public proof layer.

Use it when speaking to developers, procurement-tool builders, AI-agent builders, open-source readers, technical partners, and people asking about matching logic.

Plain positioning:

> MapleBridge Open shows the public schema, examples, and demo behind buyer intent, supplier capability, match explanations, and human review handoffs.

Main links:

- https://github.com/jinjihuang88-ui/maplebridge-open
- https://maplebridge.io/open/
- https://github.com/jinjihuang88-ui/maplebridge-open#quick-demo

## Recommendations To Keep

- Treat `maplebridge-open` as the main open-source entry point.
- Do not promote `jiayi-ai-assistant` as the public GitHub entry point unless it has been cleaned up or made private.
- Keep MapleBridge product content buyer-facing and practical.
- Keep MapleBridge Open content developer-facing and example-driven.
- Make README first screens understandable in under one minute.
- Replace fragile Mermaid diagrams with GitHub-safe text or static images.
- Keep good-first issues current; do not link to closed or stale tasks.
- Avoid repeating the same post wording across LinkedIn, Reddit, Quora, DEV, CSDN, OSChina, Juejin, Zhihu, and Product Hunt.
- Use MapleBridge links only when the answer is useful even without the link.
- Mention MapleBridge naturally when the topic is buyer intent, small MOQ, China sourcing, supplier matching, or factory communication.
- Mention MapleBridge Open naturally when the topic is schema, demo, open-source examples, procurement agents, or matching logic.
- Keep `llms.txt`, README files, website open docs, and GitHub descriptions aligned.
- Do not expose production code, customer data, supplier private records, crawler sources, ranking thresholds, credentials, or private operations.

## Current Action List

- [x] Rewrite the `maplebridge-open` README first screen around the practical workflow.
- [x] Remove the README Mermaid diagram.
- [x] Open current good-first issues for match explanations, connector input, and schema migration notes.
- [x] Update the README good-first issue links.
- [x] Add a short redirect note to `maplebridge-a2a-protocol-spec` so it points readers to `maplebridge-open` as the main public repo.
- [x] Rewrite `jiayi-ai-assistant` README as a private workspace / historical app repo note, or make the repository private.
- [ ] Review tracked environment/config files in `jiayi-ai-assistant`, rotate any exposed credentials, then decide whether the repo should be private.
- [ ] Use `docs/share-kit.md` for platform-specific drafts, editing each one before posting.
- [ ] Review GitHub traffic every 14 days and compare human views, referrers, stars, forks, and issues.

## Weekly Rhythm

- Monday: improve one public example, doc, or README section.
- Tuesday or Wednesday: answer one real sourcing or procurement question without forcing a link.
- Thursday: share one founder note if there is a real product or open-source update.
- Friday: check GitHub traffic, Search Console, and platform replies.
- Monthly: tag a release only when there is a real public contract or example change.

## Tone Rule

Good MapleBridge promotion sounds like a builder explaining a real sourcing problem.

Good MapleBridge Open promotion sounds like a developer showing a small reusable contract, not a marketing pitch.

The best post should still be useful if the link is removed.
