---
id: kerberos-relay-needs-a-coerced-service-ticket
title: Kerberos relay needs a coerced service ticket
tags: win, kerberos, relay
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Kerberos relay needs a coerced service ticket

## Claim

A coerced machine authentication can be relayed to a service that accepts Kerberos without channel binding.

## Test

Check the target service for CBT and signing. Coerce a host. Relay with a Kerberos capable tool.

## Proof

A session on the target as the machine or a user.

## Failure modes

CBT and EPA block it. A DNS mismatch breaks the SPN.
