---
id: a-uart-header-is-a-boot-log-and-a-shell
title: A UART header is a boot log and a shell
tags: firmware, uart, console
confidence: high
updated: 2026-11-26
uses: 0
sources: knowledge/firmware-uart.md, labs/firmware
status: active
---
# A UART header is a boot log and a shell

## Claim

An exposed UART often prints the boot log and drops to a shell or a bootloader prompt when interrupted.

## Test

Find the pads with a multimeter. Connect at 115200 and 3.3V. Capture the boot and send a key during the prompt.

## Proof

A shell or a bootloader prompt on the console.

## Failure modes

A console can be read only. A pinout can be wrong and damage the board.
