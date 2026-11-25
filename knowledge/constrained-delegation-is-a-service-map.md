---
id: constrained-delegation-is-a-service-map
title: Constrained delegation is a service map
tags: ad, delegation, s4u
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# Constrained delegation is a service map

## Claim

`msDS-AllowedToDelegateTo` names the services an account can impersonate to. S4U2Proxy turns that into access.

## Test

Read the attribute on each account. Request a ticket for the allowed SPN as another user.

## Proof

The service accepts the impersonated ticket.

## Failure modes

Protocol transition and the service account rights matter. A target SPN that no longer exists is dead.
