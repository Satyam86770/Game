import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/hr2/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.3
st['l1']=t;t+=dur('l1')+0.35
st['l2']=t;e2=t+dur('l2');alarm=round(e2+0.25,3);rew=round(alarm+2.9,3)
t=rew+0.4
for k,g in [('l3',0.35),('l4',0.35),('l5',0.4),('l6',0.4),('l7',0.45),('l8',0)]:
    st[k]=round(t,3);t+=dur(k)+g
smart=round(t+0.1,3);t=smart+3.3;st['l9']=round(t,3);END=round(t+dur('l9')+2.2,3)
w=lambda k,i: round(st[k]+W[k][i][1],3)
L=lambda k,ids: [None if i is None else w(k,i) for i in ids]
K=dict(padosi=w('l1',17),wire=w('l1',14),robGo=round(st['l2'],3),alarm=alarm,rew=rew,q2=st['l3'],lc=w('l3',8),prob=st['l4'],twist=w('l4',10),
 cut=w('l5',3),c1o=w('l5',8),c2o=w('l5',22),c1=st['l6'],dpi=w('l6',5),
 fillA=[x-0.1 for x in L('l6',[14,16,21,27])],numA=L('l6',[15,19,25,31]),blueA=L('l6',[None,17,22,28]),yelA=L('l6',[None,19,24,30]),resA=L('l6',[15,20,26,32]),ansA=w('l6',33),
 c2=st['l7'],fillB=[x-0.1 for x in L('l7',[5,7,12,19])],numB=L('l7',[6,10,16,23]),blueB=L('l7',[None,8,13,20]),yelB=L('l7',[None,10,15,22]),resB=L('l7',[6,11,18,25]),ansB=w('l7',26),
 fin=st['l8'],code=w('l8',6),ranges=w('l8',12),prev=w('l8',27),on=w('l8',40),smart=smart,smartEnd=round(smart+3.0,3),pay=round(smart+2.3,3),yaad=st['l9'],cta=w('l9',18))
json.dump({'K':K,'END':END,'VO':st},open(D+'timeline.json','w'))
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
