---
id: patchguard-is-a-kernel-integrity-check
title: PatchGuard is a kernel integrity check
tags: wink, patchguard, kernel
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/binary-windows-kernel.md
status: active
---
# PatchGuard is a kernel integrity check

## Claim

PatchGuard checks selected structures and bugchecks on a mismatch. A patch must preserve or restore the checked fields.

## Test

Read the protected structure and the check period. Patch one field. Wait or force a check.

## Proof

A bugcheck from the integrity check or a clean survival.

## Failure modes

A supported hook point avoids the structure. A debug mode can disable the check.
