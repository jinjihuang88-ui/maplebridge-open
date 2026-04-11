# Crawler Connector Abstraction

The public connector layer explains how ingestion sources should normalize into the matching workflow.

## Connector Contract

Input:

- source
- fetch context
- raw payload

Output:

- normalized company record
- contact hints
- provenance
- freshness
- extraction confidence

## Why This Stays Abstract

The abstraction can be public.

The following stay private:

- production source lists
- seed queries
- crawl cadence
- anti-blocking strategies
- spam filtering logic
