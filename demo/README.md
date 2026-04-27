# Local Demo

This demo makes the public matching workflow concrete without calling MapleBridge production systems.

## Run

```bash
npm run demo
```

## What It Does

- loads sample buyer and supplier intents from `examples/sample-payloads.json`
- compares category, MOQ, compliance, and market/channel fit
- prints the best match and human-readable explanation

## Out of Scope

- production `/app`
- production auth
- production database writes
- live crawler sources
- outbound notifications
