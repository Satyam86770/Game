# Username taken: "backend HashMap" explanation (3D, ~90.8s)

v3, restructured as the user asked:
1. **Not line by line:** "Par Instagram har username ko line by line check nahi karta! Warna do sau crore users ek-ek karke... bahut zyada time lag jaata!"
   - Visual: spotlight scan, then a ❌ "Line-by-line? NAHI!" stamp and "⏳ 200 crore checks = bahut time!".
2. **Backend storage:** "Backend mein sabhi usernames, ek HashMap jaisi table mein pehle se rakhe hote hain... rahul ka hash saat, rohit ka hash do, priya ka hash chaar..."
   - Visual: a "🗄️ Backend HashMap" locker wall (2×5) with the doors open. Name tags fly from the h( ) machine into their buckets: rahul→7, rohit→2, priya→4, then aarav→9, neha→0, kavya→3, rohan→8.
   - Chips show "rahul ➜ 7 • rohit ➜ 2 • priya ➜ 4 • + baaki 200 crore usernames…", then the doors close.
3. **Runtime lookup:** "Naya user aaya... type kiya rahul. Instagram usi waqt, run time pe, rahul ka hash nikaalta hai... saat! Seedha bucket saat check kiya... rahul pehle se present hai! Toh, already taken!"
   - Visual: the "rahul" block goes into the machine, a "⚡ run time: h("rahul") = 7" chip appears, and the coin flies to bucket 7. The door opens on rahul: ❌ already taken.
4. **Available case:** "rahul twenty six → hash paanch → bucket paanch khaali → available" (✅, green ring).
5. **Unchanged:** the hook (Instagram logo, 200 crore+), the Amazon card (~₹25 LPA Yr 1), the WOW (1 lookup, O(1)), the collision (now h("rahul") = h("riya") = 7, chained in bucket 7), and the CTA.

**Honesty note:** the VO says "HashMap *jaisi* table" because Instagram's internal implementation is not public. The reel teaches the concept.

Voice: Gemini TTS Algieba (n3–n6 new; u1, u2, u6, u7, u8 reused from v2). Build: three.js, `render3.js` (serve the build dir on :8765 first).
