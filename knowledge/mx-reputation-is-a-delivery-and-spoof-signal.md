---
id: mx-reputation-is-a-delivery-and-spoof-signal
title: MX reputation is a delivery and spoof signal
tags: mail, mx, reputation
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/email-spf.md
status: active
---
# MX reputation is a delivery and spoof signal

## Claim

A domain that sends through a low reputation host or has no MX at all is easier to spoof and more likely to be filtered.

## Test

Read the MX and the SPF include. Compare the sending host with the MX. Check the reputation source.

## Proof

A sender outside the MX and SPF set.

## Failure modes

A separate marketing ESP is normal. A null MX can be intentional.
