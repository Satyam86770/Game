# EASY LeetCode problems → story reels (House Robber style)

Every problem here is tagged **Easy** on LeetCode. Inputs and outputs are the official LeetCode examples unless marked *(our example)*.
Format: hook (stakes + number) → fail case → ⏪ "Famous LeetCode ###" → simple visual solution → WOW payoff → "Ek line mein yaad rakho".

Already made: 704 Binary Search (CCTV reel), 268 Missing Number (3 Idiots reel), 141 Linked List Cycle (Ghoomar reel).

## Top 7 (make these first)

| # | LC | Problem | Story hook (frame-0 text) | Fail case (drama) | Simple idea | Payoff |
|---|---|---|---|---|---|---|
| 1 | 860 | **Lemonade Change** | "Chai wala ☕ ₹5 ki chai... customer ne ₹20 ka note diya. Chhutta hai?" | He gave away his ₹5 coins early, so a later customer gets no change and leaves angry 😡 | Keep a count of ₹5 and ₹10. For ₹20, give 10+5 first, else 5+5+5 | `[5,5,5,10,20]` ✅ / `[5,5,10,10,20]` ❌ |
| 2 | 70 | **Climbing Stairs** | "Metro ki 10 seedhiyan, 1 ya 2 step... kitne tarike? 🤯" | Counting by hand gets messy | ways(n) = ways(n-1) + ways(n-2) | **10 seedhi = 89 tarike!** *(our example)* |
| 3 | 746 | **Min Cost Climbing Stairs** | "Har seedhi pe TOLL 💸... sabse sasta raasta?" | Picking the cheapest next step is wrong | dp[i] = cost[i] + min(dp[i-1], dp[i-2]) | `[10,15,20]` ➜ **15** |
| 4 | 1 | **Two Sum** | "Shaadi ke gifts 🎁... kaunse 2 gifts ka total exactly 9?" | Checking every pair = very slow | HashMap: "kitna chahiye?" ➜ seen already? | `[2,7,11,15]`, 9 ➜ **[0,1]**, 1 pass |
| 5 | 169 | **Majority Element** | "Class monitor election 🗳️... 50% se zyada vote kisko?" | Counting every name separately | Boyer-Moore: votes cancel each other, the winner survives | `[2,2,1,1,1,2,2]` ➜ **2** |
| 6 | 136 | **Single Number** | "Party mein sab JODI mein aaye 👫... ek akela kaun?" | Using a HashMap = extra space | XOR magic: a^a = 0, so the pairs cancel | `[4,1,2,1,2]` ➜ **4**, zero extra space 🤯 |
| 7 | 121 | **Best Time to Buy and Sell Stock** | "Sharma ji ka share 📈... ek baar kharido-becho, max profit?" | Selling in a panic too early | Track the lowest price so far; profit = today − min | `[7,1,5,3,6,4]` ➜ **5** |

## More easy ideas

| LC | Problem | Story hook | Fail case | Payoff |
|---|---|---|---|---|
| 20 | Valid Parentheses | "Tiffin ke dabbe 🍱: har dhakkan sahi dabbe pe?" | Counting only open/close totals: "(]" passes ❌ | Stack ➜ `"()[]{}"` ✅ `"(]"` ❌ |
| 206 | Reverse Linked List | "Train ke dabbe ULTE jodne hain 🚆" | Breaking a link first loses the rest of the train | 3 pointers ➜ `[5,4,3,2,1]` |
| 217 | Contains Duplicate | "Ek hi Aadhaar number do baar?! 🪪" | Comparing every pair = n² | HashSet ➜ `[1,2,3,1]` ✅ |
| 242 | Valid Anagram | "'anagram' aur 'nagaram': same letters? 🔤" | Comparing position by position | Count 26 letters ➜ ✅ |
| 283 | Move Zeroes | "Zero run wale batsman peeche bhejo 🏏, order same" | Swapping randomly breaks the order | Two pointers ➜ `[1,3,12,0,0]` |
| 125 | Valid Palindrome | "Ye sentence ULTA padho to bhi same?! 'A man, a plan, a canal: Panama'" | Comparing with spaces and commas | Two pointers ➜ ✅ |
| 455 | Assign Cookies | "Bachchon ko laddoo 🍬: kitne bachche khush honge?" | Giving the biggest laddoo to the first child | Sort + greedy ➜ `g=[1,2,3], s=[1,1]` ➜ **1** |
| 1046 | Last Stone Weight | "Akhaada 🤼: do sabse bhaari pehelwan ladte hain" | Choosing random pairs | Max-heap ➜ `[2,7,4,1,8,1]` ➜ **1** |
| 88 | Merge Sorted Array | "Do sorted line ek line mein 🚶" | Merging from the front overwrites values | Fill from the back ➜ `[1,2,2,3,5,6]` |

## Tips for easy reels
- Keep to **one idea and one payoff**, **45–60 sec**. Easy problems need a short reel.
- The fail case should be what a normal person would do (lazy or greedy). Then: "Par smart coder kya karega?"
- Highlight each spoken number with an arrow or colour (House Robber v2 rule).
