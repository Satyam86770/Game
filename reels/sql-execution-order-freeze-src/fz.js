const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:720,height:1280}});
await p.goto('file://'+__dirname+'/fz.html');await p.waitForTimeout(500);
for(let i=0;i<60;i++){await p.evaluate(t=>window.render(t),i/30);await p.screenshot({path:`fr/${String(i).padStart(3,'0')}.png`});}
await b.close();})();
