---
id: auth-mfa-fatigue
title: Push MFA without number matching is a fatigue target
tags: auth, mfa, push-bombing
confidence: high
updated: 2026-11-26
uses: 0
sources: https://www.cisa.gov/sites/default/files/publications/fact-sheet-implement-number-matching-in-mfa-applications-508c.pdf, https://www.cisa.gov/resources-tools/resources/implementing-phishing-resistant-mfa
status: active
---
# Push MFA without number matching is a fatigue target

## Claim

With a valid password, an attacker triggers repeated push prompts until the user taps Accept by accident or annoyance (push bombing, MFA fatigue). Plain approve-or-deny push carries no context.

## Test

Check whether the MFA app shows a number the user must type from the login screen. Try repeated prompts against a test account and see whether the tenth prompt is identical to the first.

## Proof

A config where approval is a single tap with no number matching, and repeated prompts are not rate limited or alerted.

## Failure modes

Number matching is an interim fix, not phishing-resistant. SMS and voice add SS7 and SIM-swap risk. The endpoint is still phishable without a bound credential.
