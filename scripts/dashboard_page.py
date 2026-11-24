PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="icon" type="image/png" href="data:image/png;base64,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">
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
  --accent-container:rgba(10,132,255,.24);--layer-hover:color-mix(in srgb,var(--text-primary) 8%,transparent);--layer-press:color-mix(in srgb,var(--text-primary) 12%,transparent);--glass:rgb(28 28 30/.72);--glass-bar:rgb(0 0 0/.72);--seg-on:#636366;--scrim:rgb(0 0 0/.6);
  --av:url("data:image/png;base64,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");
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
  --accent:#007aff;--accent-container:rgba(0,122,255,.14);--glass:rgb(255 255 255/.72);--glass-bar:rgb(242 242 247/.72);--seg-on:#fff;--scrim:rgb(0 0 0/.3);
  --shadow-s:0 1px 3px rgb(0 0 0/.06);--shadow-m:0 4px 6px rgb(0 0 0/.06),0 2px 4px rgb(0 0 0/.08);--shadow-l:0 20px 25px rgb(0 0 0/.1),0 8px 10px rgb(0 0 0/.12);
}}
/* Apple continuous corners: a superellipse (squircle), not a circular arc. Progressive: falls back to border-radius. */
@supports (corner-shape:squircle){*,*::before,*::after{corner-shape:squircle}}
*{box-sizing:border-box}
html,body{overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:13px/1.45 var(--font-body);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
button,input,select,textarea{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.btn:active,.chip:active,.nav a:active{transform:scale(.98)}
.shell{display:grid;grid-template-columns:216px minmax(0,1fr);min-height:100dvh}
.side{border-right:1px solid var(--line);padding:var(--s5) var(--s3);background:var(--glass);backdrop-filter:blur(20px) saturate(180%);display:flex;flex-direction:column;gap:var(--s5);position:sticky;top:0;height:100dvh}
.brand{display:grid;grid-template-columns:32px auto;column-gap:10px;align-items:center;font:600 15px/1.2 var(--font-body);padding:0 var(--s3);letter-spacing:-.01em}
.brand b{font-weight:600}
.av{grid-row:span 2;width:32px;height:32px;border-radius:50%;corner-shape:round;background:var(--av) center/cover;box-shadow:0 0 0 1px var(--line)}
.brand small{font:400 11px var(--font-body);color:var(--faint);margin:0;letter-spacing:0}
.nav{display:grid;gap:2px}
.nav a{display:flex;justify-content:space-between;align-items:center;min-height:28px;padding:6px var(--s4);border-radius:99px;color:var(--muted);font-size:13px;transition:background var(--dur) var(--ease),color var(--dur) var(--ease)}
.nav a:hover{background:var(--layer-hover);color:var(--ink)}
.nav a.on{background:var(--accent-container);color:var(--ink);font-weight:600}
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
.content{max-width:var(--max);margin:0 auto;padding:var(--s5) var(--s6) var(--s9);container-type:inline-size}
.subnav{display:flex;gap:var(--s1);margin-bottom:var(--s5);border-bottom:1px solid var(--line);overflow-x:auto}
.subnav:empty{display:none}
.subnav a{padding:var(--s2) var(--s3);color:var(--faint);font-size:13px;white-space:nowrap;border-radius:var(--r1) var(--r1) 0 0;transition:color var(--dur) var(--ease)}
.subnav a:hover{color:var(--ink);background:var(--layer-hover)}
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
tbody tr:hover{background:var(--layer-hover)}
tbody tr[data-job]{cursor:pointer}
.tbl{overflow-x:auto}
#view>.tbl{background:var(--surface);box-shadow:0 0 0 1px var(--line);border-radius:var(--r2)}
.num{font-family:var(--font-mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.reveal{animation:reveal linear both;animation-timeline:view();animation-range:entry 0% cover 28%}
@keyframes reveal{from{opacity:.001;transform:translateY(10px)}to{opacity:1;transform:none}}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(220px,100%),1fr));gap:var(--s3)}
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
.form input,.form select,.form textarea{min-width:0;width:100%;background:var(--bg);border:1px solid var(--line);border-radius:var(--r1);padding:6px var(--s3);font-size:13px}
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
.split .form{grid-template-columns:minmax(0,1fr)}
.timeline{display:grid}
.event{display:grid;grid-template-columns:74px 90px minmax(0,1fr) 70px;gap:var(--s3);padding:8px var(--s4);border-bottom:1px solid var(--line);font-size:13px;align-items:baseline}
.event:last-child{border-bottom:0}
.pad .event{padding-left:0;padding-right:0}
.event time{font:400 12px var(--font-mono);color:var(--faint)}
.mem{grid-template-columns:minmax(0,1fr) minmax(120px,220px) 64px 92px;cursor:pointer}
.mem:hover{background:var(--layer-hover)}
.mem .tags{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.noside .shell{grid-template-columns:minmax(0,1fr)}.noside .side{display:none}
.pal{position:fixed;inset:0;background:var(--scrim);display:grid;place-items:start center;padding-top:14vh;z-index:30}
.pal[hidden]{display:none}
.pal-box{width:min(520px,92vw);background:var(--surface);border-radius:28px;box-shadow:0 0 0 1px var(--line-2),var(--shadow-l);overflow:hidden}
.pal-box input{width:100%;border:0;border-bottom:1px solid var(--line);background:transparent;padding:var(--s4);font-size:15px;outline:0}
.pal-list{max-height:320px;overflow:auto;padding:var(--s2)}
.pal-item{display:flex;justify-content:space-between;width:100%;border:0;background:transparent;border-radius:var(--r1);padding:var(--s2) var(--s3);cursor:pointer;text-align:left;font-size:14px}
.pal-item small{color:var(--faint);font-size:12px}
.pal-item.on,.pal-item:hover{background:var(--layer-hover)}
/* live layer: content-level motion only, chrome stays still */
@keyframes rise{from{opacity:0;transform:translateY(8px)}}
@keyframes grow{from{transform:scaleX(0)}}
@keyframes growy{from{transform:scaleY(0)}}
@keyframes ringin{from{stroke-dashoffset:var(--c)}}
@keyframes shimmer{to{background-position:-200% 0}}
@keyframes pulse{0%{box-shadow:0 0 0 0 var(--pulse,transparent)}70%{box-shadow:0 0 0 6px transparent}100%{box-shadow:0 0 0 0 transparent}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes indet{0%{transform:translateX(-100%)}100%{transform:translateX(250%)}}
@keyframes toast-in{from{opacity:0;transform:translateY(8px) scale(.98)}}
@keyframes toast-life{to{transform:scaleX(0)}}
#view.enter>*{animation:rise 280ms var(--ease) both;animation-delay:calc(var(--i,0)*50ms)}
#view.enter tbody tr{animation:rise 260ms var(--ease) both;animation-delay:calc(min(var(--n,0),10)*25ms + 120ms)}
#view.enter .bar i,#view.enter .track i,#view.enter .sevbar i{animation:grow 700ms var(--ease) both;animation-delay:200ms}
#view.enter .stack{animation:growy 700ms var(--ease) both;animation-delay:200ms}
#view.enter .ring .val{animation:ringin 900ms var(--ease) both;animation-delay:150ms}
.track i,.sevbar i{transform-origin:left}
.sk{background:linear-gradient(90deg,var(--surface) 25%,var(--surface-2) 37%,var(--surface) 63%);background-size:200% 100%;animation:shimmer 1.4s linear infinite;border-radius:var(--r1)}
.sk.h{height:28px;width:180px;margin-bottom:var(--s3)}.sk.p{height:14px;width:320px;max-width:100%;margin-bottom:var(--s5)}.sk.c{height:110px;border-radius:var(--r2)}.sk.t{height:260px;border-radius:var(--r2)}
.sk-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s4);margin-bottom:var(--s4)}
.status.running::before{--pulse:color-mix(in srgb,var(--accent) 55%,transparent);animation:pulse 1.8s infinite}
.live{display:inline-flex;align-items:center;gap:6px;font:400 12px var(--font-mono);color:var(--faint);margin-right:var(--s2)}
.live i{width:6px;height:6px;border-radius:50%;background:var(--success);--pulse:color-mix(in srgb,var(--success) 55%,transparent);animation:pulse 2s infinite}
.spin{display:inline-block;width:12px;height:12px;border:2px solid currentColor;border-right-color:transparent;border-radius:50%;animation:spin .7s linear infinite}
.toasts{position:fixed;right:var(--s4);bottom:max(var(--s4),env(safe-area-inset-bottom));display:grid;gap:var(--s2);z-index:40;width:min(340px,calc(100vw - 32px))}
.toast{position:relative;overflow:hidden;display:flex;gap:var(--s3);align-items:center;background:var(--background-secondary);box-shadow:0 0 0 1px var(--line-2),var(--shadow-m);border-radius:var(--r2);padding:var(--s3) var(--s4);font-size:13px;animation:toast-in 220ms var(--ease)}
.toast::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--dot,var(--accent));flex:none}
.toast.ok{--dot:var(--success)}.toast.bad{--dot:var(--danger)}
.toast::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--dot,var(--accent));transform-origin:left;animation:toast-life 4s linear forwards}
.lift{transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease)}
.lift:hover{transform:translateY(-2px);box-shadow:0 0 0 1px var(--line-2),var(--shadow-m)}
.lab-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(280px,100%),1fr));gap:var(--s4)}
.lab{display:flex;flex-direction:column;gap:var(--s3);padding:var(--s4)}
.lab header{display:flex;gap:var(--s3);align-items:center}
.lab header .status{margin-left:auto}
.lab h3{margin:0;font:600 14px/1.2 var(--font-body);text-transform:capitalize}
.lab-mark{flex:none;width:36px;height:36px;border-radius:var(--r1);display:grid;place-items:center;font:600 12px var(--font-mono);background:hsl(var(--h) 60% 50%/.16);color:hsl(var(--h) 85% 72%)}
.lab-bar{height:4px;border-radius:99px;background:var(--surface-2);overflow:hidden}
.lab-bar i{display:block;height:100%;width:100%;background:var(--faint);transform-origin:left}
.lab.pass .lab-bar i{background:var(--success)}.lab.fail .lab-bar i{background:var(--danger)}
.lab.running .lab-bar i{width:40%;background:var(--accent);animation:indet 1.1s var(--ease) infinite}
.lab details summary{cursor:pointer;color:var(--muted);font-size:12px}
.lab footer{margin-top:auto;display:flex;gap:var(--s2);align-items:center}
.legend{display:flex;gap:var(--s3);flex-wrap:wrap;font-size:12px;color:var(--muted)}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend span::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--faint)}
.legend .ok::before{background:var(--success)}.legend .bad::before,.legend .sv-critical::before{background:var(--danger)}
.legend .sv-high::before{background:var(--warning)}.legend .sv-medium::before{background:#ffd60a}.legend .sv-low::before{background:var(--accent)}
.term{background:var(--bg);border-radius:var(--r1);padding:var(--s3);font:12px/1.6 var(--font-mono);max-height:240px;overflow:auto;white-space:pre-wrap;margin:var(--s2) 0 0;box-shadow:inset 0 0 0 1px var(--line)}
.t-pass{color:var(--success)}.t-fail{color:var(--danger)}.t-dim{color:var(--faint)}
.ring{position:relative;display:inline-grid;place-items:center}
.ring svg{transform:rotate(-90deg)}.ring .trk{stroke:var(--surface-2)}.ring .val{stroke:var(--accent);stroke-linecap:round}
.ring .ctr{position:absolute;text-align:center}
.train{display:grid;grid-template-columns:240px minmax(0,1fr);gap:var(--s4);align-items:start}
.weeks{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(150px,100%),1fr));gap:var(--s2)}
.wk{padding:var(--s3);border-radius:var(--r1);background:var(--surface-2);font-size:12px;color:var(--muted);box-shadow:inset 0 0 0 1px transparent}
.wk b{display:block;color:var(--ink);font-size:13px}
.wk.done{opacity:.55}.wk.done b::after{content:" \2713";color:var(--success)}
.wk.now{box-shadow:inset 0 0 0 1px var(--accent);color:var(--ink)}
.task{display:flex;gap:var(--s3);align-items:center;padding:10px var(--s4);border-bottom:1px solid var(--line)}
.task:last-child{border-bottom:0}
.check{flex:none;width:22px;height:22px;border-radius:50%;border:1.5px solid var(--line-2);background:transparent;cursor:pointer;padding:0;color:var(--success);display:grid;place-items:center;transition:background var(--dur) var(--ease),border-color var(--dur) var(--ease)}
.check:hover{border-color:var(--success);background:color-mix(in srgb,var(--success) 18%,transparent)}
.journal{position:relative;padding-left:var(--s5)}
.journal::before{content:"";position:absolute;left:4px;top:8px;bottom:8px;width:1px;background:var(--line)}
.j{position:relative;padding:var(--s2) 0}
.j::before{content:"";position:absolute;left:-24px;top:14px;width:9px;height:9px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px var(--surface)}
.sevbar{display:flex;gap:2px;height:6px;border-radius:99px;overflow:hidden;background:var(--surface-2);margin:var(--s3) 0}
.sevbar i{display:block;height:100%}
.sev-critical{background:var(--danger)}.sev-high{background:var(--warning)}.sev-medium{background:#ffd60a}.sev-low{background:var(--accent)}.sev-info{background:var(--faint)}
.target{display:flex;flex-direction:column;gap:var(--s1);min-width:0}
.target h3{margin:0;font:600 14px/1.3 var(--font-body);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cols{display:flex;align-items:flex-end;gap:6px;height:130px}
.col{flex:1;min-width:8px;max-width:64px;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:stretch;font-size:10px;color:var(--faint);text-align:center;gap:4px}
.stack{display:flex;flex-direction:column-reverse;border-radius:4px;overflow:hidden;transform-origin:bottom;min-height:3px}
.stack i{display:block}
.eq{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s4);margin-top:var(--s4)}
.rings{display:flex;gap:var(--s5);flex-wrap:wrap}.rings figure{margin:0;text-align:center;font-size:12px;color:var(--muted);max-width:120px}
.cmd{display:flex;align-items:center;gap:var(--s3);background:var(--surface);box-shadow:0 0 0 1px var(--line);border-radius:99px;padding:var(--s2) var(--s2) var(--s2) var(--s4);transition:box-shadow var(--dur) var(--ease)}
.cmd:focus-within{box-shadow:0 0 0 2px var(--accent)}
.cmd input{flex:1;min-width:0;border:0;outline:0;background:transparent;font:13px var(--font-mono);padding:6px 0}
.report-item{display:flex;justify-content:space-between;gap:var(--s3);padding:10px var(--s4);border-bottom:1px solid var(--line);font-size:13px}
.report-item:last-child{border-bottom:0}.report-item:hover{background:var(--layer-hover)}
.reportview{overflow-x:auto}.reportview table{font-size:12px}
.spark{display:block;margin:var(--s3) 0 0}
@container (max-width:900px){.train,.eq{grid-template-columns:minmax(0,1fr)}.sk-grid{grid-template-columns:minmax(0,1fr)}.ledger,.split{grid-template-columns:minmax(0,1fr)}.stats{grid-template-columns:repeat(2,1fr)}.stat:nth-child(2){border-right:0}}
@container (max-width:700px){.kpis{grid-template-columns:minmax(0,1fr)}.head h1{font-size:22px}}
@container (max-width:640px){
  .tbl thead{display:none}.tbl table,.tbl tbody,.tbl tr,.tbl td{display:block}
  .tbl tbody tr{padding:var(--s3) 0;border-bottom:1px solid var(--line)}.tbl tbody tr:last-child{border-bottom:0}
  .tbl td{display:flex;justify-content:space-between;gap:var(--s3);padding:3px var(--s4);border:0;text-align:right}
  .tbl td::before{content:attr(data-label);color:var(--faint);font-size:12px;text-align:left}
  .tbl td:first-child{display:block;text-align:left;font-weight:500}.tbl td:first-child::before{display:none}
  .timeline .event{grid-template-columns:64px minmax(0,1fr) auto}.timeline .event .status{display:none}
  .mem{grid-template-columns:minmax(0,1fr) 92px}.mem .tags,.mem .pill{display:none}
}
@media (max-width:800px){.shell{grid-template-columns:1fr}.side{position:static;height:auto;flex-direction:row;align-items:center;overflow-x:auto;padding:var(--s3) max(var(--s3),env(safe-area-inset-left))}.nav{display:flex}.brand small{display:none}.content,.top{padding-left:var(--s4);padding-right:var(--s4)}.field,#sideBtn,.top h2,#palBtn .kbd,.live{display:none}.top{gap:6px}.form{grid-template-columns:1fr}}
@media (pointer:coarse){.btn,.chip,.nav a,.subnav a,.pal-item{min-height:44px}.seg .chip{min-height:40px}.form input,.form select,.form textarea,.field input,.pal-box input,#budget{font-size:16px}.field{min-height:44px}.nav{gap:var(--s1)}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}
</style>
</head>
<body><div class="shell">
<aside class="side">
  <div class="brand"><span class="av" role="img" aria-label="Beril"></span><b>Beril</b><small>local workspace</small></div>
  <nav class="nav" id="nav">
    <a href="/" data-page="overview" data-group="overview"><span>Overview</span></a>
    <a href="/jobs" data-page="jobs" data-group="work"><span>Work</span><b id="nJobs"></b></a>
    <a href="/memory" data-page="memory" data-group="memory"><span>Memory</span><b id="nMemory"></b></a>
    <a href="/threads" data-page="threads" data-group="intel"><span>Intel</span></a>
    <a href="/labs" data-page="labs" data-group="lab"><span>Lab</span></a>
  </nav>
</aside>
<main>
  <header class="top">
    <button class="btn icon" id="sideBtn" aria-label="Toggle sidebar" aria-pressed="false" title="Toggle sidebar (Ctrl \)"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1.75" y="2.75" width="12.5" height="10.5" rx="2.5"/><path d="M6 3v10"/></svg></button><h2 id="crumb">Overview</h2><div class="grow"></div>
    <span class="live" title="Refreshes every 6 seconds"><i></i><span id="upd">live</span></span>
    <label class="field"><input id="q" placeholder="Filter this page" aria-label="Filter this page"><span class="kbd">/</span></label>
    <button class="btn" id="palBtn">Go to <span class="kbd">Ctrl K</span></button>
    <button class="btn primary" id="newJob">New job</button>
  </header>
  <div class="content"><nav class="subnav" id="subnav" aria-label="Section"></nav><div id="view"></div></div>
</main>
<div class="scrim" id="scrim" onclick="closeDrawer()"></div>
<aside class="drawer" id="drawer" aria-live="polite"></aside>
<div class="toasts" id="toasts" role="status" aria-live="polite"></div>
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
function nav(p){const go=()=>{page=p;const g=groupOf(p);document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('on',a.dataset.group===g));$('#crumb').textContent=GROUPS[g].label;$('#subnav').innerHTML=GROUPS[g].tabs.map(t=>`<a href="/${t[0]}" class="${t[0]===p?'on':''}">${t[1]}</a>`).join('');closeDrawer();route()};go()}
const pathFor=p=>p==='overview'?'/':'/'+p;
const pageFromPath=pn=>{const s=pn.replace(/^\/|\/$/g,'').split('/')[0];return PAGES.some(x=>x[0]===s)?s:'overview'};
const qp=(k,d)=>new URLSearchParams(location.search).get(k)||d;
function navTo(url){const u=new URL(url,location.origin),to=u.pathname+u.search;if(to!==location.pathname+location.search)history.pushState(null,'',to);nav(pageFromPath(u.pathname))}
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="/"]');if(!a||a.target||e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;e.preventDefault();navTo(a.getAttribute('href'))});
$('#q').oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>route(true),250)};
$('#newJob').onclick=()=>navTo('/jobs');
function setSide(off){document.body.classList.toggle('noside',off);$('#sideBtn').setAttribute('aria-pressed',off);try{localStorage.setItem('beril.noside',off?'1':'')}catch(e){}}
$('#sideBtn').onclick=()=>setSide(!document.body.classList.contains('noside'));
try{if(localStorage.getItem('beril.noside'))setSide(true)}catch(e){}
const pal=$('#pal'),palIn=$('#palIn'),palList=$('#palList');let palSel=0,palItems=[];
function palRender(){const q=palIn.value.trim().toLowerCase();palItems=PAGES.filter(x=>(x[1]+' '+x[2]).toLowerCase().includes(q));palSel=Math.min(palSel,Math.max(0,palItems.length-1));palList.innerHTML=palItems.map((x,i)=>`<button class="pal-item ${i===palSel?'on':''}" data-i="${i}"><span>${esc(x[1])}</span><small>${esc(x[2])}</small></button>`).join('')||'<div class="empty">No match.</div>'}
function palOpen(){pal.hidden=false;palIn.value='';palSel=0;palRender();palIn.focus()}
function palClose(){pal.hidden=true}
function palGo(i){const x=palItems[i];if(!x)return;palClose();navTo(pathFor(x[0]))}
$('#palBtn').onclick=palOpen;
palIn.oninput=()=>{palSel=0;palRender()};
palIn.onkeydown=e=>{if(e.key==='ArrowDown'){e.preventDefault();palSel=Math.min(palSel+1,palItems.length-1);palRender()}else if(e.key==='ArrowUp'){e.preventDefault();palSel=Math.max(palSel-1,0);palRender()}else if(e.key==='Enter'){e.preventDefault();palGo(palSel)}};
palList.onclick=e=>{const b=e.target.closest('.pal-item');if(b)palGo(+b.dataset.i)};
pal.onclick=e=>{if(e.target===pal)palClose()};
addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();pal.hidden?palOpen():palClose();return}const tag=(document.activeElement||{}).tagName;if(e.key==='/'&&tag!=='INPUT'&&tag!=='TEXTAREA'&&tag!=='SELECT'){e.preventDefault();$('#q').focus()}if((e.ctrlKey||e.metaKey)&&e.key==='\\'){e.preventDefault();$('#sideBtn').click()}if(e.key==='Escape'){closeDrawer();palClose()}});
function shell(title,sub,body,rail=''){view.innerHTML=`<div class="head"><h1>${esc(title)}</h1><p>${esc(sub)}</p></div><div class="ledger"><div>${body}</div><div class="rail">${rail}</div></div>`}
function table(items,cols){if(!items.length)return '<div class="empty">Nothing here yet.</div>';return '<div class="tbl"><table><thead><tr>'+cols.map(c=>`<th tabindex="0" onclick="sortTable(this)" onkeydown="if(event.key==='Enter')sortTable(this)">${c[0]}</th>`).join('')+'</tr></thead><tbody>'+items.map(r=>`<tr ${r.id?`data-job onclick="openJob('${r.id}')"`:''}>`+cols.map(c=>`<td data-label="${c[0]}">${c[1](r)}</td>`).join('')+'</tr>').join('')+'</tbody></table></div>'}

const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
const SKEL='<div class="sk h"></div><div class="sk p"></div><div class="sk-grid"><div class="sk c"></div><div class="sk c"></div><div class="sk c"></div></div><div class="sk t"></div>';
let busy=false;const openLabs=new Set();
function toast(msg,kind=''){const el=document.createElement('div');el.className='toast '+kind;el.textContent=msg;$('#toasts').appendChild(el);setTimeout(()=>el.remove(),4200)}
function countUp(el){const to=+el.dataset.count,money=el.dataset.fmt==='money',fmt=v=>money?'$'+v.toFixed(2):String(Math.round(v));if(reduce||!isFinite(to)){el.textContent=fmt(to);return}const t0=performance.now(),D=700,f=now=>{const k=Math.min(1,(now-t0)/D),e=1-Math.pow(1-k,3);el.textContent=fmt(to*e);if(k<1)requestAnimationFrame(f)};requestAnimationFrame(f)}
function stagger(){[...view.children].forEach((c,i)=>c.style.setProperty('--i',Math.min(i,8)));view.querySelectorAll('tbody tr').forEach((r,i)=>r.style.setProperty('--n',i));view.querySelectorAll('[data-count]').forEach(countUp);view.classList.add('enter');setTimeout(()=>view.classList.remove('enter'),1200)}
function ring(p,s=120,w=10,col){const r=(s-w)/2,c=2*Math.PI*r,off=c*(1-Math.max(0,Math.min(100,p))/100);return `<svg width="${s}" height="${s}" viewBox="0 0 ${s} ${s}" aria-hidden="true"><circle class="trk" cx="${s/2}" cy="${s/2}" r="${r}" fill="none" stroke-width="${w}"/><circle class="val" cx="${s/2}" cy="${s/2}" r="${r}" fill="none" stroke-width="${w}" stroke-dasharray="${c}" stroke-dashoffset="${off}" style="--c:${c}${col?';stroke:'+col:''}"/></svg>`}
function spark(v,w=140,h=36){if(!v||v.length<2)return '';const mx=Math.max(...v,1e-9),d=v.map((x,i)=>(i?'L':'M')+(i/(v.length-1)*w).toFixed(1)+' '+(h-2-(x/mx)*(h-6)).toFixed(1)).join('');return `<svg class="spark" width="100%" height="${h}" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" aria-hidden="true"><path d="${d}L${w} ${h}L0 ${h}Z" fill="var(--accent)" opacity=".14"/><path d="${d}" fill="none" stroke="var(--accent)" stroke-width="1.5" vector-effect="non-scaling-stroke"/></svg>`}
const ago=s=>{const d=new Date(s);if(isNaN(d))return String(s);const m=Math.round((Date.now()-d)/60000);return m<1?'just now':m<60?m+' min ago':m<1440?Math.round(m/60)+' h ago':Math.round(m/1440)+' d ago'};
const term=o=>esc(o||'').split('\n').map(l=>/^(PASS|ok\b|good)/i.test(l)?`<span class="t-pass">${l}</span>`:/^(FAIL|bad\b|error)/i.test(l)?`<span class="t-fail">${l}</span>`:l).join('\n');
function typeOut(el,text){return new Promise(res=>{const L=String(text).split('\n');let i=0;const step=()=>{const n=reduce?L.length:Math.min(3,L.length-i);for(let k=0;k<n&&i<L.length;k++,i++)el.innerHTML+=term(L[i])+'\n';el.scrollTop=el.scrollHeight;if(i<L.length)setTimeout(step,16);else res()};step()})}
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
    <section class="panel pad"><p class="label">Spend this month</p><div class="big"><span data-count="${spend}" data-fmt="money">${money(spend)}</span></div>${spark(Object.values(c.daily||{}).slice(-14))}<div class="bar"><i style="width:${pct}%"></i></div><p class="sub">${pct.toFixed(0)}% of ${money(budget)} · ${money(c.today)} today</p></section>
    <section class="panel pad"><p class="label">Running now</p><div class="big"><span data-count="${running}">${running}</span>${running?' <span class="status running"></span>':''}</div><p class="sub" style="margin-top:var(--s4)">${d.activity.length} recent entries</p></section>
    <section class="panel pad"><p class="label">Training</p><div class="big"><span data-count="${t.done}">${t.done}</span><span class="of">/${t.total}</span></div><div class="bar"><i style="width:${tpct}%"></i></div><p class="sub">${s.memory} memory cards · ${s.threads} threads</p></section>
  </div>
  <div class="ledger"><section class="panel"><div class="panel-head"><p class="label">Recent activity</p><a class="link sub" href="/activity">View all</a></div>${table(d.activity.slice(0,8),[['Work',r=>`<span class="title">${esc(r.title)}</span><div class="meta">${esc(r.type||r.kind)} · ${esc(r.actor||'')}</div>`],['When',r=>`<span class="num meta">${when(r.at)}</span>`],['Cost',r=>`<span class="num">${money(r.cost)}</span>`],['State',r=>`<span class="status ${esc(r.status)}">${esc(r.status)}</span>`]])}</section>
  <div class="rail"><section class="panel pad"><p class="label">Next training</p>${t.next.slice(0,3).map(n=>`<div class="event" style="grid-template-columns:minmax(0,1fr) auto"><span>week ${n.week} · ${esc(n.text)}</span><button class="btn" onclick="done('${n.key}')">Done</button></div>`).join('')||'<p class="sub">Queue clear.</p>'}</section>
  <section class="panel pad"><p class="label">Latest scans</p>${d.scans.map(x=>`<div class="event" style="grid-template-columns:minmax(0,1fr)"><a class="link" href="#" onclick="openReport('${x.name}');return false">${esc(x.name)}</a></div>`).join('')||'<p class="sub">No reports.</p>'}</section></div></div>
  <details class="faq" style="margin-top:var(--s4)"><summary>How to read this</summary><p>The score is severity times confidence, with verified and KEV boosts. It orders work and is not CVSS. A clean scan covers a short check list: logged-in flows, business logic and authorization stay manual. Reports live under scans/ on this machine; Posture aggregates them without uploading anything.</p></details>`;
}
async function activity(){const d=await get('/api/activity?limit=120');
  view.innerHTML=`<div class="head"><h1>Activity</h1><p>Jobs, labs, scans and journal entries in one stream. Newest first.</p></div><div class="panel pad"><div class="timeline">${d.map(r=>`<div class="event"><time>${when(r.at)}</time><span class="status ${esc(r.status)}">${esc(r.type||r.kind)}</span><span>${esc(r.title)}</span><span class="num">${money(r.cost)}</span></div>`).join('')||'<div class="empty">No activity.</div>'}</div></div>`;}
async function jobs(){const filter=qp('status','');
  const d=await get('/api/jobs?status='+filter+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Jobs</h1><p>Every unit of work, its actor, model, tokens and cost. Click a row for detail.</p></div>
  <div class="split"><div class="panel"><div style="padding:var(--s3) var(--s3) 0"><div class="chips seg">${['','running','done','failed'].map(s=>`<button class="chip ${filter===s?'on':''}" onclick="navTo('/jobs${s?'?status='+s:''}')">${s||'all'}</button>`).join('')}</div></div>${table(d,[['Started',r=>`<span class="num">${when(r.started_at)}</span>`],['Type',r=>esc(r.type)],['Work',r=>`<span class="title">${esc(r.title)}</span>`],['Model',r=>`<span class="meta">${esc(r.model||'-')}</span>`],['Cost',r=>`<span class="num">${money(r.cost_usd)}</span>`],['State',r=>`<span class="status ${esc(r.status)}">${esc(r.status)}</span>`]])}</div>
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
  const r=await post('/api/jobs',{...o,status:'running',actor:'human'});if(r.id){toast('Job created','ok');navTo('/jobs')}}
async function openJob(id){const d=await get('/api/jobs?q='+id);const r=d.find(x=>x.id===id);if(!r)return;
  scrim.classList.add('open');drawer.classList.add('open');
  drawer.innerHTML=`<div style="display:flex;gap:8px;align-items:center"><span class="status ${esc(r.status)}">${esc(r.status)}</span><div class="grow"></div><button class="btn" onclick="closeDrawer()">close</button></div><h2 style="font:400 26px/1.15 var(--font-display);margin:18px 0 6px">${esc(r.title)}</h2><p class="sub">${esc(r.type)} · ${esc(r.actor)} · ${esc(r.model||'no model')}</p>
  <div class="stats" style="grid-template-columns:1fr 1fr;margin:18px 0"><div class="stat"><b>${money(r.cost_usd)}</b><span>cost</span></div><div class="stat"><b>${(r.tokens_in||0)+(r.tokens_out||0)}</b><span>tokens</span></div></div>
  <p class="label">Started</p><p class="mono">${esc(r.started_at)}</p><p class="label">Finished</p><p class="mono">${esc(r.finished_at||'still running')}</p><p class="label">Target</p><p>${esc(r.target||'-')}</p><p class="label">Notes</p><p>${esc(r.notes||'-')}</p><p class="label">Log</p><p class="mono">${esc(r.log||'-')}</p>
  ${r.status==='running'?`<button class="btn primary" style="margin-top:18px" onclick="finishJob('${r.id}','done')">Mark done</button> <button class="btn" onclick="finishJob('${r.id}','failed')">Failed</button>`:''}`;
}
function closeDrawer(){scrim.classList.remove('open');drawer.classList.remove('open')}
async function finishJob(id,status){await post('/api/jobs/finish',{id,status});closeDrawer();toast('Job updated','ok');route(true)}
async function memory(){const d=await get('/api/memory?q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Memory</h1><p>${d.length} durable cards. Recall before a search; refresh when stale.</p></div><div class="panel">${d.map(c=>`<div class="event mem" onclick="openCard('${c.id}')"><a class="link title" href="#" onclick="event.stopPropagation();openCard('${c.id}');return false">${esc(c.title)}</a><span class="meta tags">${esc((c.tags||[]).join(' · '))}</span>${c.confidence&&c.confidence!=='high'?`<span class="pill">${esc(c.confidence)}</span>`:'<span></span>'}<span class="meta num">${esc(c.updated)}</span></div>`).join('')||'<div class="empty">No cards.</div>'}</div>`;}
async function openCard(id){const r=await get('/api/memory/card?id='+encodeURIComponent(id));scrim.classList.add('open');drawer.classList.add('open');drawer.innerHTML=`<div style="display:flex;align-items:center"><span class="label" style="margin:0">${esc(id)}</span><div class="grow"></div><button class="btn" onclick="closeDrawer()">close</button></div><div style="margin-top:18px">${r.html||r.error}</div>`;}
async function costs(){const c=await get('/api/costs');const max=Math.max(1,...Object.values(c.daily));
  view.innerHTML=`<div class="head"><h1>Costs</h1><p>Tokens priced from data/llm_prices.json. Scans and labs are zero.</p></div>
  <div class="ledger"><div class="panel pad"><p class="label">Total spend</p><div class="big"><span data-count="${c.total}" data-fmt="money">${money(c.total)}</span></div><p class="sub">${money(c.today)} today · ${money(c.week)} this week · ${money(c.month)} this month</p>
  <div class="bars" style="margin-top:24px">${Object.entries(c.daily).slice(-30).map(([d,v])=>`<div class="bar-row"><span class="num">${d.slice(5)}</span><div class="track"><i style="width:${v/max*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">No priced jobs.</p>'}</div></div>
  <div class="rail"><section class="panel pad"><p class="label">Monthly budget</p><div class="big" style="font-size:32px">${money(c.budget.monthly_usd)}</div><div class="bar"><i style="width:${Math.min(100,c.month/c.budget.monthly_usd*100)}%"></i></div><div style="display:flex;gap:8px;margin-top:8px"><input class="mono" id="budget" value="${c.budget.monthly_usd}" style="width:80px;background:var(--bg);border:1px solid var(--line);padding:6px"><button class="btn" onclick="saveBudget()">save</button></div></section>
  <section class="panel pad"><p class="label">By model</p>${Object.entries(c.by_model).map(([m,v])=>`<div class="bar-row"><span>${esc(m)}</span><div class="track"><i style="width:${v/Math.max(1,c.total)*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">None.</p>'}</section>
  <section class="panel pad"><p class="label">By type</p>${Object.entries(c.by_type).map(([m,v])=>`<div class="bar-row"><span>${esc(m)}</span><div class="track"><i style="width:${v/Math.max(1,c.total)*100}%"></i></div><span class="num">${money(v)}</span></div>`).join('')||'<p class="sub">None.</p>'}</section></div></div>`;
}
async function saveBudget(){await post('/api/budget',{monthly_usd:Number($('#budget').value)||25});toast('Budget saved','ok');route(true)}
async function threads(){const src=qp('source','');const d=await get('/api/threads?limit=200&q='+encodeURIComponent($('#q').value)+'&source='+encodeURIComponent(src));
  view.innerHTML=`<div class="head"><h1>Threads</h1><p>${d.length} public threads and reports.</p></div><div class="chips" id="srcs"></div>`+table(d,[['Source',r=>esc(r.source)],['Title',r=>`<a class="link" href="${esc(r.url)}" target="_blank">${esc(r.title)}</a>`],['Date',r=>`<span class="num">${esc((r.date||'').slice(0,10))}</span>`]]);
  const s=await get('/api/sources');$('#srcs').innerHTML=s.map(x=>`<button class="chip ${x[0]===src?'on':''}" onclick="navTo('/threads?source='+encodeURIComponent('${esc(x[0])}'))">${esc(x[0])} ${x[1]}</button>`).join('');
}
async function experts(){const d=await get('/api/experts?q='+encodeURIComponent($('#q').value));view.innerHTML=`<div class="head"><h1>Experts</h1><p>People and teams with public work.</p></div>`+table(d,[['Name',r=>`<a class="link" href="${esc(r.profile)}" target="_blank">${esc(r.name)}</a>`],['Focus',r=>esc(r.focus)],['Works',r=>r.works?.length||0]]);}
async function tools(){const kind=qp('kind','re');const d=await get('/api/tools?kind='+kind+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>Tools</h1><p>${d.length} entries. A shelf, not a verdict.</p></div><div class="chips"><button class="chip ${kind==='re'?'on':''}" onclick="navTo('/tools?kind=re')">RE and offense</button><button class="chip ${kind==='canonical'?'on':''}" onclick="navTo('/tools?kind=canonical')">Core shelf</button></div>`+table(d,[['Name',r=>`<a class="link" href="${esc(r.repo)}" target="_blank">${esc(r.name)}</a>`],['Category',r=>esc(r.category)],['Stars',r=>`<span class="num">${esc(r.stars||'-')}</span>`],['Description',r=>esc((r.description||'').slice(0,110))]]);}
async function methods(){const d=await get('/api/methods?q='+encodeURIComponent($('#q').value));view.innerHTML=`<div class="head"><h1>Methods</h1><p>Extracted structure and code density.</p></div>`+table(d,[['Title',r=>`<a class="link" href="${esc(r.url)}" target="_blank">${esc(r.title)}</a>`],['Source',r=>esc(r.source)],['Code',r=>`<span class="num">${r.code_blocks||0}</span>`]]);}
async function atlas(){const cat=qp('cat','');const d=await get('/api/atlas?category='+encodeURIComponent(cat)+'&q='+encodeURIComponent($('#q').value));
  view.innerHTML=`<div class="head"><h1>GitHub atlas</h1><p>${d.length} repositories. Stars are a snapshot.</p></div><div class="chips"><button class="chip ${!cat?'on':''}" onclick="navTo('/atlas')">all</button>${['bug-bounty','web-security','cloud-security','binary','fuzzing','detection','mobile','firmware','ai-security'].map(c=>`<button class="chip ${cat===c?'on':''}" onclick="navTo('/atlas?cat=${c}')">${c}</button>`).join('')}</div>`+table(d,[['Repo',r=>`<a class="link" href="${esc(r.url)}" target="_blank">${esc(r.repo)}</a>`],['Stars',r=>`<span class="num">${r.stars}</span>`],['Language',r=>esc(r.language||'-')],['Description',r=>esc((r.description||'').slice(0,110))]]);}
function labCard(l,r,s){const o=r.output||'',p=(o.match(/^PASS/gm)||[]).length,f=(o.match(/^FAIL/gm)||[]).length,h=[...l].reduce((a,c)=>a+c.charCodeAt(0)*7,0)%360;
  return `<article class="panel lab lift ${s}" id="lab-${esc(l)}" style="--h:${h}"><header><span class="lab-mark">${esc(l.slice(0,2).toUpperCase())}</span><div><h3>${esc(l)}</h3><p class="meta">${r.at?'Ran '+ago(r.at):'Not run yet'}</p></div><span class="status ${s==='pass'?'done':s==='fail'?'failed':''}">${s==='pass'?'Pass':s==='fail'?'Fail':'Idle'}</span></header><div class="lab-bar"><i></i></div>
  <div class="legend">${p||f?`<span class="ok">${p} passed</span>${f?`<span class="bad">${f} failed</span>`:''}`:'<span>No checks recorded</span>'}</div>
  ${o?`<details ${openLabs.has(l)?'open':''} ontoggle="this.open?openLabs.add('${esc(l)}'):openLabs.delete('${esc(l)}')"><summary>Output</summary><pre class="term">${term(o)}</pre></details>`:''}
  <footer><button class="btn" onclick="runLab('${esc(l)}',this)">Run test</button></footer></article>`}
async function labs(){const d=await get('/api/labs'),R=d.runs||{};window.LD=d;
  const st=l=>{const r=R[l]||{};return r.ok?'pass':r.ok===false?'fail':'idle'},n=d.labs.length;
  const pass=d.labs.filter(l=>st(l)==='pass').length,fail=d.labs.filter(l=>st(l)==='fail').length,idle=n-pass-fail;
  view.innerHTML=`<div class="head"><h1>Labs</h1><p>${n} labs. Each run executes the smoke test and stores the tail.</p></div>
  <div class="kpis">
    <section class="panel pad"><p class="label">Passing</p><div class="big"><span data-count="${pass}">${pass}</span><span class="of">/${n}</span></div><div class="bar"><i style="width:${pass/Math.max(1,n)*100}%;background:var(--success)"></i></div><p class="sub">${pass===n&&n?'Every lab passes.':'Last recorded run of each lab.'}</p></section>
    <section class="panel pad"><p class="label">Failing</p><div class="big"><span data-count="${fail}">${fail}</span></div><p class="sub" style="margin-top:var(--s4)">${fail?'Open a card to read the output.':'Nothing failing.'}</p></section>
    <section class="panel pad"><p class="label">Not run yet</p><div class="big"><span data-count="${idle}">${idle}</span></div><p class="sub" style="margin-top:var(--s4)">Run a test to record a result.</p></section>
  </div>
  <div class="lab-grid">${d.labs.map(l=>labCard(l,R[l]||{},st(l))).join('')}</div>`;}
async function runLab(l,b){busy=true;const c=document.getElementById('lab-'+l);if(c){c.classList.remove('pass','fail');c.classList.add('running')}b.disabled=true;b.innerHTML='<span class="spin"></span> Running';
  try{await post('/api/lab/run',{lab:l})}catch(e){}
  busy=false;openLabs.add(l);await labs();const r=((window.LD||{}).runs||{})[l]||{};toast(l+' lab '+(r.ok?'passed':'failed'),r.ok?'ok':'bad')}
async function training(){const d=await get('/api/training'),cur=(d.next[0]||{}).week;
  view.innerHTML=`<div class="head"><h1>Training</h1><p>${d.done} of ${d.total} tasks. A missed day is not a missed week.</p></div>
  <div class="train"><section class="panel pad" style="text-align:center"><div class="ring">${ring(d.pct,180,14)}<div class="ctr"><div class="big" style="font-size:40px"><span data-count="${d.pct}">${d.pct}</span>%</div><p class="sub">complete</p></div></div><p class="sub" style="margin-top:var(--s4)">${d.next.length?'Now on week '+cur:'Curriculum complete.'}</p></section>
  <div class="grid">
    <section class="panel"><div class="panel-head"><p class="label">Up next</p></div>${d.next.map(n=>`<div class="task"><button class="check" aria-label="Mark done" onclick="done('${esc(n.key)}',this)"></button><div style="flex:1;min-width:0"><div class="title">${esc(n.text)}</div><div class="meta">Week ${n.week}${n.minutes?' · '+n.minutes+' min':''}</div></div></div>`).join('')||'<div class="empty">Complete.</div>'}</section>
    <section class="panel pad"><p class="label">Curriculum</p><div class="weeks">${d.weeks.map(w=>`<div class="wk ${cur==null||w.week<cur?'done':w.week===cur?'now':''}"><b>Week ${w.week}</b>${esc(w.phase||'')}<br><span class="meta">${esc(w.title||'')}</span></div>`).join('')}</div></section>
    <section class="panel pad"><p class="label">Journal</p><div class="journal">${d.journal.map(j=>`<div class="j"><time class="meta">${esc(j.at)}</time><div>${esc(j.text)}</div></div>`).join('')||'<p class="sub">No entries yet.</p>'}</div></section>
  </div></div>`;}
async function done(k,b){if(b){b.innerHTML='&#10003;';b.style.borderColor='var(--success)'}await post('/api/training/done',{key:k});toast('Task marked done','ok');route(true)}
async function posture(){const d=await get('/api/posture');
  const SEV=['critical','high','medium','low','info'],tot={};
  d.latest.forEach(x=>Object.entries(x.counts||{}).forEach(([k,v])=>tot[k]=(tot[k]||0)+v));
  const bar=c=>`<div class="sevbar">${SEV.filter(k=>c[k]).map(k=>`<i class="sev-${k}" style="flex:${c[k]}"></i>`).join('')}</div>`;
  const legend=c=>`<div class="legend">${SEV.filter(k=>c[k]!=null).map(k=>`<span class="sv-${k}">${c[k]} ${k}`+'</span>').join('')}</div>`;
  const mx=Math.max(1,...d.series.map(x=>x.total));
  view.innerHTML=`<div class="head"><h1>Posture</h1><p>Severity over time, coverage and the latest scan per target. Built from local JSON only.</p></div>
  <div class="kpis">
    <section class="panel pad"><p class="label">Scans</p><div class="big"><span data-count="${d.scans}">${d.scans}</span></div><p class="sub" style="margin-top:var(--s4)">${d.latest.length} targets seen</p></section>
    <section class="panel pad"><p class="label">Critical and high</p><div class="big"><span data-count="${(tot.critical||0)+(tot.high||0)}">${(tot.critical||0)+(tot.high||0)}</span></div>${bar(tot)}${legend(tot)}</section>
    <section class="panel pad"><p class="label">Top check</p><div class="title" style="font-weight:600;margin-top:var(--s2)">${esc((d.top[0]||{}).check||'None')}</div><p class="sub" style="margin-top:var(--s2)">${(d.top[0]||{}).count||0} hits</p></section>
  </div>
  <div class="card-grid">${d.latest.map(x=>`<article class="panel pad lift target"><p class="meta">${esc(x.mode)} · ${ago(x.at)}</p><h3 title="${esc(x.target)}">${esc(x.target)}</h3>${bar(x.counts||{})}${legend(x.counts||{})}<p class="meta">${x.checked} checks · ${x.suppressed} suppressed</p></article>`).join('')||'<div class="panel empty">No scan JSON yet. Run a scan.</div>'}</div>
  <div class="eq"><section class="panel pad"><p class="label">New findings by day</p>${d.series.length?`<div class="cols">${d.series.map(x=>`<div class="col" title="${esc(x.day)}: ${x.total} findings, ${x.critical} critical"><div class="stack" style="height:${Math.max(4,x.total/mx*100)}%"><i class="sev-critical" style="flex:${x.critical}"></i><i class="sev-low" style="flex:${Math.max(0,x.total-x.critical)}"></i></div><span>${esc(String(x.day).slice(5))}</span></div>`).join('')}</div>`:'<p class="sub">No history.</p>'}</section>
  <section class="panel pad"><p class="label">Coverage</p><div class="rings">${d.coverage.map(c=>`<figure><div class="ring">${ring(c.value,84,8)}<div class="ctr"><b class="num">${c.value}%</b></div></div><figcaption>${esc(c.label)}</figcaption></figure>`).join('')}</div></section></div>
  <section class="panel" style="margin-top:var(--s4)"><div class="panel-head"><p class="label">Top checks</p></div>${table(d.top,[['Check',r=>esc(r.check)],['Count',r=>`<span class="num">${r.count}</span>`],['Severity',r=>`<span class="status ${esc(r.severity)}">${esc(r.severity)}</span>`]])}</section>`;}
async function scans(){const d=await get('/api/scans'),rep=qp('report','');
  view.innerHTML=`<div class="head"><h1>Scans</h1><p>Passive by default. A URL or local artifact, one report per run.</p></div>
  <form class="cmd" onsubmit="doScan(event)"><span class="meta mono">$ beril scan</span><input name="target" placeholder="https://app.example or ./sample.apk" autocomplete="off" aria-label="Scan target" enterkeyhint="go"><button class="btn primary">Run scan</button></form>
  <div class="split" style="margin-top:var(--s4)"><div><pre id="scanout" class="term hidden"></pre><div id="report"><div class="panel empty">Run a scan or pick a report.</div></div></div>
  <section class="panel"><div class="panel-head"><p class="label">Reports</p><span class="meta">${d.length}</span></div>${d.map(x=>`<a class="report-item" href="#" onclick="openReport('${esc(x.name)}');return false"><span class="title">${esc(x.name)}</span><span class="meta num">${x.size} B</span></a>`).join('')||'<div class="empty">No reports.</div>'}</section></div>`;
  if(rep)openReport(rep)}
async function doScan(e){e.preventDefault();const f=e.target,b=f.querySelector('button'),tg=f.target.value.trim();if(!tg){f.target.focus();return}
  busy=true;b.disabled=true;b.innerHTML='<span class="spin"></span> Scanning';const o=$('#scanout');o.classList.remove('hidden');o.innerHTML='<span class="t-dim">$ beril scan '+esc(tg)+'</span>\n';
  let d={};try{d=await post('/api/scan/run',{target:tg})}catch(x){d={output:String(x)}}
  busy=false;b.disabled=false;b.textContent='Run scan';await typeOut(o,d.output||'');toast(d.report?'Scan finished':'Scan returned no report',d.report?'ok':'bad');if(d.report)openReport(d.report)}
async function openReport(name){if(!$('#report'))return navTo('/scans?report='+encodeURIComponent(name));const d=await get('/api/report?name='+encodeURIComponent(name));
  $('#report').innerHTML=`<section class="panel pad reportview"><p class="label">${esc(name)}</p>${d.html||esc(d.error||'')}</section>`;$('#report').scrollIntoView({behavior:reduce?'auto':'smooth',block:'nearest'})}
async function sources(){const d=await get('/api/sources');shell('Sources','Harvested rows by source. One row is a gap.',table(d.map(x=>({name:x[0],n:x[1]})),[['Source',r=>esc(r.name)],['Rows',r=>`<span class="num">${r.n}</span>`]]),`<section class="panel pad"><p class="label">Coverage</p><p class="sub">${d.length} sources seen. Add a source in references/forums.md.</p></section>`);}
async function route(silent){
  if(!silent){closeDrawer();view.classList.remove('enter');view.innerHTML=SKEL}
  const fn={overview,activity,jobs,costs,memory,threads,experts,tools,methods,atlas,labs,training,posture,scans,sources}[page];if(!fn)return;
  await fn();if(!silent)stagger();$('#upd').textContent=new Date().toLocaleTimeString([], {hour:'2-digit',minute:'2-digit',second:'2-digit'})}
const LIVE=new Set(['overview','jobs','activity','costs','labs']);
setInterval(()=>{if(document.hidden||busy||!LIVE.has(page)||drawer.classList.contains('open'))return;const a=document.activeElement;if(a&&view.contains(a)&&/INPUT|TEXTAREA|SELECT/.test(a.tagName))return;route(true)},6000);
addEventListener('popstate',()=>nav(pageFromPath(location.pathname)));
if(location.hash.length>1)history.replaceState(null,'','/'+location.hash.slice(1));
nav(pageFromPath(location.pathname));
</script></body></html>"""
