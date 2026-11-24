# Labs and training

Beril ships ten local practice targets and a 25-week curriculum. Everything runs on your machine.

## Labs

```bash
./beril labs --run          # every smoke test
./beril labs --run web      # one lab
```

Each lab has a README, tasks, a smoke test and an answer key. The dashboard lists them under Lab and runs the smoke test from a card.

| Lab | Topic |
|---|---|
| `web` | IDOR, XSS, SQLi, traversal, SSRF, weak auth |
| `binary` | Stack, format string, UAF, integer, mitigations |
| `fuzz` | libFuzzer harness and crash triage |
| `re` | Stripped binary, static reconstruction |
| `mobile` | Exported components, deep link, JS bridge |
| `firmware` | Extraction, CGI injection, update signing |
| `cloud` | Terraform, pod, Dockerfile review |
| `ad` | ACL paths, Kerberoast, ADCS ESC1 |
| `llm` | Prompt injection, RAG leak, exfil |
| `detection` | Sigma rule and log triage |

## Curriculum

```bash
./beril train --status
./beril train --week 1
```

The plan runs from the shell to ROP, heap, AD, firmware and AI security. Each week has drills, a reading list, a checkpoint and a deliverable with a grading rubric. Progress lives in `training/` and does not enter git. Start at [Training](../docs/training.md) and the [curriculum reference](../references/curriculum.md).

## Turn a result into a note

```bash
./beril reflect
```

`reflect` saves a lab finding as a method note with a root cause and a fix. If the lesson transfers to other targets, add a memory card with `./beril remember add`. See [Memory](../docs/memory.md).

## The network defense track

A separate track from the 25-week plan:

| Page | Covers |
|---|---|
| [Network visibility](../references/network-visibility.md) | Flow, packet, DNS, IDS, eBPF and honeypot telemetry, and what each source misses |
| [Network protection](../references/network-protection.md) | Segmentation, egress, management plane, DDoS, WAF, DNS, TLS and recovery, with a test per control |
| [Network checklist](../references/network-checklist.md) | 50 controls and evidence lines for a quarterly pass |
| [BGP security](../references/bgp-security.md) | Hijack, route leak, RPKI, filtering and BMP, with tests |
| [Network toolkit](../references/network-toolkit.md) | Tools by question, limits and safety |
| [Network curriculum](../references/network-curriculum.md) | An eight-week lab track |
| [Network runbook](../docs/network-runbook.md) | Incident scope and containment order |
| [BGP runbook](../docs/bgp-runbook.md) | Hijack confirmation and mitigation |

## Reverse engineering

```bash
./install.sh --re
./beril scan --target ./sample --deep
./beril re --target ./sample --capa --floss --rizin
./scripts/ghidra_headless.sh ./sample out.json
./scripts/patch_diff.sh ghidriff old.bin new.bin
```

`--deep` runs every installed optional pass and keeps the static result. Ghidra needs `GHIDRA_HOME`. Binary Ninja needs a license and `install_api.py`. Mobile runtime work needs a device or emulator, a matching Frida server and a debuggable target.

Start with [Reverse engineering](../docs/reverse-engineering.md), then the references for [RE](../references/reverse-engineering.md), [fuzzing](../references/fuzzing.md), [exploit development](../references/exploit-development.md), [mobile](../references/mobile-reverse.md), [firmware](../references/firmware-iot.md), [Ghidra](../references/ghidra-ecosystem.md) and [Rust](../references/rust-reverse.md).
