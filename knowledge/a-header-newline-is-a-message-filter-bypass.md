---
id: a-header-newline-is-a-message-filter-bypass
title: A header newline is a message filter bypass
tags: mail, header-injection, smtp
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# A header newline is a message filter bypass

## Claim

A CRLF in a subject, a name or a custom header adds headers or a body part to the message.

## Test

Put a newline and a Bcc or a Content-Type in each field. Send to yourself and read the raw message.

## Proof

An injected header in the received message.

## Failure modes

A library that encodes the field closes it. A strict SMTP server can normalize.
