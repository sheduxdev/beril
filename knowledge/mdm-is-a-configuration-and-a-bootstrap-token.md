---
id: mdm-is-a-configuration-and-a-bootstrap-token
title: MDM is a configuration and a bootstrap token
tags: macos, mdm, management
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# MDM is a configuration and a bootstrap token

## Claim

An enrolled device trusts the MDM profile. The bootstrap token and the profile install rights are the control path.

## Test

Read the profiles and the enrollment state. Check the bootstrap token escrow. Install a test profile.

## Proof

A profile applied without a user prompt.

## Failure modes

A user approved enrollment can remove the profile. A supervised device has more.
