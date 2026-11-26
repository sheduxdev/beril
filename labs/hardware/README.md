# Hardware lab

A static board case. UART log, SPI strings, fuse map, JTAG scan, test pads and an update manifest.

```bash
./tests.sh
```

| File | Question |
|---|---|
| `uart.log` | Baud, boot state, shell and key |
| `spi_dump.txt` | Strings in the flash window |
| `fuse_map.txt` | Secure boot and debug state |
| `jtag.txt` | Is the core open |
| `pcb_notes.txt` | Which pads carry which bus |
| `update_manifest.txt` | Signature, counter and transport |

## Tasks

1. What baud and voltage does the UART use? Which pads are TX and RX?
2. Is the console read only? What proves a shell?
3. Read the SPI strings. Which URL is clear text and why does that matter?
4. Is secure boot blown? Is JTAG open? What does the pair mean?
5. What does anti_rollback_counter 7 block?
6. Name the three highest impact fixes.
7. Write the chain from the test pads to the device key.

## Constraints

Static only. No board is attached.

## Evidence

Quote the line and the file. A baud without the log line is a guess.

Answers are in `ANSWERS.md`.
