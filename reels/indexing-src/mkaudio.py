import json,subprocess
EDL=json.load(open('edl.json')); parts=[]
for i,s in enumerate(EDL):
    a,b=s['src']; o=f'seg/a{i}.wav'
    af=f"atrim={a}:{b},asetpts=PTS-STARTPTS"+(f",atempo={s['speed']}" if s['speed']!=1 else "")+",afade=t=in:d=0.02,areverse,afade=t=in:d=0.03,areverse"
    subprocess.run(['ffmpeg','-v','error','-y','-i','src.wav','-af',af,'-ar','44100','-ac','1',o],check=True); parts.append(o)
open('seg/alist.txt','w').write(''.join(f"file '{p.split('/')[-1]}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','seg/alist.txt','-c','copy','edit_voice.wav'],check=True)
print(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','edit_voice.wav']).decode())
