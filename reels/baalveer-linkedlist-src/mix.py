import json,wave,subprocess,numpy as np
SR=44100
SRC="/root/.claude/uploads/74005bc4-5fbf-5625-bb25-abf031794fcf/3498906a-VID_20261031_135920_939.mp4"
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
tl=json.load(open('timeline.json')); END=tl['END']; N=int(END*SR); t=np.arange(N)/SR
voice=np.zeros((N,2),np.float32)
for f,t0 in json.load(open('vofiles.json')):
    x=rd(f); i=int(t0*SR); voice[i:i+len(x)]+=x[:N-i]
clipa=np.zeros((N,2),np.float32); inclip=np.zeros(N,np.float32)
for c in tl['CLIPS']:
    if c['mute']: continue
    a,b=c['src']; t0,t1=c['t']; f=f"clips/a_{c['id']}.wav"
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a),'-t',f'{b-a:.3f}','-i',SRC,'-vn','-af','acompressor=threshold=-22dB:ratio=4:attack=5:release=120:makeup=2,lowpass=f=9000,loudnorm=I=-12:TP=-1.5,afade=t=in:d=0.15,areverse,afade=t=in:d=0.2,areverse','-ar',str(SR),'-ac','2',f],check=True)
    x=rd(f); i=int(t0*SR); n=min(len(x),N-i); clipa[i:i+n]+=x[:n]; inclip[i:i+n]=1
mus=rd('/tmp/work/music.wav'); reps=int(np.ceil(N/len(mus)))+1; mus=np.tile(mus,(reps,1))[:N]
env=np.abs(voice[:,0]); win=int(0.05*SR)
act=np.convolve(env,np.ones(win)/win,'same')>0.01
act=np.convolve(act.astype(np.float32),np.ones(int(0.3*SR))/(0.3*SR),'same')
duck=1-0.65*np.clip(act*1.5,0,1)
gate=1-np.clip(np.convolve(inclip,np.ones(int(0.6*SR))/(0.6*SR),'same')*1.1,0,1)  # music off in clips
fade=np.clip(t/0.6,0,1)*np.clip((END-t)/1.8,0,1)
mus=mus*(0.24*duck*(0.15+0.85*gate)*fade)[:,None]
sfx=np.zeros((N,2),np.float32)
for tc,name,g in json.load(open('cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); i=int(max(0,tc)*SR); n=min(len(x),N-i)
    if n>0: sfx[i:i+n]+=x[:n]*g*(0.3 if name=='whoosh' else 0.5)
out=voice+clipa*0.8+mus+sfx
out=out/max(1e-9,np.abs(out).max())*0.93
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',END)
