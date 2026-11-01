import json,wave,numpy as np
SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
tl=json.load(open('timeline.json')); K=tl['K']; END=tl['END']; N=int(END*SR); t=np.arange(N)/SR
voice=np.zeros((N,2),np.float32)
for f,t0 in json.load(open('vofiles.json')):
    x=rd(f); i=int(t0*SR); m=min(len(x),N-i); voice[i:i+m]+=x[:m]
mu=rd('music_puzzle.wav'); L=int(16*4*60/100*SR); mu=mu[:L]; mus=np.tile(mu,(N//L+1,1))[:N]
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.25*SR))/(0.25*SR),'same')
duck=1-0.72*np.clip(act*1.5,0,1)
gate=np.ones(N); gate[(t>K['cd0']-0.1)&(t<K['sol']-0.2)]=0
gate=np.convolve(gate,np.ones(int(0.9*SR))/(0.9*SR),'same')
fade=np.clip(t/0.5,0,1)*np.clip((END-t)/1.5,0,1)
mus*=(0.17*duck*gate*fade)[:,None]
sfx=np.zeros((N,2),np.float32)
for tc,name,g in json.load(open('cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); j=int(max(0,tc)*SR); m=min(len(x),N-j)
    gg={'whoosh':0.2,'boom':0.5,'riser':0.4,'tick':0.32,'click':0.35,'clock':0.6,'tock':0.6,'switch':0.5,'step':0.5,'door':0.4,'sizzle':0.35,'hum':0.3,'bell':0.4}.get(name,0.4)
    if name=='boom' and tc<1: gg=0.3
    if m>0: sfx[j:j+m]+=x[:m]*g*gg*0.7
out=voice+mus+sfx
fo=int(0.6*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
out=out/max(1e-9,np.abs(out).max())*0.7
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',END)
