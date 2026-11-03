import cv2,numpy as np,subprocess
fr=np.load('fr.npy')[:182]
P=10
def boxes(i):
    b=[]
    if i<48: b.append((60,30,656,156))
    if 47<=i<=80: b.append((350,20,534,206))
    if 47<=i<=79: b.append((140,424,310,536))
    if 78<=i<=157: b.append((210,96,400,364))
    if 81<=i<=138: b.append((406,446,712,594))
    if 136<=i<=156: b.append((246,440,694,580))
    if i>=156: b+= [(380,10,626,280),(236,420,466,584)]
    return b
ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','720x1280','-r','30','-i','-',
 '-vf','crop=720:690:0:200,scale=1000:958:flags=lanczos,unsharp=5:5:0.5,pad=1080:1920:40:300:black','-c:v','libx264','-crf','15','-preset','veryfast','-pix_fmt','yuv420p','h_clean.mp4'],stdin=subprocess.PIPE)
out=[]
for i,f in enumerate(fr):
    m=np.zeros(f.shape[:2],np.uint8)
    for x0,y0,x1,y1 in boxes(i): m[200+y0-P:200+y1+P, max(0,x0-P):min(720,x1+P)]=255
    m[200:390,665:720]=255
    m[872:892,:]=255
    band=f[855:892]; dark=(band.max(2)<45).astype(np.uint8)*255
    m[855:892]|=cv2.dilate(dark,np.ones((9,9),np.uint8))
    g=cv2.inpaint(f,m,6,cv2.INPAINT_TELEA); g[868:892]=g[867]; ff.stdin.write(g.tobytes()); out.append(g)
ff.stdin.close(); ff.wait()
ts=[];_=[0.3,1.7,2.4,2.6,2.8,3.3,4.2,4.9,5.3,5.9]
ims=[] and [cv2.resize(out[int(t*30)][200:890],(360,345)) for t in ts]
0 and cv2.imwrite('x.png',np.vstack([np.hstack(ims[:5]),np.hstack(ims[5:])]))
