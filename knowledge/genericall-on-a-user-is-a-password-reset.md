---
id: genericall-on-a-user-is-a-password-reset
title: GenericAll on a user is a password reset
tags: ad, acl, genericall
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/ad-acl-path.md
status: active
---
# GenericAll on a user is a password reset

## Claim

GenericAll includes the right to reset the password without knowing the old one, which turns an ACL edge into takeover.

## Test

Confirm the ACE on the object. Set a new password with ADUC or Set-ADAccountPassword. Log in.

## Proof

A session as the target user.

## Failure modes

A protected admin account can have the reset blocked. A password policy can reject the choice.
