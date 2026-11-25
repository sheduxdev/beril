# Labs

Small local targets. Each has a README, tasks, a smoke test, and an answer key.

| Lab | Topic | Run |
|---|---|---|
| `web` | IDOR, XSS, SQLi, traversal, SSRF, weak auth | `./labs/web/tests.sh` |
| `rce` | command injection, eval, pickle, traversal, upload to exec | `./labs/rce/tests.sh` |
| `auth` | session fixation, MFA skip, reset token, JWT none | `./labs/auth/tests.sh` |
| `crypto` | ECB, CBC padding oracle, CTR reuse, length extension | `./labs/crypto/tests.sh` |
| `binary` | stack, format string, UAF, integer, mitigations | `./labs/binary/tests.sh` |
| `fuzz` | libFuzzer harness and crash triage | `make -C labs/fuzz run` |
| `re` | stripped binary, static reconstruction | `./labs/re/tests.sh` |
| `mobile` | exported components, deep link, JS bridge | `./labs/mobile/tests.sh` |
| `firmware` | extraction, CGI injection, update signing | `./labs/firmware/tests.sh` |
| `cloud` | Terraform, pod, Dockerfile review | `./labs/cloud/tests.sh` |
| `ad` | ACL paths, Kerberoast, ADCS ESC1 | `./labs/ad/tests.sh` |
| `llm` | prompt injection, RAG leak, exfil | `./labs/llm/tests.sh` |
| `detection` | Sigma rule and log triage | `./labs/detection/tests.sh` |

## Rules

- Local only unless a task says otherwise.
- Snapshot before a lab that can crash or brick.
- Read the README, attempt the tasks, then open `ANSWERS.md`.
- Keep the evidence. A pass without a request or a crash log is luck.

Run every smoke test:

```bash
./beril labs --run
```

The web lab binds `127.0.0.1:8099`. The binary lab writes build outputs into `labs/binary/`. The fuzz lab writes crashes into `labs/fuzz/artifacts/`.
