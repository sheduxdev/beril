---
id: an-email-format-needs-a-real-sample
title: An email format needs a real sample
tags: osint, email, pattern
confidence: high
updated: 2026-11-26
uses: 0
sources: references/osint-toolkit.md
status: active
---
# An email format needs a real sample

## Claim

A pattern guessed from a name is a lead. Five published addresses from the domain make the pattern usable.

## Test

Collect five real addresses. Classify the local part. Test the pattern against an SMTP RCPT if the server allows it.

## Proof

Five samples that fit one pattern.

## Failure modes

A small company can mix formats. A catch all accepts every guess.
