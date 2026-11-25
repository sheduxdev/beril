---
id: an-open-relay-needs-a-foreign-sender-and-recipient
title: An open relay needs a foreign sender and recipient
tags: mail, smtp, relay
confidence: high
updated: 2026-11-26
uses: 0
sources: references/specialist-program.md
status: active
---
# An open relay needs a foreign sender and recipient

## Claim

A relay that accepts a message where neither the sender nor the recipient is local forwards mail for anyone.

## Test

Connect with EHLO. Send MAIL FROM and RCPT TO outside the domain. Check the accept and the queue.

## Proof

A queued message with two foreign addresses.

## Failure modes

A relay that requires auth is closed. A local sender can be enough for some checks.
