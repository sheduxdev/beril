---
id: report-evidence
title: Evidence must be reproducible and redacted
tags: process, report, evidence
confidence: high
updated: 2026-11-24
uses: 0
sources: references/claude-bughunter.md
status: active
---
# Evidence must be reproducible and redacted

## Claim

The report needs the raw request or crash, with tokens and PII masked, and a stable path.

## Test

Keep the original, make a redacted copy, record the hash and time. Link the copy, keep the original local.

## Proof

A triager can rerun the redacted repro and reach the same result.

## Failure modes

A screenshot alone is weak. A redaction that changes the repro breaks it.
