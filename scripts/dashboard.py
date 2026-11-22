#!/usr/bin/env python3
"""Local Beril dashboard. Read-only except scan and lab actions.

    ./beril dashboard --port 8788
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import subprocess
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SCANS = os.path.join(ROOT, "scans")
RUNS = os.path.join(ROOT, "training", "lab_runs.json")
LABS = ["web", "binary", "fuzz", "re", "mobile", "firmware", "cloud", "ad", "llm", "detection"]
REPORT_RE = re.compile(r"^[A-Za-z0-9._-]+\.md$")
LOCK = threading.Lock()


def rows(name: str) -> list[dict]:
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def stats() -> dict:
    threads = rows("threads.jsonl")
    experts = rows("experts.jsonl")
    tools = rows("canonical_tools.jsonl") + rows("re_tools.jsonl")
    methods = rows("methods.jsonl")
    atlas = rows("github_atlas.jsonl")
    return {"threads": len(threads), "experts": len(experts), "tools": len(tools),
            "methods": len(methods), "atlas": len(atlas),
            "sources": len({r.get("source", "") for r in threads})}


def training() -> dict:
    path = os.path.join(ROOT, "training", "progress.json")
    state = {"done": [], "journal": []}
    if os.path.exists(path):
        try:
            state = json.load(open(path))
        except json.JSONDecodeError:
            pass
    cur = json.load(open(os.path.join(DATA, "curriculum.json")))
    tasks = []
    for w in cur["weeks"]:
        tasks += w["drills"] + [{**w["deliverable"], "week": w["week"]}]
        for t in w["drills"]:
            t["week"] = w["week"]
    done = len([t for t in tasks if t["key"] in state["done"]])
    nxt = [t for t in tasks if t["key"] not in state["done"]][:5]
    return {"done": done, "total": len(tasks), "pct": done * 100 // max(1, len(tasks)),
            "next": nxt, "journal": state.get("journal", [])[-8:], "weeks": cur["weeks"]}


def lab_runs() -> dict:
    if not os.path.exists(RUNS):
        return {}
    try:
        return json.load(open(RUNS))
    except json.JSONDecodeError:
        return {}


def list_scans() -> list[dict]:
    if not os.path.isdir(SCANS):
        return []
    out = []
    for name in sorted(os.listdir(SCANS), reverse=True):
        if name.endswith(".md"):
            p = os.path.join(SCANS, name)
            out.append({"name": name, "size": os.path.getsize(p),
                        "mtime": dt.datetime.fromtimestamp(os.path.getmtime(p)).isoformat(timespec="minutes")})
    return out


def md_render(text: str) -> str:
    out, in_code = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            out.append("<pre>" if in_code else "</pre>")
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        line = html.escape(line)
        line = re.sub(r"^### (.*)", r"<h3>\1</h3>", line)
        line = re.sub(r"^## (.*)", r"<h2>\1</h2>", line)
        line = re.sub(r"^# (.*)", r"<h1>\1</h1>", line)
        line = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank">\1</a>', line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
        if line.startswith("- "):
            line = "<li>" + line[2:] + "</li>"
        out.append(line)
    return "\n".join(out)


def run_scan(target: str) -> dict:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", target)[:60]
    out = os.path.join(SCANS, f"dash-{stamp}-{slug}")
    os.makedirs(SCANS, exist_ok=True)
    cmd = [os.path.join(ROOT, ".venv", "bin", "python"), os.path.join(ROOT, "scripts", "scan.py"),
           "--target", target, "--out", out]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=ROOT, errors="replace")
        return {"ok": p.returncode == 0, "report": os.path.basename(out) + ".md",
                "output": (p.stdout or p.stderr)[-4000:]}
    except Exception as exc:
        return {"ok": False, "output": f"{type(exc).__name__}: {exc}"}


def run_lab(name: str) -> dict:
    if name not in LABS:
        return {"ok": False, "output": "unknown lab"}
    try:
        p = subprocess.run(["bash", os.path.join(ROOT, "labs", name, "tests.sh")],
                           capture_output=True, text=True, timeout=300, cwd=ROOT, errors="replace")
        res = {"ok": p.returncode == 0, "output": (p.stdout or p.stderr)[-4000:],
               "at": dt.datetime.now().isoformat(timespec="minutes")}
    except Exception as exc:
        res = {"ok": False, "output": f"{type(exc).__name__}: {exc}"}
    with LOCK:
        data = lab_runs()
        data[name] = res
        os.makedirs(os.path.dirname(RUNS), exist_ok=True)
        json.dump(data, open(RUNS, "w"), indent=1)
    return res


def filter_rows(items: list[dict], q: str, limit: int, offset: int) -> list[dict]:
    if q:
        ql = q.lower()
        items = [r for r in items if ql in json.dumps(r, ensure_ascii=False).lower()]
    return items[offset: offset + limit]


class Handler(BaseHTTPRequestHandler):
    server_version = "BerilDash/1"

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))

    def json(self, data, code=200):
        raw = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def html(self, text):
        raw = text.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def body(self) -> dict:
        n = int(self.headers.get("Content-Length", 0))
        if not n:
            return {}
        try:
            return json.loads(self.rfile.read(n))
        except json.JSONDecodeError:
            return {}

    def do_GET(self):
        p = urllib.parse.urlsplit(self.path)
        q = urllib.parse.parse_qs(p.query)
        path = p.path

        if path == "/":
            return self.html(PAGE)
        if path == "/api/overview":
            return self.json({"stats": stats(), "training": training(), "labs": lab_runs(),
                              "scans": list_scans()[:6], "recent": rows("threads.jsonl")[:8],
                              "thread_sources": {}})
        if path == "/api/threads":
            items = rows("threads.jsonl")
            src = q.get("source", [""])[0]
            if src:
                items = [r for r in items if r.get("source") == src]
            return self.json(filter_rows(items, q.get("q", [""])[0], int(q.get("limit", [50])[0]), int(q.get("offset", [0])[0])))
        if path == "/api/experts":
            return self.json(filter_rows(rows("experts.jsonl"), q.get("q", [""])[0], 200, 0))
        if path == "/api/tools":
            kind = q.get("kind", ["re"])[0]
            name = {"re": "re_tools.jsonl", "canonical": "canonical_tools.jsonl"}.get(kind, "re_tools.jsonl")
            items = rows(name)
            cat = q.get("category", [""])[0]
            if cat:
                items = [r for r in items if r.get("category") == cat]
            return self.json(filter_rows(items, q.get("q", [""])[0], 300, 0))
        if path == "/api/atlas":
            items = rows("github_atlas.jsonl")
            cat = q.get("category", [""])[0]
            if cat:
                items = [r for r in items if cat in r.get("categories", [])]
            return self.json(filter_rows(items, q.get("q", [""])[0], 200, 0))
        if path == "/api/methods":
            return self.json(filter_rows(rows("method_details.jsonl"), q.get("q", [""])[0], 200, 0))
        if path == "/api/labs":
            return self.json({"labs": LABS, "runs": lab_runs()})
        if path == "/api/training":
            return self.json(training())
        if path == "/api/scans":
            return self.json(list_scans())
        if path == "/api/report":
            name = q.get("name", [""])[0]
            if not REPORT_RE.match(name):
                return self.json({"error": "bad name"}, 400)
            p = os.path.join(SCANS, name)
            if not os.path.exists(p):
                return self.json({"error": "not found"}, 404)
            return self.json({"name": name, "html": md_render(open(p, encoding="utf-8").read())})
        if path == "/api/sources":
            threads = rows("threads.jsonl")
            counts = {}
            for r in threads:
                counts[r.get("source", "?")] = counts.get(r.get("source", "?"), 0) + 1
            return self.json(sorted(counts.items(), key=lambda x: -x[1]))
        return self.json({"error": "not found"}, 404)

    def do_POST(self):
        p = urllib.parse.urlsplit(self.path)
        body = self.body()
        if p.path == "/api/lab/run":
            return self.json(run_lab(body.get("lab", "")))
        if p.path == "/api/scan/run":
            target = str(body.get("target", "")).strip()
            if not target or target.startswith("-"):
                return self.json({"ok": False, "output": "target required"})
            return self.json(run_scan(target))
        if p.path == "/api/training/done":
            key = body.get("key", "")
            path = os.path.join(ROOT, "training", "progress.json")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            state = {"done": [], "journal": []}
            if os.path.exists(path):
                state = json.load(open(path))
            if key and key not in state["done"]:
                state["done"].append(key)
                json.dump(state, open(path, "w"), indent=1)
            return self.json({"ok": True, "training": training()})
        return self.json({"error": "not found"}, 404)


PAGE = r"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Beril dashboard</title>
<style>
:root{--bg:#fbfbfa;--panel:#fff;--text:#111;--muted:#6b6b6b;--line:#e7e7e4;--soft:#f4f4f1;--accent:#1f6b4d;--warn:#9a5b13;--bad:#9f2b2b;--r:8px;--mono:ui-monospace,SFMono-Regular,Menlo,monospace;--sans:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}
[data-theme=dark]{--bg:#0b0b0b;--panel:#111;--text:#f4f4f2;--muted:#9a9a94;--line:#242422;--soft:#171715;--accent:#6fce9f;--warn:#e0a45c;--bad:#ff8f8f}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:13px/1.55 var(--sans)}
a{color:inherit;text-decoration:none}.wrap{display:flex;min-height:100vh}
.side{width:224px;border-right:1px solid var(--line);padding:22px 14px;position:sticky;top:0;height:100vh;background:var(--bg)}
.brand{font-weight:800;letter-spacing:-.04em;font-size:19px;padding:0 10px 18px}.brand span{color:var(--accent)}
.nav{display:grid;gap:2px}.nav a{display:flex;justify-content:space-between;padding:7px 10px;border-radius:7px;color:var(--muted);font-size:12px}
.nav a:hover,.nav a.on{background:var(--soft);color:var(--text)}
.nav b{font-weight:600;color:var(--text)}.dot{width:6px;height:6px;border-radius:50%;background:var(--accent);display:inline-block;margin-right:6px}
.main{flex:1;min-width:0}.top{display:flex;align-items:center;gap:12px;padding:14px 28px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:2}
.crumb{font-size:12px;color:var(--muted)}.grow{flex:1}.input{background:var(--panel);border:1px solid var(--line);border-radius:7px;padding:7px 10px;color:var(--text);font:12px var(--sans);min-width:220px}
.btn{background:var(--text);color:var(--bg);border:0;border-radius:7px;padding:7px 11px;font:600 12px var(--sans);cursor:pointer}
.btn.ghost{background:transparent;color:var(--text);border:1px solid var(--line)}
.content{padding:26px 28px 60px;max-width:1240px}
h1{font-size:26px;letter-spacing:-.035em;margin:0 0 6px}h2{font-size:15px;margin:26px 0 10px;letter-spacing:-.02em}
p.sub{color:var(--muted);margin:0 0 20px}.grid{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}
.card{border:1px solid var(--line);background:var(--panel);border-radius:9px;padding:14px}
.k{font:11px var(--mono);color:var(--muted);text-transform:uppercase;letter-spacing:.08em}.v{font:600 24px/1.2 var(--mono);margin-top:6px}
table{width:100%;border-collapse:collapse;font-size:12px}th{text-align:left;color:var(--muted);font:11px var(--mono);text-transform:uppercase;letter-spacing:.06em;padding:8px;border-bottom:1px solid var(--line)}
td{padding:8px;border-bottom:1px solid var(--line);vertical-align:top}tr:hover td{background:var(--soft)}
.pill{display:inline-block;border:1px solid var(--line);border-radius:99px;padding:1px 7px;font:10px var(--mono);color:var(--muted)}
.pill.ok{color:var(--accent);border-color:var(--accent)}.pill.bad{color:var(--bad);border-color:var(--bad)}
.bar{height:5px;background:var(--soft);border-radius:99px;overflow:hidden}.bar i{display:block;height:100%;background:var(--accent)}
.muted{color:var(--muted)}.mono{font-family:var(--mono)}.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
pre{background:var(--soft);border:1px solid var(--line);border-radius:8px;padding:12px;overflow:auto;font:11px/1.5 var(--mono);max-height:420px;white-space:pre-wrap}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 14px}.chip{border:1px solid var(--line);background:var(--panel);border-radius:99px;padding:4px 9px;font-size:11px;cursor:pointer;color:var(--muted)}
.chip.on{color:var(--text);border-color:var(--text)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}.list{display:grid;gap:1px}
.item{padding:8px 0;border-bottom:1px solid var(--line)}.item a:hover{text-decoration:underline}
.hidden{display:none}@media(max-width:1000px){.grid{grid-template-columns:repeat(3,1fr)}.two{grid-template-columns:1fr}.side{width:190px}}
@media(max-width:700px){.side{display:none}.content{padding:18px}.grid{grid-template-columns:repeat(2,1fr)}.top{padding:12px 18px}}
</style>
</head>
<body><div class="wrap">
<aside class="side">
  <div class="brand">beril<span>.</span></div>
  <nav class="nav" id="nav">
    <a href="#overview" data-page="overview" class="on"><span><i class="dot"></i>Overview</span><b id="nThreads">0</b></a>
    <a href="#threads" data-page="threads"><span>Threads</span></a>
    <a href="#experts" data-page="experts"><span>Experts</span></a>
    <a href="#tools" data-page="tools"><span>Tools</span></a>
    <a href="#methods" data-page="methods"><span>Methods</span></a>
    <a href="#atlas" data-page="atlas"><span>GitHub atlas</span></a>
    <a href="#labs" data-page="labs"><span>Labs</span></a>
    <a href="#training" data-page="training"><span>Training</span></a>
    <a href="#scans" data-page="scans"><span>Scans</span></a>
    <a href="#sources" data-page="sources"><span>Sources</span></a>
  </nav>
</aside>
<main class="main">
  <header class="top"><div class="crumb" id="crumb">Overview</div><div class="grow"></div>
    <input class="input" id="q" placeholder="Search  /  to focus">
    <button class="btn ghost" id="theme">Dark</button>
  </header>
  <div class="content" id="view"></div>
</main>
</div>
<script>
const $=s=>document.querySelector(s), view=$('#view');
let page='overview', timer=null, cache={};
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const get=async u=>{const r=await fetch(u);return r.json()};
const post=async(u,b)=>{const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});return r.json()};

function setTheme(t){document.documentElement.dataset.theme=t;localStorage.setItem('beril-theme',t);$('#theme').textContent=t==='dark'?'Light':'Dark'}
setTheme(localStorage.getItem('beril-theme')||'light');$('#theme').onclick=()=>setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark');

function nav(p){page=p;document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('on',a.dataset.page===p));$('#crumb').textContent=p[0].toUpperCase()+p.slice(1);route()}
document.querySelectorAll('.nav a').forEach(a=>a.onclick=e=>{e.preventDefault();nav(a.dataset.page)});
$('#q').oninput=()=>{clearTimeout(timer);timer=setTimeout(route,220)};
addEventListener('keydown',e=>{if(e.key==='/'&&document.activeElement!==$('#q')){e.preventDefault();$('#q').focus()}});

function table(items,cols){
  if(!items.length) return '<p class="muted">No rows.</p>';
  return '<table><thead><tr>'+cols.map(c=>`<th>${c[0]}</th>`).join('')+'</tr></thead><tbody>'+
    items.map(r=>'<tr>'+cols.map(c=>`<td>${c[1](r)}</td>`).join('')+'</tr>').join('')+'</tbody></table>';
}
async function overview(){
  const d=await get('/api/overview'); const s=d.stats, t=d.training;
  $('#nThreads').textContent=s.threads;
  view.innerHTML=`<h1>Overview</h1><p class="sub">Every catalog, lab and training task on this machine. Read-only unless you press a button.</p>
  <div class="grid">
    ${[['Threads',s.threads],['Experts',s.experts],['Tools',s.tools],['Methods',s.methods],['GitHub repos',s.atlas],['Sources',s.sources]].map(x=>`<div class="card"><div class="k">${x[0]}</div><div class="v">${x[1]}</div></div>`).join('')}
  </div>
  <div class="two"><section><h2>Training</h2><div class="card"><div class="row"><b>${t.done}/${t.total}</b><span class="muted">tasks</span><div class="grow"></div><span class="mono">${t.pct}%</span></div><div class="bar" style="margin-top:10px"><i style="width:${t.pct}%"></i></div>
  <h2 style="margin:16px 0 6px">Next</h2><div class="list">${t.next.map(n=>`<div class="item">W${n.week} · ${esc(n.text)} <button class="pill" onclick="done('${n.key}')">done</button></div>`).join('')||'<p class="muted">Nothing queued.</p>'}</div></div></section>
  <section><h2>Recent research</h2><div class="card list">${d.recent.map(r=>`<div class="item"><a href="${esc(r.url)}" target="_blank">${esc(r.title)}</a><div class="muted"><span class="pill">${esc(r.source)}</span></div></div>`).join('')||'<p class="muted">Run the harvest first.</p>'}</div></section></div>
  <h2>Recent scans</h2><div class="card">${d.scans.map(x=>`<div class="item"><a href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a> <span class="muted mono">${x.mtime}</span></div>`).join('')||'<p class="muted">No scans.</p>'}</div>`;
}
async function threads(){
  const src=new URLSearchParams(location.hash.split('?')[1]||'').get('source')||'';
  const d=await get('/api/threads?limit=200&q='+encodeURIComponent($('#q').value)+'&source='+encodeURIComponent(src));
  view.innerHTML=`<h1>Threads</h1><p class="sub">${d.length} public threads and reports. Filter by source with the chips.</p><div class="chips" id="srcs"></div>`+
    table(d,[['Source',r=>`<span class="pill">${esc(r.source)}</span>`],['Title',r=>`<a href="${esc(r.url)}" target="_blank">${esc(r.title)}</a>`],['Date',r=>`<span class="muted mono">${esc((r.date||'').slice(0,10))}</span>`]]);
  const s=await get('/api/sources');
  $('#srcs').innerHTML=s.map(x=>`<span class="chip ${x[0]===src?'on':''}" onclick="location.hash='threads?source='+encodeURIComponent('${esc(x[0])}')">${esc(x[0])} ${x[1]}</span>`).join('');
}
async function experts(){const d=await get('/api/experts?q='+encodeURIComponent($('#q').value));
  view.innerHTML='<h1>Experts</h1><p class="sub">People and teams with public work.</p>'+table(d,[['Name',r=>`<a href="${esc(r.profile)}" target="_blank">${esc(r.name)}</a>`],['Focus',r=>esc(r.focus)],['Works',r=>r.works?.length||0]]);}
async function tools(){const kind=location.hash.split('?kind=')[1]||'re';
  const d=await get('/api/tools?kind='+kind+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<h1>Tools</h1><p class="sub">${d.length} entries. The shelf is a lead, not a verdict.</p>
  <div class="chips"><span class="chip ${kind==='re'?'on':''}" onclick="location.hash='tools?kind=re'">RE and offense</span><span class="chip ${kind==='canonical'?'on':''}" onclick="location.hash='tools?kind=canonical'">Core shelf</span></div>`+
  table(d,[['Name',r=>`<a href="${esc(r.repo)}" target="_blank">${esc(r.name)}</a>`],['Category',r=>`<span class="pill">${esc(r.category)}</span>`],['Stars',r=>`<span class="mono">${esc(r.stars||'-')}</span>`],['Description',r=>esc((r.description||'').slice(0,120))]]);}
async function methods(){const d=await get('/api/methods?q='+encodeURIComponent($('#q').value));
  view.innerHTML='<h1>Methods</h1><p class="sub">Extracted headings, intros and code density.</p>'+table(d,[['Title',r=>`<a href="${esc(r.url)}" target="_blank">${esc(r.title)}</a>`],['Source',r=>`<span class="pill">${esc(r.source)}</span>`],['Code',r=>`<span class="mono">${r.code_blocks||0}</span>`]]);}
async function atlas(){const cat=location.hash.split('?cat=')[1]||'';
  const d=await get('/api/atlas?category='+encodeURIComponent(cat)+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<h1>GitHub atlas</h1><p class="sub">${d.length} repositories. Stars are a snapshot.</p><div class="chips"><span class="chip ${!cat?'on':''}" onclick="location.hash='atlas'">All</span>${['bug-bounty','web-security','cloud-security','binary','fuzzing','detection','mobile','firmware','ai-security'].map(c=>`<span class="chip ${cat===c?'on':''}" onclick="location.hash='atlas?cat=${c}'">${c}</span>`).join('')}</div>`+
  table(d,[['Repo',r=>`<a href="${esc(r.url)}" target="_blank">${esc(r.repo)}</a>`],['Stars',r=>`<span class="mono">${r.stars}</span>`],['Lang',r=>esc(r.language||'-')],['Description',r=>esc((r.description||'').slice(0,120))]]);}
async function labs(){const d=await get('/api/labs');
  view.innerHTML='<h1>Labs</h1><p class="sub">Each run executes the smoke test and stores the tail.</p><div class="grid" style="grid-template-columns:repeat(2,1fr)">'+
  d.labs.map(l=>{const r=d.runs[l]||{};return `<div class="card"><div class="row"><b>${l}</b><div class="grow"></div><span class="pill ${r.ok?'ok':r.ok===false?'bad':''}">${r.ok?'pass':r.ok===false?'fail':'idle'}</span></div><p class="muted">${esc(r.at||'not run')}</p><button class="btn" onclick="runLab('${l}',this)">Run test</button><pre class="hidden" id="out-${l}">${esc(r.output||'')}</pre></div>`}).join('')+'</div>';}
async function runLab(l,b){b.disabled=true;b.textContent='Running…';const d=await post('/api/lab/run',{lab:l});const o=$('#out-'+l);o.textContent=d.output;o.classList.remove('hidden');b.disabled=false;b.textContent='Run test';}
async function training(){const d=await get('/api/training');
  view.innerHTML=`<h1>Training</h1><p class="sub">${d.done}/${d.total} tasks. A missed day is not a missed week.</p><div class="card"><div class="bar"><i style="width:${d.pct}%"></i></div><p class="mono" style="margin:8px 0">${d.pct}%</p></div>
  <h2>Next</h2><div class="list">${d.next.map(n=>`<div class="item">W${n.week} · ${esc(n.text)} <button class="pill" onclick="done('${n.key}')">done</button></div>`).join('')||'<p class="muted">Complete.</p>'}</div>
  <h2>Journal</h2><div class="card">${d.journal.map(j=>`<div class="item"><span class="mono muted">${esc(j.at)}</span> ${esc(j.text)}</div>`).join('')||'<p class="muted">No entries.</p>'}</div>`;}
async function done(k){await post('/api/training/done',{key:k});route();}
async function scans(){const d=await get('/api/scans');
  view.innerHTML=`<h1>Scans</h1><p class="sub">Run a read-only scan against a URL or local artifact.</p>
  <div class="card"><div class="row"><input class="input grow" id="target" placeholder="https://app.example or ./sample.apk"><button class="btn" onclick="doScan(this)">Scan</button></div><pre id="scanout" class="hidden"></pre></div>
  <h2>Reports</h2><div class="card">${d.map(x=>`<div class="item"><a href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a> <span class="muted mono">${x.size} B</span></div>`).join('')||'<p class="muted">No reports.</p>'}</div><div id="report"></div>`;}
async function doScan(b){const t=$('#target').value.trim();if(!t)return;b.disabled=true;b.textContent='Scanning…';const d=await post('/api/scan/run',{target:t});const o=$('#scanout');o.textContent=d.output;o.classList.remove('hidden');b.disabled=false;b.textContent='Scan';if(d.report)openReport(d.report);}
async function openReport(name){const d=await get('/api/report?name='+encodeURIComponent(name));$('#report').innerHTML=`<h2>${esc(name)}</h2><div class="card">${d.html||d.error}</div>`;scrollTo(0,0);}
async function sources(){const d=await get('/api/sources');
  view.innerHTML='<h1>Sources</h1><p class="sub">Harvested row counts by source. A source with one row is a gap.</p>'+table(d.map(x=>({name:x[0],n:x[1]})),[['Source',r=>esc(r.name)],['Rows',r=>`<span class="mono">${r.n}</span>`]]);}

async function route(){const q=$('#q').value;
  if(page==='overview')return overview();
  if(page==='threads')return threads(); if(page==='experts')return experts();
  if(page==='tools')return tools(); if(page==='methods')return methods();
  if(page==='atlas')return atlas(); if(page==='labs')return labs();
  if(page==='training')return training(); if(page==='scans')return scans();
  if(page==='sources')return sources();
}
addEventListener('hashchange',()=>{const [p]=location.hash.slice(1).split('?');if(p)nav(p)});
if(location.hash)nav(location.hash.slice(1).split('?')[0]);else overview();
</script></body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--port", type=int, default=8788)
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args()
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}/"
    print(f"dashboard {url}")
    if not args.no_open:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    srv.serve_forever()


if __name__ == "__main__":
    main()
