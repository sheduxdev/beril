---
id: trace-context
title: Trace context is a header carried across every hop
tags: observability, tracing, context
confidence: high
updated: 2026-11-25
uses: 0
sources: references/engineering-mastery.md
status: active
---
# Trace context is a header carried across every hop

## Claim

The trace id and span id travel with the request. A boundary that drops them breaks the tree.

## Test

Send a request through the queue and the worker. Check the trace tree.

## Proof

A single trace that spans the async hop.

## Failure modes

A thread-local context lost at a thread pool starts a new trace. A header not forwarded splits the trace.
