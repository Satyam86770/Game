# Missing Number — 3 Idiots result-board hook (65.1s)

v2: Farhan = 2, Raju = 5; interviewer framing — UNSORTED array of distinct natural numbers 1..n with one missing; sort + iterate = O(n log n) → REJECTED; best solution = childhood maths.

Hook (0–11.1s): creator-supplied 3 Idiots clip, 7 cuts, original audio + subtitles, Rancho reveal NOT shown:
"Check from the bottom" → "You are… last" (**Farhan = 2 ✅**) → "And you?… Second last" (**Raju = 5 ✅**) →
"Rancho?" (🔍 4?) → "Not there" (**❌ Rancho (4) MISSING! 😱**) → "My heart sank".
A rank-list array strip [❓4 Rancho, 3, 1, 5 Raju, 2 Farhan] sits under the clip and lights up with each line.

Example: n = 5, array {3, 1, 5, 2}, missing 4 (= Rancho). Total 5×6/2 = 15, array sum 11, 15 − 11 = 4 → "Mil gaya Rancho!".

| # | Voiceover (Orus) |
|---|-----------|
| z1 | Rank list mein Raju mila, Farhan mila... par Rancho? Gayab! Yahi hai interview ka famous sawaal: missing number! |
| z2 | Interviewer ne poocha: ek UNSORTED array hai, jismein ek se n tak ke alag-alag natural numbers hain... par ek number missing hai! Yahan n paanch hai. Raju paanch, Farhan do... aur Rancho, chaar, missing! Kaise dhoondhoge? |
| z3 | Agar sort karke iterate karoge, toh time complexity n log n ho jaayegi... aur interviewer tumhe reject kar dega! |
| z4 | Sabse aasaan tareeka, bachpan ki maths! Ek se n tak ka sum: n into n plus one, by two. Paanch into chheh by two... pandrah! |
| z5 | Ab array ka sum nikalo: teen, ek, paanch, do... gyaarah. Pandrah minus gyaarah... chaar! Mil gaya Rancho! |
| z6 | Na sorting, na extra space. Time O of n, space O of one. Bas itna simple tha! |
| z7 | Aise hi interview tricks ke liye, pretestpassed dot codes ko follow karo! |
