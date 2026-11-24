#!/usr/bin/env python3
"""Build the Beril docs site from the repository Markdown.

Standard library only. No network. Output goes to site/ (git-ignored).

    python3 scripts/build_docs.py            # build
    python3 scripts/build_docs.py --check    # build and fail on broken internal links
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys


def read_text(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEME = os.path.join(ROOT, "scripts", "docs_theme")
REPO = "https://github.com/sheduxdev/beril"
BRANCH = "main"
DOCS_URL = "https://sheduxdev.github.io/beril/"

# (label, blurb, entries). An entry is a repo path or a glob like "references/*.md".
NAV = [
    (
        "Start here",
        "Install it, run a first scan, learn the model, and read every command and every limit.",
        [
            "wiki/getting-started.md",
            "wiki/how-beril-works.md",
            "wiki/cli-reference.md",
            "wiki/scan-coverage.md",
            "wiki/safety-and-scope.md",
            "wiki/faq.md",
        ],
    ),
    (
        "Defend",
        "Scan what you own. Web, artifacts, secrets, MCP, supply chain, and how to report it.",
        [
            "docs/defending.md",
            "docs/scan-artifacts.md",
            "docs/secrets.md",
            "docs/mcp-supply-chain.md",
            "docs/project-health.md",
            "docs/prompt-injection.md",
            "docs/suppression.md",
            "docs/report-format.md",
            "docs/break-my-app.md",
            "docs/benchmarks.md",
        ],
    ),
    (
        "Attack and verify",
        "Hunt bugs in open source behind an ownership gate, with proof and a maintainer report.",
        [
            "docs/attacking.md",
            "docs/bug-hunt.md",
            "docs/verification.md",
            "docs/legal.md",
        ],
    ),
    (
        "Network",
        "Visibility, protection and incident runbooks for networks and BGP.",
        ["docs/network-runbook.md", "docs/bgp-runbook.md"],
    ),
    (
        "Workspace and ops",
        "The dashboard, memory, agents, automation and deployment.",
        [
            "wiki/agents-integration.md",
            "wiki/ci-and-automation.md",
            "docs/dashboard.md",
            "docs/memory.md",
            "docs/agents.md",
            "docs/automation.md",
            "docs/deployment.md",
            "docs/one-click.md",
        ],
    ),
    (
        "Learn",
        "Ten labs, a 25-week curriculum and the reverse engineering path.",
        [
            "wiki/labs-and-training.md",
            "docs/training.md",
            "docs/mastery.md",
            "docs/reverse-engineering.md",
        ],
    ),
    (
        "References",
        "Method cards, schemas, source catalogs and deep notes. Every claim links to its origin.",
        ["references/*.md"],
    ),
    (
        "Agent roles",
        "Focused role prompts the router loads.",
        ["agents/*.md"],
    ),
    (
        "Memory cards",
        "Small, tested cards an agent reads before it searches.",
        ["knowledge/*.md"],
    ),
    (
        "Project",
        "The skill file, changelog, contribution and security policy.",
        ["SKILL.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md"],
    ),
]

STATS = [
    ("556", "threads and reports"),
    ("94", "experts"),
    ("658", "tools"),
    ("2,064", "repositories in the atlas"),
    ("10", "labs"),
    ("25", "weeks of training"),
]

HTML_BLOCK = re.compile(
    r"^\s*</?(p|div|details|summary|img|a|br|table|thead|tbody|tr|td|th|center|picture|source|"
    r"h[1-6]|hr|span|sub|sup|kbd|figure|figcaption)\b",
    re.I,
)
LIST_RE = re.compile(r"^(\s*)([-*+]|\d{1,9}[.)])(\s+)(.*)$")
HR_RE = re.compile(r"^\s{0,3}([-*_])(\s*\1){2,}\s*$")
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([\w+#.-]*)")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
CALLOUT_RE = re.compile(
    r"^\s*(?:\*\*(Note|Tip|Warning|Important|Caution|Danger)\b[:.]?\*\*|\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\])\s*",
    re.I,
)


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\- ]+", "", text.strip().lower()).replace(" ", "-")
    return text or "section"


class Page:
    def __init__(self, src: str, group: str) -> None:
        self.src = src
        self.group = group
        self.out = self._out(src)
        self.title = ""
        self.meta: dict[str, str] = {}
        self.body = ""
        self.heads: list[tuple[int, str, str]] = []
        self.text = ""

    @staticmethod
    def _out(src: str) -> str:
        if src == "README.md":
            return "index.html"
        stem = os.path.splitext(src)[0]
        out = re.sub(r"\.md$", ".html", src)
        return out.lower() if stem.split("/")[-1].isupper() else out


Groups = list[tuple[str, str, list["Page"]]]


class Site:
    def __init__(self) -> None:
        self.pages: list[Page] = []
        self.by_src: dict[str, Page] = {}
        self.warnings: list[str] = []
        self.copied: set[str] = set()
        self.out_dir = ""

    # -- link resolution ----------------------------------------------------
    def resolve(self, href: str, page: Page) -> str:
        if re.match(r"^(https?:|mailto:|tel:|#|data:)", href):
            return href
        path, _, frag = href.partition("#")
        if not path:
            return "#" + frag
        target = os.path.normpath(os.path.join(os.path.dirname(page.src), path)).replace(os.sep, "/")
        frag = ("#" + frag) if frag else ""
        if target in self.by_src:
            return (
                os.path.relpath(self.by_src[target].out, os.path.dirname(page.out) or ".").replace(os.sep, "/") + frag
            )
        full = os.path.join(ROOT, target)
        if os.path.isdir(full):
            return f"{REPO}/tree/{BRANCH}/{target}"
        if os.path.isfile(full):
            return f"{REPO}/blob/{BRANCH}/{target}{frag}"
        self.warnings.append(f"{page.src}: broken link {href}")
        return href

    def asset(self, src: str, page: Page) -> str:
        if re.match(r"^(https?:|data:)", src):
            return src
        target = os.path.normpath(os.path.join(os.path.dirname(page.src), src)).replace(os.sep, "/")
        full = os.path.join(ROOT, target)
        if not os.path.isfile(full):
            self.warnings.append(f"{page.src}: missing image {src}")
            return src
        dest = os.path.join("files", target)
        self.copied.add(target)
        return os.path.relpath(dest, os.path.dirname(page.out) or ".").replace(os.sep, "/")


# -- Markdown -----------------------------------------------------------------
def esc(s: str) -> str:
    return html.escape(s, quote=False)


def inline(s: str, site: Site, page: Page) -> str:
    codes: list[str] = []

    def hold(m: re.Match) -> str:
        codes.append(m.group(2).strip())
        return f"\x00{len(codes) - 1}\x00"

    s = re.sub(r"(`+)(.+?)\1", hold, s)
    s = esc(s)
    s = re.sub(
        r"&lt;(/?)(br|kbd|sub|sup|b|i|em|strong)\s*/?&gt;", lambda m: f"<{m.group(1)}{m.group(2)}>", s, flags=re.I
    )

    def img(m: re.Match) -> str:
        return f'<img src="{html.escape(site.asset(m.group(2), page), quote=True)}" alt="{html.escape(m.group(1), quote=True)}" loading="lazy">'

    s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+&quot;[^)]*?&quot;|\s+\"[^)]*?\")?\)", img, s)

    def link(m: re.Match) -> str:
        href = site.resolve(html.unescape(m.group(2)), page)
        ext = re.match(r"^https?:", href) is not None
        extra = ' target="_blank" rel="noopener"' if ext else ""
        return f'<a href="{html.escape(href, quote=True)}"{extra}>{m.group(1)}</a>'

    s = re.sub(r"\[((?:[^\[\]]|<[^>]*>)+)\]\(([^)\s]+)(?:\s+(?:&quot;|\")[^)]*?(?:&quot;|\"))?\)", link, s)
    s = re.sub(
        r"(?<![\"'>=(/\w])(https?://[^\s<)]+[^\s<).,;:])",
        lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>',
        s,
    )
    s = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*(?=\S)(.+?)(?<=\S)\*(?![\*\w])", r"<em>\1</em>", s)
    s = re.sub(r"(?<!\w)_(?=\S)(.+?)(?<=\S)_(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"~~(?=\S)(.+?)(?<=\S)~~", r"<del>\1</del>", s)
    s = re.sub(r"( {2,}|\\)\n", "<br>\n", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{esc(codes[int(m.group(1))])}</code>", s)


def split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, cur, code, i = [], "", False, 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if ch == "`":
            code = not code
        if ch == "|" and not code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def table_cell(tag: str, txt: str, idx: int, aligns: list[str], site: Site, page: Page) -> str:
    a = aligns[idx] if idx < len(aligns) and aligns[idx] else ""
    st = f' style="text-align:{a}"' if a else ""
    return f"<{tag}{st}>{inline(txt, site, page)}</{tag}>"


def indent_of(line: str) -> int:
    return len(line.expandtabs(4)) - len(line.expandtabs(4).lstrip(" "))


def is_block_start(lines: list[str], i: int) -> bool:
    ln = lines[i]
    if FENCE_RE.match(ln) or HEAD_RE.match(ln) or HR_RE.match(ln) or ln.lstrip().startswith(">"):
        return True
    if LIST_RE.match(ln) and not HR_RE.match(ln):
        return True
    if "|" in ln and i + 1 < len(lines) and SEP_RE.match(lines[i + 1]) and "-" in lines[i + 1]:
        return True
    return bool(HTML_BLOCK.match(ln))


def render_blocks(lines: list[str], site: Site, page: Page, tight: bool = False, top: bool = False) -> str:
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        m = FENCE_RE.match(ln)
        if m:
            fence, lang = m.group(2), m.group(3)
            ind = len(m.group(1))
            i += 1
            buf = []
            while i < n and not re.match(r"^\s*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", lines[i]):
                buf.append(lines[i][ind:] if lines[i][:ind].strip() == "" else lines[i])
                i += 1
            i += 1
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f'<pre data-lang="{html.escape(lang)}"><code{cls}>{esc(chr(10).join(buf))}</code></pre>')
            continue
        m = HEAD_RE.match(ln)
        if m:
            level, text = len(m.group(1)), m.group(2)
            body = inline(text, site, page)
            plain = re.sub(r"<[^>]+>", "", html.unescape(body))
            hid = slugify(plain)
            used = page.__dict__.setdefault("_ids", {})
            k = used.get(hid, 0)
            used[hid] = k + 1
            if k:
                hid = f"{hid}-{k}"
            if top and level == 1 and not page.title:
                page.title = plain
            if level in (2, 3):
                page.heads.append((level, plain, hid))
            out.append(
                f'<h{level} id="{hid}">{body}<a class="anchor" href="#{hid}" aria-label="Link to this section">#</a></h{level}>'
            )
            i += 1
            continue
        if HR_RE.match(ln):
            out.append("<hr>")
            i += 1
            continue
        if "|" in ln and i + 1 < n and SEP_RE.match(lines[i + 1]) and "-" in lines[i + 1]:
            head = split_row(ln)
            aligns = []
            for c in split_row(lines[i + 1]):
                aligns.append("center" if c.startswith(":") and c.endswith(":") else "right" if c.endswith(":") else "")
            i += 2
            rows = []
            while i < n and lines[i].strip() and "|" in lines[i]:
                rows.append(split_row(lines[i]))
                i += 1

            thead = "<tr>" + "".join(table_cell("th", c, j, aligns, site, page) for j, c in enumerate(head)) + "</tr>"
            tbody = "".join(
                "<tr>" + "".join(table_cell("td", c, j, aligns, site, page) for j, c in enumerate(r)) + "</tr>"
                for r in rows
            )
            out.append(f'<div class="table-wrap"><table><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>')
            continue
        if ln.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            kind = ""
            cm = CALLOUT_RE.match(buf[0]) if buf else None
            if cm:
                kind = (cm.group(1) or cm.group(2)).lower()
                buf[0] = buf[0][cm.end() :]
                if kind in ("important", "caution"):
                    kind = "warning" if kind == "caution" else "note"
            inner = render_blocks(buf, site, page)
            if kind:
                out.append(
                    f'<div class="callout callout-{kind}"><div class="callout-title">{kind.capitalize()}</div>{inner}</div>'
                )
            else:
                out.append(f"<blockquote>{inner}</blockquote>")
            continue
        m = LIST_RE.match(ln)
        if m and not HR_RE.match(ln):
            html_list, i = parse_list(lines, i, site, page)
            out.append(html_list)
            continue
        if HTML_BLOCK.match(ln):
            buf = []
            while i < n and lines[i].strip():
                buf.append(lines[i])
                i += 1
            out.append("\n".join(buf))
            continue
        buf = []
        while i < n and lines[i].strip() and not (buf and is_block_start(lines, i)):
            buf.append(lines[i])
            i += 1
        text = inline("\n".join(s.rstrip() if k == len(buf) - 1 else s for k, s in enumerate(buf)), site, page)
        out.append(text if tight and not out else f"<p>{text}</p>")
    return "\n".join(out)


def parse_list(lines: list[str], i: int, site: Site, page: Page) -> tuple[str, int]:
    n = len(lines)
    m = LIST_RE.match(lines[i])
    assert m
    indent = indent_of(lines[i])
    ordered = m.group(2)[0].isdigit()
    start = int(m.group(2)[:-1]) if ordered else 1
    items: list[list[str]] = []
    loose = False
    while i < n:
        m = LIST_RE.match(lines[i])
        if not m or HR_RE.match(lines[i]) or indent_of(lines[i]) != indent or m.group(2)[0].isdigit() != ordered:
            break
        content = indent + len(m.group(2)) + len(m.group(3))
        body = [m.group(4)]
        i += 1
        while i < n:
            ln = lines[i]
            if not ln.strip():
                j = i
                while j < n and not lines[j].strip():
                    j += 1
                if j >= n:
                    i = j
                    break
                if indent_of(lines[j]) >= content:
                    body.extend([""] * (j - i))
                    i = j
                    loose = True
                    continue
                sib = LIST_RE.match(lines[j])
                if sib and indent_of(lines[j]) == indent and sib.group(2)[0].isdigit() == ordered:
                    loose = True
                    i = j
                break
            ind = indent_of(ln)
            if ind >= content:
                body.append(ln.expandtabs(4)[content:])
                i += 1
            elif ind <= indent and (LIST_RE.match(ln) or is_block_start(lines, i)):
                break
            else:
                body.append(ln.strip())
                i += 1
        items.append(body)
    tag = "ol" if ordered else "ul"
    attr = f' start="{start}"' if ordered and start != 1 else ""
    li = []
    for body in items:
        task = ""
        if body and re.match(r"^\[( |x|X)\]\s", body[0]):
            done = body[0][1] in "xX"
            task = f'<input type="checkbox" disabled{" checked" if done else ""}> '
            body[0] = body[0][4:]
        li.append(f"<li>{task}{render_blocks(body, site, page, tight=not loose)}</li>")
    return f"<{tag}{attr}>" + "".join(li) + f"</{tag}>", i


def parse_front(text: str) -> tuple[dict[str, str], str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            meta = {}
            for line in text[4:end].splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
            return meta, text[end + 4 :].lstrip("\n")
    return {}, text


# -- Collect ------------------------------------------------------------------
def humanize(path: str) -> str:
    return os.path.splitext(os.path.basename(path))[0].replace("-", " ").replace("_", " ").capitalize()


def collect(site: Site) -> list[tuple[str, str, list[Page]]]:
    groups = []
    seen: set[str] = set()
    for label, blurb, entries in NAV:
        pages: list[Page] = []
        for e in entries:
            if "*" in e:
                d = os.path.dirname(e)
                files = sorted(f for f in os.listdir(os.path.join(ROOT, d)) if f.endswith(".md"))
                paths = [f"{d}/{f}" for f in files]
            else:
                paths = [e]
            for p in paths:
                if p in seen:
                    continue
                if not os.path.isfile(os.path.join(ROOT, p)):
                    site.warnings.append(f"nav: missing {p}")
                    continue
                seen.add(p)
                pg = Page(p, label)
                pages.append(pg)
        if pages:
            groups.append((label, blurb, pages))
    # leftovers in docs/ and wiki/
    extra = []
    for d in ("docs", "wiki"):
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            p = f"{d}/{f}"
            if f.endswith(".md") and p not in seen:
                extra.append(Page(p, "More docs"))
    if extra:
        groups.append(("More docs", "Other guides.", extra))
    for _, _, pages in groups:
        for pg in pages:
            site.pages.append(pg)
            site.by_src[pg.src] = pg
    site.by_src["README.md"] = Page("README.md", "Home")
    return groups


def render_page(site: Site, pg: Page) -> None:
    raw = read_text(os.path.join(ROOT, pg.src))
    pg.meta, text = parse_front(raw)
    body = render_blocks(text.split("\n"), site, pg, top=True)
    pg.title = pg.meta.get("title") or pg.title or humanize(pg.src)
    # the page template prints the title; drop a leading H1 from the body
    body = re.sub(r"^<h1 id=\"[^\"]*\">.*?</h1>\n?", "", body, count=1, flags=re.S)
    pg.body = body
    plain = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S)
    plain = html.unescape(re.sub(r"<[^>]+>", " ", plain))
    pg.text = re.sub(r"\s+", " ", plain).strip()


# -- Output -------------------------------------------------------------------
def rootpath(out: str) -> str:
    depth = out.count("/")
    return "../" * depth if depth else "./"


def sidebar(groups: Groups, current: Page | None, root: str) -> str:
    parts = ['<nav class="nav" aria-label="Documentation">']
    parts.append(f'<a class="nav-home{" on" if current is None else ""}" href="{root}index.html">Home</a>')
    for label, _, pages in groups:
        is_open = current is not None and current.group == label
        parts.append(
            f'<details class="grp"{" open" if is_open or label == "Start here" else ""}><summary>{esc(label)}<span>{len(pages)}</span></summary>'
        )
        for p in pages:
            on = " on" if current is not None and p.src == current.src else ""
            parts.append(f'<a class="{on.strip()}" href="{root}{p.out}">{esc(p.title)}</a>')
        parts.append("</details>")
    parts.append("</nav>")
    return "\n".join(parts)


def shell(title: str, desc: str, body: str, side: str, root: str, toc: str = "", cls: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta name="color-scheme" content="dark light">
<meta name="root" content="{root}">
<link rel="icon" type="image/png" href="{root}assets/avatar.png">
<link rel="stylesheet" href="{root}assets/docs.css">
</head>
<body class="{cls}">
<header class="top">
  <button class="icon-btn menu" id="menu" aria-label="Open navigation" aria-expanded="false"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M3 5h12M3 9h12M3 13h12"/></svg></button>
  <a class="brand" href="{root}index.html"><img src="{root}assets/avatar.png" alt="" width="28" height="28"><span>Beril</span><small>docs</small></a>
  <button class="searchbtn" id="searchbtn" aria-label="Search the docs"><svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5 14 14"/></svg><span>Search</span><kbd>Ctrl K</kbd></button>
  <a class="gh" href="{REPO}" target="_blank" rel="noopener">GitHub</a>
  <button class="icon-btn" id="theme" aria-label="Switch theme" title="Theme"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="5.5"/><path d="M8 2.5v11" /><path d="M8 2.5a5.5 5.5 0 0 1 0 11z" fill="currentColor"/></svg></button>
</header>
<div class="layout">
<aside class="side" id="side">{side}</aside>
<main class="main" id="main">{body}</main>
{toc}
</div>
<div class="scrim" id="scrim"></div>
<div class="pal" id="pal" hidden><div class="pal-box" role="dialog" aria-label="Search"><input id="palin" placeholder="Search the docs" autocomplete="off" aria-label="Search the docs"><div class="pal-list" id="pallist"></div></div></div>
<script src="{root}assets/search-index.js"></script>
<script src="{root}assets/docs.js"></script>
</body>
</html>
"""


def page_html(site: Site, groups: Groups, flat: list[Page], pg: Page) -> str:
    root = rootpath(pg.out)
    idx = flat.index(pg)
    prev = flat[idx - 1] if idx > 0 else None
    nxt = flat[idx + 1] if idx + 1 < len(flat) else None
    toc_items = "".join(f'<a class="l{lvl}" href="#{i}">{esc(t)}</a>' for lvl, t, i in pg.heads)
    toc = (
        f'<aside class="toc" aria-label="On this page"><p>On this page</p>{toc_items}</aside>'
        if pg.heads
        else '<aside class="toc"></aside>'
    )
    meta = ""
    if pg.meta:
        pills = []
        for k in ("confidence", "updated", "status"):
            if pg.meta.get(k):
                pills.append(f'<span class="pill">{esc(k)}: {esc(pg.meta[k])}</span>')
        for t in (pg.meta.get("tags") or "").split(","):
            if t.strip():
                pills.append(f'<span class="pill tag">{esc(t.strip())}</span>')
        if pills:
            meta = f'<div class="pills">{"".join(pills)}</div>'
    pager = '<nav class="pager">'
    pager += (
        f'<a class="prev" href="{root}{prev.out}"><small>Previous</small><span>{esc(prev.title)}</span></a>'
        if prev
        else "<span></span>"
    )
    pager += (
        f'<a class="next" href="{root}{nxt.out}"><small>Next</small><span>{esc(nxt.title)}</span></a>'
        if nxt
        else "<span></span>"
    )
    pager += "</nav>"
    edit = f"{REPO}/edit/{BRANCH}/{pg.src}"
    body = (
        f'<article class="doc"><p class="crumb">{esc(pg.group)}</p><h1>{esc(pg.title)}</h1>{meta}{pg.body}'
        f'<footer class="docfoot"><a href="{edit}" target="_blank" rel="noopener">Edit this page on GitHub</a></footer>{pager}</article>'
    )
    return shell(f"{pg.title} | Beril docs", pg.text[:160], body, sidebar(groups, pg, root), root, toc)


def home_html(groups: Groups, version: str, first: str) -> str:
    root = "./"
    cards = "".join(
        f'<a class="card" href="{pages[0].out}"><h3>{esc(label)}</h3><p>{esc(blurb)}</p><span>{len(pages)} pages</span></a>'
        for label, blurb, pages in groups
    )
    stats = "".join(f"<div><b>{n}</b><span>{esc(t)}</span></div>" for n, t in STATS)
    body = f"""<section class="hero">
  <img class="hero-av" src="assets/avatar.png" alt="" width="96" height="96">
  <p class="eyebrow">Version {esc(version)} · local first · MIT</p>
  <h1>Beril</h1>
  <p class="lead">A cybersecurity skill for agents and people. Scan what you own, hunt bugs in open source behind an ownership gate, and turn evidence into a report a reader can act on.</p>
  <div class="cta"><a class="btn primary" href="{first}">Get started</a><a class="btn" href="{REPO}" target="_blank" rel="noopener">View on GitHub</a></div>
  <pre class="hero-code" data-lang="bash"><code>git clone https://github.com/sheduxdev/beril.git
cd beril &amp;&amp; ./install.sh
./beril scan --target https://your-app.example</code></pre>
</section>
<section class="stats">{stats}</section>
<section class="cards">{cards}</section>
<section class="two">
  <div><h2>Two lines, one finding model</h2><p>The defense line returns a ranked fix list. The attack line hunts open source behind an ownership record, a scope file and a networkless sandbox. Both write severity, confidence, evidence, impact, a fix and a plain statement of what was not tested.</p></div>
  <div><h2>Local first</h2><p>No backend, no telemetry. Catalogs are dated files with a public URL on every row. The dashboard binds loopback only. Posting to a program or a ticket stays manual.</p></div>
</section>"""
    return shell(
        "Beril docs",
        "Documentation for Beril, a local-first cybersecurity intelligence and assessment skill.",
        body,
        sidebar(groups, None, root),
        root,
        "",
        "home",
    )


def build(out_dir: str, check: bool) -> int:
    site = Site()
    site.out_dir = out_dir
    groups = collect(site)
    for pg in site.pages:
        render_page(site, pg)
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(os.path.join(out_dir, "assets"))
    flat = [p for _, _, pages in groups for p in pages]
    version = "1.4.0"
    try:
        m = re.search(r'^version\s*=\s*"([^"]+)"', read_text(os.path.join(ROOT, "pyproject.toml")), re.M)
        version = m.group(1) if m else version
    except OSError:
        pass
    for pg in flat:
        dest = os.path.join(out_dir, pg.out)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        write_text(dest, page_html(site, groups, flat, pg))
    first = flat[0].out if flat else "#"
    write_text(os.path.join(out_dir, "index.html"), home_html(groups, version, first))
    nf = shell(
        "Not found | Beril docs",
        "Page not found.",
        '<article class="doc"><h1>Page not found</h1><p>That page moved or never existed. <a href="/">Back to the docs home</a>.</p></article>',
        "",
        "./",
        "",
        "",
    )
    write_text(os.path.join(out_dir, "404.html"), nf)
    # theme
    light = read_text(os.path.join(THEME, "light.css"))
    css = read_text(os.path.join(THEME, "style.css")).replace("/*LIGHT*/", light)
    write_text(os.path.join(out_dir, "assets", "docs.css"), css)
    shutil.copy(os.path.join(THEME, "app.js"), os.path.join(out_dir, "assets", "docs.js"))
    avatar = os.path.join(ROOT, "assets", "avatar-round.png")
    if os.path.isfile(avatar):
        shutil.copy(avatar, os.path.join(out_dir, "assets", "avatar.png"))
    # search index
    index = [
        {"t": p.title, "u": p.out, "g": p.group, "h": [h[1] for h in p.heads][:24], "x": p.text[:700]} for p in flat
    ]
    write_text(
        os.path.join(out_dir, "assets", "search-index.js"),
        "window.BERIL_SEARCH=" + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ";",
    )
    for rel in site.copied:
        dest = os.path.join(out_dir, "files", rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(os.path.join(ROOT, rel), dest)
    write_text(os.path.join(out_dir, ".nojekyll"), "")
    print(f"built {len(flat)} pages into {os.path.relpath(out_dir, ROOT)}")
    for w in site.warnings:
        print("warn:", w, file=sys.stderr)
    return 1 if (check and site.warnings) else 0


# -- GitHub wiki export ---------------------------------------------------------
RAW = f"https://raw.githubusercontent.com/sheduxdev/beril/{BRANCH}"
WIKI_LINK = re.compile(r"(?<!!)\[((?:[^\[\]])+)\]\(([^)\s]+)\)")
WIKI_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")


def wiki_name(title: str, used: set[str]) -> str:
    base = re.sub(r"[^\w]+", "-", title).strip("-") or "Page"
    name, k = base, 2
    while name.lower() in used:
        name = f"{base}-{k}"
        k += 1
    used.add(name.lower())
    return name


def wiki_rewrite(text: str, page: Page, names: dict[str, str]) -> str:
    """Point relative links at wiki pages or GitHub, and images at raw files."""

    def target(href: str) -> tuple[str, str]:
        path, _, frag = href.partition("#")
        full = os.path.normpath(os.path.join(os.path.dirname(page.src), path)).replace(os.sep, "/")
        return full, ("#" + frag) if frag else ""

    def img(m: re.Match) -> str:
        href = m.group(2)
        if re.match(r"^(https?:|data:)", href):
            return m.group(0)
        full, _ = target(href)
        return f"![{m.group(1)}]({RAW}/{full})"

    def link(m: re.Match) -> str:
        href = m.group(2)
        if re.match(r"^(https?:|mailto:|tel:|#)", href):
            return m.group(0)
        full, frag = target(href)
        if full in names:
            return f"[{m.group(1)}]({names[full]}{frag})"
        if os.path.isdir(os.path.join(ROOT, full)):
            return f"[{m.group(1)}]({REPO}/tree/{BRANCH}/{full})"
        return f"[{m.group(1)}]({REPO}/blob/{BRANCH}/{full}{frag})"

    out, fenced = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            fenced = not fenced
        elif not fenced:
            line = WIKI_LINK.sub(link, WIKI_IMG.sub(img, line))
        out.append(line)
    return "\n".join(out)


def export_wiki(out_dir: str) -> int:
    site = Site()
    groups = collect(site)
    for pg in site.pages:
        render_page(site, pg)
    used: set[str] = {"home", "_sidebar", "_footer"}
    names = {pg.src: wiki_name(pg.title, used) for pg in site.pages}
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    for pg in site.pages:
        _, text = parse_front(read_text(os.path.join(ROOT, pg.src)))
        text = re.sub(r"^# .*\n+", "", text, count=1)
        body = f"> Source: [`{pg.src}`]({REPO}/blob/{BRANCH}/{pg.src}). Rendered docs: {DOCS_URL}\n\n"
        write_text(
            os.path.join(out_dir, names[pg.src] + ".md"), f"# {pg.title}\n\n" + body + wiki_rewrite(text, pg, names)
        )
    side = [f"**[Home](Home)** · [Docs site]({DOCS_URL})", ""]
    home = [
        "# Beril wiki",
        "",
        "A local-first cybersecurity skill for agents and people. Scan what you own, hunt bugs in open source behind an ownership gate, and report with evidence.",
        "",
        f"Prefer a searchable reader? Use the [docs site]({DOCS_URL}). The pages below mirror it.",
        "",
    ]
    for label, blurb, pages in groups:
        links = [f"- [{p.title}]({names[p.src]})" for p in pages]
        big = len(pages) > 12
        side += (
            [f"<details><summary><b>{label}</b> ({len(pages)})</summary>", "", *links, "", "</details>"]
            if big
            else [f"**{label}**", "", *links]
        )
        side.append("")
        home += (
            [f"## {label}", "", blurb, ""]
            + ([f"{len(pages)} pages. Start with [{pages[0].title}]({names[pages[0].src]})."] if big else links)
            + [""]
        )
    write_text(os.path.join(out_dir, "Home.md"), "\n".join(home))
    write_text(os.path.join(out_dir, "_Sidebar.md"), "\n".join(side))
    write_text(
        os.path.join(out_dir, "_Footer.md"),
        f"Generated from the repository by `scripts/build_docs.py --wiki`. Edit the source pages, not this wiki. [Docs site]({DOCS_URL}) · [Repository]({REPO})",
    )
    print(f"exported {len(site.pages)} wiki pages into {os.path.relpath(out_dir, ROOT)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=os.path.join(ROOT, "site"))
    ap.add_argument("--check", action="store_true", help="exit 1 on broken internal links")
    ap.add_argument("--wiki", metavar="DIR", help="export GitHub wiki pages into DIR instead of building the site")
    a = ap.parse_args()
    if a.wiki:
        return export_wiki(os.path.abspath(a.wiki))
    return build(os.path.abspath(a.out), a.check)


if __name__ == "__main__":
    raise SystemExit(main())
