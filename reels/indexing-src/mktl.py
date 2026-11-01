import json
EDL=json.load(open('edl.json'))
SRCK={'naam':0.0,'bara':6.2,'ke':7.98,'deen':9.94,'addr':11.70,'num':15.86,'correct':16.72,
 'agar':17.52,'sql':19.62,'intuit':22.16,'round':23.58,'fresher':25.36,'pays':26.70,'lpa':28.20,
 'answer':30.0,'indexing':31.04,'explain':32.0,'sec30':34.96,'example':35.94,'table':37.02,'name':38.62,'age':39.36,'team':40.16,
 'query':41.12,'select':43.10,'where':44.88,'n34':45.86,'yaha':46.44,'har':48.64,'iterate':49.38,'dekhega':50.30,'age34':51.42,'return':52.92,'complexity':54.18,'bigo':55.10,
 'million':55.58,'kitna':58.28,'solution':59.44,'indextable':60.92,'agecol':62.34,'sorted':63.60,'pointer':65.26,'actualrow':68.50,'playertable':70.50,
 'kyunki':71.54,'binary':74.76,'login':75.76,'value':76.14,'kaafi':77.04,'bachayega':77.92,'please':84.18,'follow':85.02}
def o(s):
    for e in EDL:
        a,b=e['src']
        if a-0.05<=s<=b+0.05: return round(e['t'][0]+(min(max(s,a),b)-a)/e['speed'],3)
    raise Exception(s)
K={k:o(v) for k,v in SRCK.items()}
AUD=EDL[-1]['t'][1]; END=round(AUD+1.95,2)
CAP=[('agar','Agar interviewer pooch le...'),('sql','SQL itna <y>FAST</y> result kaise deta hai? 🤔'),('intuit','<y>Intuit</y> ke 3rd round mein poocha gaya 😳'),
 ('pays','Intuit fresher ko deta hai <g>~35 LPA</g> 💰'),('answer','Answer hai: <y>INDEXING</y> ⚡'),('explain','30 second mein samjho 👇'),
 ('example','Ye hai Players table 🏏'),('name','Name • Age • Team'),('query','Query: <y>WHERE age = 34</y>'),('yaha','SQL <r>har row</r> ek-ek karke check karega...'),
 ('dekhega','age 34 mila? data return ✅'),('complexity','Time complexity: <r>O(N)</r> 😟'),('million','Rows <r>MILLION</r> mein hui toh? 😱'),
 ('solution','Solution: <y>INDEX TABLE</y> 💡'),('agecol','Age column — <y>SORTED</y> order mein'),('pointer','+ <c>Pointer</c> ➜ actual row ka address'),
 ('kyunki','Sorted hai ➜ <y>BINARY SEARCH</y> 🔍'),('login','Value milegi <g>log N</g> mein ⚡'),('kaafi','Kaafi time bachega! 🚀'),('please','Like karo, Follow karo! ❤️')]
CAPS=[[K[k],t] for k,t in CAP]
F2S=o(32.1)
spans=[[0,K['agar']-0.6,'hook'],[K['agar']-0.6,K['intuit']-0.15,'face'],[K['intuit']-0.15,F2S,'anim'],[F2S,K['example']-0.1,'face'],
       [K['example']-0.1,K['solution']-0.1,'anim'],[K['solution']-0.1,END,'anim']]
spans[0][1]=EDL[2]['t'][1]; spans[1][0]=EDL[2]['t'][1]
spans=[[round(a,3),round(b,3),k] for a,b,k in spans]
json.dump(dict(K=K,CAPS=CAPS,SPANS=spans,END=END,AUD=AUD),open('timeline.json','w'),ensure_ascii=False)
print(json.dumps(K));print(spans);print('END',END)
