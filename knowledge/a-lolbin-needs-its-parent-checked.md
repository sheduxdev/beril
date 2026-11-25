---
id: a-lolbin-needs-its-parent-checked
title: A LOLBin needs its parent checked
tags: detection, lolbin, parent
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-lolbins.md
status: active
---
# A LOLBin needs its parent checked

## Claim

PowerShell or certutil from Office is suspicious, from a management agent it is normal. The parent and the command line decide.

## Test

Read the parent process and the flags. Compare with the baseline for that parent. Check the network child.

## Proof

An unusual parent and a download or encoded flag in one event.

## Failure modes

A management agent can launch the same shell. A signed binary can be legitimate.
