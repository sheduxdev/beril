---
id: rpki-invalid-and-unknown-are-not-the-same
title: RPKI invalid and unknown are not the same
tags: network, rpki, roa
confidence: high
updated: 2026-11-26
uses: 0
sources: references/network-checklist.md
status: active
---
# RPKI invalid and unknown are not the same

## Claim

Invalid means a ROA exists and the announcement breaks it. Unknown means no ROA. Only invalid is a clear signal.

## Test

Query the ROA state for the prefix and origin. Repeat from a second validator. Record the state per update.

## Proof

An invalid state with a matching ROA.

## Failure modes

A missing validator or a local override hides it. Unknown prefixes are common and not proof.
