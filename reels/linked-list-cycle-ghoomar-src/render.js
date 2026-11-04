const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
(async()=>{const FPS=30;const tl=JSON.parse(fs.readFileSync('/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/gm/timeline.json','utf8'));
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.addInitScript(`window.TL=${JSON.stringify(tl)};`);
await p.goto('file:///tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/gm/reel.html');await p.evaluate(()=>document.fonts.ready);
fs.writeFileSync('/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/gm/cues.json',JSON.stringify(await p.evaluate(()=>window.CUES)));
const N=Math.round(tl.END*FPS);
const ff=spawn('ffmpeg',['-v','error','-y','-i','/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/gm/base.mp4','-f','image2pipe','-framerate',String(FPS),'-c:v','png','-i','-',
 '-filter_complex','[0:v][1:v]overlay=0:0:shortest=1,format=yuv420p','-c:v','libx264','-preset','medium','-crf','18','-r',String(FPS),'/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/gm/video_noaudio.mp4'],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<N;i++){await p.evaluate(t=>window.render(t),i/FPS);const buf=await p.screenshot({type:'png',omitBackground:true});
 if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%300==0) console.log('frame',i,'/',N)}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done')})();
