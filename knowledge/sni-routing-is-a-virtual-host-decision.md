---
id: sni-routing-is-a-virtual-host-decision
title: SNI routing is a virtual host decision
tags: network, tls, sni
confidence: medium
updated: 2026-11-26
uses: 0
sources: knowledge/detection-tls.md
status: active
---
# SNI routing is a virtual host decision

## Claim

A frontend can route by SNI before the certificate, so a wrong SNI reaches a default backend or a different certificate.

## Test

Connect with the right SNI, a wrong one and none. Compare the certificate and the body.

## Proof

A different backend answers for the wrong name.

## Failure modes

A wildcard certificate and one backend hide it. A strict frontend rejects the wrong name.
