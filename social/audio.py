import numpy as np, wave
sr=44100; dur=20.5; n=int(sr*dur); L=np.zeros(n); R=np.zeros(n)
def hz(m): return 440*2**((m-69)/12)
def bell(t0,m,vel=.3,dec=1.6,pan=0):
    i=int(t0*sr); 
    if i>=n: return
    t=np.arange(min(int(3*sr),n-i))/sr
    s=sum(a*np.sin(2*np.pi*hz(m)*r*t)*np.exp(-t*d) for r,a,d in [(1,1,dec),(2,.35,dec*1.8),(3.01,.12,dec*3),(5.4,.04,dec*5)])
    s*=vel*(1-np.exp(-t*400))
    L[i:i+len(t)]+=s*(1-pan)/2*2*.5+s*.5*(1-pan); R[i:i+len(t)]+=s*.5*(1+pan)
def pad(t0,t1,ms,vel=.05):
    i0,i1=int(t0*sr),min(int(t1*sr),n); t=np.arange(i1-i0)/sr; T=t1-t0
    env=np.minimum(1,t/1.2)*np.minimum(1,(T-t)/1.5)
    for k,m in enumerate(ms):
        s=np.sin(2*np.pi*hz(m)*t+k)*env*vel+np.sin(2*np.pi*hz(m)*1.003*t)*env*vel*.6
        L[i0:i1]+=s*(1-.2*k/3); R[i0:i1]+=s*(.8+.2*k/3)
# C Am F G, 5s each, arpeggio (midi)
chords=[([48,52,55],[72,76,79,84]),([45,48,52],[69,72,76,81]),([41,45,48],[69,72,77,81]),([43,47,50],[71,74,79,83])]
beat=0.5
for ci,(pc,arp) in enumerate(chords):
    t0=ci*5.1; pad(t0,t0+5.6,pc+[pc[0]+12])
    bell(t0,pc[0]-12+12,.18,.9)
    for k in range(10):
        tt=t0+k*beat
        if tt<dur-1: bell(tt,arp[[0,1,2,3,2,1,2,3,1,2][k]],.16 if k%2 else .22,1.8,pan=((k%4)-1.5)/6)
# transition chimes
for tt in [4.0,8.0,12.0,16.0]:
    bell(tt,91,.12,3,-.3); bell(tt+.07,96,.1,3,.3)
bell(0.0,84,.2,1.2); bell(19.2,84,.18,1.0); bell(19.55,91,.14,1.0)
fade=np.minimum(1,np.arange(n)/(sr*.6))*np.minimum(1,(n-np.arange(n))/(sr*1.2))
o=np.stack([L*fade,R*fade],1); o/=max(1e-9,np.abs(o).max())*1.15
w=wave.open("video/music.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((o*32767).astype('<i2').tobytes()); w.close()
