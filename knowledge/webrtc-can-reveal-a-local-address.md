---
id: webrtc-can-reveal-a-local-address
title: WebRTC can reveal a local address
tags: browser, webrtc, privacy
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# WebRTC can reveal a local address

## Claim

An ICE candidate can carry a host address behind a VPN, which leaks the local network layout.

## Test

Create a peer connection in the page. Read the candidate lines. Compare with the public address.

## Proof

A private address appears in a candidate.

## Failure modes

A TURN only policy with mDNS hides it. A browser update can change the behavior.
