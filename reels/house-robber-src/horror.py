import numpy as np,wave,json
SR=44100
TL=json.load(open('timeline.json'));K=TL['K'];END=TL['END']
N=int(END*SR);t=np.arange(N)/SR
rng=np.random.default_rng(7)
def lp(x,a):  # one-pole lowpass
    y=np.empty_like(x);s=0.0
    for i in range(len(x)): s+=a*(x[i]-s);y[i]=s
    return y
out=np.zeros((N,2),np.float32)
def env(t0,t1,fi=1.0,fo=1.0):
    return np.clip((t-t0)/fi,0,1)*np.clip((t1-t)/fo,0,1)
lc=K['lc'];rew=K['rew'];al=K['alarm']
# wind: lowpassed noise with slow swell, 0 -> rew
M=int((rew+1)*SR);nz=rng.standard_normal(M).astype(np.float32)
import scipy.signal as ss
b,a=ss.butter(2,[150/(SR/2),900/(SR/2)],'band');w=ss.lfilter(b,a,nz)
w*= (0.6+0.4*np.sin(2*np.pi*0.13*np.arange(M)/SR))*(0.7+0.3*np.sin(2*np.pi*0.37*np.arange(M)/SR+1))
w=w/np.abs(w).max()*0.18
wv=np.zeros(N,np.float32);wv[:M]=w;wv*=env(0,rew+0.5,0.05,0.8)
out[:,0]+=wv;out[:,1]+=np.roll(wv,300)
# drone: low detuned sines + slow tremolo, until alarm
dr=(np.sin(2*np.pi*55*t)+0.8*np.sin(2*np.pi*58.3*t)+0.4*np.sin(2*np.pi*110.5*t))*(0.75+0.25*np.sin(2*np.pi*0.5*t))
dr*=0.06*env(0,al,1.5,0.3);out+=dr[:,None]
# heartbeat: from rule to alarm, speeding up
def thump(f=55,d=0.18):
    n=int(d*SR);x=np.arange(n)/SR;return np.sin(2*np.pi*f*x*(1-0.4*x/d))*np.exp(-x*22)
hb=np.zeros(N,np.float32);tc=K['rule'];per=0.95
while tc<al-0.1:
    for off,g in [(0,1.0),(0.17,0.7)]:
        i=int((tc+off)*SR);x=thump();m=min(len(x),N-i);hb[i:i+m]+=x[:m]*g
    per=max(0.5,per*0.965);tc+=per
out+=0.55*hb[:,None]
# owl hoots at 1.2s
def hoot(t0,f=410):
    n=int(0.45*SR);x=np.arange(n)/SR;e=np.sin(np.pi*x/0.45)**1.5
    return t0,np.sin(2*np.pi*(f-40*x/0.45)*x+0.6*np.sin(2*np.pi*6*x))*e
for t0,f in [(1.0,420),(1.6,400),(1.85,395)]:
    _,h=hoot(t0,f);i=int(t0*SR);m=min(len(h),N-i);out[i:i+m,0]+=0.10*h[:m];out[i:i+m,1]+=0.07*h[:m]
# siren: wail from alarm to rew
s0=al;s1=rew-0.1;i0=int(s0*SR);i1=int(s1*SR);x=np.arange(i1-i0)/SR
f=950+350*np.sign(np.sin(2*np.pi*1.6*x))  # hi-lo two tone
ph=2*np.pi*np.cumsum(f)/SR;sir=(2/np.pi)*np.arcsin(np.sin(ph))
sir*=np.clip(x/0.15,0,1)*np.clip((s1-s0-x)/0.4,0,1)*0.14
out[i0:i1,0]+=sir;out[i0:i1,1]+=sir*0.9
# low stinger at alarm
n=int(1.2*SR);x=np.arange(n)/SR;st=(np.sin(2*np.pi*40*x)+0.5*rng.standard_normal(n)*np.exp(-x*8))*np.exp(-x*3)*0.5
i=int(al*SR);out[i:i+n]+=st[:,None]
w_=wave.open('horror.wav','wb');w_.setnchannels(2);w_.setsampwidth(2);w_.setframerate(SR)
w_.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes());w_.close();print('ok',END)
