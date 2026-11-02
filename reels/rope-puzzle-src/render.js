const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');const D=process.env.D;
(async()=>{const part=process.argv[2];const FPS=30;const TL=JSON.parse(fs.readFileSync(D+'/timeline.json','utf8'));
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.addInitScript(`window.TLALL=${JSON.stringify(TL)};window.PART='${part}';`);
await p.goto('file://'+D+'/reel.html');await p.evaluate(()=>document.fonts.ready);
fs.writeFileSync(`${D}/cues_${part}.json`,JSON.stringify(await p.evaluate(()=>window.CUES)));
const N=Math.round(TL[part].END*FPS);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','23','-maxrate','9M','-bufsize','18M','-pix_fmt','yuv420p',`${D}/video_${part}.mp4`],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<N;i++){await p.evaluate(t=>window.render(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:92});
 if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%300==0) console.log(part,'frame',i,'/',N)}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done',part)})();
