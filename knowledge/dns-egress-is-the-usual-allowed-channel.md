---
id: dns-egress-is-the-usual-allowed-channel
title: DNS egress is the usual allowed channel
tags: network, egress, dns
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/detection-dns.md
status: active
---
# DNS egress is the usual allowed channel

## Claim

A network that blocks HTTP often still allows DNS to a resolver, which becomes the tunnel and the callback path.

## Test

Query a name you control from the host. Try a long label and a TXT record. Compare with direct HTTP.

## Proof

The resolver log shows the query from the host.

## Failure modes

A local resolver with a fixed forwarder can strip the source. A DNS allowlist narrows the names.
