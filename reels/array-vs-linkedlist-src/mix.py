import json,wave,numpy as np
SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); sr=w.getframerate()
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768
    x=x.reshape(-1,ch); 
    if ch==1: x=np.repeat(x,2,1)
    assert sr==SR,(f,sr); return x
tl=json.load(open('timeline.json')); END=tl['END']; N=int(END*SR)
voice=np.zeros((N,2),np.float32)
for f,t in json.load(open('vofiles.json')):
    x=rd(f); i=int(t*SR); voice[i:i+len(x)]+=x[:N-i]
mus=rd('music.wav')[:N]; mus=np.pad(mus,((0,N-len(mus)),(0,0)))
# ducking envelope from voice activity
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.3*SR))/(0.3*SR),'same')  # smooth
duck=1-0.55*np.clip(act*1.5,0,1)
t=np.arange(N)/SR; fade=np.clip(t/0.8,0,1)*np.clip((END-t)/1.8,0,1)
mus=mus*(0.30*duck*fade)[:,None]
sfx=np.zeros((N,2),np.float32)
for tc,name,g in json.load(open('cues.json')):
    x=rd(f'sfx/{name}.wav'); i=int(max(0,tc)*SR); n=min(len(x),N-i)
    if n>0: sfx[i:i+n]+=x[:n]*g*0.55
out=voice*1.0+mus+sfx
out=out/max(1e-9,np.abs(out).max())*0.93
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',END)
