import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/rll/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.15
for k,g in [('h1',0.3),('h2',0.3),('p1',0.3),('p2',0.3),('p3',0.35),('p4',0.5),('p5',1.6),('p6',0)]:
    st[k]=round(t,3);t+=dur(k)+g
END=round(t+1.8,3)
w=lambda k,i: round(st[k]+W[k][i][1],3)
K=dict(ulta=w('h1',10),h2=st['h2'],lc=w('h2',8),p1=st['p1'],head=w('p1',11),flash=w('p1',21),p2=st['p2'],p3=st['p3'],st=[w('p3',7),w('p3',10),w('p3',18),w('p3',22)],
 p4=st['p4'],fl=[w('p3',13),w('p4',8),w('p4',12),w('p4',13),w('p4',16)],newh=w('p4',26),code=st['p5'],ret=w('p5',3),on=w('p5',3),go=round(w('p5',11)-0.2,3),pay=w('p5',15),yaad=st['p6'],cta=w('p6',11))
CAP=[]
for k in st:
    ws=W[k];ch=[ws[i:i+4] for i in range(0,len(ws),4)]
    for ci,c in enumerate(ch):
        s0=st[k]+c[0][1];e0=st[k]+(ch[ci+1][0][1] if ci+1<len(ch) else dur(k))
        CAP.append([round(s0,3),round(e0,3),[[a,round(st[k]+b,3)] for a,b in c]])
json.dump({'K':K,'END':END,'VO':st,'CAP':CAP},open(D+'timeline.json','w'),ensure_ascii=False)
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
