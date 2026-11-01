import json,wave,subprocess,numpy as np
SR=44100
def rd(f):
    w=wave.open(f); n=w.getnframes(); ch=w.getnchannels(); assert w.getframerate()==SR,f
    x=np.frombuffer(w.readframes(n),np.int16).astype(np.float32)/32768; x=x.reshape(-1,ch)
    return np.repeat(x,2,1) if ch==1 else x
tl=json.load(open('timeline.json')); END=tl['END']; N=int(END*SR); HK=tl['SPANS'][0][1]
# level-match hook (movie) and creator parts separately
subprocess.run(['ffmpeg','-v','error','-y','-i','edit_voice.wav','-af',f'atrim=0:{HK},loudnorm=I=-15:TP=-1.5:LRA=9','-ar',str(SR),'-ac','1','seg/vh.wav'],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i','edit_voice.wav','-af',f'atrim={HK},asetpts=PTS-STARTPTS,loudnorm=I=-14:TP=-1.5:LRA=7','-ar',str(SR),'-ac','1','seg/vc.wav'],check=True)
voice=np.zeros((N,2),np.float32)
a=rd('seg/vh.wav'); voice[:min(N,len(a))]+=a[:N]
b=rd('seg/vc.wav'); i=int(HK*SR); n=min(len(b),N-i); voice[i:i+n]+=b[:n]
# short crossfade at the hook/creator seam
k=int(0.12*SR); voice[i-k:i]*=np.linspace(1,0,k)[:,None]; voice[i:i+k]*=np.linspace(0,1,k)[:,None]
sfx=np.zeros((N,2),np.float32)
for tc,name,g in json.load(open('cues.json')):
    x=rd(f'/tmp/work/sfx/{name}.wav'); j=int(max(0,tc)*SR); m=min(len(x),N-j)
    gg={'whoosh':0.28,'type':0.18,'boom':0.6,'riser':0.4,'tick':0.32,'click':0.35}.get(name,0.4)
    if name=='boom' and tc>1: gg=0.3
    if name in('success','sparkle','ding') and tc>60: gg=0.25
    if m>0: sfx[j:j+m]+=x[:m]*g*gg
t=np.arange(N)/SR
out=voice+sfx
fo=int(0.7*SR); out[-fo:]*=np.linspace(1,0,fo)[:,None]
out=out/max(1e-9,np.abs(out).max())*0.93
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',END)
