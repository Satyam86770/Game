# Story-format LeetCode reels (House Robber style)

**Why this format works.** House Robber (LC 198) had a 39% skip rate and **26.5s average watch (33%)**, the best watch time on the channel so far (Indexing was 19.9s), plus 42 saves in the first hours.

**The formula:**
1. **Hook:** frame 0 shows the result or the stakes as a question with a number.
2. **Rule:** a "shart" card states the constraint and what happens if you break it.
3. **Fail case:** a greedy or lazy attempt fails dramatically (police, alarm, crash). This is the curiosity peak.
4. **Reveal:** ⏪ rewind, then "Famous LeetCode ###" with the logo.
5. **Solution:** a visual table, pointer or grid filling live, with arrows and colours on each spoken number.
6. **Payoff:** a WOW number ("₹12 Crore bina pakde", "92 tarike!"), then "Ek line mein yaad rakho" and the CTA.

LeetCode numbers and difficulties are as listed on leetcode.com. Example inputs and outputs are the problems' official examples unless noted.

## Top 7 to make first

| # | LC | Problem (difficulty) | Story hook (frame-0 text) | Fail case (the drama) | Solution visual | WOW payoff |
|---|---|---|---|---|---|---|
| 1 | 213 | **House Robber II** (Medium) | "Chor WAPAS aaya... is baar colony GOL hai! 🔁" (first and last house are neighbours) | Robs the 1st and the last house, which are neighbours on the ring, so the alarm goes off again 🚨 | Run 198 twice: skip the first house / skip the last house, then take the max | Sequel to the viral reel; viewers already know the story |
| 2 | 322 | **Coin Change** (Medium) | "Kirana wale ko ₹6 chhutta dena hai... sikke ₹1, ₹3, ₹4. Kam se kam kitne?" | Greedy grabs the biggest coin: 4+1+1 = **3 sikke ❌**. Smart answer: 3+3 = **2 ✅** | dp[amount] table fills from 0 to 6 | "Bada sikka pehle = galat! DP = sahi" |
| 3 | 70 | **Climbing Stairs** (Easy) | "Metro ki 10 seedhiyan, 1 ya 2 step... kitne tarike? 🤯" | Counting by hand gets messy halfway | Fibonacci boxes: ways(n) = ways(n-1) + ways(n-2) | **10 seedhi = 89 tarike!** |
| 4 | 42 | **Trapping Rain Water** (Hard) | "Mumbai ki baarish 🌧️... in chhaton par kitna paani rukega?" (realistic 3D rain) | "Bas sabse oonchi building dekho" gives the wrong answer | Two pointers with left-max / right-max; water fills live | `[0,1,0,2,1,0,1,3,2,1,2,1]` ➜ **6 units** |
| 5 | 994 | **Rotting Oranges** (Medium) | "Peti mein EK sada santra 🍊... poori peti kitne minute mein sad jaayegi?" | One-by-one checking is very slow | Multi-source BFS, with the rot spreading each minute | **4 minute** (official example) |
| 6 | 72 | **Edit Distance** (Medium) | "Autocorrect ko kaise pata 'helo' = 'hello'? 📱" (broad curiosity) | Letter-by-letter matching gives the wrong count | dp grid fill with insert / delete / replace arrows | "horse ➜ ros = sirf 3 operations" |
| 7 | 743 | **Network Delay Time** (Dijkstra, Medium) | "Google Maps sabse FAST raasta kaise dhundhta hai? 🗺️" | Picking the nearest road first gets stuck in traffic | Dijkstra with a priority queue; the city map lights up | Shortest time in the city |

## More ideas (same format)

| LC | Problem (difficulty) | Story hook | Fail case | Payoff |
|---|---|---|---|---|
| 121 | Best Time to Buy and Sell Stock (Easy) | "Sharma ji ka share: 7 din, ek baar kharido-becho 📈" | Buys at the day-2 low but sells too early / in panic | `[7,1,5,3,6,4]` ➜ **profit 5** |
| 1 | Two Sum (Easy) | "Shaadi ke 2 gift jinka total exactly ₹9,000 🎁" | Checking every pair = n² (very slow) | HashMap ➜ **1 pass** |
| 55 | Jump Game (Medium) | "Bandar ped se ped 🐒... aakhri ped tak pahunchega?" | The trap tree with jump 0 | `[3,2,1,0,4]` ➜ ❌ / `[2,3,1,1,4]` ➜ ✅ |
| 875 | Koko Eating Bananas (Medium) | "Bandar ko 8 ghante mein saare kele khaane hain 🍌" | Eats too fast and gets sick / too slow and the guard comes back | Binary search on the answer ➜ **speed 4** |
| 11 | Container With Most Water (Medium) | "Do deewaron ke beech sabse badi paani tanki 💧" | Picking only the two tallest walls | Two pointers ➜ **49** |
| 53 | Maximum Subarray / Kadane (Medium) | "Startup ke 9 mahine: profit-loss... best lagatar stretch?" | Including every loss month | **6** (official example) |
| 146 | LRU Cache (Medium) | "Fridge mein sirf 3 dabbon ki jagah 🥡" | Throwing away the item used most recently | Least recently used goes out |
| 207 | Course Schedule (Medium) | "Degree poori hogi? DSA se pehle C, C se pehle DSA 😵" | Cycle = stuck forever | Topological sort / cycle ➜ ❌ |
| 735 | Asteroid Collision (Medium) | "Space mein asteroids takraaye ☄️... kaun bachega?" | Moving in the same direction = no collision | Stack ➜ survivors |
| 134 | Gas Station (Medium) | "Gol road trip ⛽... kahan se start karein ki petrol khatam na ho?" | Starting at a random pump runs out of petrol | Greedy ➜ **start index 3** |
| 135 | Candy (Hard) | "Teacher toffee baant rahi 🍬: zyada marks = padosi se zyada toffee" | Giving everyone the same | Two passes ➜ min toffees |
| 62 | Unique Paths (Medium) | "Delivery boy 3×7 gali wale shehar mein 🛵... kitne raste?" | Drawing every path by hand | **28 raste** |
| 239 | Sliding Window Maximum (Hard) | "Highway camera 📸: har 3 km ki max speed" | Re-checking every window = slow | Deque ➜ O(n) |
| 416 | Partition Equal Subset Sum (Medium) | "Do bhai, property barabar baant sakte? 🏠" | Splitting greedily | `[1,5,11,5]` ➜ ✅ 11 / 11 |
| 51 | N-Queens (Hard) | "8 raniyan 👑, koi kisi ko na maare... kitne tarike?" | Placing queens row by row without checking gets stuck | **92 tarike!** |

## Production notes
- Keep **one idea and one payoff**. Hook 0–8s, fail case by ~18s, LeetCode reveal by ~25s, done in 60–80s.
- On the table or grid step, every spoken number gets an arrow or colour (the user rule from House Robber v2).
- Explain the dp meaning ("dp[i] = ab tak ka best") before filling the table (House Robber v3).
- Optional test: put a 2–3s face intro before the animation and compare skip rate with Trial Reels.
- At most 1 reel per day. Use the Indexing voice (Orus, gemini-2.5, atempo 1.07).
