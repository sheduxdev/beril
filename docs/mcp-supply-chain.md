# MCP, skill and plugin supply chain

`beril mcp` reads MCP client configs and, since 1.4.0, the manifests around
agents: `plugin.json`, `gemini-extension.json`, `marketplace.json`, `SKILL.md`,
`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `OPENAI.md` and `.cursor/rules/*.mdc`.

It never launches a server. A hit is a review lead.

## Config checks

- Unpinned `npx`/`uvx` package.
- Remote transport over plain HTTP.
- Plain API key in an env block.
- Root, home or Docker socket mount.
- Privileged container or a relaxed sandbox flag.
- Tool description that reads like an injected instruction.

## Manifest and instruction checks

| Check | Why |
|---|---|
| `mcp.supply.manifest-version` | A host cannot pin what has no version |
| `mcp.supply.manifest-license` | No licence, no clear reuse |
| `mcp.supply.manifest-repository` | No source to diff against |
| `mcp.supply.unpinned-npx-launch` | `npx -y pkg` runs whatever is current |
| `mcp.supply.curl-piped-to-a-shell` | The script runs before it is read |
| `mcp.supply.skill-allows-any-bash` | `allowed-tools: Bash` has no boundary |
| `mcp.supply.postinstall-script-present` | Install runs code |
| `mcp.supply.remote-plugin-source` | A remote source can change |

```bash
./beril mcp --target .
./beril mcp --target ~/.config/Claude --json
./beril mcp --target . --suppress .berilignore
```

## Limits

- A pinned version is not a reviewed version.
- The scanner does not resolve the package, read its tarball or check a
  registry signature.
- It does not detect a malicious description that stays under the pattern list.
- Manifest fields are checked for presence, not for a valid semver or URL.
