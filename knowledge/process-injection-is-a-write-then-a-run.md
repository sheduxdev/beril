---
id: process-injection-is-a-write-then-a-run
title: Process injection is a write then a run
tags: malware, injection, process
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mal-process-injection.md
status: active
---
# Process injection is a write then a run

## Claim

Every injection family is an allocate, a write and a run in another process. The API set and the target process are the signature.

## Test

Watch for OpenProcess, VirtualAllocEx, WriteProcessMemory and CreateRemoteThread. Compare with a clean run.

## Proof

A remote thread or a mapped section in the target.

## Failure modes

A manual mapper avoids the classic APIs. A same process hollow is a different signature.
