# Fuzzing lab answers

## 1. Grammar

`"BFZ1" | uint16_le length | length bytes`.

## 2. Corpus

The smallest valid input is `BFZ1\x01\x00A`. A 32-byte variant adds coverage without hiding the length path.

## 3. First mutation

The fuzzer grows the length field past 64 while keeping enough data. A typical crash input has a length around `0x79` and 121 bytes of body.

## 4. ASAN

`memcpy(buf, data + 6, len)` writes `len` bytes into a 64-byte stack buffer. ASAN reports a stack-buffer-overflow in `parse`.

## 5. Minimize

```bash
./fuzz -minimize_crash=1 artifacts/crash-* -max_total_time=60
```

Or trim by hand: `BFZ1` + `\x41\x00` + 65 bytes. The 65th byte is the first overflow.

## 6. Fix

```c
unsigned int len = data[4] | (data[5] << 8);
if (len > sizeof(buf)) len = sizeof(buf);
```

Or reject: `if (len > sizeof(buf)) return 0;`. Rejecting is crisper for a protocol test.

## 7. Maximum length

```c
if (len > 64 || size - 6 < len) return 0;
```

## 8. Optimization

At `-O0` the stack layout changes but the same length field reaches the copy. The offset in ASAN may differ. The primitive is unchanged.

## 9. `-max_len=32`

No. The total input cannot exceed 32 bytes, so the body cannot carry a length above 64. The bug needs at least 71 bytes.

## 10. Report shape

```markdown
### Stack buffer overflow in BFZ1 parser

- Input: BFZ1 + length 0x79 + 121 bytes
- Fault: ASAN stack-buffer-overflow at parser.c:12
- Cause: length field is trusted, copy is unbounded against buf[64]
- Impact: stack corruption, possible control flow with a crafted length
- Fix: reject length > 64 or clamp the copy
```

## Stretch notes

- A checksum narrows valid seeds, so a dictionary and a custom mutator help.
- The AFL++ harness needs `@@` and a file read. Compare coverage with libFuzzer.
- A second bug can be a chunk loop that trusts a count without checking the remaining size.
- CASR classifies the ASAN report. The severity is at least medium because the write is controlled.
