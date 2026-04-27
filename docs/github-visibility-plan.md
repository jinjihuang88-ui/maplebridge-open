# GitHub Visibility Plan

This document keeps MapleBridge Open promotion focused on useful developer and sourcing context. The goal is to make the repository easier to understand, cite, and contribute to without using spammy outreach.

## Current Public Entry Points

- Repository: https://github.com/jinjihuang88-ui/maplebridge-open
- Website: https://maplebridge.io
- Open docs: https://maplebridge.io/open/
- Release: https://github.com/jinjihuang88-ui/maplebridge-open/releases/tag/v0.1.1

## Why People Are Not Seeing It Yet

The repository is still new and has limited external signals. GitHub discovery usually needs a mix of clear positioning, practical examples, topics, releases, small issues, and outside references.

The strongest visibility improvements are:

- Keep the README specific to one problem: AI-assisted China sourcing for North American buyers.
- Show a demo in one command so developers can understand the workflow quickly.
- Use searchable topics such as `china-sourcing`, `supplier-matching`, `procurement-ai`, and `supply-chain-ai`.
- Keep releases active so GitHub and external crawlers see fresh updates.
- Create small contribution tasks that are easy for outsiders to understand.
- Link the repository from relevant, non-spam external posts only when the context fits.

## Issue Body Fixes

If GitHub issue editing is available, replace template issue bodies with the following more useful briefs.

### Issue 11: Buyer Intent Example

```markdown
## What should be improved?

Add one buyer intent example for a real sourcing category, such as packaging, drinkware, electronics accessories, pet products, apparel, or home goods.

## Suggested area

- [x] Buyer intent example
- [ ] Supplier capability example
- [ ] Match explanation
- [ ] Connector boundary
- [ ] Documentation wording
- [ ] Other

## Why it helps

Concrete buyer intent examples make the public contract easier to understand. They show how MapleBridge Open represents category, target market, MOQ, compliance needs, delivery constraints, and review state before supplier search begins.

## Public boundary check

- [x] This does not require production MapleBridge code.
- [x] This does not include customer, buyer, or supplier private data.
- [x] This does not expose private crawler, ranking, or credential details.
```

### Issue 12: Supplier Capability Examples

```markdown
## What should be improved?

Add one or two supplier capability examples that show realistic Chinese manufacturer profiles, especially OEM, ODM, private label, or low-MOQ supply cases.

## Suggested area

- [ ] Buyer intent example
- [x] Supplier capability example
- [ ] Match explanation
- [ ] Connector boundary
- [ ] Documentation wording
- [ ] Other

## Why it helps

Supplier examples make the matching contract more practical. They help readers understand how MapleBridge Open represents MOQ, compliance, export market fit, channel support, and review state without exposing real supplier records.

## Public boundary check

- [x] This does not require production MapleBridge code.
- [x] This does not include customer, buyer, or supplier private data.
- [x] This does not expose private crawler, ranking, or credential details.
```

## Outreach Sequence

Use this order to avoid duplicate or platform-risky promotion:

1. GitHub release note: already published as a concrete project update.
2. LinkedIn founder note: explain the sourcing-brief problem and link once.
3. Product Hunt update: share only as a product update, not a repeated launch.
4. Quora answers: answer specific sourcing questions first; link only when the repository is directly useful.
5. Reddit replies: avoid top-level promotion unless the subreddit allows show-and-tell posts.
6. GitHub Discussions or issues: ask for schema feedback, not generic stars.

## Short Human-Sounding Share Copy

```text
I opened the public contract layer behind MapleBridge.

It is not the production marketplace code. It is a small protocol/demo repo that shows how we structure buyer intent, supplier capability, MOQ/compliance fit, and human review handoff for China sourcing.

Useful if you are building around procurement, B2B marketplaces, sourcing workflows, or AI agents.

https://github.com/jinjihuang88-ui/maplebridge-open
```

## Weekly Maintenance

- Add or improve one realistic example.
- Check whether issues have clear, non-template descriptions.
- Answer one relevant sourcing or procurement question without forcing a link.
- Publish a release only when there is a real change.
- Keep `llms.txt`, README, and website open docs aligned.
