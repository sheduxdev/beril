---
id: grpc-reflection-exposes-the-method-list-and-the-authz-gaps
title: gRPC reflection exposes the method list and the authz gaps
tags: api, grpc, recon
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/api-grpc-reflection.md
status: active
---
# gRPC reflection exposes the method list and the authz gaps

## Claim

Reflection gives method names, message shapes and sometimes internal services. Each method needs its own authz check.

## Test

List services with grpcurl. Call each method with a low privilege token. Watch for missing auth on one method.

## Proof

A method returns data or performs an action without the expected role.

## Failure modes

Reflection can be off. A gateway can enforce auth for all methods.
