---
id: a-cgi-environment-variable-is-a-shell-input
title: A CGI environment variable is a shell input
tags: firmware, cgi, injection
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-cgi-injection.md, labs/firmware
status: active
---
# A CGI environment variable is a shell input

## Claim

Embedded CGI wrappers often build a shell string from query values, the User-Agent or the Referer.

## Test

Send a separator in each header and query value. Watch the response and a callback.

## Proof

An expanded command or a callback.

## Failure modes

A wrapper with an argv list holds. A busybox applet can parse the string again.
