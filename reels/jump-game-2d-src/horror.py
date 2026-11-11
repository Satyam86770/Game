import numpy as np,wave,json,scipy.signal as ss
SR=44100
TL=json.load(open('timeline.json'));K=TL['K'];END=TL['END']
N=int(END*SR);t=np.arange(N)/SR;rng=np.random.default_rng(9)
out=np.zeros((N,2),np.float32)
env=lambda t0,t1,fi=1.0,fo=1.0: np.clip((t-t0)/fi,0,1)*np.clip((t1-t)/fo,0,1)
def band(x,lo,hi):b,a=ss.butter(2,[lo/(SR/2),hi/(SR/2)],'band');return ss.lfilter(b,a,x)
riv=band(rng.standard_normal(N),150,2200);riv=riv/np.abs(riv).max()*0.07
out[:,0]+=riv*(0.6+0.4*env(0,K['h2'],0.01,0.5));out[:,1]+=np.roll(riv,400)*(0.6+0.4*env(0,K['h2'],0.01,0.5))
# hook: deep stinger + growl
n=int(1.6*SR);x=np.arange(n)/SR;st=(np.sin(2*np.pi*42*x)+0.4*rng.standard_normal(n)*np.exp(-x*8))*np.exp(-x*2.2)*0.55;out[:n]+=st[:,None]
n=int(1.4*SR);x=np.arange(n)/SR;gr=band((np.sin(2*np.pi*(65+8*np.sin(2*np.pi*9*x))*x)*(0.6+0.4*np.sign(np.sin(2*np.pi*21*x))))*np.exp(-x*1.5)+0.3*rng.standard_normal(n)*np.exp(-x*2),40,600);gr=gr/np.abs(gr).max()*0.4
i=int(K['zx']*SR);out[i:i+n]+=gr[:,None]
dr=(np.sin(2*np.pi*46*t)+0.6*np.sin(2*np.pi*48.7*t))*0.06*env(0,K['h2'],0.05,0.4);out+=dr[:,None]
# snap at payoff
n=int(0.4*SR);x=np.arange(n)/SR;sn=band(rng.standard_normal(n),800,6000)*np.exp(-x*30);sn=sn/np.abs(sn).max()*0.5;i=int(K['snap']*SR);out[i:i+n]+=sn[:,None]
w_=wave.open('horror.wav','wb');w_.setnchannels(2);w_.setsampwidth(2);w_.setframerate(SR);w_.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes());w_.close();print('ok')
