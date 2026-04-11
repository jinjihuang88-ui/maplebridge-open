# Agent Protocol

This protocol describes how separate buyer and seller agents should cooperate with a shared match engine.

## Lifecycle

1. Capture raw buyer brief or supplier capability statement
2. Normalize into the public intent schema
3. Request clarification if required fields are missing
4. Emit a match-ready bundle
5. Receive ranked candidates and review flags

## Public Events

- `intent.created`
- `intent.clarification_requested`
- `intent.ready_for_match`
- `match.candidate_ranked`
- `match.review_required`

## Non-Goals

This protocol does not define:

- production sessions
- production queues
- production auth
- production database writes
