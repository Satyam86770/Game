import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/hr/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
I=json.load(open(D+'idx.json'))  # word indices per key
st={};t=0.3
st['v1']=t;t+=dur('v1')+0.35
st['v2']=t;e2=t+dur('v2')
w=lambda k,i: round(st[k]+W[k][i][1],3)
alarm=round(e2+0.25,3);rew=round(alarm+2.9,3)
st['v3']=rew+0.4;t=st['v3']+dur('v3')+0.4
st['v4']=t;t+=dur('v4')+0.35
st['v5']=t;t+=dur('v5')+0.35
st['v6']=t;t+=dur('v6')+0.4
st['v7']=t;e7=t+dur('v7');t=e7+1.1
st['v8']=t;END=round(t+dur('v8')+2.2,3)
K=dict(rule=w('v1',I['rule']),wire=w('v1',I['wire']),robGo=w('v1',I['robGo']),rob1=w('v2',I['rob1'])+0.35,rob2=round(alarm-0.8,3),alarm=alarm,rew=rew,
 q2=round(st['v3'],3),lc=w('v3',I['lc']),prob=round(st['v4'],3),nums=[w('v4',i) for i in I['nums']],adj=w('v4',I['adj']),ret=w('v4',I['ret']),
 oA=w('v5',I['oA']),oB=w('v5',I['oB']),mx=w('v5',I['mx']),fill0=w('v6',I['fill'][0])-0.2,fill=[w('v6',i)-0.1 for i in I['fill']],res=[w('v6',i) for i in I['res']],
 code=round(st['v7'],3),on=w('v7',I['on']),smart=w('v7',I['smart'])-0.4,smartEnd=round(e7+0.9,3),pay=w('v7',I['pay']),yaad=round(st['v8'],3),cta=w('v8',I['cta']))
json.dump({'K':K,'END':END,'VO':st},open(D+'timeline.json','w'))
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
