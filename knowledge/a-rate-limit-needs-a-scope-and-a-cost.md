---
id: a-rate-limit-needs-a-scope-and-a-cost
title: A rate limit needs a scope and a cost
tags: design, rate-limit, abuse
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/api-rate-limit-bypass.md
status: active
---
# A rate limit needs a scope and a cost

## Claim

A limit per IP breaks behind a proxy and a limit per user misses anonymous paths. The unit must match the cost.

## Test

Send the same action from many IPs and from one user. Compare the counters. Check the proxy header trust.

## Proof

A bypass that changes the counter scope.

## Failure modes

A distributed limiter can be correct. A cached response lowers the cost.
