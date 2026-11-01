import numpy as np,wave,json,subprocess
w=wave.open('src.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
# voice band energy
X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/sr); X[(f<250)|(f>3500)]=0; v=np.fft.irfft(X,len(x))
hop=int(0.01*sr); e=np.array([np.sqrt((v[i:i+2*hop]**2).mean()) for i in range(0,len(v)-2*hop,hop)])
def snap(t,r=0.25):
    a,b=int((t-r)*100),int((t+r)*100); k=a+np.argmin(e[a:b]); return round(k/100+0.01,2)
# (src_start, src_end, kind, speed)
raw=[(0.0,2.6,'hook'),(5.7,13.4,'hook'),(14.9,17.0,'hook'),
     (17.0,46.0,'creator'),(48.4,80.1,'creator'),(85.5,87.45,'creator')]
EDL=[]
for a,b,k in raw:
    a2=a if a in(0.0,17.0) else snap(a); b2=b if b==17.0 else snap(b)
    EDL.append(dict(src=[a2,b2],kind=k,speed=1.0 if k=='hook' else 1.1))
t=0
for s in EDL:
    d=(s['src'][1]-s['src'][0])/s['speed']; s['t']=[round(t,3),round(t+d,3)]; t+=d
json.dump(EDL,open('edl.json','w'),indent=1); print(json.dumps(EDL)); print('total',round(t,2))
