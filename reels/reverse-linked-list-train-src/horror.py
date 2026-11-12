import numpy as np,wave,json,scipy.signal as ss
SR=44100
TL=json.load(open('timeline.json'));K=TL['K'];END=TL['END']
N=int(END*SR);t=np.arange(N)/SR;rng=np.random.default_rng(4)
out=np.zeros((N,2),np.float32)
env=lambda t0,t1,fi=1.0,fo=1.0: np.clip((t-t0)/fi,0,1)*np.clip((t1-t)/fo,0,1)
def band(x,lo,hi):b,a=ss.butter(2,[lo/(SR/2),hi/(SR/2)],'band');return ss.lfilter(b,a,x)
# train clatter: rhythmic clicks + rumble while moving
def clatter(t0,t1,rate):
    rum=band(rng.standard_normal(N),40,300);rum=rum/np.abs(rum).max()*0.12*env(t0,t1,0.3,0.5)
    o=np.repeat(rum[:,None],2,1)
    n=int(0.06*SR);x=np.arange(n)/SR;ck=band(rng.standard_normal(n),800,4000)*np.exp(-x*80);ck=ck/np.abs(ck).max()*0.25
    tc=t0
    while tc<t1:
        for d in (0,0.12):
            i=int((tc+d)*SR);m=min(n,N-i)
            if m>0:o[i:i+m]+=ck[:m,None]
        tc+=rate
    return o
out+=clatter(0,K['h2']+0.5,0.42)
out+=clatter(K['go'],K['yaad'],0.32)
# horn at start (wrong direction) + happy horn
def horn(t0,d,f=(311,370,466)):
    n=int(d*SR);x=np.arange(n)/SR;h=sum(np.sign(np.sin(2*np.pi*ff*x))*0.33 for ff in f)*np.clip(x/0.05,0,1)*np.clip((d-x)/0.15,0,1);h=band(h,150,2500);h=h/np.abs(h).max()*0.22
    i=int(t0*SR);out[i:i+n]+=h[:,None]
horn(0.2,0.9);horn(K['ulta'],0.6,(277,330,415))
horn(K['go']+0.1,0.5);horn(K['go']+0.75,0.9)
w_=wave.open('horror.wav','wb');w_.setnchannels(2);w_.setsampwidth(2);w_.setframerate(SR);w_.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes());w_.close();print('ok')
