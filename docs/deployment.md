# Install and deploy

Beril runs from a git checkout, a wheel, pipx, a container or a GitHub Action.
The CLI itself makes no network request unless a command asks for one.

## Requirements

- Python 3.10 or newer.
- Linux, macOS or Windows. The test matrix is advisory outside Linux.
- Optional external binaries for `beril run`, `image` and `re` are detected,
  never bundled.

## pipx

```bash
pipx install .
beril help
```

Data and references install under the pipx venv at `share/beril`. To point at
another copy:

```bash
export BERIL_DATA=/srv/beril/data
export BERIL_REFERENCES=/srv/beril/references
```

`BERIL_DOCS` overrides the prose directory used by `beril validate` and
`BERIL_BENCHMARKS` the corpus used by `beril benchmark`.

## Wheel

```bash
python -m build --wheel
python -m venv .venv-beril
.venv-beril/bin/pip install dist/beril-1.4.0-py3-none-any.whl
.venv-beril/bin/beril validate
```

The wheel carries `scripts`, `data`, `references`, `docs` and `agents`. The
`tests` directory is not shipped. A bare `pip install` without a venv is fine
but harder to remove.

## Container

The base image is pinned by digest. The process runs as uid 10001.

```bash
docker build -t beril .
docker run --rm --network none -v "$PWD:/work:ro" beril scan --target /work --out /tmp/scan
```

`--network none` proves the scan path is offline. Mount the source read-only and
write reports to a second mount. The output directory must be writable by uid
10001; `chmod 777` on a throwaway directory is enough.

`--render` needs the browser layer:

```bash
docker build --build-arg WITH_BROWSER=1 -t beril:browser .
```

That image is much larger and the browser download happens at build time.

## GitHub Action

`.github/workflows` example: `examples/github-action.yml`. The action is a
composite that installs the checkout and runs `beril scan` on the workspace. It
enables SARIF by default and fails at `high`.

```yaml
- uses: sheduxdev/beril@<full-commit-sha>
  with:
    target: .
    fail-on: high
```

Every `uses:` line in this repository is pinned to a full commit SHA. The action
does not fetch KEV, EPSS or OSV; pass `--online-deps` through `args` when the
runner may reach the network.

## Offline defaults

- `deps`, `secrets`, `mcp`, `jar`, `vibe`, `infra`, `netcheck` and `sbom` read
  local files only.
- `scan` against a path is local. A URL target needs the network to reach it.
- `feeds`, `priority --update`, `deps --online` and `beril run` active adapters
  are the online paths.
- `--render` adds a browser pass and is slower.

## Boundary

- PyPI publication is a manual release step; the version here is the source.
- Homebrew and Kali packaging need notability this project does not have yet.
- The container has no vulnerability database. Trivy, Grype and Syft must be
  installed or run from their own images.
