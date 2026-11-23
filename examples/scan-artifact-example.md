# Scan: labs/binary/stack-vuln

Generated 2026-11-23T11:12:17+00:00 by Beril 1.4.0. Mode: artifact.

| Severity | Count |
|---|---:|
| critical | 0 |
| high | 2 |
| medium | 2 |
| low | 0 |
| info | 0 |

## Fix now

1. **No PIE** (high, confidence high): Build with -fPIE -pie.
2. **Executable stack** (high, confidence high): Build with -z noexecstack.
3. **Partial RELRO** (medium, confidence high): Add -z now for full RELRO.
4. **No stack canary** (medium, confidence high): Build with -fstack-protector-strong.

## Authorization

- No authorization record. Fine for passive checks, not for active ones.

## Scope

**Checks attempted**
- Hardening flags, RPATH, string secrets
- SUID

**Checks not attempted**
- Execution and dynamic behavior
- Packed or encrypted content
- Network verification

## Limits

- File cap: 20000
- Bytes per file: 2000000
- Execution: none

## Findings

### [HIGH] No PIE

- Confidence: high
- Source: static
- CWE: CWE-693

**Evidence:** ELF type EXEC

**Impact:** Build with -fPIE -pie.

**Fix:** Build with -fPIE -pie.

### [HIGH] Executable stack

- Confidence: high
- Source: static
- CWE: CWE-693

**Evidence:** GNU_STACK RWE

**Impact:** Build with -z noexecstack.

**Fix:** Build with -z noexecstack.

### [MEDIUM] Partial RELRO

- Confidence: high
- Source: static
- CWE: CWE-693

**Evidence:** BIND_NOW absent

**Impact:** Add -z now for full RELRO.

**Fix:** Add -z now for full RELRO.

### [MEDIUM] No stack canary

- Confidence: high
- Source: static
- CWE: CWE-693

**Evidence:** __stack_chk_fail absent

**Impact:** Build with -fstack-protector-strong.

**Fix:** Build with -fstack-protector-strong.
