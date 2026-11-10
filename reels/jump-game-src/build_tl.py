import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/jg/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.3
for k,g in [('v1',0.4),('v3b',0.4),('v4',0.35),('vR',0.4),('v5',0.4),('v7b',0.4),('v8',0)]:
    st[k]=round(t,3);t+=dur(k)+g
w=lambda k,i: round(st[k]+W[k][i][1],3)
happy=round(w('v8',34)-0.2,3);hug=round(max(happy+3.8,t+0.3),3)
st['v9']=round(hug+1.5,3);END=round(st['v9']+dur('v9')+2.2,3)
L=lambda k,ids:[w(k,i) for i in ids]
K=dict(croc=w('v1',14),rule=w('v1',20),mom=w('v1',39),q2=st['v3b'],lc=w('v3b',10),prob=st['v4'],ask=w('v4',16),
 range=st['vR'],rMax=w('vR',5),rAny=w('vR',16),rEx=w('vR',25),rA1=w('vR',33),rA2=w('vR',38),rNo=round(w('vR',38)+0.6,3),
 trick=st['v5'],goal=w('v5',3),tStart=st['v7b'],tI=L('v7b',[2,12,21,30]),tS=L('v7b',[7,17,26,35]),tG=L('v7b',[9,18,27,36]),tTrue=w('v7b',39),
 code=st['v8'],cond=w('v8',7),ret=w('v8',23),on=w('v8',27),happy=happy,hj1=round(happy+1.3,3),hj2=round(happy+2.7,3),hug=hug,yaad=st['v9'],cta=w('v9',21))
json.dump({'K':K,'END':END,'VO':st},open(D+'timeline.json','w'))
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
