# TCP 3-Way Handshake — AI voice reel v2 (~73s), Indexing-style viral format

**v2 changes:** the creator's old burned-in labels in the Taarak Mehta hook clip ("3-Way Handshake",
CLIENT/server icons, "Syn", "Syn ❌", "Syn + Ack ✅", "Ack", channel logo, Step bar) are removed
frame-by-frame with OpenCV inpainting (`inp.py`, plus an ffmpeg delogo on the top-left page-curl corner) and replaced with HD labels. Hook now shows the
concept running LIVE: packets fly between client/server on the clip, and a "TCP LIVE" terminal under
the clip logs `[SYN] seq=X` → `[SYN,ACK] ack=X+1 seq=Y` → `[ACK] ack=Y+1` → ✅ CONNECTION ESTABLISHED.
Top text after 1.6s: "ORACLE ne poocha! 💰 18 LPA 😳".
Company card: **ORACLE • Applications Developer-1 • Fresher • 💰 CTC ~₹18 LPA** (counter), from the
creator's LeetCode reference post (discuss/post/7553062) and the creator's stated ~18 LPA.
SYN / ACK are spoken as full words: Synchronize, Synchronize-Acknowledgement, Acknowledgement; the
server explicitly says "tumhara SYN packet mere paas aa chuka hai".

Voice: Gemini TTS **Orus**; music: 118 BPM beat ducked; SFX.

| # | Voiceover |
|---|-----------|
| v1 | Sorry... it's okay... yahi hai internet ka three-way handshake! Oracle ne Applications Developer One, fresher role ke interview mein, yahi sawaal poocha... aur package? Pure atharah lakh ka CTC! Chalo, tees second mein samjho! |
| v2 | Client ko server se data chahiye. Socho, bas query bheji, aur data aa gaya? Nahi! Pehle dono ke beech connection banna zaroori hai, aur wo banta hai teen steps mein. |
| v3 | Step one: SYN, yaani Synchronize! Client server ko SYN packet bhejta hai, ek random sequence number ke saath... maan lo X. |
| v4 | Step two: SYN-Acknowledgement! Server kehta hai: tumhara SYN packet mere paas aa chuka hai! Isliye Acknowledgement number bhejta hai, X plus one. Aur saath mein apna SYN bhi, sequence number Y. |
| v5 | Step three: Acknowledgement! Client kehta hai: tumhara SYN bhi mujhe mil gaya, Acknowledgement Y plus one. Ab connection established, aur data flow shuru! |
| v6 | Interviewer ka twist: do steps kyun nahi? Kyunki dono taraf ka sequence number confirm hona zaroori hai! |
| v7 | Ek line mein yaad rakho: SYN, SYN-Acknowledgement, Acknowledgement! Aise hi interview concepts ke liye, pretestpassed dot codes ko follow karo! |
