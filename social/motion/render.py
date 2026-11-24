import sys, json, subprocess, pathlib
from playwright.sync_api import sync_playwright
lang=sys.argv[1]; times=[float(x) for x in sys.argv[2:]] if len(sys.argv)>2 else None
root=pathlib.Path(__file__).resolve().parent
V=json.load(open(root.parent/f"vo/{lang}.json")); total=V["end"]+1.8; FPS=30
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{root}/scene.html"); pg.evaluate(f"init('{lang}',{json.dumps(V['starts'])},{total})")
    if times:
        for t in times: pg.evaluate(f"seek({t})"); pg.screenshot(path=f"/tmp/claude-1000/f_{lang}_{t}.png")
        sys.exit()
    ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
     "-i",str(root.parent/f"vo/{lang}.mp3"),"-i",str(root.parent/f"video/music-{lang}.wav"),
     "-filter_complex",f"[1:a]apad,atrim=0:{total},asplit[v1][v2];[2:a]volume=0.55[m];[m][v2]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[md];[v1][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a]",
     "-map","0:v","-map","[a]","-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-t",str(total),"-movflags","+faststart",str(root.parent/f"video/beril-{lang}-916.mp4")],stdin=subprocess.PIPE)
    for f in range(int(total*FPS)):
        pg.evaluate(f"seek({f/FPS})"); ff.stdin.write(pg.screenshot(type="jpeg",quality=93))
    ff.stdin.close(); ff.wait(); print("done",lang)
