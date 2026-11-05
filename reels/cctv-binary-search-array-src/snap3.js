const {chromium}=require('playwright');const fs=require('fs');const D=process.env.D;
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>{if(m.type()=='error')console.log('CERR',m.text())});
await p.addInitScript(`window.TL=${fs.readFileSync(D+'/timeline.json','utf8')};`);
await p.goto('http://127.0.0.1:8765/reel.html');await p.waitForFunction(()=>window.READY===true,{timeout:60000});await p.evaluate(()=>document.fonts.ready);
for(const t of process.argv.slice(2).map(Number)){const t0=Date.now();await p.evaluate(t=>window.render(t),t);await p.screenshot({path:`${D}/ov_${t}.png`});console.log(t,Date.now()-t0,'ms')}
await b.close()})();
