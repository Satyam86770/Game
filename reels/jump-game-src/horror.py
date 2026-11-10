import numpy as np,wave,json,scipy.signal as ss
SR=44100
TL=json.load(open('timeline.json'));K=TL['K'];END=TL['END']
N=int(END*SR);t=np.arange(N)/SR;rng=np.random.default_rng(11)
out=np.zeros((N,2),np.float32)
env=lambda t0,t1,fi=1.0,fo=1.0: np.clip((t-t0)/fi,0,1)*np.clip((t1-t)/fo,0,1)
lc=K['lc']
def band(x,lo,hi):b,a=ss.butter(2,[lo/(SR/2),hi/(SR/2)],'band');return ss.lfilter(b,a,x)
nz=rng.standard_normal(N).astype(np.float32)
# rushing river (deep) + rain hiss during hook
riv=band(nz,120,1800)*(0.7+0.3*np.sin(2*np.pi*0.23*t))*(0.85+0.15*np.sin(2*np.pi*2.1*t+1));riv=riv/np.abs(riv).max()*0.16
rain=band(np.roll(nz,12345),2500,9000);rain=rain/np.abs(rain).max()*0.07
he=env(0,lc+0.6,0.02,0.8);hp=env(K['range'],K['trick'],0.5,0.5)*0.5+env(K['happy'],K['yaad']+1,0.5,1.0)*0.8
out[:,0]+=riv*(he+hp)+rain*he;out[:,1]+=np.roll(riv,500)*(he+hp)+np.roll(rain,333)*he
# deep horror drone with dissonance
dr=(np.sin(2*np.pi*43*t)+0.7*np.sin(2*np.pi*45.9*t)+0.35*np.sin(2*np.pi*87*t)+0.2*np.sin(2*np.pi*131*t))*(0.65+0.35*np.sin(2*np.pi*0.33*t))
out+=(0.09*dr*env(0,lc,0.4,0.6))[:,None]
# thunder at lightning times
for x in [1.2,6.8,11.6]:
    n=int(3.0*SR);xx=np.arange(n)/SR;th=band(rng.standard_normal(n),30,400)*(np.exp(-xx*1.3)*(1-np.exp(-xx*25)))*(0.7+0.3*np.sin(2*np.pi*3*xx));th=th/np.abs(th).max()*0.55
    cr=band(rng.standard_normal(int(0.3*SR)),1500,7000)*np.exp(-np.arange(int(0.3*SR))/SR*14)*0.35
    i=int(x*SR);m=min(n,N-i);out[i:i+m]+=th[:m,None];out[i:i+len(cr)]+=cr[:,None]
# heartbeat accelerating croc->lc
def thump(f=55,d=0.18):n=int(d*SR);xx=np.arange(n)/SR;return np.sin(2*np.pi*f*xx*(1-0.4*xx/d))*np.exp(-xx*22)
hb=np.zeros(N,np.float32);tc=K['croc'];per=0.9
while tc<lc:
    for off,g in [(0,1.0),(0.17,0.7)]:
        i=int((tc+off)*SR);xx=thump();m=min(len(xx),N-i);hb[i:i+m]+=xx[:m]*g
    per=max(0.42,per*0.955);tc+=per
out+=0.5*hb[:,None]
# croc growls (2) in hook
for x in [K['croc']+0.3,K['q2']+0.5]:
    n=int(1.5*SR);xx=np.arange(n)/SR;gr=(np.sin(2*np.pi*(65+8*np.sin(2*np.pi*9*xx))*xx)*(0.6+0.4*np.sign(np.sin(2*np.pi*21*xx))))*np.exp(-xx*1.3)*np.clip(xx/0.05,0,1)
    gr=band(gr+0.3*rng.standard_normal(n)*np.exp(-xx*2),40,600);gr=gr/np.abs(gr).max()*0.4;i=int(x*SR);out[i:i+n]+=gr[:,None]
# rising tension whine into lc
i0=int(K['q2']*SR);i1=int(lc*SR);x=np.arange(i1-i0)/SR;f=200+x/x[-1]*500;rs=np.sin(2*np.pi*np.cumsum(f)/SR)*np.clip(x/1.5,0,1)*0.04;out[i0:i1]+=rs[:,None]
# jaw snap at hj1 (baby escapes)
n=int(0.4*SR);xx=np.arange(n)/SR;sn=band(rng.standard_normal(n),800,6000)*np.exp(-xx*30);sn=sn/np.abs(sn).max()*0.6;i=int((K['hj1']+0.15)*SR);out[i:i+n]+=sn[:,None]
w_=wave.open('horror.wav','wb');w_.setnchannels(2);w_.setsampwidth(2);w_.setframerate(SR);w_.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes());w_.close();print('ok',END)
