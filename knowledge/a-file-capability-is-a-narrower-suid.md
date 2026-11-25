---
id: a-file-capability-is-a-narrower-suid
title: A file capability is a narrower SUID
tags: linux, capabilities, privilege
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A file capability is a narrower SUID

## Claim

`cap_setuid` or `cap_dac_read_search` on a binary gives the specific right without full SUID.

## Test

List capabilities with getcap. Check the binary behavior. Use the right to read a root file or set uid.

## Proof

A root file read or a uid change.

## Failure modes

A bounding set drop blocks it. An empty capability set on exec clears it.
