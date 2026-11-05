# CCTV Binary Search: array version (v2, ~80s, Orus voice)

Change requested by the user: explain the search as an ARRAY.
- arr[i] = the i-th second's frame. arr[0] = 0 s (00:00:00), arr[86,400] = 86,400 s (24:00), so n = 86,401.
- mid = (0 + 86,400) / 2 = 43,200 → 12:00:00, and the safe is there ✅.
  So indices 0..mid are never looked at, and **low = mid + 1**.
- When the safe is gone ❌, **high = mid**.

To keep "17 checks" accurate with this exact rule (low = mid + 1 / high = mid, loop while low < high), the theft time is **14:37:13** (index 52,633).
That takes exactly 17 checks, and the 17th mid is 14:37:13, where low = high = 52,633.
With 14:37:12 the same rule needs only 16 checks. ⌈log₂ 86,401⌉ = 17 is the worst case.

Steps: 12:00 ✅ → 18:00 ❌ → 15:00 ❌ → 13:30 ✅ → 14:15 ✅ → 14:37:30 ❌ → ... → 14:37:12 ✅ → 14:37:14 ❌ → 14:37:13 ❌ (low = high).

**Visual:** under the CCTV monitor, 7 array cells [low] … [mid-1] [MID] [mid+1] … [high], each with its index and time, plus low/mid/high pointers.
- The MID cell turns green or red.
- The eliminated half fades.
- A verdict line shows "arr[43,200] = 12:00:00 ➜ ✅ tijori hai ➜ low = mid+1".
- Also shown: the check counter, "bacha array" size, and a global 24 h bar.

**Complexity scene:** "Har check: array ÷ 2" (86,401 → 43,200 → … → 1, 17 times), giving O(log n). It is compared with "Ek-ek index: 86,400 checks = O(n)".

**VO:** Gemini TTS **Orus**, the same voice as the viral Indexing reel, with the hype prompt. The user asked for it. Script: `script_all.json`.
- c1 and c2 were made with gemini-3.1.
- c3–c8 were made with gemini-3.8-flash(-lite) because the daily quota was exhausted. Those models read the prompt aloud first, so the first ~4–5 s were trimmed.
