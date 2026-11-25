---
id: arp-is-the-segmentation-check-inside-a-subnet
title: ARP is the segmentation check inside a subnet
tags: network, arp, segmentation
confidence: high
updated: 2026-11-26
uses: 0
sources: references/network-checklist.md
status: active
---
# ARP is the segmentation check inside a subnet

## Claim

Two hosts in the same VLAN reach each other by ARP even when a firewall rule says deny. The rule must sit on the gateway.

## Test

Check the subnet mask. Send an ARP request and a direct ping. Compare with the firewall rule.

## Proof

Direct L2 reachability where the policy expected L3 filtering.

## Failure modes

Private VLANs and port isolation change it. A host firewall can still block.
