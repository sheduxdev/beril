# Beril plugin

The same skill packaged for three agents. Every command shells out to the
repository CLI, so the plugin stays thin and the evidence stays in `scans/`.

## Claude Code

Marketplace file: `.claude-plugin/marketplace.json`.

```bash
# From a clone of this repository
/plugin marketplace add /absolute/path/to/beril
/plugin install beril@beril
```

The plugin exposes `/beril:scan`, `/beril:verify`, `/beril:hunt`,
`/beril:report`, `/beril:run`, `/beril:watch`, `/beril:infra`,
`/beril:image` and `/beril:bgp`.

For a natural sentence, use `/beril:do`:

```text
/beril:do şu siteyi kır: https://app.example
/beril:do bu repoda açık bul: ./repo
/beril:do example.com haritasını çıkar
```

The plugin also ships the `beril-front-desk` agent for plain chat. Say "selam
beril, bunu kır" with a target and it should run instead of interviewing.

## Codex

Copy `plugin/codex/AGENTS.md` into the project or run:

```bash
./scripts/install_plugin.py --agent codex --dest ~/code/myapp
```

## Gemini CLI

The extension manifest is `plugin/gemini/gemini-extension.json`. Install with
the Gemini extension flow or copy the directory into the project.

```bash
./scripts/install_plugin.py --agent gemini --dest ~/code/myapp
```

## Rules

- Passive default. Active needs an ownership record.
- The plugin never runs a tool against a host without scope.
- All output goes to `scans/`.
- Read `SKILL.md` before the first real target.
