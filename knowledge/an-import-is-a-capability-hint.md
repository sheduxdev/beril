---
id: an-import-is-a-capability-hint
title: An import is a capability hint
tags: malware, import, capability
confidence: high
updated: 2026-11-26
uses: 0
sources: references/reverse-engineering.md
status: active
---
# An import is a capability hint

## Claim

Crypto, process, network, registry and anti analysis imports map to behavior before a single instruction is read.

## Test

List the imports by category. Map each to a technique. Drop the ones the unpacker resolves.

## Proof

A capability table tied to the imports.

## Failure modes

A dynamic import hides the table. A signed binary imports the same APIs.
