import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/mn/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.1
for k,g in [('l1',0.3),('l2',0.35),('l3',0.35),('l4',0.3),('l5',0.5),('l6',0)]:
    st[k]=round(t,3);t+=dur(k)+g
END=round(t+1.8,3)
w=lambda k,i: round(st[k]+W[k][i][1],3)
K=dict(cells=[-0.5,-0.45,-0.4,-0.35],miss=-0.3,nl=w('l1',10),ask=w('l1',19),sort=st['l2'],stop=w('l2',10),tc=w('l2',12),bad=w('l2',22),
 on=st['l3'],form=w('l3',13),n5=st['l4'],tot=w('l4',4),totv=w('l4',13),add=[w('l4',18),w('l4',20),w('l4',22),w('l4',24)],asum=w('l4',25),res=st['l5'],cx=w('l5',8),cta=st['l6'])
CAP=[]
for k in st:
    ws=W[k];ch=[ws[i:i+4] for i in range(0,len(ws),4)]
    for ci,c in enumerate(ch):
        s0=st[k]+c[0][1];e0=st[k]+(ch[ci+1][0][1] if ci+1<len(ch) else dur(k))
        CAP.append([round(s0,3),round(e0,3),[[a,round(st[k]+b,3)] for a,b in c]])
json.dump({'K':K,'END':END,'VO':st,'CAP':CAP},open(D+'timeline.json','w'),ensure_ascii=False)
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
