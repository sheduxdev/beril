import numpy as np, json, subprocess, sys, math
from PIL import Image, ImageDraw, ImageFilter
lang=sys.argv[1]; V=json.load(open(f"vo/{lang}.json")); W,H,FPS=1080,1920,30
starts=V["starts"]; total=V["end"]+1.8; ends=starts[1:]+[total]
BG=np.array([13,24,18],np.int16)
def L(n): return np.asarray(Image.open(f"src916/{lang}{n}.png").convert("RGB"),np.int16)
tag=L(0)
def bands(a):
    m=(np.abs(a-BG).max(2)>14).sum(1)>2; rows=np.where(m)[0]; out=[]; s=p=rows[0]
    for r in rows[1:]:
        if r-p>20: out.append((s,p+1)); s=r
        p=r
    out.append((s,p+1)); return out
S=[]
for i in range(1,6):
    a=L(i); bs=bands(a); S.append((a,bs)); print(i,len(bs))
hero=Image.open("src/hero.png").convert("RGB").resize((1080,720),Image.LANCZOS)
yy,xx=np.mgrid[0:720,0:1080]
fade=np.clip(np.minimum(yy/120,(719-yy)/220),0,1)[...,None]  # soft edges
grid=np.zeros((H+120,W+120),np.int16)
grid[::60,:]=7; grid[:,::60]=7
rng=np.random.default_rng(4); P=[(rng.uniform(0,W),rng.uniform(0,H),rng.uniform(6,16),rng.uniform(25,70),rng.uniform(0,6.28)) for _ in range(16)]
def ease(x): x=min(1,max(0,x)); return 1-(1-x)**3
def frame(t):
    off=(t*10)%60
    bg=np.broadcast_to(BG,(H,W,3)).astype(np.int16).copy()
    bg+=grid[int(off):int(off)+H,int(off):int(off)+W][...,None]
    # glow
    gx=int(W*(.5+.25*math.sin(t*.4))); gy=int(H*(.55+.1*math.cos(t*.3)))
    img=Image.fromarray(bg.clip(0,255).astype(np.uint8)); ov=Image.new("RGB",(W,H),(0,0,0)); d=ImageDraw.Draw(ov)
    d.ellipse((gx-420,gy-420,gx+420,gy+420),fill=(10,34,22)); ov=ov.filter(ImageFilter.GaussianBlur(160))
    out=np.maximum(np.asarray(img,np.int16),np.asarray(ov,np.int16)+BG*0)
    out=np.maximum(out,np.asarray(img,np.int16)+np.asarray(ov,np.int16)//2)
    # particles
    pl=Image.new("RGB",(W,H),(0,0,0)); d=ImageDraw.Draw(pl)
    for x,y,r,sp,ph in P:
        yv=(y-t*sp)%H; xv=x+14*math.sin(t*.7+ph); a=.5+.5*math.sin(t*1.3+ph)
        c=(int(40*a),int(110*a),int(70*a)); d.ellipse((xv-r,yv-r,xv+r,yv+r),fill=c)
    out=np.minimum(out+np.asarray(pl.filter(ImageFilter.GaussianBlur(2)),np.int16),255)
    i=max(k for k,s in enumerate(starts) if t>=s-0.0) if t>=starts[0] else 0
    st,en=starts[i],ends[i]; a,bs=S[i]
    if i==0:  # hero with slow zoom
        z=1+.06*min(1,t/total*3); w,h=int(1080*z),int(720*z)
        hz=hero.resize((w,h),Image.BILINEAR).crop(((w-1080)//2,(h-720)//2,(w-1080)//2+1080,(h-720)//2+720))
        h_arr=np.asarray(hz,np.int16)*fade; al=ease(t/0.8)
        blk=out[130:850]; out[130:850]=np.maximum(blk,(h_arr*al+blk*(1-al*fade)).astype(np.int16)) if False else (blk*(1-fade*al)+h_arr*al).astype(np.int16)
    nb=len(bs); t0=st+(0.2 if i else 0.35); step=min(.9,max(.3,(en-st-1.4)/(nb+.5)))
    outk=ease((t-(en-.35))/.35) if i<4 else 0
    for k,(y0,y1) in enumerate(bs):
        p=ease((t-(t0+k*step))/.55)
        if p<=0: continue
        dy=int((1-p)*60+outk*-40); al=p*(1-outk)
        if al<=0.01: continue
        src=a[y0:y1]; ya=y0+dy; ya0=max(0,ya); ya1=min(H,ya+(y1-y0))
        seg=src[ya0-ya:ya1-ya]; reg=out[ya0:ya1]
        out[ya0:ya1]=np.maximum(reg,BG+((seg-BG)*al).astype(np.int16))
    tg=ease(t/.6); out=np.maximum(out,BG+((tag-BG)*tg).astype(np.int16))
    # progress bar
    pw=int(W*min(1,t/total)); out[96:102,:pw]=np.maximum(out[96:102,:pw],[127,227,164]); 
    return out.clip(0,255).astype(np.uint8)
n=int(total*FPS)
ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
 "-i",f"vo/{lang}.mp3","-i",f"video/music-{lang}.wav",
 "-filter_complex",f"[1:a]apad,atrim=0:{total},asplit[v1][v2];[2:a]volume=0.55[m];[m][v2]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[md];[v1][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a]",
 "-map","0:v","-map","[a]","-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-t",f"{total}","-movflags","+faststart",f"video/beril-{lang}-916.mp4"],stdin=subprocess.PIPE)
for f in range(n): ff.stdin.write(frame(f/FPS).tobytes())
ff.stdin.close(); ff.wait(); print("done",lang,total)
