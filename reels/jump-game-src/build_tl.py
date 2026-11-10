import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/jg/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.3
st['v1']=t;t+=dur('v1')+0.3
st['v2']=t;e2=t+dur('v2');phas=round(e2+0.7,3);rew=round(phas+2.4,3)
t=rew+0.4
for k,g in [('v3',0.35),('v4',0.35),('v5',0.4),('v6',0.4),('v7',0.4),('v8',0)]:
    st[k]=round(t,3);t+=dur(k)+g
w=lambda k,i: round(st[k]+W[k][i][1],3)
happy=round(w('v8',34)-0.2,3);hug=round(max(happy+3.8,t+0.3),3)
st['v9']=round(hug+1.5,3);END=round(st['v9']+dur('v9')+2.2,3)
L=lambda k,ids:[w(k,i) for i in ids]
K=dict(croc=w('v1',14),rule=w('v1',20),mom=w('v1',39),jump=w('v2',7),zero=w('v2',18),phas=phas,rew=rew,
 ghost=[w('v3',1),w('v3',3)+0.2,w('v3',5)+0.2],q2=w('v3',13),lc=w('v3',23),prob=st['v4'],ask=w('v4',16),trick=st['v5'],goal=w('v5',3),
 fStart=st['v6'],fI=L('v6',[6,15,22,29]),fS=L('v6',[11,20,27,34]),fN=L('v6',[14,21,28,35]),fFalse=w('v6',40),
 tStart=st['v7'],tI=L('v7',[5,15,24,33]),tS=L('v7',[10,20,29,38]),tG=L('v7',[12,21,30,39]),tTrue=w('v7',42),
 code=st['v8'],cond=w('v8',7),ret=w('v8',23),on=w('v8',27),happy=happy,hj1=round(happy+1.3,3),hj2=round(happy+2.7,3),hug=hug,yaad=st['v9'],cta=w('v9',21))
json.dump({'K':K,'END':END,'VO':st},open(D+'timeline.json','w'))
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
