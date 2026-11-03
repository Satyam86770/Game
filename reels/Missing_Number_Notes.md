# Find the Missing Number (1..n) — AI voice reel (53.4s)

Own example (changed from the reference): n = 5, array {3, 1, 5, 2}, missing **4**.
Total = 5×6/2 = 15, array sum = 11, 15 − 11 = 4. Time O(n), space O(1).
Extra twist (not in the reference): sum can overflow for huge n → use XOR; comment prompt "XOR kaise kaam karega?".

The hook is animated for now and the HTML supports a prepended clip (set HK > 0 in timeline.json; clip window 900×1125 at (90,300)).

| # | Voiceover (Orus) |
|---|-----------|
| y1 | Is array mein ek number gayab hai! Ek se paanch tak ke numbers hain... par ek missing. Interview mein poocha jaaye, toh kaise dhoondhoge? |
| y2 | Zyaadatar log pehle sort karte hain, phir loop. Par sorting matlab n log n! Interviewer ko chahiye O of n. |
| y3 | Coding bhool jao, bachpan ki maths yaad karo! Ek se n tak ka sum: n into n plus one, by two. |
| y4 | Yahan n paanch hai. Toh total sum: paanch into chheh, by two... pandrah! |
| y5 | Ab array ka sum nikalo: teen, ek, paanch, do... gyaarah! |
| y6 | Pandrah minus gyaarah... chaar! Ye raha missing number! Na sorting, na extra space. Time O of n, space O of one. |
| y7 | Interviewer ka twist: n bahut bada ho, toh sum overflow ho sakta hai! Tab XOR use karo. Comment mein batao, XOR wala logic kaise kaam karega? |
| y8 | Aise hi interview tricks ke liye, pretestpassed dot codes ko follow karo! |

## Suggested hook clips (send 3–6s)
1. **3 Idiots — "Rancho kahan hai?"** (friends searching for missing Rancho) → "Number 4 kahan hai?!"
2. **Mr. India — invisible man / "Mogambo khush hua"** → the missing element is invisible.
3. **Karan Arjun — "Mere Karan Arjun aayenge"** → the missing one "comes back" via maths.
