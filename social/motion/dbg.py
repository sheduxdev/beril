import sys,json,pathlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parent
V=json.load(open(root.parent/"vo/tr.json")); total=V["end"]+1.8
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.on("pageerror",lambda e:print("PAGEERR",e))
    pg.goto(f"file://{root}/scene5.html")
    try: pg.evaluate(f"init('tr',{json.dumps(V['starts'])},{total})")
    except Exception as e: print("INIT",str(e)[:300])
    for t in [x*0.5 for x in range(150)]:
        try: pg.evaluate(f"seek({t})")
        except Exception as e: print("SEEK",t,str(e)[:400]); break
