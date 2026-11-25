---
id: a-uart-console-is-a-boot-log-and-often-a-shell
title: A UART console is a boot log and often a shell
tags: hardware, uart, console
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-uart.md
status: active
---
# A UART console is a boot log and often a shell

## Claim

A debug UART prints the boot and accepts a key to interrupt the bootloader. The baud and the voltage are the gate.

## Test

Find the pads. Measure the idle level. Connect at 115200 and 3.3V. Send a key during the prompt.

## Proof

A bootloader prompt or a shell.

## Failure modes

A read only console has no input. A wrong voltage can damage the pin.
