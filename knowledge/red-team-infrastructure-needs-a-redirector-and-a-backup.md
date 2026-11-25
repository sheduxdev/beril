---
id: red-team-infrastructure-needs-a-redirector-and-a-backup
title: Red team infrastructure needs a redirector and a backup
tags: red, infra, redirector
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-toolkit.md
status: active
---
# Red team infrastructure needs a redirector and a backup

## Claim

A direct C2 IP is a blockable single point. A redirector and a fallback domain give the operation a second path.

## Test

Draw the path from the target to the C2. Name the redirector and the fallback. Kill one and continue.

## Proof

The operation survives one link loss.

## Failure modes

A short operation can skip the redirector. A managed C2 hides the path.
