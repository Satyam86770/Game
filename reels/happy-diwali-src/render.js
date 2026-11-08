const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/ov.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const N=Math.round(35.2*30);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-c:v','qtrle','ov.mov']);
for(let i=0;i<N;i++){await p.evaluate(t=>window.render(t),i/30);const buf=await p.screenshot({omitBackground:true});
 if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();})();
