set -e
cd /tmp/claude-0/-home-user-Game/74005bc4-5fbf-5625-bb25-abf031794fcf/scratchpad/poly
#node render.js 2>&1 | tail -1
CB=$(python3 -c "import json;print(json.load(open('timeline.json'))['K']['clipB'])"); CC=$(python3 -c "import json;print(json.load(open('timeline.json'))['K']['clipC'])")
ffmpeg -v error -y -i video_noaudio.mp4 -itsoffset $CB -i clips/mB.mp4 -itsoffset $CC -i clips/mC.mp4 -loop 1 -i wm_tile.png -loop 1 -i wm_move.png -filter_complex "[0:v][1:v]overlay=260:940:eof_action=pass:enable='between(t,$CB,$CB+1.5)'[a];[a][2:v]overlay=260:940:eof_action=pass:enable='between(t,$CC,$CC+1.9)'[b];[b][3:v]overlay=0:0:shortest=1[c];[c][4:v]overlay=x='if(lt(mod(t,12),6),40,360)':y='if(lt(mod(t,18),9),1480,1545)':shortest=1,format=yuv420p" -t $(python3 -c "import json;print(json.load(open('timeline.json'))['END'])") -c:v libx264 -crf 20 -preset medium video_final.mp4
python3 mix.py
ffmpeg -v error -y -i video_final.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -af "loudnorm=I=-14:TP=-1.0:LRA=9,alimiter=limit=0.95" -c:a aac -b:a 192k -ar 44100 -movflags +faststart /home/user/Game/reels/Polymorphism_Ninja_Hattori_Reel.mp4
ffprobe -v error -show_entries format=duration,size -of csv=p=0 /home/user/Game/reels/Polymorphism_Ninja_Hattori_Reel.mp4
