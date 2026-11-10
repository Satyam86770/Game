import numpy as np,wave,json,scipy.signal as ss
SR=44100
TL=json.load(open('timeline.json'));K=TL['K'];END=TL['END']
N=int(END*SR);t=np.arange(N)/SR;rng=np.random.default_rng(11)
out=np.zeros((N,2),np.float32)
env=lambda t0,t1,fi=1.0,fo=1.0: np.clip((t-t0)/fi,0,1)*np.clip((t1-t)/fo,0,1)
rew=K['rew'];ph=K['phas'];z=K['zero']
def band(x,lo,hi):b,a=ss.butter(2,[lo/(SR/2),hi/(SR/2)],'band');return ss.lfilter(b,a,x)
# river ambience: gurgling water during fail scene and happy ending
M=N;nz=rng.standard_normal(M).astype(np.float32)
riv=band(nz,200,2500)*(0.7+0.3*np.sin(2*np.pi*0.21*t))*(0.8+0.2*np.sin(2*np.pi*1.7*t+1))
riv=riv/np.abs(riv).max()*0.10
renv=env(0,rew+0.4,0.05,0.6)+env(K['happy'],K['yaad']+1,0.5,1.0)
out[:,0]+=riv*renv;out[:,1]+=np.roll(riv,400)*renv
# tense drone
dr=(np.sin(2*np.pi*49*t)+0.7*np.sin(2*np.pi*51.7*t)+0.35*np.sin(2*np.pi*98*t))*(0.7+0.3*np.sin(2*np.pi*0.4*t))
out+=(0.07*dr*env(0,ph,1.2,0.4))[:,None]
# rising tension pitch from croc to phas
s0=K['croc'];i0=int(s0*SR);i1=int(ph*SR);x=np.arange(i1-i0)/SR;f=120+x/(x[-1])*260
rs=np.sin(2*np.pi*np.cumsum(f)/SR)*np.clip(x/2,0,1)*0.035
out[i0:i1]+=rs[:,None]
# heartbeat accelerating
def thump(f=55,d=0.18):n=int(d*SR);xx=np.arange(n)/SR;return np.sin(2*np.pi*f*xx*(1-0.4*xx/d))*np.exp(-xx*22)
hb=np.zeros(N,np.float32);tc=K['croc'];per=0.95
while tc<ph+0.5:
    for off,g in [(0,1.0),(0.17,0.7)]:
        i=int((tc+off)*SR);xx=thump();m=min(len(xx),N-i);hb[i:i+m]+=xx[:m]*g
    per=max(0.42,per*0.955);tc+=per
out+=0.5*hb[:,None]
# croc growl at zero (low rough rumble)
n=int(1.6*SR);xx=np.arange(n)/SR;gr=(np.sin(2*np.pi*(70+8*np.sin(2*np.pi*9*xx))*xx)*(0.6+0.4*np.sign(np.sin(2*np.pi*23*xx))))*np.exp(-xx*1.2)*np.clip(xx/0.05,0,1)
gr=band(gr+0.3*rng.standard_normal(n)*np.exp(-xx*2),40,600);gr=gr/np.abs(gr).max()*0.45
i=int(z*SR);out[i:i+n]+=gr[:,None]
# jaw snap at phas
n=int(0.5*SR);xx=np.arange(n)/SR;sn=band(rng.standard_normal(n),800,6000)*np.exp(-xx*30);sn=sn/np.abs(sn).max()*0.6
i=int(ph*SR);out[i:i+n]+=sn[:,None]
n=int(1.4*SR);xx=np.arange(n)/SR;st=(np.sin(2*np.pi*38*xx)+0.4*rng.standard_normal(n)*np.exp(-xx*9))*np.exp(-xx*2.5)*0.5;out[i:i+n]+=st[:,None]
# birds chirps in hook
for k in range(6):
    t0=0.6+k*0.9+rng.random()*0.3;n=int(0.12*SR);xx=np.arange(n)/SR;ch=np.sin(2*np.pi*(3000+2000*xx/0.12)*xx)*np.sin(np.pi*xx/0.12)*0.04;i=int(t0*SR);out[i:i+n,k%2]+=ch
w_=wave.open('horror.wav','wb');w_.setnchannels(2);w_.setsampwidth(2);w_.setframerate(SR);w_.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes());w_.close();print('ok',END)
