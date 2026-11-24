---
id: api-rate-limit-bypass
title: Rate limits are only as strong as the key
tags: api, rate-limit, bypass
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Rate limits are only as strong as the key

## Claim

The limiter keys on IP, header or route, and the attacker can change that key or hit an unlisted sibling route.

## Test

Identify the key. Rotate IP, user agent, account and path case. Test a trailing slash, version prefix and a batched body.

## Proof

More requests than the policy allows with the same account.

## Failure modes

A limit that is intentionally per-IP is not a bug. Distributed sources change the test.
