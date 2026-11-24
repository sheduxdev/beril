# Getting started

Beril runs on your machine. It reads files and public pages, writes Markdown and JSON, and sends nothing anywhere. This page takes you from a fresh clone to a first report you can act on.

## What you need

| Need | Detail |
|---|---|
| Python | 3.11.5 or newer |
| Disk | About 300 MB for the Camoufox browser, only if you use the research layers |
| Headless Linux | Install `xvfb` for the headful fallback |
| Platform | Linux is the tested platform. Windows and macOS artifact paths exist, but the optional toolchain is documented for Linux |

## Install

The short path installs the base tools and wraps the CLI:

```bash
git clone https://github.com/sheduxdev/beril.git
cd beril
./install.sh
```

Other flags: `./install.sh --tools` adds the specialist scanners, `./install.sh --re` adds the reverse engineering toolchain, and `./install.sh --dev` adds ruff, pyright and pytest.

With uv:

```bash
uv sync --extra dev
uv run camoufox fetch
uv run pytest
uv run python scripts/validate.py
```

With venv and pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
camoufox fetch
./beril validate
```

`pyproject.toml` is the dependency source of truth. `requirements.txt` and `requirements-re.txt` are compatibility mirrors. Other install paths are `pipx install .`, a wheel, a pinned container image and a composite GitHub Action. See [Deployment](../docs/deployment.md).

## Your first scan

Scan something you own:

```bash
./beril scan --target https://your-app.example --profile engineer
```

The scan is passive. It sends `GET` requests with a Beril user agent, reads at most 400 KB per response, honors `robots.txt`, runs at 2 requests per second with a budget of 250 requests, and backs off on 429 and 503.

It writes two files:

| File | Use |
|---|---|
| `scans/<target>.md` | The report you read |
| `scans/<target>.json` | The same evidence in the finding schema, for tools and re-rendering |

## Read the result

1. Open the Markdown report and start with the top five findings.
2. Open the card for each class in [Techniques](../references/techniques.md) and follow its confirmation step.
3. Confirm the exposure by hand with a minimal request or input. A scanner hit is a lead, not a finding.
4. Mark each finding as confirmed or inferred. Keep the evidence path.
5. Render the report for the reader. The next section lists the profiles.
6. Write down what you did not test.

## Pick a report profile

```bash
./beril scan --target https://your-app.example --profile smb --out scans/app-smb
./beril report --input scans/app.json --profile bugbounty
```

| Profile | Reader |
|---|---|
| `engineer` | A developer who will fix it |
| `bugbounty` | A program triager |
| `smb` | A small business owner, one page, with a KVKK note |
| `maintainer` | An open source maintainer |
| `cra` | A Cyber Resilience Act file |
| `json`, `sarif` | Machines. SARIF is checked against the schema |

## Go further

Active probes need an ownership record first:

```bash
./beril verify --new your-app.example
# publish the token at one of the three paths, then
./beril verify --verify your-app.example
./beril scan --target https://your-app.example --active --profile bugbounty
```

Hunt an open source repository in the networkless sandbox:

```bash
./beril hunt --target ./some-open-source-repo --sandbox --report HUNT.md
```

Run a research pass instead of a scan:

```bash
./beril harvest forums --sources 0x00sec,htb,reddit,hackerone --limit 20
./beril harvest tools --sources canonical --limit 60
./beril dossier
./beril validate
```

Then open `examples/dossier.md`.

## Next

- [How Beril works](how-beril-works.md) explains the two lines and the finding model.
- [Command reference](cli-reference.md) lists every command.
- [Safety and scope](safety-and-scope.md) is required reading before an active scan.
- [Defending](../docs/defending.md) and [Attacking](../docs/attacking.md) are the two operating guides.
