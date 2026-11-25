---
id: an-ats-arbitrary-load-exception-covers-every-domain
title: An ATS arbitrary load exception covers every domain
tags: mobile, ios, ats
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/mobile-ios-ats.md
status: active
---
# An ATS arbitrary load exception covers every domain

## Claim

`NSAllowsArbitraryLoads` disables transport security for all hosts, not only the broken one.

## Test

Read Info.plist. Find a request that uses HTTP. Capture it with a proxy.

## Proof

Cleartext traffic leaves the device.

## Failure modes

A domain exception is narrow. A local network exception can be intended.
