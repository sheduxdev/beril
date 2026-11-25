---
id: a-logging-gap-is-the-first-cloud-finding
title: A logging gap is the first cloud finding
tags: cloud, logging, detection
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ir-cloud.md
status: active
---
# A logging gap is the first cloud finding

## Claim

A trail or a diagnostic setting that omits the data plane hides the very actions an attacker takes.

## Test

List the trails and the diagnostic settings. Perform a read and a write. Check whether both appear.

## Proof

An action with no log entry.

## Failure modes

A management event can still be logged. A short retention hides it later.
