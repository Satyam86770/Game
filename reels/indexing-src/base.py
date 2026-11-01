import json,subprocess
F="/root/.claude/uploads/74005bc4-5fbf-5625-bb25-abf031794fcf/eabbbcbb-18136879063466934.mp4"
FPS=30; EDL=json.load(open('edl.json')); tl=json.load(open('timeline.json')); END=tl['END']
segs=[dict(e) for e in EDL]
last=segs[-1]; tail=END-last['t'][1]
segs.append(dict(src=[last['src'][1],last['src'][1]+tail*1.1],speed=1.1,t=[last['t'][1],END]))
parts=[]
for i,s in enumerate(segs):
    n=round(s['t'][1]*FPS)-round(s['t'][0]*FPS); a,b=s['src']
    o=f'seg/v{i}.mp4'
    vf=f"trim={a}:{b+0.5},setpts=(PTS-STARTPTS)/{s['speed']},fps={FPS}"
    subprocess.run(['ffmpeg','-v','error','-y','-i',F,'-vf',vf,'-frames:v',str(n),'-an','-c:v','libx264','-crf','14','-preset','veryfast','-pix_fmt','yuv420p',o],check=True); parts.append(o)
open('seg/vlist.txt','w').write(''.join(f"file '{p.split('/')[-1]}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','seg/vlist.txt','-c','copy','edit.mp4'],check=True)
L={'hook':"[0:v]crop=270:162:45:148,scale=1000:600:flags=lanczos,unsharp=5:5:0.7,pad=1080:1920:40:450:black",
   'face':"[0:v]scale=1080:1920:flags=lanczos,unsharp=5:5:0.6",
   'anim':"[0:v]crop=180:180:90:122,scale=250:250:flags=lanczos,unsharp=5:5:0.6,pad=1080:1920:795:1620:black"}
for k,f in L.items():
    subprocess.run(['ffmpeg','-v','error','-y','-i','edit.mp4','-filter_complex',f+',format=yuv420p','-c:v','libx264','-crf','15','-preset','veryfast',f'L_{k}.mp4'],check=True)
parts=[]
for i,(a,b,k) in enumerate(tl['SPANS']):
    n0,n1=round(a*FPS),round(b*FPS); o=f'seg/s{i}.mp4'
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'L_{k}.mp4','-vf',f"select='between(n,{n0},{n1-1})',setpts=N/{FPS}/TB",'-frames:v',str(n1-n0),'-c:v','libx264','-crf','15','-preset','veryfast','-pix_fmt','yuv420p',o],check=True); parts.append(o)
open('seg/slist.txt','w').write(''.join(f"file '{p.split('/')[-1]}'\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','seg/slist.txt','-c','copy','base.mp4'],check=True)
for f in ['edit.mp4','base.mp4']: print(f,subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_entries','stream=nb_read_frames','-of','csv=p=0',f]).decode().strip())
