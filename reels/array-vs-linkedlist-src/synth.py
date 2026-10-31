import numpy as np, wave
SR=44100
def save(name,x):
    x=np.clip(x,-1,1); 
    if x.ndim==1: x=np.stack([x,x],1)
    w=wave.open(name,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
def t_(d): return np.arange(int(SR*d))/SR
rng=np.random.default_rng(7)
def lp(x,a):  # one-pole lowpass
    y=np.empty_like(x); s=0.
    for i,v in enumerate(x): s+=a*(v-s); y[i]=s
    return y
# ---------- music ----------
BPM=96; beat=60/BPM; bars=26; L=bars*4*beat
mus=np.zeros((int(SR*(L+2)),2))
def add(buf,x,t0,pan=0.,g=1.):
    i=int(t0*SR); n=min(len(x),len(buf)-i)
    if n<=0: return
    buf[i:i+n,0]+=x[:n]*g*(1-pan)*1.0; buf[i:i+n,1]+=x[:n]*g*(1+pan)*1.0
def kick():
    t=t_(0.35); f=50+90*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*9)*0.9
def snare():
    t=t_(0.25); n=rng.standard_normal(len(t)); n=n-lp(n,0.15)
    return (n*0.45*np.exp(-t*18)+np.sin(2*np.pi*190*t)*0.25*np.exp(-t*25))
def hat(o=False):
    t=t_(0.18 if o else 0.05); n=rng.standard_normal(len(t)); n=n-lp(n,0.5)
    return n*0.18*np.exp(-t*(15 if o else 70))
def note(f,d,typ='pad'):
    t=t_(d)
    if typ=='pad':
        x=sum(np.sin(2*np.pi*f*k*t+0.3*np.sin(2*np.pi*0.4*t))/k**1.6 for k in range(1,5))
        env=np.minimum(1,t/0.08)*np.exp(-t*0.6)
        return x*env*0.12
    if typ=='pluck':
        x=np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*2*f*t)+0.15*np.sin(2*np.pi*3*f*t)
        return x*np.exp(-t*7)*0.10
    if typ=='bass':
        x=np.sin(2*np.pi*f*t)+0.25*np.sin(2*np.pi*2*f*t)
        return x*np.minimum(1,t/0.01)*np.exp(-t*2.2)*0.32
m=lambda n:440*2**((n-69)/12)
prog=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,65]]  # Am7 Fmaj7 Cmaj7 G7
bassn=[45,41,36,43]
mel=[76,74,72,74, 72,69,72,74, 71,72,74,76, 74,71,67,71]
for b in range(bars):
    t0=b*4*beat; ch=prog[b%4]
    for n in ch: add(mus,note(m(n),4*beat,'pad'),t0,pan=rng.uniform(-.3,.3))
    add(mus,note(m(bassn[b%4]),2*beat,'bass'),t0); add(mus,note(m(bassn[b%4]),1.5*beat,'bass'),t0+2.5*beat)
    drums = b>=1
    for q in range(4):
        tq=t0+q*beat
        if drums:
            if q in(0,2): add(mus,kick(),tq)
            if q==2 and b%2: add(mus,kick()*0.7,tq+0.75*beat)
            if q in(1,3): add(mus,snare(),tq+0.012,g=0.9)
            for e in range(2):
                sw=0.0 if e==0 else 0.56*beat
                add(mus,hat(e==1 and q==3),tq+sw,pan=0.25,g=0.9 if e==0 else 0.6)
        if b>=2:
            for e in range(2):
                n=mel[(b*8+q*2+e)%16]
                if rng.random()<0.65: add(mus,note(m(n),0.5,'pluck'),tq+e*0.5*beat,pan=-0.2)
# vinyl crackle
cr=np.zeros(len(mus)); idx=rng.integers(0,len(cr),int(len(cr)/SR*25)); cr[idx]=rng.uniform(-.25,.25,len(idx))
mus[:,0]+=lp(cr,0.4)*0.25; mus[:,1]+=lp(cr,0.4)*0.25
mus=mus/np.abs(mus).max()*0.8
save('/tmp/work/music.wav',mus)
# ---------- sfx ----------
def whoosh():
    t=t_(0.45); n=rng.standard_normal(len(t)); env=np.sin(np.pi*np.minimum(t/0.45,1))**2
    y=np.zeros_like(n); s=0.; 
    for i,v in enumerate(n):
        a=0.02+0.25*(i/len(n)); s+=a*(v-s); y[i]=s
    return y*env*2.2
def pop():
    t=t_(0.09); f=900-600*t/0.09; return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*45)*0.6
def ding():
    t=t_(0.9); return (np.sin(2*np.pi*1318*t)+0.5*np.sin(2*np.pi*1975*t)+0.3*np.sin(2*np.pi*2637*t))*np.exp(-t*5)*0.25
def buzz():
    t=t_(0.45); x=np.sign(np.sin(2*np.pi*110*t))*0.5+np.sign(np.sin(2*np.pi*116*t))*0.5; return lp(x,0.2)*np.exp(-t*3)*0.35
def click():
    t=t_(0.03); return rng.standard_normal(len(t))*np.exp(-t*250)*0.5+np.sin(2*np.pi*2000*t)*np.exp(-t*200)*0.4
def success():
    out=np.zeros(int(SR*0.6))
    for i,f in enumerate([784,988,1318]):
        t=t_(0.35); x=np.sin(2*np.pi*f*t)*np.exp(-t*8)*0.25; a=int(i*0.08*SR); out[a:a+len(x)]+=x[:len(out)-a]
    return out
def sparkle():
    out=np.zeros(int(SR*1.2))
    for i in range(14):
        f=rng.uniform(2000,4500); t=t_(0.25); x=np.sin(2*np.pi*f*t)*np.exp(-t*18)*0.12; a=int(rng.uniform(0,0.9)*SR); out[a:a+len(x)]+=x
    return out
def tick():
    t=t_(0.06); return np.sin(2*np.pi*1500*t)*np.exp(-t*80)*0.35
for n,f in dict(whoosh=whoosh,pop=pop,ding=ding,buzz=buzz,click=click,success=success,sparkle=sparkle,tick=tick).items(): save(f'/tmp/work/sfx/{n}.wav',f())
print('ok',len(mus)/SR)
