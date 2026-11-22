# Fuzzing lab

A parser with a length bug. The header is `BFZ1`, then a 16-bit little-endian length, then that many bytes. The destination is 64 bytes.

```bash
make
make run
```

## Tasks

1. Read `parser.c` and write the input grammar in one line.
2. Build the seed corpus. Start with the smallest valid input.
3. Run the fuzzer. Which mutation broke it first?
4. Read the ASAN report. Which line wrote past the buffer?
5. Minimize the crash to the shortest input.
6. Fix the parser with a bound check. Rerun for 60 seconds. Does the crash return?
7. Add a maximum length check before the copy.
8. Build with `-O0` and compare the crash input.
9. Run with `-max_len=32`. Can the bug still trigger?
10. Write the root cause and the fix in a report.

## Evidence

Keep the crash file, the ASAN top frame, and the minimized input. A crash without a root cause is noise.

## Stretch

- Add a checksum byte and see how it changes coverage.
- Build an AFL++ harness with `scripts/afl_harness.c` and compare findings.
- Add a second bug: a signed length or a chunk loop.
- Run CASR on the crash and classify the severity.

Answers are in `ANSWERS.md`.
