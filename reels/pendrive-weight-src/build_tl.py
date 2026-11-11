import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/pd/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.3
for k,g in [('k1',0.45),('s1',0.45),('s2',0.4),('n1',0)]:
    st[k]=round(t,3);t+=dur(k)+g
cd=round(t+0.15,3);t=cd+2.15;cut=round(t,3)
for k in ['v3','v4','v5','v6','v7','v8']:
    st[k]=round(t,3);t+=dur(k)+0.4
END=round(t+1.8,3)
w=lambda k,i: round(st[k]+W[k][i][1],3)
e=lambda k: round(st[k]+dur(k),3)
K=dict(k1=st['k1'],k1e=e('k1'),s1=st['s1'],s1e=e('s1'),mv=[w('s1',5),w('s1',6),w('s1',7),w('s1',10)],s2=st['s2'],s2e=e('s2'),n1=st['n1'],
 opts=w('n1',14),o1=w('n1',14)+0.2,o2=w('n1',14)+0.5,o3=w('n1',14)+0.8,cd=cd,cut=cut,fillEnd=-5,q=cut,
 ans=w('v3',10),chip=st['v4'],leg=w('v4',21),cnt=w('v5',8),ein=w('v6',14),emc=w('v6',19),dig=st['v7'],cmp=w('v7',9),x30=w('v7',14),yaad=st['v8'],cta=w('v8',16))
json.dump({'K':K,'END':END,'VO':st},open(D+'timeline.json','w'))
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
