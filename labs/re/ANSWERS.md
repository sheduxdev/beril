# Reverse engineering lab answers

## 1. File

ELF 64-bit x86_64, stripped, non-PIE, executable stack, no canary. The missing symbols are the point.

## 2. Entry

`main` references the usage string and calls `check` with `argv[1]` and `strlen`.

## 3. Check function

The function compares `n` with 12, then calls `memcmp` against `BERL`.

## 4. Stage 1

Length 12. Any other length returns 1.

## 5. Stage 2

The first four bytes are `BERL`.

## 6. Stage 3

The loop XORs bytes 4 to 7 with `0x2a` and compares against `E`, `Y`, `E`, `S`.

```text
E ^ 0x2a = 0x6f  o
Y ^ 0x2a = 0x73  s
E ^ 0x2a = 0x6f  o
S ^ 0x2a = 0x79  y
```

So bytes 4 to 7 are `osoy`.

## 7. Stage 4

The first eight bytes are summed: `B+E+R+L+o+s+o+y = 751`. The result is formatted as `%04u`, so the last four bytes are the ASCII string `0751`.

## 8. Input

```text
BERLosoy0751
```

```bash
./challenge BERLosoy0751
# flag{re_static_wins}
```

## 9. Confirm

The binary returns the flag and exit code 0.

## 10. Patch

In Ghidra, patch the first conditional jump after the length compare to the fall-through path, or patch the `memcmp` result test. Export the patched binary and run it with `WRONG`. The new path reaches the later stages, so it fails there with a different message. Patch all four checks to return success for a full bypass.

## Stretch notes

- Reimplement stages in Python: length, prefix, XOR, sum, format.
- `rizin -q -j -c 'iz;iI;iS' challenge` gives the strings and the hardening in JSON.
- A fifth stage with a hash needs a brute force or a symbolic tool. Keep it small.
- Renaming functions and exporting a diff is the start of a real RE report.
