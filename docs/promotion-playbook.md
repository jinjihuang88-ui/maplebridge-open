# Promotion Playbook

This playbook keeps MapleBridge Open promotion useful, specific, and compliant with platform norms. The goal is to earn attention by showing a real sourcing workflow, not by dropping links.

## Positioning

Short version:

> MapleBridge Open is a public protocol layer for AI-assisted China sourcing: buyer intent, supplier capability, and match explanations for North American buyers.

Use this when the audience is technical:

> We are making the contract layer public: normalized buyer intents, supplier capability profiles, match scoring dimensions, and review handoff boundaries.

Use this when the audience is buyers:

> Most sourcing failures start before supplier search. The brief is unclear. MapleBridge Open shows how we structure the brief before matching.

## Where To Share

| Platform | Best Format | Link Behavior |
| --- | --- | --- |
| LinkedIn | Founder note with one lesson from building | One link at the end |
| DEV Community | Technical write-up about schema and matching | Link to repo and docs |
| Product Hunt | Product update, not a repeated launch | Link to GitHub as update |
| Reddit | Reply only when directly relevant | Avoid top-level promotional posts |
| Quora | Answer sourcing questions with practical advice | Link only if it truly helps |
| GitHub Discussions | Ask for schema feedback | No marketing tone |

Use [share-kit.md](share-kit.md) for short drafts. Edit the wording before posting so each platform gets a natural version.

## LinkedIn Draft

I have been working on MapleBridge from a simple sourcing problem: many North American buyers do not fail because there are no Chinese suppliers. They fail because supplier search starts before the buying brief is clear.

So I opened the protocol layer we use to think about the problem:

- buyer intent
- supplier capability
- MOQ and compliance fit
- match explanation
- human review handoff

The repo is not our production app. It is the public contract layer for builders, buyers, and partners who want to understand the workflow.

GitHub: https://github.com/jinjihuang88-ui/maplebridge-open

## DEV Community Draft

Title: Opening the contract layer behind an AI supplier-matching workflow

I have been building MapleBridge for North American buyers sourcing from China. One thing became clear: supplier discovery is not the first problem. The first problem is normalizing the buyer brief into something a supplier can actually be matched against.

I opened the public contract layer here:

https://github.com/jinjihuang88-ui/maplebridge-open

It includes:

- normalized buyer intent examples
- supplier capability examples
- a public matching explanation boundary
- connector and notification interfaces
- a small local demo that does not touch production systems

I would be interested in feedback from people building procurement tools, B2B marketplaces, or agent workflows.

## Product Hunt Update Draft

Quick update on MapleBridge: I opened the public protocol layer behind the sourcing workflow.

It is not the production marketplace code. It shows the public contract layer: buyer intent, supplier capability, matching dimensions, connector boundaries, and human review handoffs.

Useful if you are building around sourcing, procurement, B2B marketplaces, or AI agents.

GitHub: https://github.com/jinjihuang88-ui/maplebridge-open

## Reddit Rule

Do not create a new promotional post unless the subreddit explicitly allows launches or show-and-tell posts.

Better pattern:

1. Find a specific sourcing question.
2. Answer with practical advice first.
3. Mention MapleBridge only if the repo directly helps explain the workflow.
4. Avoid repeating the same wording across threads.

## Quora Rule

Answer the question directly. A good Quora answer should still be useful if the MapleBridge link is removed.

Use profile credibility first. Link only in one sentence when the answer needs an example.

## Weekly Cadence

- Monday: improve one example or doc page.
- Wednesday: answer one relevant sourcing question without forcing a link.
- Friday: post one build note or product update if there is a real change.
- Monthly: tag a small release and summarize what changed.

## Quality Bar

- Prefer one useful comment over five generic link drops.
- Link to the repo only after giving practical sourcing or implementation advice.
- Use concrete terms people search for: `small MOQ`, `verified Chinese manufacturers`, `Alibaba alternative`, `OEM`, `ODM`, `private label`, `China sourcing`.
- Do not imply MapleBridge has vetted a supplier unless that vetting happened in the production workflow.
