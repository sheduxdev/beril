---
id: firmware-cgi-injection
title: Firmware CGI builds a shell string from the query
tags: firmware, iot, command
confidence: high
updated: 2026-11-24
uses: 0
sources: references/firmware-iot.md, labs/firmware
status: active
---
# Firmware CGI builds a shell string from the query

## Claim

A CGI passes QUERY_STRING into a shell command without quoting or validation. Root execution is common on embedded systems.

## Test

Extract the rootfs. Read the CGI. Call it with a separator and a command. Confirm with id.

## Proof

Command output in the HTTP response or a callback.

## Failure modes

A reflected parameter is not injection. The command must run.
