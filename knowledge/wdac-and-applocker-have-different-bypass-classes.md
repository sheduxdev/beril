---
id: wdac-and-applocker-have-different-bypass-classes
title: WDAC and AppLocker have different bypass classes
tags: win, wdac, applocker
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# WDAC and AppLocker have different bypass classes

## Claim

A rule that trusts a path, a publisher or a script host can be used if the trusted object is writable or has a scripting host.

## Test

Read the policy in audit or enforce mode. Find a trusted writable path or a signed binary with a script parameter.

## Proof

Unsigned code runs under the policy.

## Failure modes

A strict WDAC with a managed installer holds. AppLocker on scripts is weaker than on executables.
