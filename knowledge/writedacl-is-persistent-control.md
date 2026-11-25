---
id: writedacl-is-persistent-control
title: WriteDACL is persistent control
tags: ad, acl, writedacl
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ad-acl-path.md
status: active
---
# WriteDACL is persistent control

## Claim

WriteDACL lets an attacker grant themselves GenericAll, so the path survives a password change and is easy to miss.

## Test

Check the ACE. Add a GenericAll for your user. Repeat the target action. Remove the ACE.

## Proof

The new right works after the original edge is gone.

## Failure modes

Inheritance and owner rights can confuse the check. SDProp can revert admin changes.
