import json,subprocess
SRC="/root/.claude/uploads/74005bc4-5fbf-5625-bb25-abf031794fcf/3498906a-VID_20261031_135920_939.mp4"
S=dict(json.load(open('script.json'))); TEMPO=1.06
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
vd={}
for k in S:
    af=("silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.03,areverse,"
        "silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.05,areverse,"
        "silenceremove=stop_periods=-1:stop_duration=0.32:stop_threshold=-42dB:stop_silence=0.22,"
        f"atempo={TEMPO},loudnorm=I=-16:TP=-1.5:LRA=7,aresample=44100")
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'vo/{k}.wav','-af',af,'-ac','1',f'vo2/{k}.wav'],check=True)
    vd[k]=dur(f'vo2/{k}.wav')
seq=[('clip','A',0.0,3.0),('gap',.15),('vo','v1'),('gap',.2),('clip','C',8.3,11.0),('gap',.15),('vo','v2'),('gap',.2),
     ('clip','D',13.8,20.6),('gap',.15),('vo','v3'),('gap',.2),('clip','E',30.0,32.9),('gap',.15),('vo','v4'),('gap',.3),('vo','v5')]
t=0; TL={}; CL=[]; vof=[]
for it in seq:
    if it[0]=='gap': t+=it[1]
    elif it[0]=='clip':
        _,n,a,b=it; CL.append(dict(id=n,src=[a,b],t=[round(t,3),round(t+b-a,3)],mute=False)); t+=b-a
    else:
        k=it[1]; TL[k]=[round(t,3),round(t+vd[k],3)]; vof.append([f'vo2/{k}.wav',t])
        if k=='v1': CL.append(dict(id='B',src=[3.2,3.2+4.6],t=[round(t,3),round(t+4.6,3)],mute=True))
        t+=vd[k]
END=round(t+2.0,2)
json.dump(dict(TL=TL,TX=S,END=END,CLIPS=CL),open('timeline.json','w'),ensure_ascii=False)
json.dump(vof,open('vofiles.json','w'))
print(json.dumps(TL)); print(json.dumps(CL)); print('END',END)
