import numpy as np, wave, json, sys
from scipy.signal import butter, sosfilt
lang=sys.argv[1]; ev=json.load(open(f"/tmp/claude-1000/ev_{lang}.json")); total=json.load(open(f"../vo/{lang}.json"))["end"]+1.8
sr=44100; n=int(sr*total); rng=np.random.default_rng(7)
X=[np.zeros(n),np.zeros(n)]
def put(t0,s,pan=0.0):
    i=int(t0*sr)
    if i<0 or i>=n: return
    s=s[:n-i]; X[0][i:i+len(s)]+=s*(1-max(0,pan)); X[1][i:i+len(s)]+=s*(1+min(0,pan))
for t,kind,v in ev:
    if kind=='key':   # soft low thock, no sharp click
        tt=np.arange(int(.05*sr))/sr; s=np.sin(2*np.pi*(150+rng.uniform(-15,15))*tt)*np.exp(-tt*70)*.16+np.sin(2*np.pi*420*tt)*np.exp(-tt*110)*.05
        put(t,s,rng.uniform(-.15,.15))
    elif kind=='tick':
        tt=np.arange(int(.12*sr))/sr; put(t,np.sin(2*np.pi*760*tt)*np.exp(-tt*38)*.12)
    elif kind=='pop':
        tt=np.arange(int(.18*sr))/sr; f=260+260*np.minimum(1,tt/.08); put(t,np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*20)*.16)
    elif kind=='switch':
        tt=np.arange(int(.12*sr))/sr; put(t,np.sin(2*np.pi*190*tt)*np.exp(-tt*45)*.2+np.sin(2*np.pi*520*tt)*np.exp(-tt*60)*.05)
    elif kind=='knock':
        tt=np.arange(int(.12*sr))/sr; put(t,np.sin(2*np.pi*95*tt)*np.exp(-tt*38)*.35+np.sin(2*np.pi*240*tt)*np.exp(-tt*70)*.08)
    elif kind=='whoosh':
        k=int(.5*sr); x=rng.standard_normal(k); env=np.sin(np.pi*np.arange(k)/k)**2
        y=np.convolve(x,np.ones(90)/90,'same'); put(t-.3,y*env*1.1)
sos=butter(2,2800,'low',fs=sr,output='sos')
L=sosfilt(sos,X[0]); R=sosfilt(sos,X[1])
o=np.stack([L,R],1); o=o/max(1e-9,np.abs(o).max())*0.8
w=wave.open(f"../video/sfx3-{lang}.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((o*32767).astype('<i2').tobytes()); w.close()
print("audio ok",lang,len(ev))
