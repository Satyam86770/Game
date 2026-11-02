import json,wave,subprocess,numpy as np
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/wf'; SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
TL=json.load(open(f'{D}/timeline.json')); END=TL['END']; N=int(END*SR); t=np.arange(N)/SR
voice=np.zeros((N,2),np.float32)
for f,t0 in json.load(open(f'{D}/vofiles.json')):
    x=rd(f); i=int(t0*SR); m=min(len(x),N-i); voice[i:i+m]+=x[:m]
mu=rd('/tmp/ai/music_hype.wav'); L=int(64*60/118*SR); mu=mu[:L]; mus=np.tile(mu,(N//L+2,1))[:N].copy()
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.25*SR))/(0.25*SR),'same')
duck=1-0.72*np.clip(act*1.5,0,1); fade=np.clip(t/0.6,0,1)*np.clip((END-t)/1.5,0,1)
mus*=(0.14*duck*fade)[:,None]
sfx=np.zeros((N,2),np.float32)
G={'whoosh':0.18,'type':0.18,'boom':0.4,'riser':0.35,'click':0.35,'pop':0.4,'ding':0.4,'success':0.45,'sparkle':0.4,'buzz':0.35,'slap':0.4}
for tc,name,g in json.load(open(f'{D}/cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); j=int(max(0,tc)*SR); m=min(len(x),N-j)
    if m>0: sfx[j:j+m]+=x[:m]*g*G.get(name,0.4)
out=voice+mus+sfx; fo=int(0.6*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
out=out/max(1e-9,np.abs(out).max())*0.7
w=wave.open(f'{D}/mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{D}/mix.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=9,alimiter=limit=0.89','-ar','44100',f'{D}/mix2.wav'],check=True)
print('mixed',END)
