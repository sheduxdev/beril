---
id: process-bounty-platform
title: Program rules decide what is payable
tags: process, bounty, scope
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/claude-bughunter.md
status: active
---
# Program rules decide what is payable

## Claim

The brief defines assets, exclusions, severity, payout and disclosure. A valid bug can still be out of scope.

## Test

Parse the brief into allow and deny rules. Check the VRT mapping, the payout table and the disclosure terms.

## Proof

A finding with a scope citation and a payout line.

## Failure modes

A platform default can be overridden by the program. A closed report can still be a valid bug.
