import sys, json, pathlib
from playwright.sync_api import sync_playwright
lang=sys.argv[1]; times=[float(x) for x in sys.argv[2:]]
root=pathlib.Path(__file__).resolve().parent
V=json.load(open(root.parent/f"vo/{lang}.json")); total=V["end"]+1.8
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e))); pg.on("console",lambda m:errs.append(m.text) if m.type=="error" else None)
    pg.goto(f"file://{root}/scene5.html"); pg.evaluate(f"init('{lang}',{json.dumps(V['starts'])},{total})")
    for t in times: pg.evaluate(f"seek({t})"); pg.screenshot(path=f"/tmp/claude-1000/g_{lang}_{t}.png")
    print(errs[:5]); print(len(pg.evaluate("events()")))
