# Linked List Cycle (Floyd) — Amazon SDE-1 reel (~81s)

Viral formula: the concept runs live in the hook, then the company + CTC card, then the wrong answer ❌ REJECTED, then the best answer.

- **Hook (0–5s):** a rho-shaped list 1→2→3→4→5→6→(back to 3). A yellow dot loops forever. A live terminal shows
  `while (node != null) node = node.next;` with the step counter shooting up "⏳ ∞".
  Top text: "Ye Linked List kabhi khatam nahi hoti! 😱" + "🔁 Andar ek LOOP hai!".
- **Company card:** AMAZON • SDE-1 • Fresher, the question "Linked List mein CYCLE detect karo", and a 💰 CTC ~₹44 LPA counter.
- **Normal list (ends in NULL) vs cycle list:** the back edge pulses, "∞ infinite loop!".
- **Idea 1, HashSet:** visited {1..6}, then 3 is seen again → cycle. Needs O(n) extra space; the interviewer says "Bina extra space ke karo!", then ❌ REJECTED stamp.
- **BEST: Floyd (🐢 slow +1, 🐇 fast +2).** Live race: step1 (2,3), step2 (3,5), step3 (4,3), step4 (5,5) → 💥 they meet at 5. Time O(n), space O(1).
- **Twist:** slow goes back to head, then both move +1: (2,6), (3,3) → 🎯 the cycle starts at 3. Comment CTA.
- **End:** Ek line mein yaad rakho, then Follow @pretestpassed.codes with confetti.

Voice: Gemini TTS Orus (c3 trimmed: the TTS read part of the prompt at the start). Music: 118 BPM beat ducked; SFX.

| # | Voiceover |
|---|---|
| c1 | Ye linked list kabhi khatam hi nahi hoti... kyunki iske andar ek loop hai! |
| c2 | Amazon ne SDE One, fresher interview mein yahi poocha: linked list mein cycle detect karo! Aur package? Lagbhag chawalis lakh ka CTC! |
| c3 | Normal list mein last node ka next, null hota hai. Par cycle wali list mein, last node wapas kisi purane node pe point karta hai... aur loop chalta rehta hai, infinite! |
| c4 | Pehla idea: har node ko HashSet mein daalo. Agar koi node dobara mila, toh cycle! Kaam toh karega... par O of n extra space! Interviewer bolega: bina extra space ke karo... Rejected! |
| c5 | Best solution: Floyd ka algorithm, yaani kachua aur khargosh! Do pointers lo: slow ek step chalega, aur fast do step. |
| c6 | Agar cycle nahi hai, toh fast null tak pahunch jaayega. Par agar cycle hai, toh gol track ki race jaisa, tez runner slow wale ko peeche se pakad lega! Jahan slow aur fast mile... cycle confirm! |
| c7 | Time O of n, aur space O of one. Bas do pointers! |
| c8 | Interviewer ka twist: cycle shuru kahan se hoti hai? Slow ko wapas head pe le jao, aur dono ko ek-ek step chalao. Jahan milenge, wahi cycle ka start! Comment mein batao, ye kyun kaam karta hai? |
| c9 | Ek line mein yaad rakho: slow ek step, fast do step, mile toh cycle! Aise hi interview concepts ke liye, pretestpassed dot codes ko follow karo! |

## Hook clip options (to swap into a framed window at 0–4s, like the 3 Idiots / Taarak Mehta reels)
1. **Bhool Bhulaiyaa (2007):** Chhote Pandit (Rajpal Yadav) runs through the haveli corridors and keeps ending up at the same spot. This is a literal "stuck in a loop". The live list dot loops below the clip.
2. **Bhaag Milkha Bhaag:** a track race where the leader laps the slower runner. This is Floyd's "fast catches slow" moment.
3. **Tom & Jerry:** chasing each other round and round a table or pole, until Tom finally catches Jerry when they meet.
4. **Golmaal (2006) / Dhamaal:** a chase that runs in circles around the same place.
