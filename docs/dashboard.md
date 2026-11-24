# Dashboard

![dashboard](../assets/dashboard.png)

A local dashboard for every catalog in Beril. Orbit roles, Apple HIG values, Material 3 state layers. Light and dark follow the system.

```bash
./beril dashboard
```

It binds `127.0.0.1:8788` and opens the browser. Use `--port` to change and `--no-open` on a headless host.

## Pages

Five sidebar sections. Work, Intel and Lab hold tabs, so the sidebar never grows past five items.

| Section | Tabs |
|---|---|
| Overview | Spend, running work, training, recent activity |
| Work | Jobs, Activity, Costs |
| Memory | One list of cards |
| Intel | Threads, Experts, Tools, Methods, GitHub atlas, Sources |
| Lab | Labs, Training, Posture, Scans |


| Page | What it shows | Action |
|---|---|---|
| Overview | Spend, ledger, counts, training queue, scans | Mark a task done |
| Activity | Jobs, labs, scans and journal in one stream | Open context |
| Jobs | Every job with actor, model, tokens and cost | Create, finish, inspect |
| Costs | Spend today/week/month, by model and type | Set the budget |
| Memory | 53 durable cards, confidence and freshness | Open a card |
| Threads | Every harvested thread with source filter and search | Open the source |
| Experts | Profiles, focus, work count | Open the profile |
| Tools | Core shelf and RE/offense shelf, search | Open the repo |
| Methods | Extracted method notes and code density | Open the source |
| GitHub atlas | 2,064 repos by category and stars | Open the repo |
| Labs | Ten labs and last run status | Run the smoke test |
| Training | Progress, next tasks, journal | Mark done |
| Posture | Severity trend, latest target, top checks, coverage and suppressed count from local JSON | Open a target report |
| Scans | Passive scan and report viewer | Scan a URL or artifact |
| Sources | Row counts per source | Find coverage gaps |

Keyboard: `/` filters the page, `Ctrl K` opens the go-to palette, `Ctrl \` hides the sidebar (remembered in localStorage). Click a table header to sort; click again to reverse.

## Cost tracking

Jobs store `tokens_in`, `tokens_out`, a model and `cost_usd`. The price table is `data/llm_prices.json`; unknown models cost zero until you add a rate.

```bash
./beril job log --type llm --title "Triage CVE notes" --model claude-sonnet-4.5 \
  --tokens-in 12000 --tokens-out 800 --status done
./beril job budget --set 30
```

Scans and labs create jobs automatically with zero cost. The budget is a soft bar, not a hard stop.

## Design

Three references, one system. Tokens are plain CSS custom properties at the top of `scripts/dashboard_page.py`.

- **Orbit (Polar).** Design by subtraction: one spacing scale, three radii, one accent. Colour by role: `background-*`, `text-*`, `border-*`.
- **Apple HIG.** System colours (`#0a84ff`, `#30d158`, `#ff9f0a`, `#ff453a`), 13 px base text, capsule buttons, a segmented control for the job filter, sortable columns, a hideable sidebar, blur only on the floating bars. Corners are continuous (`corner-shape: squircle`) where the browser supports it and fall back to a normal radius.
- **Material 3.** The active sidebar item is a capsule indicator on a tinted container. Hover and pressed states are 8% and 12% layers of the text colour. Modals use the extra-large 28 px corner.
- **Light and dark** follow `prefers-color-scheme`.
- No page-change animation: the sidebar and top bar stay still while the content swaps. `prefers-reduced-motion` removes the rest.
- Brand: the round avatar is `assets/avatar-round.png`, inlined as the favicon and the sidebar mark.

### Responsive

The layout reacts to the content width (container queries), not the window, so it holds inside a narrow browser pane.

| Content width | Change |
|---|---|
| under 900 px | Side panels and forms stack under the main list |
| under 700 px | KPI cards stack |
| under 640 px | Table rows become cards with labelled values |
| under 800 px window | Sidebar becomes a top strip; filter field hides |
| touch screens | 44 px targets and 16 px inputs, so iOS does not zoom |

Reference repositories used while designing (not copied): axiaoge2/apple-hig-designer (MIT), dickwu/apple-design-skill, raintree-technology/hig-doctor, and the Material Web tokens. Apple's guideline text stays Apple's.

No framework and no build step. One Python file, one HTML string, standard library only.

## Security

- Binds loopback only.
- A random per-run token is injected into the page and required as
  `X-Beril-Token` on every POST.
- `Origin`, when present, must be the loopback origin.
- CSP, `nosniff`, `DENY` frame and `no-store` headers are set.
- Read-only reads for every GET.
- POST actions: jobs, budget, lab test and scan.
- Scan targets are passed as list arguments, never a shell string.
- Report names are matched against `^[A-Za-z0-9._-]+\.md$`.
- Lab names are checked against a fixed list.

The dashboard has no login. The token stops a random local process or a
cross-site form from firing actions, not a local user. Do not expose it beyond
loopback without a proxy and auth.

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
