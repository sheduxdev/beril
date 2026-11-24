import pathlib
D=pathlib.Path(__file__).parent/"src916"; D.mkdir(exist_ok=True)
ns={"__file__":__file__}; exec(open(pathlib.Path(__file__).parent/"build.py").read().split("for L,t in T.items()")[0],ns); T=ns["T"]
CSS="""
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;background:#0d1812;color:#f1f7ee;font-family:'Noto Sans','DejaVu Sans',sans-serif;position:relative;overflow:hidden}
.g{color:#7fe3a4}.mono{font-family:'JetBrainsMono Nerd Font Mono','DejaVu Sans Mono',monospace}
.pad{position:absolute;left:0;right:0;padding:0 80px}
h1{font-size:200px;line-height:1;font-weight:800;letter-spacing:-.02em}
h2{font-size:96px;line-height:1.1;font-weight:800;margin-bottom:56px}
.rule{width:200px;height:8px;background:#7fe3a4;margin:26px 0}
.card{background:#16281e;border:2px solid #2c5a41;border-radius:26px;padding:48px 52px;margin-bottom:40px}
.card h3{font-size:60px;margin-bottom:16px}.card p{font-size:46px;line-height:1.4;color:#d3e4d8}
.row{display:flex;gap:20px}
.chip{flex:1;background:#16281e;border:2px solid #2c5a41;border-radius:20px;padding:26px 10px;text-align:center}
.chip b{display:block;font-size:76px;color:#7fe3a4}.chip span{font-size:28px;color:#cfe3d6}
li{list-style:none;font-size:50px;line-height:1.35;margin-bottom:44px;color:#e2efe6}

pre{font-family:'JetBrainsMono Nerd Font Mono',monospace;background:#13241b;border:2px solid #2c5a41;border-radius:22px;padding:36px 40px;font-size:38px;line-height:1.7;color:#d8efe0;margin-bottom:40px}
.tag{position:absolute;top:170px;right:64px;font-size:30px;letter-spacing:.2em;color:#0d1812;background:#7fe3a4;padding:10px 24px;border-radius:8px;font-weight:700}
"""
def page(n,b): (D/f"{n}.html").write_text(f"<!doctype html><meta charset=utf-8><style>{CSS}</style><body>{b}</body>")
for L,t in T.items():
    page(f"{L}0",f"<div class=tag>{t['tag']}</div>")
    chips="".join(f"<div class=chip><b>{a}</b><span>{b}</span></div>" for a,b in t['chips'])
    page(f"{L}1",f"""<div class=pad style='top:900px'><h1>BERIL</h1><div class=rule></div>
<div class=mono style='font-size:38px;letter-spacing:.28em;color:#7fe3a4;margin-bottom:28px'>{t['cover_sub']}</div>
<p style='font-size:42px;line-height:1.4;color:#d3e4d8;margin-bottom:44px'>{t['cover_line']}</p><div class=row>{chips}</div></div>""")
    cards="".join(f"<div class=card><h3 class=g>{a}</h3><p>{b}</p></div>" for a,b in t['s2'])
    page(f"{L}2",f"<div class=pad style='top:270px'><h2>{t['s2_h']}</h2>{cards}<p style='font-size:38px;color:#9fb8aa;line-height:1.45'>{t['s2_foot']}</p></div>")
    for i,k in ((3,'s3'),(4,'s4')):
        lis="".join(f"<li>{x}</li>" for x in t[k]); page(f"{L}{i}",f"<div class=pad style='top:270px'><h2>{t[k+'_h']}</h2><ul>{lis}</ul></div>")
    page(f"{L}5",f"""<div class=pad style='top:270px'><h2>{t['s5_h']}</h2>
<pre>git clone github.com/sheduxdev/beril
cd beril &amp;&amp; ./install.sh
./beril scan --target &lt;url&gt;</pre>
<p style='font-size:44px;color:#d3e4d8;line-height:1.45;margin-bottom:44px'>{t['s5_note']}</p>
<div class=card style='text-align:center'><h3 class=g>{t['s5_cta']}</h3><p style='font-size:34px'>{t['s5_cta2']}</p></div></div>""")
