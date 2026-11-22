PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Local Beril workspace: research, jobs, costs, labs and scans.">
<title>Beril workspace</title>
<style>
/* Hallmark · v2.0.0 · shape: app screen · genre: modern-minimal
 * pre-emit critique: P4 H5 E4 S4 R4 V4 · weakest: P, the ledger is the product; led with spend and live jobs, not a KPI wall
 * floor: 0 FAIL · fixed: 39a, 48, 56, 24b, 26b, 41 · built: Beril */
:root{
  --bg:#080807;--surface:#0e0e0d;--surface-2:#141412;--ink:#f0f0ec;--muted:#96968f;--faint:#6b6b65;
  --line:#232320;--line-2:#34342f;--accent:#d8ff5c;--ok:#a8e6a0;--warn:#e7b96b;--bad:#ff9b96;
  --font-display:"Liberation Serif","DejaVu Serif",serif;
  --font-body:"Noto Sans","Segoe UI",system-ui,sans-serif;
  --font-mono:"DejaVu Sans Mono","Liberation Mono",monospace;
  --s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:24px;--s6:32px;--s7:48px;--s8:64px;--s9:96px;
  --r1:4px;--r2:8px;--r3:12px;--max:1420px;--scrim:rgb(8 8 7/.62);
  --dur:140ms;--ease:cubic-bezier(.2,.7,.2,1);
}
*{box-sizing:border-box}
html,body{overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.55 var(--font-body);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
button,input,select,textarea{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.btn:active,.chip:active,.nav a:active{transform:translateY(1px)}
.shell{display:grid;grid-template-columns:210px minmax(0,1fr);min-height:100vh}
.side{border-right:1px solid var(--line);padding:var(--s5) var(--s3);background:var(--bg);display:flex;flex-direction:column;gap:var(--s5)}
.brand{font:700 24px/1 var(--font-display);padding:0 var(--s2);letter-spacing:-.02em}
.brand small{display:block;font:400 11px var(--font-body);color:var(--faint);margin-top:var(--s2);letter-spacing:0}
.nav{display:grid;gap:1px}
.nav .group{font:400 11px/1 var(--font-body);color:var(--faint);padding:var(--s3) var(--s2) var(--s1)}
.nav a{display:flex;justify-content:space-between;align-items:baseline;padding:8px var(--s2);border-radius:var(--r1);color:var(--muted);font-size:13px}
.nav a:hover,.nav a.on{background:var(--surface);color:var(--ink)}
.nav a b{font:400 11px var(--font-mono);color:var(--faint)}
main{min-width:0}
.top{display:flex;align-items:center;gap:var(--s3);padding:var(--s3) var(--s6);border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5}
.top h2{font:600 15px/1 var(--font-body);margin:0;text-wrap:balance}
.grow{flex:1}
.field{display:flex;align-items:center;gap:var(--s2);border:1px solid var(--line);background:var(--surface);border-radius:var(--r1);padding:0 var(--s2);min-width:240px}
.field input{border:0;background:transparent;padding:8px 0;width:100%;outline:0;font-size:12px}
.field input::placeholder{color:var(--faint)}
.clock{font:400 11px var(--font-mono);color:var(--faint);white-space:nowrap}
.btn{border:1px solid var(--line-2);background:var(--surface);border-radius:var(--r1);padding:8px 12px;font-size:12px;cursor:pointer;transition:background var(--dur) var(--ease),border-color var(--dur) var(--ease)}
.btn:hover{background:var(--surface-2);border-color:var(--muted)}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--bg);font-weight:700}
.btn.primary:hover{background:var(--ink);border-color:var(--ink)}
.btn:disabled{background:var(--surface-2);color:var(--muted);border-color:var(--line);cursor:wait}
.content{max-width:var(--max);margin:0 auto;padding:var(--s6) var(--s6) var(--s9)}
.head{display:flex;align-items:flex-end;gap:var(--s4);margin-bottom:var(--s5)}
.head h1{font:400 clamp(28px,3vw,44px)/1.05 var(--font-display);letter-spacing:-.025em;margin:0;overflow-wrap:break-word;min-width:0;text-wrap:balance}
.head p{margin:0 0 4px;color:var(--muted);font-size:12px;max-width:48ch}
.grid{display:grid;gap:var(--s4)}
.ledger{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:var(--s5);align-items:start}
.panel{border:1px solid var(--line);background:var(--surface);border-radius:var(--r2);color:var(--ink)}
.panel .pad{padding:var(--s4)}
.rail{display:grid;gap:var(--s4)}
.label{font:400 12px/1 var(--font-body);color:var(--muted);margin:0 0 var(--s3)}
.big{font:600 clamp(38px,5vw,64px)/1 var(--font-mono);font-variant-numeric:tabular-nums;letter-spacing:-.04em}
.sub{font-size:12px;color:var(--muted)}
.bar{height:6px;background:var(--surface-2);border-radius:99px;overflow:hidden;margin:var(--s3) 0 var(--s2)}
.bar i{display:block;height:100%;background:var(--accent);transition:transform var(--dur) var(--ease);transform-origin:left}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stat{padding:var(--s4) var(--s3);border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat b{display:block;font:500 24px/1.1 var(--font-mono);font-variant-numeric:tabular-nums}
.stat span{display:block;font-size:12px;color:var(--muted);margin-top:var(--s1)}
table{width:100%;border-collapse:collapse}
th{text-align:left;font:400 12px/1.3 var(--font-body);color:var(--muted);padding:var(--s3) var(--s3);border-bottom:1px solid var(--line)}
td{padding:var(--s3) var(--s3);border-bottom:1px solid var(--line);vertical-align:top;font-size:12px}
tbody tr{transition:background var(--dur) var(--ease)}
tbody tr:hover{background:var(--surface-2)}
tbody tr[data-job]{cursor:pointer}
.num{font-family:var(--font-mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.title{font-size:13px;overflow-wrap:break-word}
.meta{color:var(--muted);font-size:11px}
.status{font:400 11px/1.6 var(--font-body);border-bottom:1px solid currentColor;white-space:nowrap}
.status.running{color:var(--accent)}
.status.done{color:var(--ok)}
.status.failed{color:var(--bad)}
.status.cancelled,.status.note{color:var(--faint)}
.chips{display:flex;gap:var(--s1);flex-wrap:wrap;margin-bottom:var(--s4)}
.chip{border:1px solid var(--line);background:transparent;border-radius:99px;padding:4px 12px;font-size:12px;color:var(--muted);cursor:pointer}
.chip.on{color:var(--ink);border-color:var(--line-2);background:var(--surface)}
.empty{padding:var(--s6) var(--s4);color:var(--muted);font-size:12px}
.mono{font-family:var(--font-mono)}
.hidden{display:none}
.form{display:grid;grid-template-columns:1fr 1fr;gap:var(--s3);padding:var(--s4)}
.form label{display:grid;gap:var(--s1);font-size:12px;color:var(--muted)}
.form input,.form select,.form textarea{background:var(--bg);border:1px solid var(--line);border-radius:var(--r1);padding:8px 8px;font-size:12px}
.form .wide{grid-column:1/-1}
pre{background:var(--bg);border:1px solid var(--line);border-radius:var(--r1);padding:var(--s3);overflow:auto;max-height:380px;font:11px/1.55 var(--font-mono);white-space:pre-wrap}
.drawer{position:fixed;inset:0 0 0 auto;width:min(540px,92vw);background:var(--surface);border-left:1px solid var(--line);padding:var(--s5);overflow:auto;transform:translateX(100%);transition:transform var(--dur) var(--ease);z-index:20}
.drawer.open{transform:translateX(0)}
.scrim{position:fixed;inset:0;background:var(--scrim);opacity:0;pointer-events:none;transition:opacity var(--dur) var(--ease);z-index:19}
.scrim.open{opacity:1;pointer-events:auto}
.bars{display:grid;gap:4px}
.bar-row{display:grid;grid-template-columns:78px minmax(0,1fr) 74px;align-items:center;gap:var(--s2);font-size:11px}
.bar-row .track{height:4px;background:var(--surface-2)}
.bar-row .track i{display:block;height:100%;background:var(--accent)}
.link{border-bottom:1px solid var(--line-2)}
.link:hover{border-color:var(--accent)}
.split{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:var(--s5)}
.timeline{display:grid}
.event{display:grid;grid-template-columns:74px 90px minmax(0,1fr) 70px;gap:var(--s3);padding:8px 0;border-bottom:1px solid var(--line);font-size:12px;align-items:baseline}
.event time{font:400 11px var(--font-mono);color:var(--faint)}
@media (max-width:1100px){.ledger,.split{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}.stat:nth-child(2){border-right:0}}
@media (max-width:800px){.shell{grid-template-columns:1fr}.side{position:static;height:auto}.nav{grid-template-columns:repeat(2,1fr)}.content,.top{padding-left:var(--s4);padding-right:var(--s4)}.head{align-items:flex-start;flex-direction:column}.form{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
</head>
<body><div class="shell">
<aside class="side">
  <div class="brand">Beril<small>local workspace</small></div>
  <nav class="nav" id="nav">
    <div class="group">workspace</div>
    <a href="#overview" data-page="overview"><span>Overview</span><b id="nJobs"></b></a>
    <a href="#activity" data-page="activity"><span>Activity</span></a>
    <a href="#jobs" data-page="jobs"><span>Jobs</span></a>
    <a href="#costs" data-page="costs"><span>Costs</span></a>
    <div class="group">intel</div>
    <a href="#threads" data-page="threads"><span>Threads</span><b id="nThreads"></b></a>
    <a href="#experts" data-page="experts"><span>Experts</span></a>
    <a href="#tools" data-page="tools"><span>Tools</span></a>
    <a href="#methods" data-page="methods"><span>Methods</span></a>
    <a href="#atlas" data-page="atlas"><span>GitHub atlas</span></a>
    <div class="group">operate</div>
    <a href="#labs" data-page="labs"><span>Labs</span></a>
    <a href="#training" data-page="training"><span>Training</span></a>
    <a href="#scans" data-page="scans"><span>Scans</span></a>
    <a href="#sources" data-page="sources"><span>Sources</span></a>
  </nav>
</aside>
<main>
  <header class="top">
    <h2 id="crumb">Overview</h2><div class="grow"></div>
    <label class="field"><input id="q" placeholder="Search the workspace, / to focus" aria-label="Search"></label>
    <span class="clock" id="clock"></span>
    <button class="btn" id="newJob">Log work</button>
  </header>
  <div class="content" id="view"></div>
</main>
<div class="scrim" id="scrim" onclick="closeDrawer()"></div>
<aside class="drawer" id="drawer" aria-live="polite"></aside>
<script>
const $=s=>document.querySelector(s), view=$('#view'), drawer=$('#drawer'), scrim=$('#scrim');
let page='overview', timer=null;
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const get=async u=>{const r=await fetch(u);return r.json()};
const post=async(u,b)=>{const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});return r.json()};
const money=n=>'$'+Number(n||0).toFixed(2);
const when=s=>{if(!s)return '';const d=new Date(s);return isNaN(d)?String(s).slice(0,16):d.toLocaleString([], {month:'short',day:'2-digit',hour:'2-digit',minute:'2-digit'})};
function tick(){$('#clock').textContent=new Date().toLocaleTimeString([], {hour:'2-digit',minute:'2-digit',second:'2-digit'})}tick();setInterval(tick,1000);
function nav(p){page=p;document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('on',a.dataset.page===p));$('#crumb').textContent=p[0].toUpperCase()+p.slice(1);closeDrawer();route()}
document.querySelectorAll('.nav a').forEach(a=>a.onclick=e=>{e.preventDefault();nav(a.dataset.page)});
$('#q').oninput=()=>{clearTimeout(timer);timer=setTimeout(route,250)};
$('#newJob').onclick=()=>nav('jobs');
addEventListener('keydown',e=>{if(e.key==='/'&&document.activeElement!==$('#q')){e.preventDefault();$('#q').focus()}if(e.key==='Escape')closeDrawer()});
function table(items,cols){if(!items.length)return '<div class="empty">Nothing here yet.</div>';return '<table><thead><tr>'+cols.map(c=>`<th>${c[0]}</th>`).join('')+'</tr></thead><tbody>'+items.map(r=>`<tr ${r.id?`data-job onclick="openJob('${r.id}')"`:''}>`+cols.map(c=>`<td>${c[1](r)}</td>`).join('')+'</tr>').join('')+'</tbody></table>'}

async function overview(){
  const d=await get('/api/overview'), s=d.stats, c=d.costs, t=d.training;
  $('#nThreads').textContent=s.threads; $('#nJobs').textContent=d.activity.filter(x=>x.status==='running').length||'';
  const spend=c.month, budget=Number(c.budget.monthly_usd||25), pct=Math.min(100, spend/budget*100);
  view.innerHTML=`<div class="head"><h1>Workspace</h1><p>Every catalog, job and cost on this machine. One ledger, loopback only.</p></div>
  <div class="ledger"><div class="panel"><div class="pad"><p class="label">Spend this month against the ${money(budget)} budget</p><div class="big">${money(spend)}</div><div class="bar"><i style="width:${pct}%"></i></div><p class="sub">${money(c.today)} today · ${money(c.week)} this week · ${pct.toFixed(0)}% of budget</p></div>
  <div class="stats"><div class="stat"><b>${s.threads}</b><span>threads</span></div><div class="stat"><b>${s.tools}</b><span>tools</span></div><div class="stat"><b>${s.atlas}</b><span>repos indexed</span></div><div class="stat"><b>${t.done}/${t.total}</b><span>training tasks</span></div></div>
  <div class="pad" style="padding-top:var(--s4);padding-bottom:var(--s2)"><p class="label">Ledger</p></div>${table(d.activity,[['Time',r=>`<span class="num">${when(r.at)}</span>`],['Kind',r=>esc(r.type||r.kind)],['Work',r=>`<span class="title">${esc(r.title)}</span>`],['Actor',r=>`<span class="meta">${esc(r.actor||'')}</span>`],['Cost',r=>`<span class="num">${money(r.cost)}</span>`],['State',r=>`<span class="status ${esc(r.status)}">${esc(r.status)}</span>`]])}</div>
  <div class="rail"><section class="panel pad"><p class="label">Next training</p>${t.next.map(n=>`<div class="event" style="grid-template-columns:minmax(0,1fr) auto"><span>week ${n.week} · ${esc(n.text)}</span><button class="btn" onclick="done('${n.key}')">done</button></div>`).join('')||'<p class="sub">Queue clear.</p>'}</section>
  <section class="panel pad"><p class="label">Coverage</p>${[['experts',s.experts],['methods',s.methods],['sources',s.sources]].map(x=>`<div class="bar-row"><span>${x[0]}</span><div class="track"><i style="width:${Math.min(100,x[1]/6)}%"></i></div><span class="num">${x[1]}</span></div>`).join('')}</section>
  <section class="panel pad"><p class="label">Latest scans</p>${d.scans.map(x=>`<div class="event" style="grid-template-columns:minmax(0,1fr)"><a class="link" href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a></div>`).join('')||'<p class="sub">No reports.</p>'}</section></div></div>`;
}
async function activity(){const d=await get('/api/activity?limit=120');
  view.innerHTML=`<div class="head"><h1>Activity</h1><p>Jobs, labs, scans and journal entries in one stream. Newest first.</p></div><div class="panel pad"><div class="timeline">${d.map(r=>`<div class="event"><time>${when(r.at)}</time><span class="status ${esc(r.status)}">${esc(r.type||r.kind)}</span><span>${esc(r.title)}</span><span class="num">${money(r.cost)}</span></div>`).join('')||'<div class="empty">No activity.</div>'}</div></div>`;}
async function jobs(){const filter=location.hash.split('?status=')[1]||'';
  const d=await get('/api/jobs?status='+filter+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Jobs</h1><p>Every unit of work, its actor, model, tokens and cost. Click a row for detail.</p></div>
  <div class="split"><div class="panel"><div class="chips" style="padding:var(--s3) var(--s3) 0">${['','running','done','failed'].map(s=>`<button class="chip ${filter===s?'on':''}" onclick="location.hash='jobs${s?'?status='+s:''}'">${s||'all'}</button>`).join('')}</div>${table(d,[['Started',r=>`<span class="num">${when(r.started_at)}</span>`],['Type',r=>esc(r.type)],['Work',r=>`<span class="title">${esc(r.title)}</span>`],['Model',r=>`<span class="meta">${esc(r.model||'-')}</span>`],['Cost',r=>`<span class="num">${money(r.cost_usd)}</span>`],['State',r=>`<span class="status ${esc(r.status)}">${esc(r.status)}</span>`]])}</div>
  <form class="panel form" onsubmit="logJob(event)"><p class="label wide">Log a job</p>
    <label class="wide">Title<input name="title" required placeholder="What is being done"></label>
    <label>Type<select name="type"><option>llm</option><option>manual</option><option>scan</option><option>harvest</option><option>report</option></select></label>
    <label>Model<input name="model" placeholder="claude-sonnet-4.5"></label>
    <label>Target<input name="target" placeholder="host, file or task"></label>
    <label>Input tokens<input name="tokens_in" type="number" min="0" value="0"></label>
    <label>Output tokens<input name="tokens_out" type="number" min="0" value="0"></label>
    <label class="wide">Notes<textarea name="notes" rows="2"></textarea></label>
    <div class="wide" style="display:flex;justify-content:flex-end"><button class="btn primary">Create job</button></div></form></div>`;
}
async function logJob(e){e.preventDefault();const f=new FormData(e.target),o={};f.forEach((v,k)=>o[k]=v);
  const r=await post('/api/jobs',{...o,status:'running',actor:'human'});if(r.id)nav('jobs');}
async function openJob(id){const d=await get('/api/jobs?q='+id);const r=d.find(x=>x.id===id);if(!r)return;
  scrim.classList.add('open');drawer.classList.add('open');
  drawer.innerHTML=`<div style="display:flex;gap:8px;align-items:center"><span class="status ${esc(r.status)}">${esc(r.status)}</span><div class="grow"></div><button class="btn" onclick="closeDrawer()">close</button></div><h2 style="font:400 26px/1.15 var(--font-display);margin:18px 0 6px">${esc(r.title)}</h2><p class="sub">${esc(r.type)} · ${esc(r.actor)} · ${esc(r.model||'no model')}</p>
  <div class="stats" style="grid-template-columns:1fr 1fr;margin:18px 0"><div class="stat"><b>${money(r.cost_usd)}</b><span>cost</span></div><div class="stat"><b>${(r.tokens_in||0)+(r.tokens_out||0)}</b><span>tokens</span></div></div>
  <p class="label">Started</p><p class="mono">${esc(r.started_at)}</p><p class="label">Finished</p><p class="mono">${esc(r.finished_at||'still running')}</p><p class="label">Target</p><p>${esc(r.target||'-')}</p><p class="label">Notes</p><p>${esc(r.notes||'-')}</p><p class="label">Log</p><p class="mono">${esc(r.log||'-')}</p>
  ${r.status==='running'?`<button class="btn primary" style="margin-top:18px" onclick="finishJob('${r.id}','done')">Mark done</button> <button class="btn" onclick="finishJob('${r.id}','failed')">Failed</button>`:''}`;
}
function closeDrawer(){scrim.classList.remove('open');drawer.classList.remove('open')}
async function finishJob(id,status){await post('/api/jobs/finish',{id,status});closeDrawer();route()}
async function costs(){const c=await get('/api/costs');const max=Math.max(1,...Object.values(c.daily));
  view.innerHTML=`<div class="head"><h1>Costs</h1><p>Tokens priced from data/llm_prices.json. Scans and labs are zero.</p></div>
  <div class="ledger"><div class="panel pad"><p class="label">Total spend</p><div class="big">${money(c.total)}</div><p class="sub">${money(c.today)} today · ${money(c.week)} this week · ${money(c.month)} this month</p>
  <div class="bars" style="margin-top:24px">${Object.entries(c.daily).slice(-30).map(([d,v])=>`<div class="bar-row"><span class="num">${d.slice(5)}</span><div class="track"><i style="width:${v/max*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">No priced jobs.</p>'}</div></div>
  <div class="rail"><section class="panel pad"><p class="label">Monthly budget</p><div class="big" style="font-size:32px">${money(c.budget.monthly_usd)}</div><div class="bar"><i style="width:${Math.min(100,c.month/c.budget.monthly_usd*100)}%"></i></div><div style="display:flex;gap:6px;margin-top:8px"><input class="mono" id="budget" value="${c.budget.monthly_usd}" style="width:80px;background:var(--bg);border:1px solid var(--line);padding:6px"><button class="btn" onclick="saveBudget()">save</button></div></section>
  <section class="panel pad"><p class="label">By model</p>${Object.entries(c.by_model).map(([m,v])=>`<div class="bar-row"><span>${esc(m)}</span><div class="track"><i style="width:${v/Math.max(1,c.total)*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">None.</p>'}</section>
  <section class="panel pad"><p class="label">By type</p>${Object.entries(c.by_type).map(([m,v])=>`<div class="bar-row"><span>${esc(m)}</span><div class="track"><i style="width:${v/Math.max(1,c.total)*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">None.</p>'}</section></div></div>`;
}
async function saveBudget(){await post('/api/budget',{monthly_usd:Number($('#budget').value)||25});route()}
async function threads(){const src=location.hash.split('?source=')[1]||'';const d=await get('/api/threads?limit=200&q='+encodeURIComponent($('#q').value)+'&source='+encodeURIComponent(src));
  view.innerHTML=`<div class="head"><h1>Threads</h1><p>${d.length} public threads and reports.</p></div><div class="chips" id="srcs"></div>`+table(d,[['Source',r=>esc(r.source)],['Title',r=>`<a class="link" href="${esc(r.url)}" target="_blank">${esc(r.title)}</a>`],['Date',r=>`<span class="num">${esc((r.date||'').slice(0,10))}</span>`]]);
  const s=await get('/api/sources');$('#srcs').innerHTML=s.map(x=>`<button class="chip ${x[0]===src?'on':''}" onclick="location.hash='threads?source='+encodeURIComponent('${esc(x[0])}')">${esc(x[0])} ${x[1]}</button>`).join('');
}
async function experts(){const d=await get('/api/experts?q='+encodeURIComponent($('#q').value));view.innerHTML=`<div class="head"><h1>Experts</h1><p>People and teams with public work.</p></div>`+table(d,[['Name',r=>`<a class="link" href="${esc(r.profile)}" target="_blank">${esc(r.name)}</a>`],['Focus',r=>esc(r.focus)],['Works',r=>r.works?.length||0]]);}
async function tools(){const kind=location.hash.split('?kind=')[1]||'re';const d=await get('/api/tools?kind='+kind+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Tools</h1><p>${d.length} entries. A shelf, not a verdict.</p></div><div class="chips"><button class="chip ${kind==='re'?'on':''}" onclick="location.hash='tools?kind=re'">RE and offense</button><button class="chip ${kind==='canonical'?'on':''}" onclick="location.hash='tools?kind=canonical'">Core shelf</button></div>`+table(d,[['Name',r=>`<a class="link" href="${esc(r.repo)}" target="_blank">${esc(r.name)}</a>`],['Category',r=>esc(r.category)],['Stars',r=>`<span class="num">${esc(r.stars||'-')}</span>`],['Description',r=>esc((r.description||'').slice(0,110))]]);}
async function methods(){const d=await get('/api/methods?q='+encodeURIComponent($('#q').value));view.innerHTML=`<div class="head"><h1>Methods</h1><p>Extracted structure and code density.</p></div>`+table(d,[['Title',r=>`<a class="link" href="${esc(r.url)}" target="_blank">${esc(r.title)}</a>`],['Source',r=>esc(r.source)],['Code',r=>`<span class="num">${r.code_blocks||0}</span>`]]);}
async function atlas(){const cat=location.hash.split('?cat=')[1]||'';const d=await get('/api/atlas?category='+encodeURIComponent(cat)+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>GitHub atlas</h1><p>${d.length} repositories. Stars are a snapshot.</p></div><div class="chips"><button class="chip ${!cat?'on':''}" onclick="location.hash='atlas'">all</button>${['bug-bounty','web-security','cloud-security','binary','fuzzing','detection','mobile','firmware','ai-security'].map(c=>`<button class="chip ${cat===c?'on':''}" onclick="location.hash='atlas?cat=${c}'">${c}</button>`).join('')}</div>`+table(d,[['Repo',r=>`<a class="link" href="${esc(r.url)}" target="_blank">${esc(r.repo)}</a>`],['Stars',r=>`<span class="num">${r.stars}</span>`],['Language',r=>esc(r.language||'-')],['Description',r=>esc((r.description||'').slice(0,110))]]);}
async function labs(){const d=await get('/api/labs');view.innerHTML=`<div class="head"><h1>Labs</h1><p>Each run executes the smoke test and stores the tail.</p></div><div class="panel">${d.labs.map(l=>{const r=d.runs[l]||{};return `<div class="event" style="grid-template-columns:120px minmax(0,1fr) 90px 110px 90px"><b>${l}</b><pre class="${r.output?'':'hidden'}" id="out-${l}" style="max-height:120px">${esc(r.output||'')}</pre><span class="status ${r.ok?'done':r.ok===false?'failed':'cancelled'}">${r.ok?'pass':r.ok===false?'fail':'idle'}</span><span class="meta">${esc(r.at||'not run')}</span><button class="btn" onclick="runLab('${l}',this)">run test</button></div>`}).join('')}</div>`;}
async function runLab(l,b){b.disabled=true;b.textContent='running';const d=await post('/api/lab/run',{lab:l});const o=$('#out-'+l);o.textContent=d.output;o.classList.remove('hidden');b.disabled=false;b.textContent='run test';}
async function training(){const d=await get('/api/training');view.innerHTML=`<div class="head"><h1>Training</h1><p>${d.done}/${d.total} tasks. A missed day is not a missed week.</p></div><div class="panel pad"><div class="bar"><i style="width:${d.pct}%"></i></div><p class="num">${d.pct}%</p></div><h2 class="label" style="margin-top:24px">Next</h2><div class="panel">${d.next.map(n=>`<div class="event" style="grid-template-columns:minmax(0,1fr) auto"><span>week ${n.week} · ${esc(n.text)}</span><button class="btn" onclick="done('${n.key}')">done</button></div>`).join('')||'<div class="empty">Complete.</div>'}</div><h2 class="label" style="margin-top:24px">Journal</h2><div class="panel">${d.journal.map(j=>`<div class="event" style="grid-template-columns:90px minmax(0,1fr)"><time>${esc(j.at)}</time><span>${esc(j.text)}</span></div>`).join('')||'<div class="empty">No entries.</div>'}</div>`;}
async function done(k){await post('/api/training/done',{key:k});route()}
async function scans(){const d=await get('/api/scans');view.innerHTML=`<div class="head"><h1>Scans</h1><p>Read-only. A URL or local artifact.</p></div><form class="panel pad" onsubmit="doScan(event)"><div style="display:flex;gap:8px"><input name="target" class="grow" placeholder="https://app.example or ./sample.apk" style="background:var(--bg);border:1px solid var(--line);padding:8px"><button class="btn primary">scan</button></div><pre id="scanout" class="hidden"></pre></form><h2 class="label" style="margin-top:24px">Reports</h2><div class="panel">${d.map(x=>`<div class="event" style="grid-template-columns:minmax(0,1fr) 80px"><a class="link" href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a><span class="meta">${x.size} B</span></div>`).join('')||'<div class="empty">No reports.</div>'}</div><div id="report"></div>`;}
async function doScan(e){e.preventDefault();const b=e.target.querySelector('button'),t=e.target.target.value.trim();if(!t)return;b.disabled=true;b.textContent='scanning';const d=await post('/api/scan/run',{target:t});const o=$('#scanout');o.textContent=d.output;o.classList.remove('hidden');b.disabled=false;b.textContent='scan';if(d.report)openReport(d.report);}
async function openReport(name){const d=await get('/api/report?name='+encodeURIComponent(name));$('#report').innerHTML=`<h2 class="label" style="margin-top:24px">${esc(name)}</h2><div class="panel pad">${d.html||d.error}</div>`;scrollTo(0,0)}
async function sources(){const d=await get('/api/sources');view.innerHTML=`<div class="head"><h1>Sources</h1><p>Harvested rows by source. One row is a gap.</p></div>`+table(d.map(x=>({name:x[0],n:x[1]})),[['Source',r=>esc(r.name)],['Rows',r=>`<span class="num">${r.n}</span>`]]);}
async function route(){closeDrawer();if(page==='overview')return overview();if(page==='activity')return activity();if(page==='jobs')return jobs();if(page==='costs')return costs();if(page==='threads')return threads();if(page==='experts')return experts();if(page==='tools')return tools();if(page==='methods')return methods();if(page==='atlas')return atlas();if(page==='labs')return labs();if(page==='training')return training();if(page==='scans')return scans();if(page==='sources')return sources();}
addEventListener('hashchange',()=>{const p=location.hash.slice(1).split('?')[0];if(p)nav(p)});
if(location.hash)nav(location.hash.slice(1).split('?')[0]);else overview();
</script></body></html>"""
