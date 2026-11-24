---
id: web-desync-parser-disagreement
title: Desync needs two HTTP parsers and an ambiguous length
tags: web, http, smuggling
confidence: high
updated: 2026-11-24
uses: 0
sources: references/techniques.md, references/ghidra-ecosystem.md
status: active
---
# Desync needs two HTTP parsers and an ambiguous length

## Claim

A front end and back end disagree about where a request ends, usually through Content-Length, Transfer-Encoding or HTTP/2 downgrade.

## Test

Send ambiguous requests. Try CL.TE, TE.CL, TE.TE, CRLF header injection and HTTP/2 pseudo-header tricks. Confirm with timing and a second client.

## Proof

A second clean client receives the wrong response, or a repeatable timing signal.

## Failure modes

One 400 does not prove desync. Shared proxies make results non-deterministic.
