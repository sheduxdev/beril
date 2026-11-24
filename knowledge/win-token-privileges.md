---
id: win-token-privileges
title: Windows token privileges are the privesc surface
tags: windows, token, privesc
confidence: high
updated: 2026-11-24
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Windows token privileges are the privesc surface

## Claim

A token holds SeImpersonate, SeAssignPrimaryToken, SeBackup, SeRestore or SeDebug. A service account with one of them can escalate.

## Test

Run whoami /priv. Match the privilege to a technique: potato, backup, debug. Use a known tool in a lab.

## Proof

A SYSTEM shell or a sensitive file read.

## Failure modes

An enabled privilege on an admin token may be expected. The starting user matters.
