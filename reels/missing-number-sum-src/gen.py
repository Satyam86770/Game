import json,subprocess,time,os
P="Say in a smooth, confident, conversational young Indian male explainer voice, fast and rhythmic Hinglish, clear emphasis on key words like a professional tech educator: "
S=json.load(open('script.json'))
for k,v in S.items():
    for a in range(4):
        if os.path.exists(f'vo/{k}.wav'):break
        r=subprocess.run(['python3','/tmp/work/tts.py','gemini-2.5-flash-preview-tts','Alnilam',P+v,f'vo/{k}.wav'],capture_output=True,text=True)
        print(time.strftime('%H:%M:%S'),k,r.stdout.strip(),r.stderr.strip()[-60:],flush=True);time.sleep(25)
print('DONE')
