---
id: a-netns-is-a-network-stack-copy
title: A netns is a network stack copy
tags: link, netns, network
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/os-namespaces.md
status: active
---
# A netns is a network stack copy

## Claim

A new netns has its own interfaces and routes but shares the kernel. A veth pair connects it to the host.

## Test

List the netns and the veth pairs. Enter one and read the route. Check the peer in the host.

## Proof

A path between the namespace and the host.

## Failure modes

A firewall on the veth blocks it. A nested netns hides the peer.
