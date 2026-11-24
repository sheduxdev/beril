PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Local Beril workspace: posture, research, jobs, costs, labs and scans.">
<meta name="theme-color" content="#000000">
<meta name="color-scheme" content="dark light">
<title>Beril workspace</title>
<style>
/* Hallmark · v2.0.0 · shape: app screen · genre: modern-minimal
 * pre-emit critique: P4 H5 E4 S4 R4 V4 · weakest: P, the ledger is the product; led with spend and live jobs, not a KPI wall
 * floor: 0 FAIL · fixed: 7a, 20, 48, 56, 24b, 29, F24 · built: Beril
 * Orbit (polar.sh) roles + Apple HIG values: system colors, 13px base, capsule buttons, sortable columns.
 * Reference repos: axiaoge2/apple-hig-designer (MIT), dickwu/apple-design-skill, raintree-technology/hig-doctor.
 * Geist-style restraint.
 * Subtraction: one spacing scale, three radii, one accent, shadow-as-border.
 * Roles: background-*, text-*, border-*. Legacy aliases below keep old rules working. */
:root{color-scheme:dark light;
  --background-primary:#000;--background-secondary:#1c1c1e;--background-card:#1c1c1e;--background-hover:#2c2c2e;
  --text-primary:#fff;--text-secondary:#aeaeb2;--text-tertiary:#8e8e93;
  --border-primary:rgba(84,84,88,.6);--border-secondary:#48484a;
  --accent:#0a84ff;--accent-solid:#0071e3;--success:#30d158;--warning:#ff9f0a;--danger:#ff453a;
  --glass:rgb(28 28 30/.72);--glass-bar:rgb(0 0 0/.72);--seg-on:#636366;--scrim:rgb(0 0 0/.6);
  --bg:var(--background-primary);--surface:var(--background-card);--surface-2:var(--background-hover);
  --ink:var(--text-primary);--muted:var(--text-secondary);--faint:var(--text-tertiary);
  --line:var(--border-primary);--line-2:var(--border-secondary);--ok:var(--success);--warn:var(--warning);--bad:var(--danger);
  --font-body:-apple-system,BlinkMacSystemFont,"SF Pro Text","SF Pro Display","Inter","Noto Sans",system-ui,sans-serif;
  --font-display:var(--font-body);
  --font-mono:ui-monospace,"SF Mono",SFMono-Regular,"JetBrains Mono","DejaVu Sans Mono",monospace;
  --s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:24px;--s6:32px;--s7:48px;--s8:64px;--s9:96px;
  --r1:8px;--r2:12px;--r3:16px;--max:1240px;
  --shadow-s:0 1px 3px rgb(0 0 0/.4);--shadow-m:0 4px 6px rgb(0 0 0/.4),0 2px 4px rgb(0 0 0/.5);--shadow-l:0 20px 25px rgb(0 0 0/.4),0 8px 10px rgb(0 0 0/.5);
  --dur:150ms;--ease:cubic-bezier(.25,.1,.25,1);
}
@media (prefers-color-scheme:light){:root{
  --background-primary:#f2f2f7;--background-secondary:#fff;--background-card:#fff;--background-hover:#e5e5ea;
  --text-primary:#000;--text-secondary:#48484a;--text-tertiary:#6e6e73;
  --border-primary:rgba(60,60,67,.18);--border-secondary:rgba(60,60,67,.36);
  --accent:#007aff;--glass:rgb(255 255 255/.72);--glass-bar:rgb(242 242 247/.72);--seg-on:#fff;--scrim:rgb(0 0 0/.3);
  --shadow-s:0 1px 3px rgb(0 0 0/.06);--shadow-m:0 4px 6px rgb(0 0 0/.06),0 2px 4px rgb(0 0 0/.08);--shadow-l:0 20px 25px rgb(0 0 0/.1),0 8px 10px rgb(0 0 0/.12);
}}
@view-transition{navigation:auto}
::view-transition-old(root){animation:out 120ms var(--ease)}
::view-transition-new(root){animation:in 180ms var(--ease)}
@keyframes out{to{opacity:.001}}
@keyframes in{from{opacity:.001;transform:translateY(6px)}}
*{box-sizing:border-box}
html,body{overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:13px/1.45 var(--font-body);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
button,input,select,textarea{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.btn:active,.chip:active,.nav a:active{transform:scale(.98)}
.shell{display:grid;grid-template-columns:216px minmax(0,1fr);min-height:100vh}
.side{border-right:1px solid var(--line);padding:var(--s5) var(--s3);background:var(--glass);backdrop-filter:blur(20px) saturate(180%);display:flex;flex-direction:column;gap:var(--s5);position:sticky;top:0;height:100vh}
.brand{font:600 16px/1 var(--font-body);padding:0 var(--s3);letter-spacing:-.01em}
.brand small{display:block;font:400 12px var(--font-body);color:var(--faint);margin-top:var(--s2);letter-spacing:0}
.nav{display:grid;gap:2px}
.nav a{display:flex;justify-content:space-between;align-items:center;min-height:28px;padding:5px var(--s3);border-radius:var(--r1);color:var(--muted);font-size:13px;transition:background var(--dur) var(--ease),color var(--dur) var(--ease)}
.nav a:hover{background:var(--surface-2);color:var(--ink)}
.nav a.on{background:var(--surface-2);color:var(--ink);font-weight:500}
.nav a b{font:400 12px var(--font-mono);color:var(--faint)}
main{min-width:0}
.top{display:flex;align-items:center;gap:var(--s2);height:52px;padding:0 var(--s5);border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--glass-bar);backdrop-filter:blur(20px) saturate(180%);z-index:5}
.top h2{font:600 14px/1 var(--font-body);margin:0;color:var(--muted)}
.grow{flex:1}
.field{display:flex;align-items:center;gap:var(--s2);background:var(--surface-2);border-radius:var(--r1);min-height:28px;padding:0 var(--s2) 0 var(--s3);width:220px}
.field input{border:0;background:transparent;padding:4px 0;width:100%;outline:0;font-size:13px}
.field input::placeholder{color:var(--faint)}
.kbd{font:400 11px/1 var(--font-mono);color:var(--faint);border:1px solid var(--line-2);border-radius:6px;padding:4px 8px}
.btn{display:inline-flex;align-items:center;gap:var(--s2);min-height:28px;border:1px solid transparent;background:var(--surface-2);border-radius:99px;padding:4px 14px;font-size:13px;cursor:pointer;transition:background var(--dur) var(--ease),transform var(--dur) var(--ease)}
.btn:hover{background:var(--line-2)}
.btn.primary{background:var(--accent-solid);color:#fff;font-weight:600}
.btn.primary:hover{background:#0a84ff}
.btn.icon{padding:4px 8px}.btn.icon svg{display:block}
.btn:disabled{background:var(--surface-2);color:var(--faint);cursor:wait}
.content{max-width:var(--max);margin:0 auto;padding:var(--s5) var(--s6) var(--s9)}
.subnav{display:flex;gap:var(--s1);margin-bottom:var(--s5);border-bottom:1px solid var(--line);overflow-x:auto}
.subnav:empty{display:none}
.subnav a{padding:var(--s2) var(--s3);color:var(--faint);font-size:13px;white-space:nowrap;border-radius:var(--r1) var(--r1) 0 0;transition:color var(--dur) var(--ease)}
.subnav a:hover{color:var(--ink)}
.subnav a.on{color:var(--ink);box-shadow:inset 0 -2px 0 var(--ink)}
.head{display:flex;flex-direction:column;gap:var(--s1);margin-bottom:var(--s5)}
.head h1{font:600 26px/1.2 var(--font-body);letter-spacing:-.01em;margin:0;overflow-wrap:break-word;min-width:0;text-wrap:balance}
.head p{margin:0;color:var(--muted);font-size:13px;max-width:64ch}
.grid{display:grid;gap:var(--s4)}
.ledger{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:var(--s4);align-items:start}
.kpis{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s4);margin-bottom:var(--s4)}
.panel{box-shadow:0 0 0 1px var(--line);background:var(--surface);border-radius:var(--r2);color:var(--ink);overflow:hidden}
.panel .pad,.panel.pad{padding:var(--s4)}
.panel-head{display:flex;justify-content:space-between;align-items:center;padding:var(--s4) var(--s4) var(--s2)}
.panel-head .label{margin:0}
.rail{display:grid;gap:var(--s4)}
.label{font:500 12px/1 var(--font-body);color:var(--muted);margin:0 0 var(--s3)}
.big{font:600 clamp(28px,3.4vw,40px)/1 var(--font-mono);font-variant-numeric:tabular-nums;letter-spacing:-.04em}
.big .of{color:var(--faint);font-weight:400}
.sub{font-size:12px;color:var(--muted);margin:0}
.bar{height:4px;background:var(--surface-2);border-radius:99px;overflow:hidden;margin:var(--s3) 0 var(--s2)}
.bar i{display:block;height:100%;background:var(--accent);transition:transform var(--dur) var(--ease);transform-origin:left}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stat{padding:var(--s4) var(--s3);border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat b{display:block;font:500 22px/1.1 var(--font-mono);font-variant-numeric:tabular-nums}
.stat span{display:block;font-size:12px;color:var(--muted);margin-top:var(--s1)}
table{width:100%;border-collapse:collapse}
th{text-align:left;font:500 12px/1.3 var(--font-body);color:var(--faint);padding:var(--s3) var(--s4);border-bottom:1px solid var(--line);cursor:pointer;user-select:none;white-space:nowrap}
th:hover{color:var(--ink)}
th[data-dir=asc]::after{content:' \2191'}th[data-dir=desc]::after{content:' \2193'}
td{padding:var(--s3) var(--s4);border-bottom:1px solid var(--line);vertical-align:top;font-size:13px}
tbody tr:last-child td{border-bottom:0}
tbody tr{transition:background var(--dur) var(--ease)}
tbody tr:hover{background:var(--surface-2)}
tbody tr[data-job]{cursor:pointer}
.tbl{overflow-x:auto}
#view>.tbl{background:var(--surface);box-shadow:0 0 0 1px var(--line);border-radius:var(--r2)}
.num{font-family:var(--font-mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.reveal{animation:reveal linear both;animation-timeline:view();animation-range:entry 0% cover 28%}
@keyframes reveal{from{opacity:.001;transform:translateY(10px)}to{opacity:1;transform:none}}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:var(--s3)}
.posture-card{display:grid;grid-row:span 4;grid-template-rows:subgrid;gap:var(--s1);box-shadow:0 0 0 1px var(--line);background:var(--surface);color:var(--ink);padding:var(--s4);border-radius:var(--r2);transition:box-shadow var(--dur) var(--ease)}
.posture-card:hover{box-shadow:0 0 0 1px var(--line-2),var(--shadow-m)}
.posture-card h3{font:600 14px/1.3 var(--font-body);margin:0}
.posture-card p{margin:0;color:var(--muted);font-size:12px}
.faq{box-shadow:0 0 0 1px var(--line);border-radius:var(--r1);background:var(--surface);margin-top:var(--s2)}
.faq summary{padding:var(--s3);cursor:pointer;font-weight:500;font-size:13px}
.faq p{padding:0 var(--s3) var(--s3);margin:0;color:var(--muted);font-size:13px}
.title{font-size:13px;overflow-wrap:break-word}
.meta{color:var(--faint);font-size:12px}
.status{display:inline-flex;align-items:center;gap:8px;font:400 12px/1.4 var(--font-body);color:var(--muted);white-space:nowrap}
.status::before{content:"";width:6px;height:6px;border-radius:99px;background:var(--dot,var(--faint))}
.status.running{--dot:var(--accent)}
.status.done{--dot:var(--success)}
.status.failed,.status.critical,.status.high{--dot:var(--danger)}
.status.medium{--dot:var(--warning)}
.pill{font:500 11px/1 var(--font-body);padding:4px 8px;border-radius:99px;background:var(--surface-2);color:var(--muted);white-space:nowrap}
.chips{display:flex;gap:var(--s1);flex-wrap:wrap;margin-bottom:var(--s4)}
.chip{border:1px solid var(--line);background:transparent;border-radius:99px;min-height:28px;padding:4px 12px;font-size:12px;color:var(--muted);cursor:pointer;transition:background var(--dur) var(--ease)}
.chip:hover{background:var(--surface-2)}
.chip.on{color:var(--ink);border-color:var(--line-2);background:var(--surface-2)}
.seg{display:inline-flex;gap:0;background:var(--surface-2);border-radius:var(--r1);padding:2px;margin:0}
.seg .chip{border:0;border-radius:6px;min-height:24px;padding:2px 14px;background:transparent}
.seg .chip.on{background:var(--seg-on);color:var(--ink);box-shadow:var(--shadow-s)}
.empty{padding:var(--s6) var(--s4);color:var(--muted);font-size:13px}
.mono{font-family:var(--font-mono)}
.hidden{display:none}
.form{display:grid;grid-template-columns:1fr 1fr;gap:var(--s3);padding:var(--s4)}
.form label{display:grid;gap:var(--s1);font-size:12px;color:var(--muted)}
.form input,.form select,.form textarea{background:var(--bg);border:1px solid var(--line);border-radius:var(--r1);padding:8px var(--s3);font-size:13px}
.form .wide{grid-column:1/-1}
pre{background:var(--bg);border:1px solid var(--line);border-radius:var(--r1);padding:var(--s3);overflow:auto;max-height:380px;font:12px/1.55 var(--font-mono);white-space:pre-wrap}
.drawer{position:fixed;inset:0 0 0 auto;width:min(540px,92vw);background:var(--background-secondary);border-left:1px solid var(--line);box-shadow:none;padding:var(--s5);overflow:auto;transform:translateX(100%);transition:transform var(--dur) var(--ease);z-index:20}
.drawer.open{transform:translateX(0)}
.scrim{position:fixed;inset:0;background:var(--scrim);opacity:0;pointer-events:none;transition:opacity var(--dur) var(--ease);z-index:19}
.scrim.open{opacity:1;pointer-events:auto}
.bars{display:grid;gap:var(--s1)}
.bar-row{display:grid;grid-template-columns:78px minmax(0,1fr) 74px;align-items:center;gap:var(--s2);font-size:12px}
.bar-row .track{height:4px;background:var(--surface-2);border-radius:99px;overflow:hidden}
.bar-row .track i{display:block;height:100%;background:var(--accent)}
.link{color:var(--ink)}
.link:hover{text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--faint)}
.split{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:var(--s4);align-items:start}
.timeline{display:grid}
.event{display:grid;grid-template-columns:74px 90px minmax(0,1fr) 70px;gap:var(--s3);padding:8px var(--s4);border-bottom:1px solid var(--line);font-size:13px;align-items:baseline}
.event:last-child{border-bottom:0}
.pad .event{padding-left:0;padding-right:0}
.event time{font:400 12px var(--font-mono);color:var(--faint)}
.mem{grid-template-columns:minmax(0,1fr) minmax(120px,220px) 64px 92px;cursor:pointer}
.mem:hover{background:var(--surface-2)}
.mem .tags{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.noside .shell{grid-template-columns:minmax(0,1fr)}.noside .side{display:none}
.pal{position:fixed
.pal[hidden]{display:none}
.pal-box{width:min(520px,92vw);background:var(--surface);border-radius:var(--r3);box-shadow:0 0 0 1px var(--line-2),var(--shadow-l);overflow:hidden}
.pal-box input{width:100%;border:0;border-bottom:1px solid var(--line);background:transparent;padding:var(--s4);font-size:15px;outline:0}
.pal-list{max-height:320px;overflow:auto;padding:var(--s2)}
.pal-item{display:flex;justify-content:space-between;width:100%;border:0;background:transparent;border-radius:var(--r1);padding:var(--s2) var(--s3);cursor:pointer;text-align:left;font-size:14px}
.pal-item small{color:var(--faint);font-size:12px}
.pal-item.on,.pal-item:hover{background:var(--surface-2)}
@media (max-width:1100px){.ledger,.split{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}.stat:nth-child(2){border-right:0}.kpis{grid-template-columns:1fr}}
@media (max-width:800px){.shell{grid-template-columns:1fr}.side{position:static;height:auto;flex-direction:row;align-items:center;overflow-x:auto;padding:var(--s3)}.nav{display:flex}.brand small{display:none}.content,.top{padding-left:var(--s4);padding-right:var(--s4)}.field,#sideBtn{display:none}.form{grid-template-columns:1fr}.mem{grid-template-columns:minmax(0,1fr) 92px}.mem .tags,.mem .pill{display:none}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}.reveal{animation:none}}
</style>
</head>
<body><div class="shell">
<aside class="side">
  <div class="brand">Beril<small>local workspace</small></div>
  <nav class="nav" id="nav">
    <a href="#overview" data-page="overview" data-group="overview"><span>Overview</span></a>
    <a href="#jobs" data-page="jobs" data-group="work"><span>Work</span><b id="nJobs"></b></a>
    <a href="#memory" data-page="memory" data-group="memory"><span>Memory</span><b id="nMemory"></b></a>
    <a href="#threads" data-page="threads" data-group="intel"><span>Intel</span></a>
    <a href="#labs" data-page="labs" data-group="lab"><span>Lab</span></a>
  </nav>
</aside>
<main>
  <header class="top">
    <button class="btn icon" id="sideBtn" aria-label="Toggle sidebar" aria-pressed="false" title="Toggle sidebar (Ctrl \)"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1.75" y="2.75" width="12.5" height="10.5" rx="2.5"/><path d="M6 3v10"/></svg></button><h2 id="crumb">Overview</h2><div class="grow"></div>
    <label class="field"><input id="q" placeholder="Filter this page" aria-label="Filter this page"><span class="kbd">/</span></label>
    <button class="btn" id="palBtn">Go to <span class="kbd">Ctrl K</span></button>
    <button class="btn primary" id="newJob">New job</button>
  </header>
  <div class="content"><nav class="subnav" id="subnav" aria-label="Section"></nav><div id="view"></div></div>
</main>
<div class="scrim" id="scrim" onclick="closeDrawer()"></div>
<aside class="drawer" id="drawer" aria-live="polite"></aside>
<div class="pal" id="pal" hidden><div class="pal-box" role="dialog" aria-label="Go to page"><input id="palIn" placeholder="Go to page" autocomplete="off" aria-label="Go to page"><div class="pal-list" id="palList"></div></div></div>
<script>
const $=s=>document.querySelector(s), view=$('#view'), drawer=$('#drawer'), scrim=$('#scrim');
let page='overview', timer=null;
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const TOKEN='__BERIL_TOKEN__';
const get=async u=>{const r=await fetch(u);return r.json()};
const post=async(u,b)=>{const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json','X-Beril-Token':TOKEN},body:JSON.stringify(b)});return r.json()};
const money=n=>'$'+Number(n||0).toFixed(2);
const when=s=>{if(!s)return '';const d=new Date(s);return isNaN(d)?String(s).slice(0,16):d.toLocaleString([], {month:'short',day:'2-digit',hour:'2-digit',minute:'2-digit'})};
const GROUPS={overview:{label:'Overview',tabs:[]},work:{label:'Work',tabs:[['jobs','Jobs'],['activity','Activity'],['costs','Costs']]},memory:{label:'Memory',tabs:[]},intel:{label:'Intel',tabs:[['threads','Threads'],['experts','Experts'],['tools','Tools'],['methods','Methods'],['atlas','GitHub atlas'],['sources','Sources']]},lab:{label:'Lab',tabs:[['labs','Labs'],['training','Training'],['posture','Posture'],['scans','Scans']]}};
const groupOf=p=>Object.keys(GROUPS).find(g=>g===p||GROUPS[g].tabs.some(t=>t[0]===p))||'overview';
const PAGES=Object.keys(GROUPS).flatMap(g=>GROUPS[g].tabs.length?GROUPS[g].tabs.map(t=>[t[0],t[1],GROUPS[g].label]):[[g,GROUPS[g].label,'']]);
function nav(p){const go=()=>{page=p;const g=groupOf(p);document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('on',a.dataset.group===g));$('#crumb').textContent=GROUPS[g].label;$('#subnav').innerHTML=GROUPS[g].tabs.map(t=>`<a href="#${t[0]}" class="${t[0]===p?'on':''}">${t[1]}</a>`).join('');closeDrawer();route()};if(document.startViewTransition)document.startViewTransition(go);else go()}
document.querySelectorAll('.nav a').forEach(a=>a.onclick=e=>{e.preventDefault();nav(a.dataset.page)});
$('#q').oninput=()=>{clearTimeout(timer);timer=setTimeout(route,250)};
$('#newJob').onclick=()=>nav('jobs');
function setSide(off){document.body.classList.toggle('noside',off);$('#sideBtn').setAttribute('aria-pressed',off);try{localStorage.setItem('beril.noside',off?'1':'')}catch(e){}}
$('#sideBtn').onclick=()=>setSide(!document.body.classList.contains('noside'));
try{if(localStorage.getItem('beril.noside'))setSide(true)}catch(e){}
const pal=$('#pal'),palIn=$('#palIn'),palList=$('#palList');let palSel=0,palItems=[];
function palRender(){const q=palIn.value.trim().toLowerCase();palItems=PAGES.filter(x=>(x[1]+' '+x[2]).toLowerCase().includes(q));palSel=Math.min(palSel,Math.max(0,palItems.length-1));palList.innerHTML=palItems.map((x,i)=>`<button class="pal-item ${i===palSel?'on':''}" data-i="${i}"><span>${esc(x[1])}</span><small>${esc(x[2])}</small></button>`).join('')||'<div class="empty">No match.</div>'}
function palOpen(){pal.hidden=false;palIn.value='';palSel=0;palRender();palIn.focus()}
function palClose(){pal.hidden=true}
function palGo(i){const x=palItems[i];if(!x)return;palClose();if(location.hash.slice(1).split('?')[0]===x[0])nav(x[0]);else location.hash=x[0]}
$('#palBtn').onclick=palOpen;
palIn.oninput=()=>{palSel=0;palRender()};
palIn.onkeydown=e=>{if(e.key==='ArrowDown'){e.preventDefault();palSel=Math.min(palSel+1,palItems.length-1);palRender()}else if(e.key==='ArrowUp'){e.preventDefault();palSel=Math.max(palSel-1,0);palRender()}else if(e.key==='Enter'){e.preventDefault();palGo(palSel)}};
palList.onclick=e=>{const b=e.target.closest('.pal-item');if(b)palGo(+b.dataset.i)};
pal.onclick=e=>{if(e.target===pal)palClose()};
addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();pal.hidden?palOpen():palClose();return}const tag=(document.activeElement||{}).tagName;if(e.key==='/'&&tag!=='INPUT'&&tag!=='TEXTAREA'&&tag!=='SELECT'){e.preventDefault();$('#q').focus()}if((e.ctrlKey||e.metaKey)&&e.key==='\\'){e.preventDefault();$('#sideBtn').click()}if(e.key==='Escape'){closeDrawer();palClose()}});
function shell(title,sub,body,rail=''){view.innerHTML=`<div class="head"><h1>${esc(title)}</h1><p>${esc(sub)}</p></div><div class="ledger"><div>${body}</div><div class="rail">${rail}</div></div>`}
function table(items,cols){if(!items.length)return '<div class="empty">Nothing here yet.</div>';return '<div class="tbl"><table><thead><tr>'+cols.map(c=>`<th tabindex="0" onclick="sortTable(this)" onkeydown="if(event.key==='Enter')sortTable(this)">${c[0]}</th>`).join('')+'</tr></thead><tbody>'+items.map(r=>`<tr ${r.id?`data-job onclick="openJob('${r.id}')"`:''}>`+cols.map(c=>`<td>${c[1](r)}</td>`).join('')+'</tr>').join('')+'</tbody></table></div>'}

function sortTable(th){const tb=th.closest('table'),i=th.cellIndex,dir=th.dataset.dir==='asc'?'desc':'asc';tb.querySelectorAll('th').forEach(h=>delete h.dataset.dir);th.dataset.dir=dir;
  const val=r=>{const s=r.cells[i].textContent.trim(),n=parseFloat(s.replace(/[$,]/g,''));return isNaN(n)||!/^[$\d]/.test(s)?s.toLowerCase():n};
  const rows=[...tb.tBodies[0].rows].sort((a,b)=>{const x=val(a),y=val(b);return (x>y?1:x<y?-1:0)*(dir==='asc'?1:-1)});rows.forEach(r=>tb.tBodies[0].appendChild(r))}
async function overview(){
  const [d,mem]=await Promise.all([get('/api/overview'),get('/api/memory')]), s={...d.stats,memory:mem.length}, c=d.costs, t=d.training;
  const running=d.activity.filter(x=>x.status==='running').length;
  $('#nJobs').textContent=running||''; $('#nMemory').textContent=s.memory;
  const spend=c.month, budget=Number(c.budget.monthly_usd||25), pct=Math.min(100, spend/budget*100), tpct=t.total?t.done/t.total*100:0;
  view.innerHTML=`<div class="head"><h1>Overview</h1><p>Spend, live work and the latest activity on this machine. Loopback only.</p></div>
  <div class="kpis">
    <section class="panel pad"><p class="label">Spend this month</p><div class="big">${money(spend)}</div><div class="bar"><i style="width:${pct}%"></i></div><p class="sub">${pct.toFixed(0)}% of ${money(budget)} · ${money(c.today)} today</p></section>
    <section class="panel pad"><p class="label">Running now</p><div class="big">${running}</div><p class="sub" style="margin-top:var(--s4)">${d.activity.length} recent entries</p></section>
    <section class="panel pad"><p class="label">Training</p><div class="big">${t.done}<span class="of">/${t.total}</span></div><div class="bar"><i style="width:${tpct}%"></i></div><p class="sub">${s.memory} memory cards · ${s.threads} threads</p></section>
  </div>
  <div class="ledger"><section class="panel"><div class="panel-head"><p class="label">Recent activity</p><a class="link sub" href="#activity">View all</a></div>${table(d.activity.slice(0,8),[['Work',r=>`<span class="title">${esc(r.title)}</span><div class="meta">${esc(r.type||r.kind)} · ${esc(r.actor||'')}</div>`],['When',r=>`<span class="num meta">${when(r.at)}</span>`],['Cost',r=>`<span class="num">${money(r.cost)}</span>`],['State',r=>`<span class="status ${esc(r.status)}">${esc(r.status)}</span>`]])}</section>
  <div class="rail"><section class="panel pad"><p class="label">Next training</p>${t.next.slice(0,3).map(n=>`<div class="event" style="grid-template-columns:minmax(0,1fr) auto"><span>week ${n.week} · ${esc(n.text)}</span><button class="btn" onclick="done('${n.key}')">Done</button></div>`).join('')||'<p class="sub">Queue clear.</p>'}</section>
  <section class="panel pad"><p class="label">Latest scans</p>${d.scans.map(x=>`<div class="event" style="grid-template-columns:minmax(0,1fr)"><a class="link" href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a></div>`).join('')||'<p class="sub">No reports.</p>'}</section></div></div>
  <details class="faq" style="margin-top:var(--s4)"><summary>How to read this</summary><p>The score is severity times confidence, with verified and KEV boosts. It orders work and is not CVSS. A clean scan covers a short check list: logged-in flows, business logic and authorization stay manual. Reports live under scans/ on this machine; Posture aggregates them without uploading anything.</p></details>`;
}
async function activity(){const d=await get('/api/activity?limit=120');
  view.innerHTML=`<div class="head"><h1>Activity</h1><p>Jobs, labs, scans and journal entries in one stream. Newest first.</p></div><div class="panel pad"><div class="timeline">${d.map(r=>`<div class="event"><time>${when(r.at)}</time><span class="status ${esc(r.status)}">${esc(r.type||r.kind)}</span><span>${esc(r.title)}</span><span class="num">${money(r.cost)}</span></div>`).join('')||'<div class="empty">No activity.</div>'}</div></div>`;}
async function jobs(){const filter=location.hash.split('?status=')[1]||'';
  const d=await get('/api/jobs?status='+filter+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Jobs</h1><p>Every unit of work, its actor, model, tokens and cost. Click a row for detail.</p></div>
  <div class="split"><div class="panel"><div style="padding:var(--s3) var(--s3) 0"><div class="chips seg">${['','running','done','failed'].map(s=>`<button class="chip ${filter===s?'on':''}" onclick="location.hash='jobs${s?'?status='+s:''}'">${s||'all'}</button>`).join('')}</div></div>${table(d,[['Started',r=>`<span class="num">${when(r.started_at)}</span>`],['Type',r=>esc(r.type)],['Work',r=>`<span class="title">${esc(r.title)}</span>`],['Model',r=>`<span class="meta">${esc(r.model||'-')}</span>`],['Cost',r=>`<span class="num">${money(r.cost_usd)}</span>`],['State',r=>`<span class="status ${esc(r.status)}">${esc(r.status)}</span>`]])}</div>
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
async function memory(){const d=await get('/api/memory?q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Memory</h1><p>${d.length} durable cards. Recall before a search; refresh when stale.</p></div><div class="panel">${d.map(c=>`<div class="event mem" onclick="openCard('${c.id}')"><a class="link title" href="#" onclick="event.stopPropagation();openCard('${c.id}');return false">${esc(c.title)}</a><span class="meta tags">${esc((c.tags||[]).join(' · '))}</span>${c.confidence&&c.confidence!=='high'?`<span class="pill">${esc(c.confidence)}</span>`:'<span></span>'}<span class="meta num">${esc(c.updated)}</span></div>`).join('')||'<div class="empty">No cards.</div>'}</div>`;}
async function openCard(id){const r=await get('/api/memory/card?id='+encodeURIComponent(id));scrim.classList.add('open');drawer.classList.add('open');drawer.innerHTML=`<div style="display:flex;align-items:center"><span class="label" style="margin:0">${esc(id)}</span><div class="grow"></div><button class="btn" onclick="closeDrawer()">close</button></div><div style="margin-top:18px">${r.html||r.error}</div>`;}
async function costs(){const c=await get('/api/costs');const max=Math.max(1,...Object.values(c.daily));
  view.innerHTML=`<div class="head"><h1>Costs</h1><p>Tokens priced from data/llm_prices.json. Scans and labs are zero.</p></div>
  <div class="ledger"><div class="panel pad"><p class="label">Total spend</p><div class="big">${money(c.total)}</div><p class="sub">${money(c.today)} today · ${money(c.week)} this week · ${money(c.month)} this month</p>
  <div class="bars" style="margin-top:24px">${Object.entries(c.daily).slice(-30).map(([d,v])=>`<div class="bar-row"><span class="num">${d.slice(5)}</span><div class="track"><i style="width:${v/max*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">No priced jobs.</p>'}</div></div>
  <div class="rail"><section class="panel pad"><p class="label">Monthly budget</p><div class="big" style="font-size:32px">${money(c.budget.monthly_usd)}</div><div class="bar"><i style="width:${Math.min(100,c.month/c.budget.monthly_usd*100)}%"></i></div><div style="display:flex;gap:8px;margin-top:8px"><input class="mono" id="budget" value="${c.budget.monthly_usd}" style="width:80px;background:var(--bg);border:1px solid var(--line);padding:6px"><button class="btn" onclick="saveBudget()">save</button></div></section>
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
async function labs(){const d=await get('/api/labs');view.innerHTML=`<div class="head"><h1>Labs</h1><p>Each run executes the smoke test and stores the tail.</p></div><div class="panel">${d.labs.map(l=>{const r=d.runs[l]||{};return `<div class="event" style="grid-template-columns:120px minmax(0,1fr) 90px 110px 90px"><b>${l}</b><pre class="${r.output?'':'hidden'}" id="out-${l}" style="max-height:120px">${esc(r.output||'')}</pre><span class="status ${r.ok?'done':r.ok===false?'failed':'cancelled'}">${r.ok?'pass':r.ok===false?'fail':'idle'}</span><span class="meta">${esc(r.at||'not run')}</span><button class="btn" onclick="runLab('${l}',this)">Run test</button></div>`}).join('')}</div>`;}
async function runLab(l,b){b.disabled=true;b.textContent='Running';const d=await post('/api/lab/run',{lab:l});const o=$('#out-'+l);o.textContent=d.output;o.classList.remove('hidden');b.disabled=false;b.textContent='run test';}
async function training(){const d=await get('/api/training');view.innerHTML=`<div class="head"><h1>Training</h1><p>${d.done}/${d.total} tasks. A missed day is not a missed week.</p></div><div class="panel pad"><div class="bar"><i style="width:${d.pct}%"></i></div><p class="num">${d.pct}%</p></div><h2 class="label" style="margin-top:24px">Next</h2><div class="panel">${d.next.map(n=>`<div class="event" style="grid-template-columns:minmax(0,1fr) auto"><span>week ${n.week} · ${esc(n.text)}</span><button class="btn" onclick="done('${n.key}')">done</button></div>`).join('')||'<div class="empty">Complete.</div>'}</div><h2 class="label" style="margin-top:24px">Journal</h2><div class="panel">${d.journal.map(j=>`<div class="event" style="grid-template-columns:90px minmax(0,1fr)"><time>${esc(j.at)}</time><span>${esc(j.text)}</span></div>`).join('')||'<div class="empty">No entries.</div>'}</div>`;}
async function done(k){await post('/api/training/done',{key:k});route()}
async function posture(){const d=await get('/api/posture');
  const cards=d.latest.map(x=>`<article class="posture-card reveal"><h3>${esc(x.target)}</h3><p class="num">${x.counts.critical} critical · ${x.counts.high} high</p><p>${esc(x.mode)} · ${esc(x.at)}</p><p class="meta">${x.checked} checks · ${x.suppressed} suppressed</p></article>`).join('')||'<div class="empty">No scan JSON yet. Run a scan.</div>';
  shell('Posture','Severity over time, coverage and the latest scan per target. Built from local JSON only.',`<div class="card-grid">${cards}</div><h2 class="label" style="margin-top:24px">New findings by day</h2><div class="panel pad">${d.series.map(x=>`<div class="bar-row"><span class="num">${x.day}</span><div class="track"><i style="width:${x.total?Math.min(100,x.critical/x.total*100):0}%"></i></div><span class="num">${x.total}</span></div>`).join('')||'<p class="sub">No history.</p>'}</div><h2 class="label" style="margin-top:24px">Top checks</h2><div class="panel">${table(d.top,[['Check',r=>esc(r.check)],['Count',r=>`<span class="num">${r.count}</span>`],['Severity',r=>`<span class="status ${esc(r.severity)}">${esc(r.severity)}</span>`]])}</div>`,d.coverage.map(c=>`<section class="panel pad"><p class="label">${esc(c.label)}</p><div class="big" style="font-size:34px">${c.value}%</div><div class="bar"><i style="width:${c.value}%"></i></div></section>`).join(''));}
async function scans(){const d=await get('/api/scans');shell('Scans','Passive by default. A URL or local artifact, one report per run.',`<form class="panel pad" onsubmit="doScan(event)"><div style="display:flex;gap:8px"><input name="target" class="grow" placeholder="https://app.example or ./sample.apk" style="background:var(--bg);border:1px solid var(--line);padding:8px"><button class="btn primary">Run scan</button></div><pre id="scanout" class="hidden"></pre></form><div id="report"></div>`,`<section class="panel pad"><p class="label">Reports</p>${d.map(x=>`<div class="event" style="grid-template-columns:minmax(0,1fr) 70px"><a class="link" href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a><span class="meta">${x.size} B</span></div>`).join('')||'<div class="empty">No reports.</div>'}</section>`);}
async function doScan(e){e.preventDefault();const b=e.target.querySelector('button'),t=e.target.target.value.trim();if(!t)return;b.disabled=true;b.textContent='Running';const d=await post('/api/scan/run',{target:t});const o=$('#scanout');o.textContent=d.output;o.classList.remove('hidden');b.disabled=false;b.textContent='Run scan';if(d.report)openReport(d.report);}
async function openReport(name){const d=await get('/api/report?name='+encodeURIComponent(name));$('#report').innerHTML=`<h2 class="label" style="margin-top:24px">${esc(name)}</h2><div class="panel pad">${d.html||d.error}</div>`;scrollTo(0,0)}
async function sources(){const d=await get('/api/sources');shell('Sources','Harvested rows by source. One row is a gap.',table(d.map(x=>({name:x[0],n:x[1]})),[['Source',r=>esc(r.name)],['Rows',r=>`<span class="num">${r.n}</span>`]]),`<section class="panel pad"><p class="label">Coverage</p><p class="sub">${d.length} sources seen. Add a source in references/forums.md.</p></section>`);}
async function route(){closeDrawer();if(page==='overview')return overview();if(page==='activity')return activity();if(page==='jobs')return jobs();if(page==='costs')return costs();if(page==='memory')return memory();if(page==='threads')return threads();if(page==='experts')return experts();if(page==='tools')return tools();if(page==='methods')return methods();if(page==='atlas')return atlas();if(page==='labs')return labs();if(page==='training')return training();if(page==='posture')return posture();if(page==='scans')return scans();if(page==='sources')return sources();}
addEventListener('hashchange',()=>{const p=location.hash.slice(1).split('?')[0];if(p)nav(p)});
nav(location.hash?location.hash.slice(1).split('?')[0]:'overview');
</script></body></html>"""
