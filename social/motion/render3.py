import sys, json, subprocess, pathlib
from playwright.sync_api import sync_playwright
lang=sys.argv[1]; root=pathlib.Path(__file__).resolve().parent
V=json.load(open(root.parent/f"vo/{lang}.json")); total=V["end"]+1.8; FPS=30
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{root}/scene5.html"); pg.evaluate(f"init('{lang}',{json.dumps(V['starts'])},{total})")
    json.dump(pg.evaluate("events()"),open(f"/tmp/claude-1000/ev_{lang}.json","w"))
    subprocess.run(["python3","audio3.py",lang],cwd=root,check=True)
    ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
     "-i",str(root.parent/f"vo/{lang}.mp3"),"-i",str(root.parent/f"video/sfx3-{lang}.wav"),
     "-filter_complex",f"[1:a]apad,atrim=0:{total}[v];[2:a]volume=0.45[sx];[v][sx]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a]",
     "-map","0:v","-map","[a]","-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-t",str(total),"-movflags","+faststart",str(root.parent/f"video/beril-{lang}-916-nomusic.mp4")],stdin=subprocess.PIPE)
    for f in range(int(total*FPS)):
        pg.evaluate(f"seek({f/FPS})"); ff.stdin.write(pg.screenshot(type="jpeg",quality=93))
    ff.stdin.close(); ff.wait(); print("done",lang)
