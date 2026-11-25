---
id: a-retest-needs-the-original-request-and-a-new-result
title: A retest needs the original request and a new result
tags: consulting, retest, fix
confidence: high
updated: 2026-11-26
uses: 0
sources: docs/defending.md, references/senior-bar.md
status: active
---
# A retest needs the original request and a new result

## Claim

A fix is verified by replaying the original request and two variants, not by reading the patch alone.

## Test

Run the original, a variant and a bypass. Check the regression test. Record the new response.

## Proof

The original fails and the regression test passes.

## Failure modes

A fix that only blocks the string passes the first and fails the variant. A WAF rule is not a code fix.
