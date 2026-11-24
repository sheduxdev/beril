---
id: api-oauth-device
title: Device code flow is phishing with a real code
tags: api, oauth, device-code
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/techniques.md
status: active
---
# Device code flow is phishing with a real code

## Claim

The device flow asks the user to enter a code on a legitimate page. An attacker can send their own code.

## Test

Start a device flow. Send the code to a victim. Poll for the token.

## Proof

A token issued to the attacker after the victim approves.

## Failure modes

A code that expires quickly is lower risk. The consent screen must be read.
