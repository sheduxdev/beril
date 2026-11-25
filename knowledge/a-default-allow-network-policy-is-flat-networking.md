---
id: a-default-allow-network-policy-is-flat-networking
title: A default allow network policy is flat networking
tags: cloud, k8s, network
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/cloud-service-mesh.md
status: active
---
# A default allow network policy is flat networking

## Claim

A namespace without a default deny policy allows every pod to reach every other pod, so one RCE spreads.

## Test

List the policies in the namespace. From one pod, connect to a database and to another pod service.

## Proof

The connection succeeds where the policy should have denied it.

## Failure modes

A CNI can enforce at another layer. A policy can exist but select no pods.
