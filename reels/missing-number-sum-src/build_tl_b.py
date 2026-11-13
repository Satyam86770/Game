import json
D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/mn/'
W=json.load(open(D+'bunty/words_en.json'))
FIX={'Pundhra!':'Pandrah!','Pundhra':'Pandrah','teem.':'teen!','Buz':'Bas','hoega!':'hoga!','solv':'solve','x':'×','dhimag':'dimaag','baara.':'baarah!','baara,':'baarah,','usse':'use','1':'one','2.':'two.','6':'chhe'}
O=0.1
w=lambda i: round(O+W[i][1],3)
END=round(O+58.04+1.8,3)
K=dict(cells=[-0.5,-0.45,-0.4,-0.35],miss=-0.3,nl=w(28),ask=w(0),sort=w(39),stop=w(49),tc=w(51),bad=w(61),
 on=w(65),form=w(78),n5=w(96),tot=w(100),totv=w(109),add=[w(114),w(116),w(118),w(120)],asum=w(121),res=w(122),cx=w(131),cta=w(142),say=[w(24),w(25),w(26),w(27)])
CAP=[];cur=[]
for i,(a,b) in enumerate(W):
    cur.append([FIX.get(a,a),round(O+b,3)])
    end=a[-1:] in '.,!?' or len(cur)>=4
    if end or i==len(W)-1:
        e=round(O+(W[i+1][1] if i+1<len(W) else 58.04),3);CAP.append([cur[0][1],e,cur]);cur=[]
json.dump({'K':K,'END':END,'CAP':CAP},open(D+'timeline.json','w'),ensure_ascii=False)
json.dump([[D+'vo3/bunty_full.wav',O]],open(D+'vofiles.json','w'))
print(json.dumps(K),END)
