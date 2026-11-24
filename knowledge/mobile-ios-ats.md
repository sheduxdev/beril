---
id: mobile-ios-ats
title: ATS exceptions are domain-scoped trust decisions
tags: mobile, ios, ats
confidence: medium
updated: 2026-11-24
uses: 0
sources: references/mobile-reverse.md
status: active
---
# ATS exceptions are domain-scoped trust decisions

## Claim

NSAllowsArbitraryLoads or a per-domain exception permits HTTP, or a WKWebView bridge trusts any loaded page.

## Test

Read Info.plist. Proxy the app. Test an HTTP host and a bridge method from an attacker page.

## Proof

Plaintext traffic or a bridge call from an untrusted origin.

## Failure modes

An exception for a local host may be intended. ATS does not cover every framework.
