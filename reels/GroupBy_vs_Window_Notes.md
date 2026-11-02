# GROUP BY vs Window Function — AI voice reel (52.4s)

Same style as the Indexing/Handshake AI reels: Orus voice, energetic beat, SFX, captions, HD animations.
Animated hook for now (GROUP BY 🆚 WINDOW FN, 4 rows collapsing → "Rows gayab!"); a movie/meme clip
can be prepended later (≤6s) and the video will still be under ~60s.

| # | Voiceover |
|---|-----------|
| w1 | SQL mein GROUP BY already hai... toh phir Window Function ki zaroorat kyun? Ye sawaal data analyst interviews mein bahut poocha jaata hai! |
| w2 | Ye rahi employees table. A aur B, HR mein. C aur D, IT mein. |
| w3 | Department-wise total salary chahiye? GROUP BY lagao. HR, sattar hazaar. IT, ek lakh das hazaar. Easy! |
| w4 | Lekin interviewer bola: mujhe har employee ka naam bhi chahiye, aur saath mein uske department ka total bhi! Ab GROUP BY fail! Kyunki usne rows ko collapse kar diya. |
| w5 | Yahan entry hoti hai Window Function ki! SUM salary OVER, PARTITION BY department. |
| w6 | Har employee ki row safe, aur saath mein department total! A aur B, sattar hazaar. C aur D, ek lakh das hazaar. |
| w7 | Ek line mein yaad rakho: GROUP BY rows ko collapse karta hai, Window Function nahi! Aise hi concepts ke liye, pretestpassed dot codes ko follow karo! |

## Suggested hook clips (send 3–6s, just the iconic line)
1. **Sholay — "Kitne aadmi the?" / "Sardar, do aadmi the"** → GROUP BY gives only the count; "kaun kaun the?" → names lost → window function keeps every row + total.
2. **"Rasode mein kaun tha?" (Kokilaben meme)** → she wants *names*, GROUP BY only knows the total.
3. **3 Idiots result notice board** → every name + rank = RANK() OVER (good for a Part 2: RANK vs DENSE_RANK).
