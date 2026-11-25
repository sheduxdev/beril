---
id: origin-ip-scoring-needs-a-direct-response-check
title: Origin IP scoring needs a direct-response check
tags: recon, cdn, origin
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/artex-flask.md
status: active
---
# Origin IP scoring needs a direct-response check

## Claim

MX hosts, IP disclosure headers, certificate transparency and subdomain A records can expose an origin behind a CDN. Rank by method reliability, then prove the address answers with the right Host header.

## Test

Collect candidates, drop private and CDN ranges, check an open web port, then send a request to the IP with Host set to the target. Compare the body and certificate with the edge.

## Proof

The IP serves the same application with the target Host header and is not in a CDN range.

## Failure modes

Shared hosting returns a neighbour site. A second CDN node looks like an origin. The apex address leaks into its own candidate set.
