import json,subprocess
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/jg2/'
W=json.load(open(D+'words.json'))
dur=lambda k: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo3/{k}.wav']))
st={};t=0.15
for k,g in [('h1',0.25),('h2',0.3),('p1',0.3),('p2',0.3),('p3',0.35),('p4',0.35),('p5',0.35),('p6',0.4),('p7',0)]:
    st[k]=round(t,3);t+=dur(k)+g
j1=round(t+0.9,3);j2=round(j1+1.2,3);hug=round(j2+1.1,3);st['p8']=round(hug+1.0,3);END=round(st['p8']+dur('p8')+2.0,3)
w=lambda k,i: round(st[k]+W[k][i][1],3)
L=lambda k,ids:[None if i is None else w(k,i) for i in ids]
K=dict(zx=w('h1',1)+0.2,h2=st['h2'],co=L('h2',[0,1,2]),lc=w('h2',8),lcEnd=st['p1'],p1=st['p1'],p2=st['p2'],ar=L('p2',[8,14,16]),p3=st['p3'],tf=w('p3',9),
 p4=st['p4'],tl=L('p4',[4,7,10,12]),tleR=w('p4',15),ulta=st['p5'],goal=w('p5',3),wStart=st['p6'],wI=L('p6',[2,12,21,28]),wS=L('p6',[7,None,26,None]),wY=L('p6',[None,17,None,33]),
 wG=L('p6',[18,39]),tru=w('p6',42),code=st['p7'],cond=w('p7',7),ret=w('p7',22),j1=j1,snap=round(j1+0.3,3),j2=j2,hug=hug,yaad=st['p8'],cta=w('p8',9))
CAP=[]
for k in st:
    ws=W[k];chunks=[ws[i:i+4] for i in range(0,len(ws),4)]
    for ci,c in enumerate(chunks):
        s0=st[k]+c[0][1];e0=st[k]+(chunks[ci+1][0][1] if ci+1<len(chunks) else dur(k))
        CAP.append([round(s0,3),round(e0,3),[[a,round(st[k]+b,3)] for a,b in c]])
json.dump({'K':K,'END':END,'VO':st,'CAP':CAP},open(D+'timeline.json','w'),ensure_ascii=False)
json.dump([[D+f'vo3/{k}.wav',v] for k,v in st.items()],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
