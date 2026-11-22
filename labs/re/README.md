# Reverse engineering lab

A stripped binary checks a 12-byte argument in four stages. Recover the input without running the checker first.

```bash
make
./challenge test
```

## Tasks

1. Run `file`, `strings`, and `readelf -h`. Record the architecture and the hardening.
2. Open the binary in Ghidra or rizin. Find `main` from the usage string.
3. Follow the call into the check function.
4. Stage 1: what length is required?
5. Stage 2: what are the first four bytes?
6. Stage 3: recover the XOR key and the four target bytes.
7. Stage 4: what is summed, and how is the result encoded?
8. Build the full 12-byte input.
9. Confirm with the binary.
10. Patch one comparison to accept `WRONG` and prove the new path.

## Rules

Static first. Do not use the source until you have a decompiled reconstruction. `challenge.c` is in the directory, so close it.

## Evidence

Keep the addresses, the decompiled snippet, and the final input. A flag without a path is a guess.

## Stretch

- Rebuild the check in Python and brute force a missing byte.
- Rename every function in the database and export a diff.
- Use `rizin -j` and extract the constants automatically.
- Add a fifth stage with a hash and rebuild.

Answers are in `ANSWERS.md`.
