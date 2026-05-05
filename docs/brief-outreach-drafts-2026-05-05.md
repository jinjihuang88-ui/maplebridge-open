# Brief Outreach Drafts - 2026-05-05

Use these drafts to reference the new investor and builder brief without repeating the earlier MapleBridge Open launch copy.

## LinkedIn Founder Post

I added a short investor/builder brief for MapleBridge Open.

The point is not "we open sourced a repo." The point is the product thesis:

Most B2B sourcing tools still begin with supplier search.

But in real sourcing, the first problem is usually not the supplier list. It is the buyer brief.

A buyer may say:

"Need FCC-certified Bluetooth earbuds for Amazon US FBA, custom packaging, around 500 units, production in 6 weeks."

That sounds specific, but it is still missing important information: exact compliance coverage, packaging files, sample vs production MOQ, carton details, inspection preference, timeline risk, and what should be reviewed before any supplier introduction.

This is why I think agent-to-agent workflows are useful in B2B sourcing.

One agent should structure buyer intent.
Another should structure supplier capability.
A match layer should compare category, MOQ, compliance, export-market fit, packaging, and review risk.
And a human should still review uncertain or high-risk cases.

I wrote the brief here:
https://github.com/jinjihuang88-ui/maplebridge-open/blob/main/docs/investor-and-builder-brief.md

## Medium Article Draft

Title:

Why AI Sourcing Should Start With the Brief, Not the Supplier List

Subtitle:

A short note on why I am building MapleBridge around buyer intent, supplier capability, and human-reviewed matching.

Body:

Most sourcing software still starts from the same place: search.

Search for factories. Search for suppliers. Search for quotes. Search through profiles.

That makes sense if the buyer already knows exactly what they need. But many buyers do not start with a clean RFQ. They start with an incomplete message.

For example:

"Need FCC-certified Bluetooth earbuds for Amazon US FBA, custom packaging, around 500 units, production in 6 weeks."

At first glance, that sounds specific. But a sourcing operator would still slow down and ask several questions:

- Is 500 units a sample order, trial order, or production order?
- Does FCC apply to the exact SKU and wireless module, or only to a similar product?
- Are packaging dielines ready?
- Is the buyer shipping to Amazon FBA, a 3PL, or their own warehouse?
- Are carton dimensions, labeling, and inspection requirements known?
- Is this OEM, ODM, or private label?

Until those questions are answered, supplier search is premature.

This is the reason I am building MapleBridge around the sourcing brief first.

My view is that B2B sourcing needs several layers:

1. A buyer-side agent that turns messy demand into structured buyer intent.
2. A supplier-side agent that turns factory capability into comparable supplier signals.
3. A matching layer that compares category, MOQ, compliance, packaging, export-market fit, and communication fit.
4. A human review layer for cases where the AI is not confident or the risk is high.

That is the product thesis behind MapleBridge Open.

The open repo is not the production marketplace code. It is the public contract surface: schemas, example payloads, matching dimensions, connector boundaries, and review handoff states.

I added a short investor and builder brief here:

https://github.com/jinjihuang88-ui/maplebridge-open/blob/main/docs/investor-and-builder-brief.md

If you are building in procurement, B2B marketplaces, sourcing workflows, or agent-to-agent systems, the reusable idea is not a supplier database.

The reusable idea is the workflow boundary:

messy buyer demand -> structured intent -> comparable supplier capability -> explainable match -> human review when needed.

That is the part I think matters.

## GitHub Discussion Prompt

Title:

How should AI sourcing systems separate buyer intent from supplier capability?

Body:

I added a short investor/builder brief for MapleBridge Open:

https://github.com/jinjihuang88-ui/maplebridge-open/blob/main/docs/investor-and-builder-brief.md

The core assumption is that B2B sourcing should not start with supplier search. It should start with a structured sourcing brief, then compare buyer intent against supplier capability.

Open question for builders:

When modeling sourcing workflows, would you keep buyer intent and supplier capability as two separate agent states, or collapse both into one marketplace/CRM record?

My current view is that they should stay separate because the two sides expose different information:

- buyer side: category, target market, MOQ, compliance needs, packaging, timeline, review risk
- supplier side: capability, export readiness, MOQ support, certifications, channels, category fit, responsiveness

Would be useful to hear from anyone building procurement, B2B marketplace, or agent workflow systems.

## Short Reply Variant

One pattern I am testing is to separate supplier search from brief normalization.

Before comparing factories, the system should structure category, target market, MOQ, compliance, packaging, timeline, and review risk. Only then does matching supplier capability make sense.

I wrote a short brief on the workflow boundary here:
https://github.com/jinjihuang88-ui/maplebridge-open/blob/main/docs/investor-and-builder-brief.md

## Use Rules

- Do not post all drafts on the same day.
- Do not paste the same wording across platforms.
- Do not post in unrelated AI or startup threads.
- Use the LinkedIn post first.
- Use the Medium article only if there is time to publish it cleanly.
- Use the GitHub discussion prompt only if discussions are active and it will not duplicate release notes.
