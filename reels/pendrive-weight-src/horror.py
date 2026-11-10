import numpy as np,wave,json,scipy.signal as ss
SR=44100
TL=json.load(open('timeline.json'));K=TL['K'];END=TL['END']
N=int(END*SR);t=np.arange(N)/SR;rng=np.random.default_rng(5)
out=np.zeros((N,2),np.float32)
env=lambda t0,t1,fi=1.0,fo=1.0: np.clip((t-t0)/fi,0,1)*np.clip((t1-t)/fo,0,1)
pad=(np.sin(2*np.pi*110*t)+0.6*np.sin(2*np.pi*138.6*t)+0.5*np.sin(2*np.pi*164.8*t)+0.3*np.sin(2*np.pi*55*t))*(0.7+0.3*np.sin(2*np.pi*0.25*t))
out+=(0.045*pad*env(0,K['ans'],0.3,0.4))[:,None]
# rising whine into the pause
i0=int(K['opts']*SR);i1=int(K['cd']*SR);x=np.arange(i1-i0)/SR;f=300+x/x[-1]*500;out[i0:i1]+=(np.sin(2*np.pi*np.cumsum(f)/SR)*np.clip(x/1.5,0,1)*0.03)[:,None]
def thump(f=55,d=0.18):n=int(d*SR);xx=np.arange(n)/SR;return np.sin(2*np.pi*f*xx*(1-0.4*xx/d))*np.exp(-xx*22)
for k in range(5):
    for off,g in [(0,1.0),(0.17,0.7)]:
        i=int((K['cd']+k*0.45+off)*SR);xx=thump();out[i:i+len(xx)]+=0.5*g*xx[:,None]
w_=wave.open('horror.wav','wb');w_.setnchannels(2);w_.setsampwidth(2);w_.setframerate(SR);w_.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes());w_.close();print('ok')
