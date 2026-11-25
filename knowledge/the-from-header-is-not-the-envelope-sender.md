---
id: the-from-header-is-not-the-envelope-sender
title: The From header is not the envelope sender
tags: mail, from, spoof
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/email-dmarc.md
status: active
---
# The From header is not the envelope sender

## Claim

The visible From is a header. SPF checks the envelope MAIL FROM. Only DMARC ties the two together.

## Test

Send with a mismatched envelope and From. Read the auth results. Check the DMARC alignment.

## Proof

A message with a forged From and a passing SPF but a DMARC fail.

## Failure modes

A strict DMARC record catches it. A rewritten envelope can align.
