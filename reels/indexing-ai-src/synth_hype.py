import numpy as np,wave
SR=44100; rng=np.random.default_rng(11)
BPM=118; b=60/BPM; L=64*b*1.0  # 16 bars
N=int(SR*(L+2)); mus=np.zeros((N,2))
def T(d): return np.arange(int(SR*d))/SR
def add(x,t0,pan=0,g=1):
    i=int(t0*SR); n=min(len(x),N-i)
    if n>0: mus[i:i+n,0]+=x[:n]*g*(1-pan); mus[i:i+n,1]+=x[:n]*g*(1+pan)
def lp(x,a):
    y=np.empty_like(x); s=0.
    for i,v in enumerate(x): s+=a*(v-s); y[i]=s
    return y
def kick():
    t=T(.32); f=48+120*np.exp(-t*35); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*8)*1.0
def clap():
    t=T(.22); n=rng.standard_normal(len(t)); n=n-lp(n,.2); env=np.exp(-t*25)+0.5*np.exp(-((t-.012)*300)**2)+0.4*np.exp(-((t-.024)*300)**2)
    return n*env*0.35
def hat(o=False):
    t=T(.12 if o else .04); n=rng.standard_normal(len(t)); n=n-lp(n,.6); return n*np.exp(-t*(20 if o else 90))*0.16
m=lambda n:440*2**((n-69)/12)
def saw(f,d,cut=.15,amp=.12,dec=6):
    t=T(d); x=sum(np.sin(2*np.pi*f*k*t)/k for k in range(1,9)); x=lp(x,cut); return x*np.exp(-t*dec)*amp
def pad(fs,d):
    t=T(d); x=sum(sum(np.sin(2*np.pi*f*(1+dt)*t) for dt in(-.004,0,.004)) for f in fs)
    return lp(x,.05)*np.minimum(1,t/.3)*np.minimum(1,(d-t)/.3)*0.035
prog=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]  # Am F C G
bass=[45,41,36,43]
arp=[0,1,2,1,0,2,1,2]
for bar in range(16):
    t0=bar*4*b; ch=prog[bar%4]
    add(pad([m(n) for n in ch]+[m(ch[0]+12)],4*b),t0)
    for q in range(4):
        tq=t0+q*b
        add(kick(),tq,g=.95)
        if q in(1,3): add(clap(),tq,g=.9)
        add(hat(),tq+b/2,pan=.3); add(hat(),tq+b/4,pan=-.2,g=.5); add(hat(),tq+3*b/4,pan=-.2,g=.5)
        # bass on offbeats (pumping feel)
        add(saw(m(bass[bar%4]),b/2,cut=.08,amp=.28,dec=7),tq+b/2)
    for e in range(8):
        n=ch[arp[e]]+12+(12 if bar%2 and e>=4 else 0)
        add(saw(m(n),b/2,cut=.25,amp=.07,dec=9),t0+e*b/2,pan=(-.4 if e%2 else .4))
# sidechain pump
t=np.arange(N)/SR; ph=(t%b)/b; pump=0.55+0.45*np.minimum(1,ph/0.35)
mus*=pump[:,None]
mus=mus/np.abs(mus).max()*0.85
w=wave.open('/tmp/ai/music_hype.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mus,-1,1)*32767).astype(np.int16).tobytes()); w.close()
print('len',N/SR)
