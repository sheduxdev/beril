---
id: a-catch-all-address-hides-user-enumeration
title: A catch all address hides user enumeration
tags: mail, catch-all, enumeration
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/email-user-enum.md
status: active
---
# A catch all address hides user enumeration

## Claim

A catch all accepts every local part, so a valid and an invalid address look the same at RCPT time.

## Test

Send RCPT for a random local part and a likely real one. Compare the code and the later bounce.

## Proof

Both are accepted at RCPT.

## Failure modes

A later bounce reveals the invalid one. A per user rate limit hides it.
