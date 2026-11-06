# OOPs in 30 sec, Ep 1: Polymorphism (Ninja Hattori), ~60s

- **Hook (frame 0):** the user's Ninja Hattori clip ("Look badalne ki ninja technique... nin nin").
  - Cuts used: 0–4.0 (face masks / papa), 7.6–9.25 ("Hello, mummy yahan hai!"), 11.0–13.2 ("Hello doston!" as Kenichi).
  - On top: "🥷 OOPs in 30 sec • Ep 1" and the title "Ek Hattori... 3 roop?! 🤯".
  - Under the clip, role chips 👨 Papa • 👩 Mummy • 👦 Kenichi light up as each form appears.
- **VO (Gemini TTS Orus, the viral Indexing voice):**
  1. "Hattori ek hi hai... isi ko kehte hain Polymorphism!"
  2. "Poly = many, morph = forms".
  3. The code section, written around the user's idea:
     ```java
     void ninjaHattoriKaRoop(Papa p)    { print("Papa aa gaye!"); }
     void ninjaHattoriKaRoop(Mummy m)   { print("Mummy yahan hai!"); }
     void ninjaHattoriKaRoop(Kenichi k) { print("Hello dosto!"); }
     ```
- **Call and output:**
  - `ninjaHattoriKaRoop(mummy);` → the VO says "toh print hua:" → the **cartoon clip itself plays** with "Hello, mummy yahan hai!", and the output line "> Mummy yahan hai!" appears.
  - `ninjaHattoriKaRoop(kenichi);` → the "Hello doston!" clip plays, and "> Hello dosto!" appears.
- **Concept:** same name, different parameter, different work. That is **Method Overloading = Compile-time Polymorphism**. The bonus chip teases Overriding (runtime) as the next reel.
- **End:** "Ek line: Ek naam, kai roop!", the comment prompt, and "Next: Ep 2 ➜ Inheritance".
- **v2 (user feedback):**
  - The watermark was removed.
  - All VO is now gemini-2.5 Orus with the Indexing prompt and atempo 1.07, so it matches the viral Indexing voice.
  - The code walk-through is step by step: the call `ninjaHattoriKaRoop(mummy)` → "🔎 parameter mummy ➜ Mummy type" → the matching overload glows "✅ match!" → its print line → the cartoon clip "Hello, mummy yahan hai!" → the output "> Mummy yahan hai!". The same flow repeats for kenichi → "Hello doston!".
  - Added a real overloading example: `int add(int,int)` → add(1,2) ➜ 3, and `String add(String,String)` → add("ninja","hattori") ➜ "ninjahattori".
  - Length is ~78s.
