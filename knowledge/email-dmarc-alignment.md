---
id: email-dmarc-alignment
title: DMARC enforces alignment that SPF and DKIM alone do not
tags: email, dmarc, spf, dkim, bec
confidence: high
updated: 2026-11-26
uses: 0
sources: https://www.m3aawg.org/sites/default/files/m3aawg-email-authentication-recommended-best-practices-09-2020.pdf, https://datatracker.ietf.org/doc/html/rfc7489, https://datatracker.ietf.org/doc/html/rfc7208
status: active
---
# DMARC enforces alignment that SPF and DKIM alone do not

## Claim

SPF checks the envelope sender path; DKIM signs the body and headers. Neither ties the result to the visible From. DMARC requires SPF or DKIM to pass and align with the From domain, then tells receivers to quarantine or reject on failure.

## Test

Read the DMARC record policy: `p=none` only reports. Send a spoof from an unauthorized host and read the Authentication-Results header. Check the SPF record stays within the 10 DNS lookup limit, or it PermErrors.

## Proof

A spoof of the org domain rejected under `p=reject`, and legitimate mail still aligned and delivered.

## Failure modes

`p=none` is visibility, not protection. DMARC does not stop look-alike domains or mail from a compromised real account; that is the BEC gap. Forwarding breaks SPF, so DKIM alignment and ARC matter.
