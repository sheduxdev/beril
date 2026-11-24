---
id: process-retest
title: A fix is not a fix until the same request fails
tags: process, retest, regression
confidence: high
updated: 2026-11-24
uses: 0
sources: docs/break-my-app.md
status: active
---
# A fix is not a fix until the same request fails

## Claim

The vendor reports a patch. The original request may still work on another path or version.

## Test

Replay the exact request. Test the sibling path and the old version. Record the response and the date.

## Proof

The original proof now fails for the right reason.

## Failure modes

A 200 with an error body is not a fix. A WAF block is not a code fix.
