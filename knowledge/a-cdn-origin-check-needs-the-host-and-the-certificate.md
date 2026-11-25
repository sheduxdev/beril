---
id: a-cdn-origin-check-needs-the-host-and-the-certificate
title: A CDN origin check needs the Host and the certificate
tags: network, cdn, origin
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/recon.md, knowledge/net-cdn.md
status: active
---
# A CDN origin check needs the Host and the certificate

## Claim

An origin that answers any Host is reachable directly. One that checks Host needs the right value and the certificate can still leak the name.

## Test

Resolve the origin candidate. Request with the target Host. Compare the body and the certificate with the edge.

## Proof

The origin serves the app with the target Host.

## Failure modes

A shared origin returns a neighbour. A second CDN node looks the same.
