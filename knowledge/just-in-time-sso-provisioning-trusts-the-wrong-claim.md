---
id: just-in-time-sso-provisioning-trusts-the-wrong-claim
title: Just in time SSO provisioning trusts the wrong claim
tags: auth, sso, provisioning
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/techniques.md
status: active
---
# Just in time SSO provisioning trusts the wrong claim

## Claim

If account creation keys on email from the IdP without a verified domain or issuer check, an attacker IdP or unverified email creates an account.

## Test

Read the provisioning rule. Try an unverified email at the tenant domain. Try a second IdP with the same email.

## Proof

The new identity lands in the target tenant or takes over an existing account.

## Failure modes

Domain verification and issuer pinning close it. A manual approval step limits impact.
