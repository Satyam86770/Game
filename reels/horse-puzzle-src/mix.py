import json,wave,numpy as np,subprocess,scipy.signal as ss
SR=44100;T=json.load(open('timeline.json'));K=T['K'];END=T['END'];N=int(END*SR);t=np.arange(N)/SR
subprocess.run(['ffmpeg','-v','error','-y','-i','../horse_ref/r.mp4','-vn','-ac','2','-ar',str(SR),'orig.wav'])
def rd(f):
    w=wave.open(f);x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;x=x.reshape(-1,w.getnchannels());return np.repeat(x,2,1) if x.shape[1]==1 else x
v=rd('orig.wav')[:N];v=np.pad(v,((0,N-len(v)),(0,0)))
rng=np.random.default_rng(3);out=v.copy()
def band(x,lo,hi):b,a=ss.butter(2,[lo/(SR/2),hi/(SR/2)],'band');return ss.lfilter(b,a,x)
env=lambda a,b,fi=0.3,fo=0.4: np.clip((t-a)/fi,0,1)*np.clip((b-t)/fo,0,1)
# crowd
cr=band(rng.standard_normal(N),300,3000);cr=cr/np.abs(cr).max()
crowd=np.zeros(N)
for a,b in [(0,11.8)]+[(s,e+0.8) for s,e in zip(K['rowStart'],K['rowEnd'])]+[(K['r6'],K['r6']+3.4),(K['r7'],K['r7']+3.8)]:crowd+=env(a,b)
out+=(0.06*cr*np.clip(crowd,0,1))[:,None]
# gallop: thump pairs at ~3.3Hz per horse
def thump(d=0.06):n=int(d*SR);x=np.arange(n)/SR;return band(rng.standard_normal(n),60,500)*np.exp(-x*60)
gal=np.zeros(N);th=thump();th/=np.abs(th).max()
for a,b in [(0,11.8)]+list(zip(K['rowStart'],[e+0.3 for e in K['rowEnd']]))+[(K['r6'],K['r6']+2.8),(K['r7'],K['r7']+3.2)]:
    tc=a
    while tc<b:
        for off in (0,0.07,0.14,0.21):
            i=int((tc+off+rng.random()*0.02)*SR);m=min(len(th),N-i)
            if m>0:gal[i:i+m]+=th[:m]*0.5
        tc+=0.33
out+=(0.12*gal)[:,None]
for tc,name,gg in json.load(open('cues.json')):
    w=wave.open(f'/tmp/work/sfx/{name}.wav');x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;x=x.reshape(-1,w.getnchannels());x=np.repeat(x,2,1) if x.shape[1]==1 else x
    i=int(tc*SR);m=min(len(x),N-i)
    if m>0:out[i:i+m]+=x[:m]*gg*0.35
out=out/max(1e-9,np.abs(out).max())*0.9
w=wave.open('mix.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close();print('mixed')
