---
id: ntlm-relay-needs-signing-off-and-a-coercion
title: NTLM relay needs signing off and a coercion
tags: win, ntlm, relay
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ad-acl-path.md
status: active
---
# NTLM relay needs signing off and a coercion

## Claim

SMB or LDAP without signing lets a coerced authentication be relayed to another service as the victim.

## Test

Check the signing policy on SMB and LDAP. Coerce a host with PetitPotam or a printer. Relay to LDAP for a machine account.

## Proof

A new machine account or a directory change.

## Failure modes

SMB signing and LDAP signing with CBT close it. A blocked egress path stops the relay.
