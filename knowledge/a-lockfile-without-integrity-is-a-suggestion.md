---
id: a-lockfile-without-integrity-is-a-suggestion
title: A lockfile without integrity is a suggestion
tags: supply, lockfile, integrity
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/supply-lockfile.md
status: active
---
# A lockfile without integrity is a suggestion

## Claim

A lockfile that records a range or a registry URL without a hash lets a compromised registry or a mutable tag serve new bytes.

## Test

Inspect the lock entries for a hash. Compare the installed hash with the lock. Check a git or URL dependency.

## Proof

A changed artifact installs without a lock mismatch.

## Failure modes

A private registry can pin by digest. An old lockfile can still have weak entries.
