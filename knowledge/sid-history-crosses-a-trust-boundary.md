---
id: sid-history-crosses-a-trust-boundary
title: SID history crosses a trust boundary
tags: ad, trust, sid
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# SID history crosses a trust boundary

## Claim

An account with an extra SID from a trusted domain can carry rights from that domain into the current one.

## Test

Read the SID history on users and groups. Compare with the trusted domain groups. Check token size and logon.

## Proof

The foreign SID grants access in the current domain.

## Failure modes

SID filtering on the trust strips it. A migrated account can be a legitimate carry over.
