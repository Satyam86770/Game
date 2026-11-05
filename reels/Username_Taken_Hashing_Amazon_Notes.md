# "Username already taken" — Hashing reel (Amazon SDE-1, ~70.5s)

Built on the data-backed viral formula in CLAUDE.md: the hook is a visible RESULT that makes viewers ask "kaise?", the topic is broad (every Insta user has seen "username taken"), and the reel ends on a wow-number payoff.

- **Hook (0–10s):** a generic phone signup screen (camera emoji, no Instagram logo or UI copy).
  - "rahul" → ❌ "isn't available", then "rahul123" ❌, then "rahul.official" ❌, with a shake + buzz on each.
  - Chip: "⚡ checked in 0.001 sec".
  - Top text: "Naya username try karte hain... 🤞" → "Ye bhi TAKEN?! 😤" → "200 crore users mein check 0.001 sec mein?! 🤯", plus a counter "🔍 2,00,00,00,000 users".
- **Second hook (company card):** AMAZON • SDE-1 • Fresher, the question "HashMap andar se kaise kaam karta hai?" (listed on GfG's Amazon interview questions page),
  and 💰 CTC ~₹25 LPA (Year 1): base ₹19.17L, sign-on ₹6.47L, RSU ₹15.56L/4y (source: LeetCode Discuss, Bangalore, Feb 2025).
- **Normal way:** a linear scan of @aarav ❌ @priya ❌ @rohan ❌..., with the counter racing to 200 crore: "😵 Har signup pe 200 crore checks!" 🖥️💨🔥.
- **Hashing:** "rahul" → h() → 4 → bucket [4] (10 buckets, 2 rows) → ❌ TAKEN • 1 lookup. Then "rahul_2026" → 7 → bucket [7] is empty → ✅ AVAILABLE.
  Code card: `unordered_set<string> users; users.count("rahul"); // O(1)`.
- **WOW:** "200 CRORE users ⬇️ 1 LOOKUP ⚡", with List 200,00,00,000 checks vs Hash 1 check, and ⏱ O(1).
- **Follow-up:** h("rahul") = h("riya") = 4 → 💥 COLLISION → chaining (rahul ➜ riya ➜ ∅).
- **End:** Ek line (hash ➜ bucket ➜ O(1)), the comment prompt "Tumhara kaunsa username TAKEN tha?", and Follow @pretestpassed.codes with confetti.

Note: hash values are illustrative ("maan lo"). Instagram's real internal implementation is not public, so the reel teaches the concept, not Instagram's code.

Voice: Gemini TTS Orus. VO script in `username-taken-hashing-src/script.json`.
