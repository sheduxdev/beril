---
id: a-macro-runs-in-a-parent-process
title: A macro runs in a parent process
tags: malware, macro, office
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-lolbins.md
status: active
---
# A macro runs in a parent process

## Claim

An Office macro starts in WINWORD or EXCEL, then spawns the shell. The parent child relation is the detection.

## Test

Open the document in a sandbox. Read the VBA with olevba. Watch the child process.

## Proof

The macro source and the child process tree.

## Failure modes

A signed macro can still be malicious. A macro can run only after a click.
