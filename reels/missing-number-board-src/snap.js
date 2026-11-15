const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript('window.TL='+fs.readFileSync('/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/mnc/timeline.json','utf8'));await p.goto('file:///tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/mnc/reel.html');await p.waitForFunction(()=>window.READY===true);
for(const t of process.argv.slice(2).map(Number)){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:'/tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/mnc/s_'+t+'.png'})}await b.close()})();
