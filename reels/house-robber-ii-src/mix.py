import json,wave,numpy as np
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/hr2/'
SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
tl=json.load(open(D+'timeline.json')); K=tl['K']; END=tl['END']; N=int(END*SR); t=np.arange(N)/SR
voice=np.zeros((N,2),np.float32)
for f,t0 in json.load(open(D+'vofiles.json')):
    x=rd(f); i=int(t0*SR); m=min(len(x),N-i); voice[i:i+m]+=x[:m]
hor=rd(D+'horror.wav')[:N]; hor=np.pad(hor,((0,N-len(hor)),(0,0)))
mu=rd('/tmp/ai/music_hype.wav'); s=int(K['lc']*SR); need=N-s
mus=np.zeros((N,2),np.float32); mus[s:]=np.tile(mu,(need//len(mu)+1,1))[:need]
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.25*SR))/(0.25*SR),'same')
duck=1-0.7*np.clip(act*1.5,0,1)
fade=np.clip((END-t)/1.5,0,1)*np.clip((t-K['lc'])/0.6,0,1)
mus*=(0.13*duck*fade)[:,None]
hduck=1-0.45*np.clip(act*1.5,0,1); hor*=hduck[:,None]
sfx=np.zeros((N,2),np.float32)
G={'whoosh':0.2,'click':0.22,'pop':0.3,'ding':0.22,'boom':0.5,'door':0.6,'cash':0.45,'rewind':0.55,'thump':0.6,'buzz':0.25,'sparkle':0.35,'success':0.45}
for tc,name,g in json.load(open(D+'cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); j=int(max(0,tc)*SR); m=min(len(x),N-j)
    if m>0: sfx[j:j+m]+=x[:m]*g*G.get(name,0.4)
out=voice*1.0+hor+mus+sfx
fo=int(0.6*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
out=out/max(1e-9,np.abs(out).max())*0.93
w=wave.open(D+'mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',END)
