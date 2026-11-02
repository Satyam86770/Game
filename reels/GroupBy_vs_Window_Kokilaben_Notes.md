# GROUP BY vs Window Function — "Rasode mein kaun tha?" hook (56s)

Hook (0–5.03s): creator-supplied Yashraj Mukhate remix clip (credit watermark kept), 3 cuts:
"…tab rasode mein kaun tha?" (8.3–9.9) → "Main thi? Tum thi? Kaun tha?" (14.6–16.1) → "KAUN THA?!" (17.3–19.25),
with overlays: 🎤 Interviewer: "Rows mein KAUN tha?" → GROUP BY: "Bas total pata hai... 180" 🤷 → 😱 GROUP BY ke paas NAAM nahi!

Own example data (not the reference creator's): IPL match — Rohit 40 & Surya 60 (MI), Dhoni 30 & Jadeja 50 (CSK).
GROUP BY team → MI 100, CSK 80. Window: SUM(runs) OVER (PARTITION BY team) AS team_total → every player row kept.

| # | Voiceover (Orus) |
|---|-----------|
| x1 | Kokilaben ko naam chahiye... aur GROUP BY sirf total batata hai! Isiliye aaya Window Function. Data analyst interviews ka favourite sawaal! |
| x2 | Ye rahi IPL match ki table. Rohit aur Surya, Mumbai mein. Dhoni aur Jadeja, Chennai mein. |
| x3 | Team-wise total runs chahiye? GROUP BY lagao. Mumbai, sau runs. Chennai, assi runs. Easy! |
| x4 | Lekin interviewer bola: mujhe har player ka naam bhi chahiye, aur saath mein uski team ka total bhi! Ab GROUP BY fail! Kyunki usne rows ko collapse kar diya. |
| x5 | Yahan entry hoti hai Window Function ki! SUM runs OVER, PARTITION BY team. |
| x6 | Har player ki row safe, aur saath mein team total! Rohit aur Surya, sau. Dhoni aur Jadeja, assi. |
| x7 | Ek line mein yaad rakho: GROUP BY rows ko collapse karta hai, Window Function nahi! Aise hi concepts ke liye, pretestpassed dot codes ko follow karo! |
