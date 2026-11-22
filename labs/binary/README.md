# Binary lab

Four small bugs with different primitives. Build and run locally.

```bash
make all integer-asan
./tests.sh
```

| Binary | Bug | Target |
|---|---|---|
| `stack-vuln` | stack overflow via `strcpy` | return address, `win()` |
| `stack-hard` | same, with PIE, canary, NX, full RELRO | mitigation comparison |
| `fmt` | user string passed to `printf` | leak the stack and the secret |
| `uaf` | stale pointer after `free` | reallocate and call `win()` |
| `integer` | 32-bit wrap in `count * size` | tiny allocation, large read |

## Tasks

1. Run `file`, `readelf -h`, `readelf -l`, and `readelf -d` on both stack builds. List every difference.
2. Find the offset to the return address in `stack-vuln` with a cyclic pattern.
3. Redirect execution to `win` and record the exact payload.
4. Do the same against `stack-hard`. What blocks the simple offset?
5. In `fmt`, send `%p.%p.%p` and find the stack offset of the input.
6. Find the address of `secret` with `nm` and print it with `%s`.
7. In `uaf`, free the object, send 32 controlled bytes, and call `win`.
8. In `integer`, find an input pair whose product wraps. Explain why ASAN reports a 1-byte region.
9. Check `stack-hard` with `checksec`. Which mitigations are active?
10. Write the exploitability of the stack bug with NX on and off.

## Evidence

For each task keep the command, the register state or ASAN report, and one sentence on the primitive.

## Stretch

- Build a ROP chain for `stack-hard` that calls `win`.
- Turn the format string into a write with `%n`.
- Add a heap overflow and a double free.
- Rebuild `stack-vuln` with `-fstack-protector-strong` and measure the change.

Answers are in `ANSWERS.md`.
