# Dashboard

![dashboard](../assets/dashboard.png)

A local dashboard for every catalog in Beril. Orbit-style: monochrome, thin rules, one spacing scale, flat panels, light and dark.

```bash
./beril dashboard
```

It binds `127.0.0.1:8788` and opens the browser. Use `--port` to change and `--no-open` on a headless host.

## Pages

| Page | What it shows | Action |
|---|---|---|
| Overview | Counts, training progress, recent research, scans | Mark a task done |
| Threads | Every harvested thread with source filter and search | Open the source |
| Experts | Profiles, focus, work count | Open the profile |
| Tools | Core shelf and RE/offense shelf, search | Open the repo |
| Methods | Extracted method notes and code density | Open the source |
| GitHub atlas | 2,064 repos by category and stars | Open the repo |
| Labs | Ten labs and last run status | Run the smoke test |
| Training | Progress, next tasks, journal | Mark done |
| Scans | Run a read-only scan, read reports | Scan a URL or artifact |
| Sources | Row counts per source | Find coverage gaps |

Keyboard: `/` focuses search. Theme is stored in localStorage.

## Design

Inspired by the Polar Orbit system:

- Design by subtraction. One accent, one radius scale, no gradients.
- Derived, not decorated. Spacing and type come from a single scale.
- Precision as respect. Numbers use a mono stack, columns align.
- Card borders instead of shadows. Hover is a soft background, not a lift.
- Light and dark from the same tokens.

No framework and no build step. One Python file, one HTML string, standard library only.

## Security

- Binds loopback only.
- Read-only reads for every GET.
- Two POST actions: run a lab test and run a scan.
- Scan targets are passed as list arguments, never a shell string.
- Report names are matched against `^[A-Za-z0-9._-]+\.md$`.
- Lab names are checked against a fixed list.

The dashboard has no login. Do not expose it beyond loopback without a proxy and auth.

## Limits

- A scan can take up to 300 seconds and the request waits.
- The overview loads counts from JSONL on each request. Large files add latency.
- The report renderer handles headings, links, bold and code. It does not render tables.
- The dashboard does not edit catalog rows. Use the scripts for that.

## Refresh

```bash
./beril harvest forums --sources 0x00sec,reddit,hackerone
./beril harvest tools --sources canonical
./beril train --status
```
