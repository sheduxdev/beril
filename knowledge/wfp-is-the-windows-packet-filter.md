---
id: wfp-is-the-windows-packet-filter
title: WFP is the Windows packet filter
tags: wink, wfp, network
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/network-protection.md
status: active
---
# WFP is the Windows packet filter

## Claim

A filter driver sees and can block traffic at the stack. A callout with a user proxy can be a bypass path.

## Test

List the filters and the callouts. Send traffic through the proxy. Compare with a direct path.

## Proof

A traffic path that bypasses the filter.

## Failure modes

A default block closes it. A layered filter can inspect both paths.
