import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/pd/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.3
st['v1']=t;t+=dur('v1')+0.35
st['v2']=round(t,3);t+=dur('v2');cd=round(t+0.15,3);t=cd+2.15
for k in ['v3','v4','v5','v6','v7','v8']:
    st[k]=round(t,3);t+=dur(k)+0.4
END=round(t+1.8,3)
w=lambda k,i: round(st[k]+W[k][i][1],3)
K=dict(fillEnd=w('v1',19),q=w('v1',26),opts=st['v2'],o1=w('v2',4),o2=w('v2',5),o3=w('v2',8),cd=cd,ans=w('v3',10),chip=st['v4'],leg=w('v4',21),
 cnt=w('v5',8),ein=w('v6',14),emc=w('v6',19),dig=st['v7'],cmp=w('v7',9),x30=w('v7',14),yaad=st['v8'],cta=w('v8',16))
json.dump({'K':K,'END':END,'VO':st},open(D+'timeline.json','w'))
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
