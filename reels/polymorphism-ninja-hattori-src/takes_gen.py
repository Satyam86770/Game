import json,subprocess,time,datetime
S='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/poly'
while datetime.datetime.utcnow()<datetime.datetime(2026,11,7,8,1): time.sleep(30)
P0='Say in a fast, high-energy, hyped, fun young Indian Hinglish Instagram tech reel creator voice, punchy with dramatic pauses (pronounce English tech words like SQL, index, pointer, binary search clearly): '
L={'p1':"Hattori ek hi hai... par kabhi Kenichi ke papa! Kabhi mummy! Aur kabhi khud Kenichi! Ek insaan, kai roop... isi ko kehte hain Polymorphism!",
   'q1':"Ab call karo: ninja Hattori ka roop, mummy ke saath! Compiler dekhta hai, parameter Mummy type ka hai... toh Mummy wala version chalega, aur print hoga:",
   'p5':"Function ka naam same, bas parameter badla... aur kaam badal gaya! Ise kehte hain method overloading, yaani compile time polymorphism!",
   'q3':"Ab asli code dekho! add do numbers ka: add ek, do... return teen! Aur add do strings ka: add ninja, hattori... return ninjahattori! Naam same add, par kaam alag. Yahi hai polymorphism!"}
jobs=[('p1','a'),('p1','b'),('p1','c'),('q1','a'),('q1','b'),('p5','a'),('p5','b'),('q3','a'),('q3','b')]
for k,v in jobs:
    for i in range(2):
        r=subprocess.run(['timeout','200','python3','/tmp/work/tts.py','gemini-2.5-flash-preview-tts','Orus',P0+L[k],f'{S}/takes2/{k}{v}.wav'],capture_output=True,text=True)
        if r.returncode==0: print(k+v,r.stdout.split()[-2],flush=True); break
        print(k+v,'err',r.stderr.strip().splitlines()[-1][:70],flush=True); time.sleep(20)
print('DONE')
