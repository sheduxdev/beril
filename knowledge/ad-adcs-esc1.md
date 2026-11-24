---
id: ad-adcs-esc1
title: ESC1 is an enrollable SAN on a client-auth template
tags: ad, adcs, certificate
confidence: high
updated: 2026-11-24
uses: 0
sources: labs/ad, references/vulnerability-research.md
status: active
---
# ESC1 is an enrollable SAN on a client-auth template

## Claim

A template lets a low-privilege principal enroll and supply a subject alternative name for another identity.

## Test

Read the template flags. Enroll with an arbitrary UPN. Use the certificate for PKINIT or Schannel.

## Proof

A TGT or session as the target user from the crafted certificate.

## Failure modes

A template with approval or no client auth is not ESC1. Check the CA and the version.
