# FAQ and limits

## Limits

| Limit | Detail |
|---|---|
| It does not weaponize | Active probes are four minimal GET patterns. No POST body, upload, SSRF callback or race. No working exploit is generated |
| The active set is narrow | A quote, a marker, a redirect, a traversal, OPTIONS and TRACE per parameter. Depth needs a human |
| No login automation | Sessions work through `--header`, `--cookie` or `--auth-file`. Beril does not fill login forms or refresh tokens |
| Artifact scans are static | Samples are read, not executed. Packed, encrypted or heavily obfuscated files can hide most behavior |
| The sandbox is a container | The host kernel is shared. Use a VM for hostile samples |
| Reachability is a grep | An unused package can still arrive transitively, so it is reported low, not removed |
| Version matching is a hint | The offline CMS and OSV seeds are small. Use the adapters, `--online` or the real advisory database for currency |
| Live secret checks leave the host | `--verify` sends the key to the provider read endpoint. It is off by default |
| Camoufox has a ceiling | CAPTCHAs, hard login walls and aggressive fingerprint checks can still win. No paid CAPTCHA service is used |
| One identity per session | A fresh IP may be needed after repeated challenges |
| The catalogs are snapshots | Stars, report totals and thread counts move. The date travels with every number |
| It cannot judge a technique | `extract` records structure, not truth. You read the top notes and replay the request |
| Deep tooling is external | Ghidra, Binary Ninja, IDA, rizin, capa, FLOSS, AFL++, unblob, EMBA, MobSF and YARA need their own install and sometimes a license |
| Mobile runtime work needs a device | Frida hooks need an emulator or phone, a matching Frida server and a debuggable target |
| The dashboard is single-user | Loopback only, no login. Do not expose it without a proxy and auth |
| No backend and no telemetry | Catalogs are files. Jobs and spending stay local |
| No automatic submission | Posting to a program, a ticket or a chat is manual |

## Questions

**A page returns 403 or an empty JavaScript shell to curl. Can Beril read it?**
Yes, for public pages. The research layers use Camoufox, which reads RSS, JSON, shadow DOM and challenge pages. See the [Camoufox playbook](../references/camoufox-playbook.md). For your own app, `./beril scan --render` runs the passive checks on a rendered page.

**The scan found nothing. Is the app safe?**
No. A clean scan covers a short checklist. Logged-in flows, business logic and authorization stay manual. Read the "not tested" line in the report.

**Why was an active scan refused?**
Active probes need an ownership record and a scope entry. Run `./beril verify --new <host>`, publish the token, then `./beril verify --verify <host>`.

**A secret turned up in history. What now?**
Revoke it at the provider first. Then rotate. Then clean the history. Cleaning first leaves a live key in every clone.

**How do I scan an app behind a login?**
Pass a session with `--header`, `--cookie` or `--auth-file`. Beril does not fill login forms.

**The dashboard will not start on 8788.**
Another process holds the port. Use `./beril dashboard --port 8790`. On a headless host add `--no-open`.

**What does the score mean?**
Severity times confidence, with verified and KEV boosts. It orders work and is not CVSS.

**Where do reports go?**
Under `scans/` on your machine. Nothing is uploaded. The dashboard Posture page reads them locally.

**Can I use it on Windows or macOS?**
Artifact paths exist for both, but Linux is the tested platform and the optional toolchain is documented for Linux.

**How do I add what I learned?**
Run `./beril remember add` for a durable card, or `./beril reflect` for a lab finding. Check first with `./beril recall "<topic>" --decide` so you do not duplicate a card.
