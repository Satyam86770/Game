import json,wave,subprocess,numpy as np
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/bs'; SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
TL=json.load(open(f'{D}/timeline.json')); K=TL['K']; END=TL['END']; N=int(END*SR); t=np.arange(N)/SR
V=json.load(open(f'{D}/vtl.json'))
voice=np.zeros((N,2),np.float32)
for f,t0 in V['files']:
    x=rd(f'{D}/{f}'); i=int(t0*SR); m=min(len(x),N-i); voice[i:i+m]+=x[:m]
mu=rd(f'{D}/../mh/music_mh.wav'); L=int(16*4*60/92*SR); mu=mu[:L]; mus=np.tile(mu,(N//L+2,1))[:N].copy()
r0=int(K['rw0']*SR); r1=int(K['rw1']*SR); ts=int(0.35*SR)
seg=mus[r0-ts:r0].copy(); idx=np.clip(np.cumsum(np.linspace(1,0.15,ts)).astype(int),0,ts-1); mus[r0-ts:r0]=seg[idx]*np.linspace(1,0.3,ts)[:,None]
gate=np.ones(N); gate[r0:r1+int(0.15*SR)]=0; gate[int((K['cd0']-0.2)*SR):int((K['cd1']+0.05)*SR)]=0
gate=np.convolve(gate,np.ones(int(0.25*SR))/(0.25*SR),'same')
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.25*SR))/(0.25*SR),'same')
duck=1-0.6*np.clip(act*1.5,0,1); fade=np.clip(t/0.3,0,1)*np.clip((END-t)/1.2,0,1)
mus*=(0.13*duck*gate*fade)[:,None]
sfx=np.zeros((N,2),np.float32)
G={'whoosh':0.22,'boom':0.55,'riser':0.35,'tick':0.45,'click':0.4,'alarm':0.3,'slap':0.45,'rewind':0.55,'thump':0.6,'step':0.4,'pop':0.4,'ding':0.4,'success':0.45,'sparkle':0.4,'switch':0.5,'hum':0.3,'clock':0.6,'tock':0.6,'bell':0.4,'sizzle':0.35,'door':0.4}
for tc,name,g in json.load(open(f'{D}/cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); j=int(max(0,tc)*SR); m=min(len(x),N-j)
    if m>0: sfx[j:j+m]+=x[:m]*g*G.get(name,0.4)*0.72
out=voice+mus+sfx; fo=int(0.4*SR); out[-fo:]*=np.linspace(1,0.4,fo)[:,None]
out=out/max(1e-9,np.abs(out).max())*0.7
w=wave.open(f'{D}/mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{D}/mix.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.89','-ar','44100',f'{D}/mix2.wav'],check=True)
print('mixed',END)
