const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
const D='/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/rll';
(async()=>{const FPS=30;const tl=JSON.parse(fs.readFileSync(D+'/timeline.json','utf8'));
const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(`window.TL=${JSON.stringify(tl)};`);
await p.goto('http://127.0.0.1:8771/reel.html');await p.waitForFunction(()=>window.READY===true,{timeout:60000});await p.evaluate(()=>document.fonts.ready);
fs.writeFileSync(D+'/cues.json',JSON.stringify(await p.evaluate(()=>window.CUES)));
const N=Math.round(tl.END*FPS);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',String(FPS),D+'/video_noaudio.mp4'],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<N;i++){await p.evaluate(t=>window.render(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:95});
 if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%300==0) console.log('frame',i,'/',N,new Date().toISOString())}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done')})();
