# "Username already taken": 3D version (three.js), ~76.5s

v2 of the hashing reel. It follows the user's 1M-view reference (3D low-poly scenes, small top-left labels, warm narrator).

**Voice: Gemini TTS Algieba.** In an 8-voice audition against the reference narrator (Orus, Achird, Sadachbia, Umbriel, Algieba, Iapetus, Puck, Zubenelgenubi), Gemini rated Algieba 10/10 for pleasantness and closeness. The prompt asks for a warm, friendly, smooth storyteller who never shouts.

**Opening VO:** "Instagram pe naya ID banane ke liye username daala... aur Instagram bola: already taken! Doosra try kiya... ye bhi taken! Par socho, Instagram pe do sau crore se bhi zyada users hain. Itni jaldi pata kaise chala?"

**Scenes:**
- **Intro:** an Instagram-style logo tile (gradient rounded square with camera glyph) spins in.
- **Hook:** a 3D phone shows a signup screen. "rahul" → ❌ isn't available, then "rahul123" → ❌. The camera pulls back to reveal 2,600 capsule people receding into fog, with the counter "👥 2,00,00,00,000+ users".
- **Company card:** AMAZON SDE-1 card with the CTC (~₹25 LPA Yr 1, source: LeetCode Discuss Feb 2025).
- **Linear scan:** a spotlight checks @aarav, @priya and @rohan one by one (❌ tags). The camera then rises over an endless line while the counter climbs to 200 crore.
- **Hashing:**
  - The "rahul" block rides a belt into the purple h( ) machine (spinning gears).
  - A "4" coin flies to locker 4 in a 2×5 locker wall. The door opens on "rahul", so it is ❌ TAKEN.
  - "rahul_26" gives 7. Locker 7 is empty, so it is ✅ AVAILABLE.
  - C++ `unordered_set` card.
- **Wow:** the crowd plus "200 CRORE users → 1 LOOKUP ⚡" (List 200,00,00,000 checks vs Hash 1 check).
- **Collision:** locker 4 holds rahul ↓ riya (chaining).
- **End:** CTA "Ek line" (hash • bucket • O(1)), the comment prompt "Tumhara kaunsa username TAKEN tha?", then Follow with confetti.

**Rendering:** three.js 0.160, served over a local HTTP server (`python3 -m http.server 8765` in the build dir) and rendered by Playwright Chromium (SwiftShader WebGL) with `render3.js`.
