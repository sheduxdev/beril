---
id: starttls-can-be-stripped-on-the-mx-path
title: STARTTLS can be stripped on the MX path
tags: mail, starttls, downgrade
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-tls.md
status: active
---
# STARTTLS can be stripped on the MX path

## Claim

A hop that does not require TLS can be downgraded by an active attacker, and the later hop cannot see it.

## Test

Read the MTA STS or DANE policy. Capture a delivery. Remove the STARTTLS offer and observe the retry in clear.

## Proof

A delivery without TLS where a policy expected it.

## Failure modes

MTA STS and DANE enforce it. A provider with a fixed route can hide the path.
