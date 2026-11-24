s=open('scene3.html').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:60],s.count(a)); s=s.replace(a,b)
# ---------- renames (descending)
for o,n in ((6,12),(5,11),(4,9),(3,4),(2,3)):
    rep(f'<div class=scene id=s{o}>',f'<div class=scene id=s{n}>')
for o,n in ((6,12),(5,11),(4,9),(3,4),(2,3)):
    rep(f' if(i=={o}){{',f' if(i=={n}){{')
rep("const SC=['s0','s1','s2','s3','s4','s5','s6'];","const SC=['s0','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12'];")
rep('const n=7;','const n=13;'); rep('(i<6?S[i+1]:TOTAL+1)','(i<12?S[i+1]:TOTAL+1)')
# ---------- stats row: 4 cards
rep("[['65',{tr:'test',en:'tests'}],['10',{tr:'pratik lab',en:'labs'}],['25',{tr:'haftalık plan',en:'week plan'}]]","[['37',{tr:'komut',en:'commands'}],['189',{tr:'test',en:'tests'}],['10',{tr:'lab',en:'labs'}],['25',{tr:'hafta',en:'weeks'}]]")
rep("[0,1,2].forEach(k=>{const a=ez((u-3.0-k*.3)/.4);$('ch'+k)","[0,1,2].forEach(k=>{const a=ez((u-2.6-k*.25)/.4);$('ch'+k)")
rep("const a2=ez((u-3.9-k*.3)/.4);$('st'+k).style.opacity=a2;$('st'+k).style.transform=`translateY(${(1-a2)*24}px)`;\n   $('sn'+k).textContent=Math.round([65,10,25][k]*ez((u-4-k*.3)/1.1));});",
    "});[0,1,2,3].forEach(k=>{const a2=ez((u-3.4-k*.25)/.4);$('st'+k).style.opacity=a2;$('st'+k).style.transform=`translateY(${(1-a2)*24}px)`;$('sn'+k).textContent=Math.round([37,189,10,25][k]*ez((u-3.5-k*.25)/1.1));});")
rep("'35 paths'","'34 paths'")
# ---------- gates real numbers
rep("rows:['sahiplik kaydı','kapsam dosyası','istek bütçesi + hız sınırı','sırlar maskeli','telemetri'],on:['AÇIK','AÇIK','AÇIK','AÇIK','KAPALI']",
    "rows:['sahiplik kaydı · 30 gün','kapsam dosyası','2 istek/sn · en çok 250','robots.txt uyumu','sırlar maskeli','telemetri'],on:['AÇIK','AÇIK','AÇIK','AÇIK','AÇIK','KAPALI']")
rep("rows:['ownership record','scope file','request budget + rate limit','secrets masked','telemetry'],on:['ON','ON','ON','ON','OFF']",
    "rows:['ownership record · 30 days','scope file','2 req/s · 250 max','robots.txt respected','secrets masked','telemetry'],on:['ON','ON','ON','ON','ON','OFF']")
rep("const step=(d-2.6)/5;","const step=(d-2.6)/T.rows.length;")
# ---------- text additions
TR="""ch:['AÇILIŞ','BERİL','37 KOMUT','PASİF TARAMA','SIZMA DENEMESİ','İKİLİ ANALİZ','SIRLAR VE BAĞIMLILIK','YAPAY ZEKÂ ÇAĞI','İSTİHBARAT','RAPOR','LAB VE EĞİTİM','KAPILAR','BAŞLA'],bub:['merhaba ♡','ben Beril ♡','hepsi burada ✦','sessizce bakıyorum','şimdi deniyorum','çalıştırmadan okurum','anahtarlar maskeli ♡','yeni tehditler de var','hepsi kaynaklı ✦','çözümü de yazarım','birlikte öğrenelim ♡','iznin yoksa dokunmam','hep yanındayım ♡'],
 cmdt:'komut,<br>tek çatı altında',ex:'örnek çıktı',stat:'çalıştırılmaz · statik inceleme',opt:'isteğe bağlı',secT:'GİZLİ ANAHTAR',steps:['iptal et','yenile','geçmişi temizle'],depT:'BAĞIMLILIK',aiT:'MCP AYARI',aiF:['sabitlenmemiş paket','düz metin anahtar','docker.sock bağlı'],vibeT:'YAPAY ZEKÂYLA YAZILAN UYGULAMA',nosrv:'sunucu başlatılmaz',
 intelL:['konu','uzman','araç','yöntem','depo','kaynak'],camo:'403 ya da boş JS sayfası → metin ✓',rdesc:['mühendis: teknik ayrıntı + çözüm','bug bounty: kanıt + etki','KOBİ: tek sayfa, trafik ışığı','bakımcı: yeniden üretim','CRA: AB uyum notu','JSON: makine çıktısı','SARIF: IDE ve CI'],
 labsT:'10 LAB',weeksT:'25 HAFTA',ph:['kurulum','temel','keşif+web','kod+binary','sömürü+altyapı','uzman','ustalık'],"""
EN="""ch:['COLD OPEN','BERIL','37 COMMANDS','PASSIVE SCAN','BREAK-IN ATTEMPT','BINARY ANALYSIS','SECRETS & DEPS','AI ERA','INTELLIGENCE','REPORT','LABS & TRAINING','GATES','START'],bub:['hello ♡','i\\'m Beril ♡','all in here ✦','looking quietly','now i try','i read, never run','keys stay masked ♡','new threats too','every one sourced ✦','i write the fix too','let\\'s learn together ♡','no permission, no touch','always beside you ♡'],
 cmdt:'commands,<br>one roof',ex:'sample output',stat:'never executed · static review',opt:'optional',secT:'SECRET',steps:['revoke','rotate','clean history'],depT:'DEPENDENCIES',aiT:'MCP CONFIG',aiF:['unpinned package','plaintext key','docker.sock mounted'],vibeT:'AI-WRITTEN APP',nosrv:'server is never started',
 intelL:['threads','experts','tools','methods','repos','sources'],camo:'403 or empty JS shell → text ✓',rdesc:['engineer: technical detail + fix','bug bounty: proof + impact','SMB: one page, traffic light','maintainer: reproduction','CRA: EU compliance note','JSON: machine output','SARIF: IDE and CI'],
 labsT:'10 LABS',weeksT:'25 WEEKS',ph:['setup','basics','recon+web','code+binary','exploit+infra','expert','mastery'],"""
rep("lead:'ipucu',clean:'temiz',",TR+"lead:'ipucu',clean:'temiz',")
rep("lead:'lead',clean:'clean',",EN+"lead:'lead',clean:'clean',")
# ---------- new global elements
rep('<div id=root></div>','''<div id=chap class=mono></div><div id=mas><div id=av></div><div id=bb class=mono></div></div>
<div id=root></div>''')
rep('#vig{','''#chap{position:absolute;top:148px;left:56px;font-size:27px;letter-spacing:.14em;color:var(--pk)}
#mas{position:absolute;left:56px;top:1390px;display:flex;align-items:center;gap:20px;opacity:0}
#av{width:112px;height:112px;border-radius:50%;border:3px solid var(--g);background:url(hero.png) -150px -28px/520px auto;box-shadow:0 0 30px rgba(127,227,164,.35)}
#bb{background:rgba(255,183,213,.95);color:#2a0f1b;font-size:29px;font-weight:700;padding:14px 24px;border-radius:24px 24px 24px 6px;white-space:nowrap}
.gl{background:linear-gradient(160deg,rgba(22,40,30,.88),rgba(9,17,12,.92))}
#vig{''')
# ---------- new scenes html
CM=["scan","verify","secrets","mcp","jar","vibe","deps","sbom","guard","priority","run","ingest","watch","infra","image","netcheck","bgp","health","benchmark","hunt","triage","re","harvest","extract","dossier","feeds","github","current","incidents","evidence","validate","train","labs","reflect","report","dashboard","job"]
assert len(CM)==37
NEW2='''<div class=scene id=s2>
 <div style="display:flex;align-items:center;gap:26px"><div id=cn class='mono g' style="font-size:190px;line-height:1;font-weight:800">0</div><div style="font-size:56px;font-weight:800;line-height:1.1">${T.cmdt}</div></div>
 <div style="display:flex;flex-wrap:wrap;gap:11px;margin-top:30px">${CM.map((c,k)=>`<span id=cm${k} class='chip mono' style="font-size:26px;padding:9px 16px">${c}</span>`).join('')}</div>
 <div class=win style="margin-top:26px"><div class='bar mono'>${dots}&nbsp;beril</div><div class='term mono' id=t_pal style="font-size:29px;height:96px;line-height:1.5"></div></div>
</div>
<div class=scene id=s5>
 <div style="display:flex;gap:10px;margin-bottom:20px">${['APK','IPA','EXE','ELF','JAR'].map((x,k)=>`<div class='chip mono' id=ft${k} style="flex:1;text-align:center;font-size:30px;padding:12px 4px">${x}</div>`).join('')}</div>
 ${[['ELF',['PIE','NX','RELRO','canary'],['✓','✓','▲ partial','✗']],['APK',['debuggable','exported','cleartext','backup'],['▲ true','▲ 3','▲ true','✓ false']]].map((c,i)=>`<div class='card gl' id=rc${i} style="margin-bottom:18px;padding:24px 30px"><div style="display:flex;justify-content:space-between"><b class='mono g' style="font-size:34px">${c[0]}</b><span class='mono dim' style="font-size:22px">${T.ex}</span></div>${c[1].map((r,k)=>`<div class=mono id=rr${i}${k} style="display:flex;justify-content:space-between;font-size:30px;line-height:1.7"><span>${r}</span><span id=rv${i}${k}></span></div>`).join('')}</div>`).join('')}
 <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:6px;align-items:center"><span class='mono dim' style="font-size:24px">${T.opt}:</span>${['capa','FLOSS','rizin','YARA','Ghidra'].map((x,k)=>`<span id=tl${k} class='chip mono' style="font-size:26px;padding:9px 16px">${x}</span>`).join('')}</div>
 <div id=stt class='chip mono' style="margin-top:20px;font-size:27px;color:var(--cy);border-color:#1d4a55">🔒 ${T.stat}</div>
</div>
<div class=scene id=s6>
 <div class='card gl' style="padding:26px 30px;margin-bottom:18px" id=sa><div style="display:flex;justify-content:space-between"><b class='mono pk' style="font-size:30px;letter-spacing:.12em">${T.secT}</b><span class='mono dim' style="font-size:22px">git history</span></div>
  <div class='mono' style="font-size:28px;line-height:1.7;margin:10px 0 14px;white-space:pre"><span class=dim>3f2a91c</span> <span class=g>+</span>AWS_ACCESS_KEY_ID=<span id=mk class=pk></span>\\n<span class=dim>b71d0e4</span> <span class=g>+</span>token=<span class=pk>ghp_••••••••••••9xQ2</span></div>
  <div style="display:flex;gap:10px;align-items:center">${T.steps.map((x,k)=>`<div id=sp${k} class='chip mono' style="flex:1;text-align:center;font-size:26px;padding:12px 4px">${k+1} · ${x}</div>`).join('')}</div></div>
 <div class='card gl' style="padding:26px 30px;margin-bottom:18px" id=sb><div style="display:flex;justify-content:space-between"><b class='mono w' style="font-size:30px;letter-spacing:.12em">${T.depT}</b><span class='mono dim' style="font-size:22px">${T.ex}</span></div>
  ${[['lib-a 1.2.0','KEV',.94,'reachable'],['lib-b 4.0.1','',.31,'not-found'],['lib-c 0.9.3','KEV',.62,'unknown']].map((r,k)=>`<div id=dr${k} class=mono style="display:flex;align-items:center;gap:14px;font-size:26px;margin-top:14px"><span style="width:230px">${r[0]}</span><span style="width:70px;color:${r[1]?'#ff6b8b':'#7a9886'}">${r[1]||'–'}</span><span style="flex:1;height:12px;border-radius:6px;background:#10211a"><i id=eb${k} style="display:block;height:12px;border-radius:6px;background:linear-gradient(90deg,#7fe3a4,#ffb7d5);width:0"></i></span><span class=dim style="width:150px;text-align:right;font-size:22px">${r[3]}</span></div>`).join('')}</div>
 <div style="display:flex;gap:10px;flex-wrap:wrap">${['CycloneDX 1.5','SPDX 2.3','OpenVEX 0.2'].map((x,k)=>`<span id=sx${k} class='chip mono cy' style="font-size:26px;border-color:#1d4a55">${x}</span>`).join('')}</div>
</div>
<div class=scene id=s7>
 <div class='card gl' style="padding:24px 30px;margin-bottom:18px"><div class='mono cy' style="font-size:28px;letter-spacing:.12em;margin-bottom:8px">${T.aiT}</div>
  <div class=mono style="font-size:27px;line-height:1.75;white-space:pre"><span class=dim>"command":</span> "npx"<span id=ai0 class=pk></span>\\n<span class=dim>"args":</span> ["-y", "some-mcp-server"]\\n<span class=dim>"env":</span> {"API_KEY": "sk-••••"}<span id=ai1 class=pk></span>\\n<span class=dim>"volumes":</span> ["/var/run/docker.sock"]<span id=ai2 class=pk></span></div></div>
 <div class='card gl' style="padding:24px 30px;margin-bottom:18px"><div class='mono pk' style="font-size:28px;letter-spacing:.1em;margin-bottom:14px">${T.vibeT}</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px">${['rls-missing','public-bucket','service-role-client','public-secret','vite-secret','dangerous-html','cors-star-credentials','firebase-open','route-no-auth'].map((x,k)=>`<span id=vb${k} class='chip mono' style="font-size:25px;padding:9px 14px">${x}</span>`).join('')}</div></div>
 <div id=nsv class='chip mono' style="font-size:27px;color:var(--cy);border-color:#1d4a55">🔒 ${T.nosrv}</div>
</div>
<div class=scene id=s8>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">${[[556,0],[94,1],[88,2],[191,3],[2064,4],[20,5]].map((x,k)=>`<div class='card gl' id=ic${k} style="padding:22px 26px"><div class='mono g' id=in${k} style="font-size:84px;line-height:1.05;font-weight:800">0</div><div class='mono dim' style="font-size:26px">${T.intelL[k]}</div></div>`).join('')}</div>
 <div style="overflow:hidden;white-space:nowrap;margin:24px 0 16px;border-top:2px solid var(--ln);border-bottom:2px solid var(--ln);padding:14px 0"><div id=tick class=mono style="display:inline-block;font-size:30px;color:var(--cy)"></div></div>
 <div id=cam class='chip mono' style="font-size:27px;color:var(--warn);border-color:#5a4a1d">🦊 Camoufox · ${T.camo}</div>
</div>
<div class=scene id=s10>
 <div class='mono g' style="font-size:30px;letter-spacing:.14em;margin-bottom:14px">${T.labsT}</div>
 <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px">${['web','binary','fuzz','re','mobile','firmware','cloud','ad','llm','detection'].map((x,k)=>`<div id=lb${k} class='card gl mono' style="padding:20px 6px;text-align:center;font-size:25px;border-radius:20px">${x}</div>`).join('')}</div>
 <div class='mono pk' style="font-size:30px;letter-spacing:.14em;margin:34px 0 14px">${T.weeksT}</div>
 <div style="position:relative"><div style="display:flex;gap:6px">${[[1,0],[4,1],[5,2],[5,3],[5,4],[4,5],[1,6]].map((p,k)=>`<div id=ph${k} style="flex:${p[0]};height:34px;border-radius:10px;background:#16241c;border:2px solid var(--ln)"></div>`).join('')}</div>
  <div id=head style="position:absolute;top:-10px;left:0;width:6px;height:54px;background:var(--pk);border-radius:3px;box-shadow:0 0 18px var(--pk)"></div></div>
 <div style="display:flex;gap:6px;margin-top:10px">${[[1,0],[4,1],[5,2],[5,3],[5,4],[4,5],[1,6]].map((p,k)=>`<div id=pt${k} class='mono dim' style="flex:${p[0]};font-size:19px;text-align:center;overflow:hidden">${p[0]>=4?T.ph[k]:''}</div>`).join('')}</div>
 <div id=wk class='mono g' style="font-size:60px;margin-top:26px;font-weight:800"></div>
</div>
'''
rep("<div class=scene id=s4>\n <div style=\"display:flex;justify-content:space-between;align-items:center;margin-bottom:20px\">","<div class=scene id=s4>\n <div style=\"display:flex;justify-content:space-between;align-items:center;margin-bottom:20px\">")
# insert NEW2 (s2,s5,s6,s7,s8,s10) before the first scene html of old s3 (radar, now id=s3)
rep('<div class=scene id=s3>\n <div style="display:flex;gap:22px;align-items:stretch">',NEW2+'<div class=scene id=s3>\n <div style="display:flex;gap:22px;align-items:stretch">')
rep('const dots=','const CM='+str(CM)+';\nconst dots=')
# ---------- report tabs
rep("<div class=win><div class='bar mono'>${dots}&nbsp;${T.rep}.md","<div style=\"display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px\">${['engineer','bugbounty','smb','maintainer','cra','json','sarif'].map((x,k)=>`<span id=rt${k} class='chip mono' style=\"font-size:24px;padding:8px 14px\">${x}</span>`).join('')}</div><div id=rtd class='mono g' style=\"font-size:28px;margin-bottom:14px;min-height:40px\"></div>\n <div class=win><div class='bar mono'>${dots}&nbsp;${T.rep}.md")
# ---------- new updaters
NEWJS='''
 if(i==2){
  $('cn').textContent=Math.round(37*ez(u/1.2));
  const G={scan:0,verify:0,secrets:0,mcp:0,jar:0,vibe:0,deps:0,sbom:0,guard:0,priority:0,run:0,ingest:0,watch:0,infra:0,image:0,netcheck:0,bgp:0,health:0,benchmark:0,hunt:1,triage:1,re:1,harvest:2,extract:2,dossier:2,feeds:2,github:2,current:2,incidents:2,evidence:2,validate:2,train:3,labs:3,reflect:3,report:4,dashboard:4,job:4};
  const COL=['#7fe3a4','#ffb7d5','#8fe8ff','#ffd27a','#eaf5ee'];
  CM.forEach((c,k)=>{const t0=.8+k*(d*.58/37);const a=ez((u-t0)/.3),e=$('cm'+k);e.style.opacity=a;const hot=u>t0&&u<t0+.35;e.style.color=hot?'#ffb7d5':COL[G[c]];e.style.borderColor=hot?'#ffb7d5':COL[G[c]]+'55';e.style.transform=`scale(${.85+.15*a})`});
  const cs=['./beril scan --target https://your-app.example','./beril hunt --target ./repo --sandbox','./beril re --target ./sample --capa --floss','./beril report --profile smb'];
  const k=Math.min(3,Math.floor(u/(d/4)));const ty=typed(cs[k],u-k*(d/4),.2,38);
  $('t_pal').innerHTML='<span class=g>$</span> '+ESC(ty)+'<span class=cur></span>';
 }
 if(i==5){
  const act=Math.min(4,Math.floor(u/(d/5)));
  for(let k=0;k<5;k++){const e=$('ft'+k);const on=(k==3&&u<d*.5)||(k==0&&u>=d*.5)||k==act&&false;e.style.borderColor=on?'#ffb7d5':'#1c3a2a';e.style.color=on?'#ffb7d5':'#eaf5ee';e.style.opacity=ez((u-.1-k*.08)/.3)}
  [0,1].forEach(c=>{const t0=.5+c*d*.3,a=ez((u-t0)/.5);const e=$('rc'+c);e.style.opacity=a;e.style.transform=`translateY(${(1-a)*40}px)`;
   const R=[['✓','✓','▲ partial','✗'],['▲ true','▲ 3','▲ true','✓ false']][c];
   for(let r=0;r<4;r++){const tr=t0+.5+r*.35;const on=u>tr;$('rv'+c+r).textContent=on?R[r]:'…';$('rv'+c+r).style.color=!on?'#7a9886':(R[r].startsWith('✓')?'#7fe3a4':(R[r].startsWith('✗')||R[r].startsWith('▲ t')?'#ffb7d5':'#ffd27a'))}});
  for(let k=0;k<5;k++){const t0=d*.62+k*.22;const a=ez((u-t0)/.3);const e=$('tl'+k);e.style.opacity=a;e.style.color=u>t0&&u<t0+.4?'#ffb7d5':'#eaf5ee'}
  $('stt').style.opacity=ez((u-d*.82)/.4);
 }
 if(i==6){
  const a=ez((u-.2)/.4);$('sa').style.opacity=a;$('sa').style.transform=`translateY(${(1-a)*40}px)`;
  const m='AKIA••••••••MNOP';$('mk').textContent=m.slice(0,Math.floor(cl((u-.9)*20,0,m.length)));
  const act=u<d*.3?-1:u<d*.38?0:u<d*.46?1:2;
  for(let k=0;k<3;k++){const e=$('sp'+k);const on=u>d*(.3+k*.08);e.style.borderColor=on?'#7fe3a4':'#1c3a2a';e.style.color=on?'#7fe3a4':'#7a9886'}
  const b=ez((u-d*.36)/.5);$('sb').style.opacity=b;$('sb').style.transform=`translateY(${(1-b)*40}px)`;
  [.94,.31,.62].forEach((v,k)=>{$('eb'+k).style.width=(100*v*ez((u-d*.42-k*.2)/.8))+'%';$('dr'+k).style.opacity=ez((u-d*.4-k*.2)/.3)});
  for(let k=0;k<3;k++)$('sx'+k).style.opacity=ez((u-d*.7-k*.2)/.3);
 }
 if(i==7){
  $('ai0').textContent=u>d*.2?'  ▲ '+T.aiF[0]:'';$('ai1').textContent=u>d*.3?'  ▲ '+T.aiF[1]:'';$('ai2').textContent=u>d*.4?'  ▲ '+T.aiF[2]:'';
  const hot=[0,2,3,5,7];
  for(let k=0;k<9;k++){const e=$('vb'+k);const t0=d*.45+k*.07*d*.6/ (9*.07);const a=ez((u-(d*.45+k*.1))/.3);const flag=[0,2,3].includes(k);e.style.opacity=.25+.75*a;e.style.borderColor=a>.6&&flag?'#ffb7d5':'#1c3a2a';e.style.color=a>.6&&flag?'#ffb7d5':'#eaf5ee';e.style.boxShadow=a>.6&&flag?'0 0 16px rgba(255,183,213,.45)':'none'}
  $('nsv').style.opacity=ez((u-d*.82)/.4);
 }
 if(i==8){
  [556,94,88,191,2064,20].forEach((v,k)=>{const a=ez((u-.3-k*.25)/1.1);$('in'+k).textContent=Math.round(v*a).toLocaleString('en-US');const e=$('ic'+k);const o=ez((u-.2-k*.25)/.4);e.style.opacity=o;e.style.transform=`translateY(${(1-o)*30}px)`});
  const SRC='HackerOne · Hacker News · PortSwigger · HTB · 0x00sec · Intigriti · Trail of Bits · Lobsters · infosec.exchange · Reddit · ';
  $('tick').textContent=SRC+SRC;$('tick').style.transform=`translateX(${-(u*180)%(SRC.length*17.5)}px)`;
  $('cam').style.opacity=ez((u-d*.7)/.4);
 }
 if(i==10){
  for(let k=0;k<10;k++){const t0=.4+k*(d*.4/10);const a=ez((u-t0)/.3);const e=$('lb'+k);e.style.opacity=a;e.style.transform=`scale(${.8+.2*a})`;const hot=u>t0&&u<t0+.4;e.style.borderColor=hot?'#ffb7d5':'#1c3a2a';e.style.color=hot?'#ffb7d5':'#eaf5ee'}
  const p=cl((u-d*.45)/(d*.5));const W=968;$('head').style.left=(p*W-3)+'px';const wk=Math.round(p*25);
  $('wk').textContent=u>d*.45?(LANG=='tr'?'hafta ':'week ')+wk+' / 25':'';
  [[1,0],[4,1],[5,2],[5,3],[5,4],[4,5],[1,6]].forEach((q,k)=>{const st=[0,1,5,10,15,20,24][k];const on=wk>=st&&u>d*.45;const e=$('ph'+k);e.style.background=on?'linear-gradient(90deg,#7fe3a4,#ffb7d5)':'#16241c';e.style.borderColor=on?'#7fe3a4':'#1c3a2a'});
 }'''
rep("\n if(i==3){\n  $('sweep')",NEWJS+"\n if(i==3){\n  $('sweep')")
# report tab cycling: insert at start of report updater
rep(" if(i==9){\n  [2,4,3]"," if(i==9){\n  {const pi=Math.min(6,Math.floor(cl(u/d,0,.999)*7));for(let k=0;k<7;k++){const e=$('rt'+k);e.style.borderColor=k==pi?'#7fe3a4':'#1c3a2a';e.style.color=k==pi?'#7fe3a4':'#7a9886'}$('rtd').textContent=typed(T.rdesc[pi],u-pi*d/7,.05,45)}\n  [2,4,3]")
# ---------- seek: chapter + mascot + floor
rep("function seek(t){","""function floor(t){cx.strokeStyle='rgba(127,227,164,.13)';cx.lineWidth=1.5;const vy=1560;
 for(let k=0;k<14;k++){const p=((k+t*.5)%14)/14;const y=vy+(1920-vy)*p*p;cx.beginPath();cx.moveTo(0,y);cx.lineTo(1080,y);cx.stroke()}
 for(let k=-10;k<=10;k++){cx.beginPath();cx.moveTo(540+k*10,vy);cx.lineTo(540+k*160,1920);cx.stroke()}}
function seek(t){""")
rep(" bg(t);\n"," bg(t);floor(t);\n")
rep("  if(op>0)scene(i,t-s0,s1-s0);}","  if(op>0){scene(i,t-s0,s1-s0);$('chap').textContent=String(i+1).padStart(2,'0')+' / 13 · '+T.ch[i];$('bb').textContent=T.bub[i];$('mas').style.opacity=a*(1-o);$('mas').style.transform=`translateY(${(1-a)*20}px)`}}")
# ---------- events rewrite
a=s.index('function events(){'); b=s.index('// ---- background canvas')
ev='''function events(){const ev=[];const add=(t,k,v)=>ev.push([t,k,v||1]);
 for(let i=0;i<CMD0.length;i++)add(S[0]+TY0+i/TYC,'key');
 for(let k=0;k<3;k++)add(S[0]+1.3+k*.42,'tick');
 for(let i=1;i<13;i++)add(S[i]-.05,'whoosh');
 add(S[1]+1.3,'pop');const tg=T.tagl;for(let i=0;i<tg.length;i++)add(S[1]+1.9+i/34,'key');
 for(let k=0;k<7;k++)add(S[1]+2.6+k*.25,'pop');
 const d2=D(2);for(let k=0;k<37;k++)add(S[2]+.8+k*(d2*.58/37),'tick');
 const d3=D(3),st3=Math.max(.5,(d3*.62)/9);for(let k=0;k<9;k++)add(S[3]+.7+k*st3+st3*.8,'tick');
 const d4=D(4);for(let i=0;i<ACMD.length;i++)add(S[4]+.6+i/ACPS,'key');
 for(let k=0;k<4;k++)add(S[4]+d4*(.28+k*.1)+.55,'tick');add(S[4]+d4*.74,'pop');
 const d5=D(5);for(let c=0;c<2;c++)for(let r=0;r<4;r++)add(S[5]+.5+c*d5*.3+.5+r*.35,'tick');for(let k=0;k<5;k++)add(S[5]+d5*.62+k*.22,'pop');
 const d6=D(6);for(let k=0;k<3;k++)add(S[6]+d6*(.3+k*.08),'switch');for(let k=0;k<3;k++)add(S[6]+d6*.42+k*.2,'tick');
 const d7=D(7);for(let k=0;k<3;k++)add(S[7]+d7*(.2+k*.1),'pop');for(let k=0;k<9;k++)add(S[7]+d7*.45+k*.1,'tick');
 const d8=D(8);for(let k=0;k<6;k++)add(S[8]+.3+k*.25,'pop');
 const d9=D(9);for(let k=0;k<7;k++)add(S[9]+k*d9/7,'tick');add(S[9]+d9*.2,'pop');add(S[9]+d9*.5,'pop');
 const d10=D(10);for(let k=0;k<10;k++)add(S[10]+.4+k*d10*.4/10,'tick');
 const d11=D(11);for(let k=0;k<6;k++)add(S[11]+.7+k*((d11-2.6)/6)+.3,'switch');
 let t0=S[12]+1.6;for(let k=0;k<3;k++){for(let i=0;i<CMDS[k].length;i++)add(t0+i/30,'key');t0+=CMDS[k].length/30+.4}
 return ev}

'''
s=s[:a]+ev+s[b:]
open('scene4.html','w').write(s)
print('ok')
