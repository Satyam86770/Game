import json,subprocess
SRC="/root/.claude/uploads/74005bc4-5fbf-5625-bb25-abf031794fcf/3498906a-VID_20261031_135920_939.mp4"
tl=json.load(open('timeline.json')); END=tl['END']; FPS=30
segs=[]; t=0; i=0
def black(d):
    global i; f=f'clips/seg{i:02d}.mp4'; i+=1; n=int(round(d*FPS))
    if n<=0: return
    subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=c=black:s=1080x1920:r={FPS}','-frames:v',str(n),'-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',f],check=True); segs.append(f)
for c in sorted(tl['CLIPS'],key=lambda c:c['t'][0]):
    a,b=c['src']; t0,t1=c['t']
    t0=round(t0*FPS)/FPS; t1=round(t1*FPS)/FPS; n=int(round((t1-t0)*FPS))
    if t0-t>0.001: black(t0-t)
    f=f'clips/seg{i:02d}.mp4'; i+=1
    vf=f"crop=975:835:67:615,scale=1000:856,pad=1080:1920:40:430:black,fps={FPS}"
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a),'-i',SRC,'-vf',vf,'-frames:v',str(n),'-an','-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p',f],check=True); segs.append(f)
    t=t1
black(round(END*FPS)/FPS-t)
open('clips/list.txt','w').write(''.join(f"file '{s.split('/')[-1]}'\n" for s in segs))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','clips/list.txt','-c','copy','base.mp4'],check=True)
print(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','base.mp4']).decode())
