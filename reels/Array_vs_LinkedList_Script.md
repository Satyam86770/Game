# Array vs Linked List — Reel Script (Hinglish, ~66s)

Style: same format as the "Auth vs Authz" reel — dark gradient, @pretestpassed.codes watermark, step pills,
real-life analogy, "Ek line mein yaad rakho", Save/Share/Follow CTA.
Voice: Gemini TTS, voice **Puck** (picked as the closest match to the reference: young male, energetic, fast Hinglish).
Music: original lo-fi hip-hop beat (synthesized), ducked under the voice. SFX: whoosh / pop / ding / buzz / click / sparkle.

| # | Scene | Voiceover |
|---|-------|-----------|
| 1 | Hook | Array aur Linked List... dono mein data hi store hota hai. Phir interviewer kyun poochta hai, fark kya hai? |
| 2 | ARRAY vs LINKED LIST | Kyunki dono ka data rakhne ka tareeka bilkul alag hai! Chalo cinema hall aur treasure hunt se samajhte hain. |
| 3 | Step 1 • Array (cinema row) | Array matlab cinema hall ki ek row. Saari seats ek ke baad ek, line mein... memory mein bhi bilkul aise hi, continuous. |
| 4 | Direct jump | Seat number pata hai? Seedha wahin pahuncho! Index paanch, ek hi jump mein. Yehi hai O of one access. |
| 5 | Step 2 • Linked List (treasure hunt) | Ab Linked List. Ye hai treasure hunt! Har box mein data, aur agle box ka address, yaani pointer. |
| 6 | Traversal | Boxes memory mein kahin bhi bikhre ho sakte hain. Paanchva box chahiye? Shuru se ek-ek clue follow karo. Yaani, O of N! |
| 7 | Twist • Insert (array) | Ab aaya twist! Beech mein ek naya dost aa gaya. Toh Array mein? Sabko ek-ek seat khiskna padega. O of N, poori mehnat! |
| 8 | Insert (linked list) | Linked List mein? Bas do arrow badlo, aur naya box jud gaya. Koi shifting nahi! |
| 9 | Ek line mein yaad rakho | Toh ek line mein yaad rakho. Array: fast access, fixed size. Linked List: easy insert aur delete, dynamic size. |
| 10 | Rule of thumb | Padhna zyada hai? Toh Array. Badalna zyada hai? Toh Linked List. |
| 11 | CTA | Interview mein ye sawaal pakka aata hai! Reel save karo, aur us dost ko bhejo jo dono ko same samajhta hai. |
| 12 | Follow | Aur jaate-jaate, Pretest Passed ko follow karna mat bhoolna! |

## Rebuild
Sources are in `array-vs-linkedlist-src/` (`GEMINI_API_KEY` is read from the environment):
`tts.py` (voice per line) → `synth.py` (music + SFX) → `render.js` (frames via Playwright → `video_noaudio.mp4`) → `mix.py` → mux with ffmpeg.
