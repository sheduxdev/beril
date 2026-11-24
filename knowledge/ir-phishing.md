---
id: ir-phishing
title: Phishing triage reads headers and detonates the payload
tags: ir, phishing, email
confidence: medium
updated: 2026-11-25
uses: 0
sources: references/vulnerability-research.md
status: active
---
# Phishing triage reads headers and detonates the payload

## Claim

The header chain, URL redirects and attachment type tell the story. The user action and the credential entry decide impact.

## Test

Read the Received chain and authentication results. Expand the URL. Detonate in a sandbox.

## Proof

A payload and a credential capture proof.

## Failure modes

A lookalike domain without a payload is lower. A QR code needs a mobile detonation.
