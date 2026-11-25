---
id: a-kerberoastable-spn-is-an-offline-crack-target
title: A Kerberoastable SPN is an offline crack target
tags: ad, kerberos, kerberoast
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md, knowledge/ad-acl-path.md
status: active
---
# A Kerberoastable SPN is an offline crack target

## Claim

Any domain user can request a service ticket for an SPN and take the encrypted part offline to crack the service account password.

## Test

Request the ticket with Rubeus or GetUserSPNs. Save the hash. Check the account name and the password age.

## Proof

The service account password is recovered or the hash is crackable with a wordlist.

## Failure modes

A 40 character managed password is not crackable. AES only tickets are harder than RC4.
