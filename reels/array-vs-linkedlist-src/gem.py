import os,sys,json,base64,urllib.request
def gen(model, parts, cfg=None):
    k=os.environ['GEMINI_API_KEY']
    body={"contents":[{"parts":parts}]}
    if cfg: body["generationConfig"]=cfg
    req=urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={k}",data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(req,timeout=300))
