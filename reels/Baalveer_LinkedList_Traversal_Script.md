# Baalveer × Singly Linked List Traversal — Reel (~70s)

Hook + real Baalveer clips (original dialogue/music) alternate with animated explanation.
Voice: Gemini TTS **Puck**. Handle: **@pretestpassed.codes**.

| Time | Part | Audio / Voiceover |
|------|------|-------------------|
| 0:00 | CLIP: "Khush raho Dooba Dooba chaar" — *Baalveer ne sikhaya LINKED LIST?! 😱* | original clip |
| 0:03 | CLIP (muted) → animation: staircase DD4 (HEAD) → DD3 → DD2 → DD1 → Rani Pari 👑 → NULL | Baalveer ka ye scene yaad hai? Isme poora Singly Linked List traversal chhupa hai! Dekho, Dooba Dooba chaar ko ek sandesh mila, jo Rani Pari tak pahunchana hai. Yahan Dooba Dooba chaar hai hamara HEAD node, aur sandesh hai uska data. |
| 0:15 | CLIP: "Ab main pahunchata hoon sandesh!" — `temp = head;` | original clip |
| 0:18 | Code: `Node* temp = head; while(temp != NULL){ cout<<temp->data; temp = temp->next; }` | Ab traversal shuru! Ek pointer lo, temp, jo head pe khada hai. Jab tak temp NULL nahi hota, loop chalta rahega. Har node pe data print karo, aur temp ko next pe bhej do. |
| 0:28 | CLIP: DD4 → DD3 → DD2 "Khush raho…" — `temp = temp->next;` | original clip |
| 0:35 | temp moves DD4→DD3→DD2→DD1, output prints; "Peeche nahi ja sakte → SINGLY" | Dooba Dooba chaar se teen, teen se do, do se ek... har baar bas next pointer pakdo, aur aage badho. Peeche jaane ka koi raasta nahi, isiliye ye Singly Linked List hai! |
| 0:43 | CLIP: "Khush raho Rani Pari" — *Rani Pari = LAST NODE, next ➜ NULL* | original clip |
| 0:47 | temp → Rani Pari → NULL, while ❌ EXIT, ✅ SANDESH DELIVERED, O(N) | Aur Rani Pari hai last node! Uske next mein hai NULL. Temp jaise hi NULL hua, loop ruk gaya, aur sandesh deliver! Har node sirf ek baar visit hua, toh time complexity hai O of N. |
| 0:58 | Ek line mein yaad rakho + comment prompt + Save/Share + Follow @pretestpassed.codes | Toh ek line mein yaad rakho: Head se shuru, next pakad ke chalo, NULL pe ruk jao! Comment mein batao, agla concept kaunse Baalveer scene se samjhaun? Save karo, share karo, aur pretestpassed dot codes ko follow karna mat bhoolna! |

Note: the code uses the standard `while (temp != NULL)` loop (the old reel's `head->next != null`
skips printing the last node), and the old burned-in code overlays are covered with corrected labels.

## Rebuild (`baalveer-linkedlist-src/`)
`build_tl.py` (trim voice, timeline) → `base.py` (clips into the window) → `render.js` (overlay frames) → `mix.py` → mux with ffmpeg.
Voice clips come from `/tmp/work/tts.py` (Gemini TTS, voice Puck); music/SFX from `../array-vs-linkedlist-src/synth.py`.
