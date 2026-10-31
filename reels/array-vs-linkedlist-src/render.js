const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
(async()=>{const FPS=30;const tl=JSON.parse(fs.readFileSync('timeline.json','utf8'));
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.addInitScript(`Object.assign(window, ${JSON.stringify(tl)});`);
await p.goto('file:///tmp/work/reel.html');await p.evaluate(()=>document.fonts.ready);
fs.writeFileSync('cues.json',JSON.stringify(await p.evaluate(()=>window.CUES)));
const N=Math.round(tl.END*FPS);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','video_noaudio.mp4'],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<N;i++){await p.evaluate(t=>window.render(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:93});
 if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%300==0) console.log('frame',i,'/',N)}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done')})();
