import numpy as np,wave
SR=44100; rng=np.random.default_rng(5)
def save(path,x):
    x=np.clip(x,-1,1)
    if x.ndim==1: x=np.stack([x,x],1)
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
def T(d): return np.arange(int(SR*d))/SR
def ks(f,d,damp=.996,bright=.5):   # karplus-strong pluck
    n=int(SR/f); buf=rng.uniform(-1,1,n); out=np.zeros(int(SR*d)); 
    for i in range(len(out)):
        j=i%n; out[i]=buf[j]; buf[j]=damp*(bright*buf[j]+(1-bright)*buf[(j+1)%n])
    return out
m=lambda n:440*2**((n-69)/12)
BPM=100; b=60/BPM; bars=16; N=int(SR*(bars*4*b+2)); mus=np.zeros((N,2))
def add(x,t0,pan=0,g=1):
    i=int(t0*SR); n=min(len(x),N-i)
    if n>0: mus[i:i+n,0]+=x[:n]*g*(1-pan); mus[i:i+n,1]+=x[:n]*g*(1+pan)
def kick():
    t=T(.25); return np.sin(2*np.pi*np.cumsum(55+70*np.exp(-t*30))/SR)*np.exp(-t*12)*.6
def shaker():
    t=T(.06); n=rng.standard_normal(len(t)); return (n-np.convolve(n,np.ones(4)/4,'same'))*np.exp(-t*60)*.08
# sneaky whimsical line (D minor) : bass staccato + melody plucks
bassline=[38,None,45,None,41,None,45,None, 38,None,45,None,43,None,41,40]
mel=[[62,None,65,None,69,67,65,None],[62,None,65,None,70,69,67,None],[69,None,67,65,64,None,62,None],[64,65,67,None,69,None,None,None]]
for bar in range(bars):
    t0=bar*4*b
    for e in range(8):
        te=t0+e*b/2
        bn=bassline[(bar%2)*8+e]
        if bn: add(ks(m(bn),.35,damp=.99,bright=.3)*.55,te,pan=-.1)
        mn=mel[bar%4][e]
        if mn and bar>=1: add(ks(m(mn),.45,damp=.995,bright=.55)*.32,te+(0.03 if e%2 else 0),pan=.25)
        add(shaker(),te+b/4,pan=.4,g=.8)
    for q in range(4):
        if q in(0,2): add(kick(),t0+q*b)
        if q in(1,3): 
            t=T(.12); n=rng.standard_normal(len(t)); add((n-np.convolve(n,np.ones(6)/6,'same'))*np.exp(-t*30)*.18,t0+q*b)  # snap
mus=mus/np.abs(mus).max()*.85; save('/tmp/pz/music_puzzle.wav',mus)
S='/tmp/work/sfx/'
t=T(.09); save(S+'clock.wav',(np.sin(2*np.pi*1800*t)*np.exp(-t*90)+rng.standard_normal(len(t))*np.exp(-t*200)*.3)*.5)
t=T(.09); save(S+'tock.wav',(np.sin(2*np.pi*1100*t)*np.exp(-t*80)+rng.standard_normal(len(t))*np.exp(-t*200)*.3)*.5)
t=T(1.2); n=rng.standard_normal(len(t)); cr=np.where(rng.random(len(t))<.004,rng.uniform(-1,1,len(t)),0)
siz=(n-np.convolve(n,np.ones(3)/3,'same'))*.15+np.convolve(cr,np.ones(30)/30,'same')*4; save(S+'sizzle.wav',siz*np.minimum(1,t/.1)*np.exp(-t*1.5)*.8)
t=T(.12); save(S+'step.wav',np.sin(2*np.pi*np.cumsum(90+60*np.exp(-t*40))/SR)*np.exp(-t*30)*.5+rng.standard_normal(len(t))*np.exp(-t*60)*.08)
t=T(.9); f=180+60*np.sin(2*np.pi*3*t)+40*t; d=np.sign(np.sin(2*np.pi*np.cumsum(f)/SR))*.2; d=np.convolve(d,np.ones(20)/20,'same'); save(S+'door.wav',d*np.minimum(1,t/.05)*np.exp(-t*2)*.7)
t=T(.08); save(S+'switch.wav',rng.standard_normal(len(t))*np.exp(-t*400)*.6+np.sin(2*np.pi*600*t)*np.exp(-t*120)*.4)
t=T(1.5); bell=sum(a*np.sin(2*np.pi*f*t)*np.exp(-t*dd) for f,a,dd in[(1568,.5,2.5),(3136,.25,4),(4704,.12,6),(2350,.15,5)]); save(S+'bell.wav',bell*.6)
t=T(.7); save(S+'hum.wav',np.sin(2*np.pi*120*t)*.15*np.minimum(1,t/.05)*np.exp(-t*3)+np.sin(2*np.pi*240*t)*.06*np.exp(-t*3))
print('ok',N/SR)
