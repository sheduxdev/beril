---
id: dmarc-alignment-is-the-real-policy
title: DMARC alignment is the real policy
tags: mail, dmarc, alignment
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/email-dmarc.md
status: active
---
# DMARC alignment is the real policy

## Claim

DMARC passes only when SPF or DKIM passes and the authenticated domain aligns with the From header. A relaxed mode compares the organizational domain.

## Test

Read the DMARC record for p and adkim and aspf. Send from a subdomain and a lookalike. Check the alignment result.

## Proof

A message that fails alignment despite a passing SPF.

## Failure modes

A strict alignment block holds. A shared organizational domain can pass.
