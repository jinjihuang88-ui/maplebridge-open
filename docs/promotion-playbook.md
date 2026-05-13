# Promotion Playbook

This playbook keeps MapleBridge and MapleBridge Open promotion useful, specific, and compliant with platform norms. The goal is to earn attention by showing a real sourcing workflow, not by dropping links.

## Positioning

Product version:

> MapleBridge helps North American buyers turn unclear sourcing requests into structured supplier-matching conversations with Chinese manufacturers.

Open-source version:

> MapleBridge Open is a public protocol layer for AI-assisted China sourcing: buyer intent, supplier capability, and match explanations for North American buyers.

Use this when the audience is technical:

> MapleBridge Open makes the contract layer public: normalized buyer intents, supplier capability profiles, match scoring dimensions, and review handoff boundaries.

Use this when the audience is buyers:

> Most sourcing failures start before supplier search. The brief is unclear. MapleBridge helps structure the brief before matching.

## Where To Share

| Platform | Best Format | Link Behavior |
| --- | --- | --- |
| LinkedIn | Founder note with one lesson from building | Link to MapleBridge or MapleBridge Open, not both every time |
| DEV Community | Technical write-up about schema and matching | Link to repo and docs |
| Product Hunt | Product update, not a repeated launch | Link to GitHub as update when the open repo is the update |
| Reddit | Reply only when directly relevant | Avoid top-level promotional posts |
| Quora | Answer sourcing questions with practical advice | Link only if it truly helps |
| GitHub Discussions | Ask for schema feedback | No marketing tone |

Use [share-kit.md](share-kit.md) for short drafts. Edit the wording before posting so each platform gets a natural version.

## LinkedIn Product Draft

I did not start MapleBridge because I wanted to build another sourcing platform.

The starting point was the frustration I kept seeing on both sides. Small buyers had to work through too much supplier information, and good factories often had to depend on rankings, ads, or luck to be discovered.

The real signal is usually already inside the buyer's request: product category, market, MOQ, certification concerns, sample timing, packaging, and the parts that still need a human check.

That is what I am building with MapleBridge: structure the sourcing conversation first, then match buyers and factories from facts instead of platform ranking alone.

https://maplebridge.io

## LinkedIn Open Draft

I opened a small public layer behind MapleBridge.

It is not the production marketplace code. It shows how I think about buyer intent, supplier capability, match explanations, and human review before introductions happen.

The hard part in sourcing is often not "find more suppliers." It is turning a messy buying request into something both sides can actually work with.

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
