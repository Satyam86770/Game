import sys,base64,wave; sys.path.insert(0,'/tmp/work'); from gem import gen
model,voice,text,out=sys.argv[1:5]
r=gen(model,[{"text":text}],{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName":voice}}}})
p=r['candidates'][0]['content']['parts'][0]['inlineData']
pcm=base64.b64decode(p['data'])
w=wave.open(out,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm); w.close()
print(out, p['mimeType'], len(pcm)/48000,'s')
