---
id: adcs-http-enrollment-is-an-ntlm-relay-target
title: ADCS HTTP enrollment is an NTLM relay target
tags: ad, adcs, relay
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/ad-adcs-esc1.md, references/specialist-program.md
status: active
---
# ADCS HTTP enrollment is an NTLM relay target

## Claim

An HTTP enrollment endpoint that accepts NTLM lets a coerced machine or user authenticate be relayed into a certificate.

## Test

Look for the Web Enrollment role over HTTP. Coerce a host. Relay to the CA with petitpotam and ntlmrelayx.

## Proof

A certificate for the machine is issued and used.

## Failure modes

EPA and SMB signing can block it. HTTPS alone is not enough.
