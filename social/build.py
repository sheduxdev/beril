import pathlib
D = pathlib.Path(__file__).parent / "src"
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;background:#0d1812;color:#f1f7ee;font-family:'Noto Sans','DejaVu Sans',sans-serif;position:relative;overflow:hidden}
.mono{font-family:'JetBrainsMono Nerd Font Mono','DejaVu Sans Mono',monospace}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(120,200,150,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(120,200,150,.06) 1px,transparent 1px);background-size:60px 60px}
.pad{position:absolute;inset:0;padding:80px 72px}
.g{color:#7fe3a4}
.tag{position:absolute;top:56px;right:64px;font-size:26px;letter-spacing:.2em;color:#0d1812;background:#7fe3a4;padding:8px 20px;border-radius:6px;font-weight:700;z-index:5}
.pg{position:absolute;bottom:48px;left:72px;right:72px;display:flex;justify-content:space-between;font-size:24px;color:#8aa597;letter-spacing:.08em}
h1{font-size:150px;line-height:1;font-weight:800;letter-spacing:-.02em}
h2{font-size:86px;line-height:1.1;font-weight:800;margin-bottom:36px}
.rule{width:180px;height:6px;background:#7fe3a4;margin:22px 0}
.card{background:rgba(127,227,164,.07);border:2px solid rgba(127,227,164,.28);border-radius:22px;padding:44px 46px;margin-bottom:34px}
.card h3{font-size:54px;margin-bottom:12px}
.card p{font-size:40px;line-height:1.4;color:#d3e4d8}
.row{display:flex;gap:18px}
.chip{flex:1;background:rgba(127,227,164,.1);border:2px solid rgba(127,227,164,.35);border-radius:18px;padding:22px 10px;text-align:center}
.chip b{display:block;font-size:64px;color:#7fe3a4}
.chip span{font-size:24px;color:#cfe3d6}
li{list-style:none;font-size:44px;line-height:1.35;margin-bottom:34px;color:#e2efe6}

code{font-family:'JetBrainsMono Nerd Font Mono',monospace;color:#7fe3a4;font-size:.86em}
pre{font-family:'JetBrainsMono Nerd Font Mono',monospace;background:#07100b;border:2px solid rgba(127,227,164,.3);border-radius:18px;padding:30px 34px;font-size:36px;line-height:1.7;color:#d8efe0;margin-bottom:28px}
"""
def page(name, body):
    (D/f"{name}.html").write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style><body><div class=grid></div>{body}</body>")

T = {
"tr": dict(tag="TÜRKÇE",
 cover_sub="SİBER İSTİHBARAT",
 cover_line="Yerel çalışan, açık kaynak siber güvenlik skill'i. Uygulamanı tara, açığı kanıtla, raporu yaz.",
 chips=[("65","test"),("10","pratik lab"),("25","haftalık plan")],
 s2_h="İki hat,<br><span class=g>tek bulgu modeli</span>",
 s2=[("Savunma hattı","Sahibi olduğun uygulamayı, repoyu, APK/JAR'ı, MCP ayarını veya Minecraft eklentisini tarar. Çıktı: önceliklendirilmiş düzeltme listesi."),
     ("Saldırı hattı","Açık kaynakta hata avlar. Sahiplik kapısı, ağsız sandbox ve bakımcıya rapor. Zararlı exploit üretmez.")],
 s2_foot="Her bulguda: önem, güven, kanıt, etki, düzeltme ve test edilmeyenler.",
 s3_h="Neleri <span class=g>tarar?</span>",
 s3=["Web uygulaması: başlıklar, CSP, çerez, CORS, TLS, SPF/DKIM/DMARC","Gizli anahtarlar: git geçmişi dahil, maskeli çıktı","Bağımlılıklar: KEV, EPSS ve CVSS ile öncelik","MCP ayarları ve vibe-coded uygulamalar (RLS, service_role)","APK, IPA, EXE, ELF ve JAR: çalıştırmadan statik inceleme","Terraform, Kubernetes, Docker ve SBOM"],
 s4_h="Sınırları <span class=g>açıkça yazar</span>",
 s4=["Sahiplik kaydı olmadan aktif test yok","Kapsam dosyası, istek bütçesi ve hız sınırı zorunlu","Sırlar maskelenir, önce iptal sonra temizlik","Tarayıcı bulgusu ipucudur, elle doğrulanır","Telemetri yok, yükleme yok, her şey yerelde","Doğrulanan ile tahmin edilen ayrı etiketlenir"],
 s5_h="Dene: <span class=g>3 komut</span>",
 s5_note="Raporu 4 okur profiline göre al: mühendis, bug bounty, KOBİ, bakımcı.",
 s5_cta="MIT lisans · GitHub: sheduxdev/beril",
 s5_cta2="Sadece sahibi olduğun hedefleri test et."),
"en": dict(tag="ENGLISH",
 cover_sub="CYBER INTELLIGENCE",
 cover_line="A local-first, open source cybersecurity skill. Scan your app, prove the bug, write the report.",
 chips=[("65","tests"),("10","practice labs"),("25","week plan")],
 s2_h="Two lines,<br><span class=g>one finding model</span>",
 s2=[("Defense line","Scans an app, repo, APK/JAR, MCP config or Minecraft plugin you own. Output: a ranked fix list."),
     ("Attack line","Hunts bugs in open source. Ownership gate, networkless sandbox and a maintainer report. No weaponized exploits.")],
 s2_foot="Every finding: severity, confidence, evidence, impact, fix and what was not tested.",
 s3_h="What it <span class=g>scans</span>",
 s3=["Web apps: headers, CSP, cookies, CORS, TLS, SPF/DKIM/DMARC","Secrets: git history included, masked output","Dependencies: ranked with KEV, EPSS and CVSS","MCP configs and vibe-coded apps (RLS, service_role)","APK, IPA, EXE, ELF and JAR: static review, never executed","Terraform, Kubernetes, Docker and SBOM"],
 s4_h="It states its <span class=g>limits</span>",
 s4=["No active probes without an ownership record","Scope file, request budget and rate limit required","Secrets masked, revoke first then clean history","A scanner hit is a lead, confirmed by hand","No telemetry, no uploads, everything stays local","Confirmed and inferred are labeled apart"],
 s5_h="Try it: <span class=g>3 commands</span>",
 s5_note="Get the report for 4 readers: engineer, bug bounty, SMB, maintainer.",
 s5_cta="MIT license · GitHub: sheduxdev/beril",
 s5_cta2="Only test targets you own."),
}
for L,t in T.items():
    n=5
    ft=lambda i:f"<div class='pg mono'><span>BERIL · v1.4.0</span><span>{i}/{n}</span></div>"
    chips="".join(f"<div class=chip><b>{a}</b><span>{b}</span></div>" for a,b in t['chips'])
    page(f"{L}1", f"""<div class=tag>{t['tag']}</div>
<div style="position:absolute;top:0;left:0;width:1080px;height:720px;background:url(hero.png) center/cover"></div>
<div style="position:absolute;top:380px;left:0;width:1080px;height:340px;background:linear-gradient(transparent,#0d1812)"></div>
<div class=pad style="top:640px"><h1>BERIL</h1><div class=rule></div>
<div class=mono style="font-size:34px;letter-spacing:.28em;color:#7fe3a4;margin-bottom:22px">{t['cover_sub']}</div>
<p style="font-size:36px;line-height:1.4;color:#d3e4d8;margin-bottom:34px">{t['cover_line']}</p>
<div class=row>{chips}</div></div>""")
    cards="".join(f"<div class=card><h3 class=g>{a}</h3><p>{b}</p></div>" for a,b in t['s2'])
    page(f"{L}2", f"<div class=tag>{t['tag']}</div><div class=pad style='padding-top:150px'><h2>{t['s2_h']}</h2>{cards}<p style='font-size:36px;color:#9fb8aa;margin-top:30px;line-height:1.45'>{t['s2_foot']}</p></div>{ft(2)}")
    lis="".join(f"<li>{x}</li>" for x in t['s3'])
    page(f"{L}3", f"<div class=tag>{t['tag']}</div><div class=pad style='padding-top:150px'><h2>{t['s3_h']}</h2><ul>{lis}</ul></div>{ft(3)}")
    lis="".join(f"<li>{x}</li>" for x in t['s4'])
    page(f"{L}4", f"<div class=tag>{t['tag']}</div><div class=pad style='padding-top:150px'><h2>{t['s4_h']}</h2><ul>{lis}</ul></div>{ft(4)}")
    page(f"{L}5", f"""<div class=tag>{t['tag']}</div><div class=pad style='padding-top:150px'><h2>{t['s5_h']}</h2>
<pre>git clone github.com/sheduxdev/beril
cd beril &amp;&amp; ./install.sh
./beril scan --target &lt;url&gt;</pre>
<p style='font-size:40px;color:#d3e4d8;line-height:1.45;margin-bottom:34px'>{t['s5_note']}</p>
<div class=card style='text-align:center'><h3 class=g class=mono>{t['s5_cta']}</h3><p style='font-size:28px'>{t['s5_cta2']}</p></div></div>{ft(5)}""")
