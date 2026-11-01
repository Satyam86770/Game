import json,wave,numpy as np
SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
tl=json.load(open('timeline.json')); END=tl['END']; N=int(END*SR); HK=tl['SPANS'][0][1]; t=np.arange(N)/SR
hook=rd('/tmp/ix/seg/vh.wav'); hk=np.zeros((N,2),np.float32); n=min(len(hook),int(HK*SR)); hk[:n]=hook[:n]
k=int(0.15*SR); hk[n-k:n]*=np.linspace(1,0,k)[:,None]
voice=np.zeros((N,2),np.float32)
for f,t0 in json.load(open('vofiles.json')):
    x=rd(f); i=int(t0*SR); m=min(len(x),N-i); voice[i:i+m]+=x[:m]
mu=rd('/tmp/ai/music_hype.wav'); BPM=118; L=int(64*60/BPM*SR); mu=mu[:L]
start=int((HK-0.02)*SR); need=N-start; mus=np.zeros((N,2),np.float32); mus[start:]=np.tile(mu,(need//L+1,1))[:need]
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.25*SR))/(0.25*SR),'same')
duck=1-0.72*np.clip(act*1.5,0,1)
fade=np.clip((END-t)/1.5,0,1)*np.clip((t-HK)/0.8,0,1)
mus*=(0.135*duck*fade)[:,None]
sfx=np.zeros((N,2),np.float32)
for tc,name,g in json.load(open('cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); j=int(max(0,tc)*SR); m=min(len(x),N-j)
    gg={'whoosh':0.17,'type':0.18,'boom':0.55,'riser':0.4,'tick':0.32,'click':0.35}.get(name,0.4)
    if name=='boom' and 1<tc<HK-0.5: gg=0.3
    if name=='boom' and abs(tc-HK)<0.3: gg=0.3
    if name=='whoosh' and abs(tc-HK)<0.4: gg=0.08
    if m>0: sfx[j:j+m]+=x[:m]*g*gg
out=hk+voice+mus+sfx
fo=int(0.6*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
out=out/max(1e-9,np.abs(out).max())*0.93
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',END)
