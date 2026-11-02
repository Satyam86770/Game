import numpy as np,wave
SR=44100; rng=np.random.default_rng(21)
OUT='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/mh/'
def save(path,x):
    x=np.clip(x,-1,1)
    if x.ndim==1: x=np.stack([x,x],1)
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
def T(d): return np.arange(int(SR*d))/SR
def lp(x,a):
    y=np.empty_like(x); s=0.
    for i,v in enumerate(x): s+=a*(v-s); y[i]=s
    return y
S='/tmp/work/sfx/'
# rewind: fast chirpy reversed blips + sweeping filtered noise
t=T(1.0); n=rng.standard_normal(len(t)); sweep=np.sin(2*np.pi*np.cumsum(300+2500*(0.5+0.5*np.sin(2*np.pi*7*t)))/SR)*.25
bl=np.zeros(len(t))
for k in range(26):
    a=int(k*len(t)/26); f=rng.uniform(800,3000); tt=T(.03); bl[a:a+len(tt)]+=np.sin(2*np.pi*f*tt)*np.exp(-tt*80)*.5
rw=(n-lp(n,.3))*.15*(0.6+0.4*np.sin(2*np.pi*13*t))+sweep+bl
save(S+'rewind.wav',rw*np.minimum(1,t/.05)*np.minimum(1,(1-t)/.1)*.8)
# rumble
t=T(1.6); n=rng.standard_normal(len(t)); r=lp(n,.01)*6+np.sin(2*np.pi*42*t)*.4*(1+0.3*rng.standard_normal(len(t)).cumsum()/3000)
save(S+'rumble.wav',np.clip(r,-1,1)*np.minimum(1,t/.15)*np.exp(-t*1.2)*.9)
# match strike
t=T(.9); n=rng.standard_normal(len(t)); scr=(n-lp(n,.4))*np.exp(-((t-.08)/.06)**2)*.8
ign=lp(n,.08)*np.exp(-t*3)*np.minimum(1,np.maximum(0,(t-.12)/.05))*2.2
save(S+'match.wav',scr+ign)
# fire crackle
t=T(2.0); cr=np.where(rng.random(len(t))<.0025,rng.uniform(-1,1,len(t)),0); cr=np.convolve(cr,np.exp(-np.arange(80)/10),'same')
roar=lp(rng.standard_normal(len(t)),.03)*1.5
save(S+'fire.wav',(cr*.6+roar)*np.minimum(1,t/.2)*np.minimum(1,(2-t)/.4)*.7)
# alarm beeps (digital)
out=np.zeros(int(SR*1.0))
for k in range(3):
    tt=T(.16); x=np.sign(np.sin(2*np.pi*2200*tt))*.25; a=int(k*.25*SR); out[a:a+len(tt)]+=lp(x,.5)
save(S+'alarm.wav',out)
# slap (sticker)
t=T(.12); n=rng.standard_normal(len(t)); save(S+'slap.wav',(lp(n,.35)*2*np.exp(-t*45)+np.sin(2*np.pi*140*t)*np.exp(-t*40)*.5)*.8)
# snip
out=np.zeros(int(SR*.3))
for a in (0,.11):
    tt=T(.05); x=(rng.standard_normal(len(tt))*.5+np.sin(2*np.pi*4200*tt))*np.exp(-tt*120)*.5; i=int(a*SR); out[i:i+len(tt)]+=x
save(S+'snip.wav',out)
# thump
t=T(.3); save(S+'thump.wav',np.sin(2*np.pi*np.cumsum(70+80*np.exp(-t*25))/SR)*np.exp(-t*14)*.9)
# --- music: dark escape-room synth, 92 BPM, 16 bars ---
BPM=92; b=60/BPM; bars=16; N=int(SR*(bars*4*b+2)); mus=np.zeros((N,2))
def add(x,t0,pan=0,g=1):
    i=int(t0*SR); n2=min(len(x),N-i)
    if n2>0: mus[i:i+n2,0]+=x[:n2]*g*(1-pan); mus[i:i+n2,1]+=x[:n2]*g*(1+pan)
m=lambda n:440*2**((n-69)/12)
def pad(fs,d):
    t=T(d); x=sum(sum(np.sin(2*np.pi*f*(1+dt)*t+np.sin(2*np.pi*.2*t)) for dt in(-.005,0,.005)) for f in fs)
    return lp(x,.03)*np.minimum(1,t/.8)*np.minimum(1,(d-t)/.8)*.03
def subp(f,d):
    t=T(d); return np.sin(2*np.pi*f*t)*np.exp(-t*4)*.45
def tickhh():
    t=T(.03); n=rng.standard_normal(len(t)); return (n-lp(n,.6))*np.exp(-t*150)*.12
def bell(f):
    t=T(1.6); return sum(a*np.sin(2*np.pi*f*k*t)*np.exp(-t*dd) for k,a,dd in[(1,.5,2.2),(2.76,.2,3.5),(5.4,.1,5)])*.12
prog=[[45,52,57,60],[41,48,53,57],[43,50,55,58],[40,47,52,56]]  # Am, F, Gm-ish, E
motif=[76,72,69,71]
for bar in range(bars):
    t0=bar*4*b; ch=prog[bar%4]
    add(pad([m(n) for n in ch],4*b),t0)
    for q in range(4):
        add(subp(m(ch[0]-12),b*.9),t0+q*b,g=.9 if q%2==0 else .5)
        for e in range(4): add(tickhh(),t0+q*b+e*b/4,pan=.3*(1 if e%2 else -1),g=1 if e%2==0 else .6)
    if bar%2==1: add(bell(m(motif[(bar//2)%4])),t0+2*b,pan=-.3)
mus=mus/np.abs(mus).max()*.85; save(OUT+'music_mh.wav',mus)
print('ok',N/SR)
