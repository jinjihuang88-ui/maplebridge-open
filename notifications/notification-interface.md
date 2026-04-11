# Notification Interface

The public notification layer defines event names and payload intent for bilateral matching workflows.

## Public Notification Events

- `intro.ready`
- `followup.suggested`
- `review.required`
- `profile.incomplete`

## Public Goal

Allow builders and partners to understand:

- when a notification should be triggered
- what payload shape is expected
- where review hooks fit

## Private Boundary

This repository does not include:

- production provider credentials
- live sequences
- private follow-up timing rules
- production anti-spam guardrails
