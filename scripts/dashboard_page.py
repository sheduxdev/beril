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
:root{color-scheme:dark;
  --background-primary:#080807;--background-secondary:#10100f;--background-card:#111110;--background-hover:#191917;
  --text-primary:#efefeb;--text-secondary:#9d9d97;--text-tertiary:#75756f;
  --border-primary:#252522;--border-secondary:#363631;--paper:#f4f4ef;
  --accent:#d8ff5c;--accent-solid:#d8ff5c;--success:#9ee39a;--warning:#e6bd78;--danger:#ff9a94;--medium:#e6cf6e;
  --accent-container:rgba(216,255,92,.16);--layer-hover:color-mix(in srgb,var(--text-primary) 7%,transparent);--layer-press:color-mix(in srgb,var(--text-primary) 11%,transparent);--glass:#080807;--glass-bar:#080807;--seg-on:#4a4a44;--scrim:rgb(8 8 7/.64);
  --av:url("(image attached below)");
  --bg:var(--background-primary);--surface:var(--background-card);--surface-2:var(--background-hover);
  --ink:var(--text-primary);--muted:var(--text-secondary);--faint:var(--text-tertiary);
  --line:var(--border-primary);--line-2:var(--border-secondary);--ok:var(--success);--warn:var(--warning);--bad:var(--danger);
  --font-body:"Noto Sans","Segoe UI",system-ui,sans-serif;
  --font-display:"Liberation Serif","DejaVu Serif",serif;
  --font-mono:"DejaVu Sans Mono","Liberation Mono",monospace;
  --s1:4px;--s2:8px;--s3:12px;--s4:16px;--s5:24px;--s6:32px;--s7:48px;--s8:64px;--s9:96px;
  --r1:8px;--r2:12px;--r3:16px;--max:1240px;
  --shadow-s:0 1px 3px rgb(0 0 0/.4);--shadow-m:0 4px 6px rgb(0 0 0/.4),0 2px 4px rgb(0 0 0/.5);--shadow-l:0 20px 25px rgb(0 0 0/.4),0 8px 10px rgb(0 0 0/.5);
  --dur:150ms;--ease:cubic-bezier(.25,.1,.25,1);
}
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
.side{border-right:1px solid var(--line);padding:var(--s5) var(--s3);background:var(--glass);display:flex;flex-direction:column;gap:var(--s5)}
.brand{display:grid;grid-template-columns:32px auto;column-gap:8px;align-items:center;font:600 15px/1.2 var(--font-body);padding:0 var(--s3);letter-spacing:-.01em}
.brand b{font-weight:600}
.av{grid-row:span 2;width:32px;height:32px;border-radius:50%;corner-shape:round;background:var(--av) center/cover;box-shadow:0 0 0 1px var(--line)}
.brand small{font:400 11px var(--font-body);color:var(--faint);margin:0;letter-spacing:0}
.nav{display:grid;gap:2px}
.nav a{display:flex;justify-content:space-between;align-items:center;min-height:28px;padding:8px var(--s4);border-radius:99px;color:var(--muted);font-size:13px;transition:background var(--dur) var(--ease),color var(--dur) var(--ease)}
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
.btn{display:inline-flex;align-items:center;gap:var(--s2);min-height:28px;border:1px solid transparent;background:var(--surface-2);border-radius:99px;padding:4px 16px;font-size:13px;cursor:pointer;transition:background var(--dur) var(--ease),transform var(--dur) var(--ease)}
.btn:hover{background:var(--line-2)}
.btn.primary{background:var(--accent-solid);color:var(--bg);font-weight:600}
.btn.primary:hover{background:var(--paper)}
.btn.icon{padding:4px 8px}.btn.icon svg{display:block}
.btn:disabled{background:var(--surface-2);color:var(--muted);cursor:wait}
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
.seg .chip{border:0;border-radius:6px;min-height:24px;padding:4px 16px;background:transparent}
.seg .chip.on{background:var(--seg-on);color:var(--ink);box-shadow:var(--shadow-s)}
.empty{padding:var(--s6) var(--s4);color:var(--muted);font-size:13px}
.mono{font-family:var(--font-mono)}
.hidden{display:none}
.form{display:grid;grid-template-columns:1fr 1fr;gap:var(--s3);padding:var(--s4)}
.form label{display:grid;gap:var(--s1);font-size:12px;color:var(--muted)}
.form input,.form select,.form textarea{min-width:0;width:100%;background:var(--bg);border:1px solid var(--line);border-radius:var(--r1);padding:8px var(--s3);font-size:13px}
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
.live{display:inline-flex;align-items:center;gap:8px;font:400 12px var(--font-mono);color:var(--faint);margin-right:var(--s2)}
.live i{width:6px;height:6px;border-radius:50%;background:var(--success);--pulse:color-mix(in srgb,var(--success) 55%,transparent);animation:pulse 2s infinite}
.spin{display:inline-block;width:12px;height:12px;border:2px solid currentColor;border-right-color:transparent;border-radius:50%;animation:spin .7s linear infinite}
.toasts{position:fixed;right:var(--s4);bottom:max(var(--s4),env(safe-area-inset-bottom));display:grid;gap:var(--s2);z-index:40;width:340px;max-width:calc(100% - 32px)}
.toast{position:relative;overflow:hidden;display:flex;gap:var(--s3);align-items:center;background:var(--background-secondary);box-shadow:0 0 0 1px var(--line-2),var(--shadow-m);border-radius:var(--r2);padding:var(--s3) var(--s4);font-size:13px;animation:toast-in 220ms var(--ease)}
.toast::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--dot,var(--accent));flex:none}
.toast.ok{--dot:var(--success)}.toast.bad{--dot:var(--danger)}
.toast::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--dot,var(--accent));transform-origin:left;animation:toast-life 4s linear forwards}
.lift{transition:transform var(--dur) var(--ease),box-shadow var(--dur) var(--ease)}
.lift:hover{transform:translateY(-2px);box-shadow:0 0 0 1px var(--line-2),var(--shadow-m)}
.lab-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(280px,100%),1fr));gap:var(--s4)}
.lab{display:flex;flex-direction:column;gap:var(--s3);padding:var(--s4)}
.target h2{font:600 13px/1.3 var(--font-body);margin:0}
.lab h2{font:600 13px/1.3 var(--font-body);margin:0;text-wrap:balance}
.lab header{display:flex;gap:var(--s3);align-items:center}
.target h2{font:600 13px/1.3 var(--font-body);margin:0}
.lab h2{font:600 13px/1.3 var(--font-body);margin:0;text-wrap:balance}
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
.legend span{display:inline-flex;align-items:center;gap:8px}
.legend span::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--faint)}
.legend .ok::before{background:var(--success)}.legend .bad::before,.legend .sv-critical::before{background:var(--danger)}
.legend .sv-high::before{background:var(--warning)}.legend .sv-medium::before{background:var(--medium)}.legend .sv-low::before{background:var(--accent)}
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
.task{display:flex;gap:var(--s3);align-items:center;padding:12px var(--s4);border-bottom:1px solid var(--line)}
.task:last-child{border-bottom:0}
.check{flex:none;width:22px;height:22px;border-radius:50%;border:1.5px solid var(--line-2);background:transparent;cursor:pointer;padding:0;color:var(--success);display:grid;place-items:center;transition:background var(--dur) var(--ease),border-color var(--dur) var(--ease)}
.check:hover{border-color:var(--success);background:color-mix(in srgb,var(--success) 18%,transparent)}
.journal{position:relative;padding-left:var(--s5)}
.journal::before{content:"";position:absolute;left:4px;top:8px;bottom:8px;width:1px;background:var(--line)}
.j{position:relative;padding:var(--s2) 0}
.j::before{content:"";position:absolute;left:-24px;top:14px;width:9px;height:9px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px var(--surface)}
.sevbar{display:flex;gap:2px;height:6px;border-radius:99px;overflow:hidden;background:var(--surface-2);margin:var(--s3) 0}
.sevbar i{display:block;height:100%}
.sev-critical{background:var(--danger)}.sev-high{background:var(--warning)}.sev-medium{background:var(--medium)}.sev-low{background:var(--accent)}.sev-info{background:var(--faint)}
.target{display:flex;flex-direction:column;gap:var(--s1);min-width:0}
.target h3{margin:0;font:600 14px/1.3 var(--font-body);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cols{display:flex;align-items:flex-end;gap:8px;height:130px}
.col{flex:1;min-width:8px;max-width:64px;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:stretch;font-size:10px;color:var(--faint);text-align:center;gap:4px}
.stack{display:flex;flex-direction:column-reverse;border-radius:4px;overflow:hidden;transform-origin:bottom;min-height:3px}
.stack i{display:block}
.eq{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s4);margin-top:var(--s4)}
.rings{display:flex;gap:var(--s5);flex-wrap:wrap}.rings figure{margin:0;text-align:center;font-size:12px;color:var(--muted);max-width:120px}
.cmd{display:flex;align-items:center;gap:var(--s3);background:var(--surface);box-shadow:0 0 0 1px var(--line);border-radius:99px;padding:var(--s2) var(--s2) var(--s2) var(--s4);transition:box-shadow var(--dur) var(--ease)}
.cmd:focus-within{box-shadow:0 0 0 2px var(--accent)}
.cmd input{flex:1;min-width:0;border:0;outline:0;background:transparent;font:13px var(--font-mono);padding:8px 0}
.report-item{display:flex;justify-content:space-between;gap:var(--s3);padding:12px var(--s4);border-bottom:1px solid var(--line);font-size:13px}
.report-item:last-child{border-bottom:0}.report-item:hover{background:var(--layer-hover)}
.reportview{overflow-x:auto}.reportview table{font-size:12px}
.spark{display:block;margin:var(--s3) 0 0}
@container (max-width:900px){.train,.eq{grid-template-columns:minmax(0,1fr)}.sk-grid{grid-template-columns:minmax(0,1fr)}.ledger,.split{grid-template-columns:minmax(0,1fr)}.stats{grid-template-columns:repeat(2,1fr)}.stat:nth-child(2){border-right:0}}
@container (max-width:700px){.kpis{grid-template-columns:minmax(0,1fr)}.head h1{font-size:22px}}
@container (max-width:640px){
  .tbl thead{display:none}.tbl table,.tbl tbody,.tbl tr,.tbl td{display:block}
  .tbl tbody tr{padding:var(--s3) 0;border-bottom:1px solid var(--line)}.tbl tbody tr:last-child{border-bottom:0}
  .tbl td{display:flex;justify-content:space-between;gap:var(--s3);padding:4px var(--s4);border:0;text-align:right}
  .tbl td::before{content:attr(data-label);color:var(--faint);font-size:12px;text-align:left}
  .tbl td:first-child{display:block;text-align:left;font-weight:500}.tbl td:first-child::before{display:none}
  .timeline .event{grid-template-columns:64px minmax(0,1fr) auto}.timeline .event .status{display:none}
  .mem{grid-template-columns:minmax(0,1fr) 92px}.mem .tags,.mem .pill{display:none}
}
@media (max-width:800px){.shell{grid-template-columns:1fr}.side{position:static;height:auto;flex-direction:row;align-items:center;overflow-x:auto;padding:var(--s3) max(var(--s3),env(safe-area-inset-left))}.nav{display:flex}.brand small{display:none}.content,.top{padding-left:var(--s4);padding-right:var(--s4)}.field,#sideBtn,.top h2,#palBtn .kbd,.live{display:none}.top{gap:8px}.form{grid-template-columns:1fr}}
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
  return `<article class="panel lab lift ${s}" id="lab-${esc(l)}" style="--h:${h}"><header><span class="lab-mark">${esc(l.slice(0,2).toUpperCase())}</span><div><h2>${esc(l)}</h2><p class="meta">${r.at?'Ran '+ago(r.at):'Not run yet'}</p></div><span class="status ${s==='pass'?'done':s==='fail'?'failed':''}">${s==='pass'?'Pass':s==='fail'?'Fail':'Idle'}</span></header><div class="lab-bar"><i></i></div>
  <div class="legend">${p||f?`<span class="ok">${p} passed</span>${f?`<span class="bad">${f} failed</span>`:''}`:'<span>No checks recorded</span>'}</div>
  ${o?`<details ${openLabs.has(l)?'open':''} ontoggle="this.open?openLabs.add('${esc(l)}'):openLabs.delete('${esc(l)}')"><summary>Output</summary><pre class="term">${term(o)}</pre></details>`:''}
  <footer><button class="btn" onclick="runLab('${esc(l)}',this)">Run test</button></footer></article>`}
async function labs(){const d=await get('/api/labs'),R=d.runs||{};window.LD=d;
  const st=l=>{const r=R[l]||{};return r.ok?'pass':r.ok===false?'fail':'idle'},n=d.labs.length;
  const pass=d.labs.filter(l=>st(l)==='pass').length,fail=d.labs.filter(l=>st(l)==='fail').length,idle=n-pass-fail;
  view.innerHTML=`<div class="head"><h1>Labs</h1><p>${n} labs. Each run executes the smoke test and stores the tail.</p></div><h2 class="label">Available labs</h2>
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
  <div class="card-grid">${d.latest.map(x=>`<article class="panel pad lift target"><p class="meta">${esc(x.mode)} · ${ago(x.at)}</p><h2 title="${esc(x.target)}">${esc(x.target)}</h2>${bar(x.counts||{})}${legend(x.counts||{})}<p class="meta">${x.checked} checks · ${x.suppressed} suppressed</p></article>`).join('')||'<div class="panel empty">No scan JSON yet. Run a scan.</div>'}</div>
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
