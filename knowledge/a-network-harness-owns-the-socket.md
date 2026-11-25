---
id: a-network-harness-owns-the-socket
title: A network harness owns the socket
tags: fuzz, network, socket
confidence: medium
updated: 2026-11-26
uses: 0
sources: references/fuzzing.md
status: active
---
# A network harness owns the socket

## Claim

A server that reads from a real socket can be fuzzed without a full client if the harness controls the peer and the timing.

## Test

Start the server on a local port. Connect and send the seed. Parse the response as the oracle. Kill and restart per run.

## Proof

A crash from a captured byte stream.

## Failure modes

A slow handshake limits the rate. A threaded server needs a restart.
