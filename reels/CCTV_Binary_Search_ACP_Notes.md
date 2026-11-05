# CCTV Binary Search: ACP Pradyuman hook (~77s)

**Concept:** binary search on time. 24 h of CCTV = 24×60×60 = 86,400 s. The safe is present until 14:37:12 and gone after,
so the answers form a monotonic ✅✅✅❌❌❌ pattern. Checking the middle each time finds the theft second in ⌈log₂ 86,400⌉ = 17 checks.
Steps (lo, hi, mid): 12:00 ✅, 18:00 ❌, 15:00 ❌, 13:30 ✅, 14:15 ✅, 14:37:30 ❌, ... check 17 = 14:37:12 ❌, the first "gone" second.

**Hook (frame 0, to keep skip rate low):**
- The user's CID clip ("Nahi nahi... Salunke, yahan kuch toh gadbad hai... zaroor koi na koi gadbad hai"), 4.2 s with its original audio.
- Cropped to exclude the Sony TV logo, shown in a red frame at (40,290).
- Top text from frame 0: "24 ghante ki CCTV... chor sirf 17 checks mein?! 🤯".
- Below the clip: a mini CCTV monitor plus a "BINARY SEARCH LIVE" card. It counts check 0→17 and shows footage 86,400s → 1s and "🎯 chor: 14:37:12", so the result is visible within 4 s.

**Body (three.js CCTV vault):**
- **Look:** green-tinted CCTV feed with REC dot, CAM 01, live timestamp, grain, scanlines and a static burst on each jump. The safe sits on a table, and a masked thief walks in at 14:36:47, grabs it at 14:37:12 and leaves.
- **Beats:**
  - Theft playback, then "24 × 60 × 60 = 86,400 s".
  - Linear scrub "check 1…/86,400 ⏳", then "ACP: sirf 17 checks ⚡" with an ACP face chip.
  - Amazon card: "Binary Search • interviewers ka favourite" with SDE-1 ~₹25 LPA (LeetCode Discuss source).
  - Timeline bar 00:00–24:00: eliminated halves are hatched, a mid marker drops, and the verdict "12:00:00 ➜ ✅ tijori hai ➡️ baad mein hui". Includes the check counter, remaining seconds and zoom range.
  - Checks 1–3 are synced to the VO; checks 4–16 run fast; check 17 lands on 14:37:12, then "🎯 CHOR: 14:37:12".
  - WOW: "86,400 seconds ⬇️ 17 CHECKS ⚡" and O(log n).
  - Ek line "✅✅✅✅❌❌❌ ➜ Binary Search", the comment prompt "Tum ise aur kahan lagaoge?", and Follow.

**Voice:** Gemini TTS Algieba (warm). VO in `cctv-binary-search-src/script.json`.

**Build:**
1. Serve the build dir: `python3 -m http.server 8765`.
2. Render frames: `node render3.js`.
3. Overlay the clip: `ffmpeg overlay clip_w.mp4 at 40:290 for t<4.2`.
4. Mix audio: `mix.py` (hook audio + VO + ducked music + SFX).
