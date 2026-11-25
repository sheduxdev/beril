---
id: a-phishing-pretext-needs-a-sender-and-a-reason
title: A phishing pretext needs a sender and a reason
tags: red, phishing, pretext
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/email-dmarc.md, knowledge/ir-phishing.md
status: active
---
# A phishing pretext needs a sender and a reason

## Claim

The click rate follows the sender trust and the reason, not the template design. A lookalike domain is the first check.

## Test

Write the sender, the reason and the action. Check SPF, DKIM and DMARC for the lookalike. Send a small batch.

## Proof

A delivered message that passes the lookalike check.

## Failure modes

A protected brand domain can block the lookalike. A user can report the message early.
