---
id: sip-is-a-kernel-enforced-macos-boundary
title: SIP is a kernel enforced macOS boundary
tags: macos, sip, boundary
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# SIP is a kernel enforced macOS boundary

## Claim

System Integrity Protection restricts writes to system paths and to task ports even for root. A SIP disabled host is a different target.

## Test

Read `csrutil status`. Try to write `/System` and to attach to a platform binary. Compare with a SIP off VM.

## Proof

A write or an attach that only works with SIP off.

## Failure modes

A signed installer can write. A reboot into recovery can disable it.
