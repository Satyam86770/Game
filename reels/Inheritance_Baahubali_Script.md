# OOPs Ep 2: Inheritance (Baahubali hook), script

Target length **32–35 sec**, so the "OOPs in 30 sec" pill is true. The idea is "Beta ko papa ki har cheez free milti hai = `extends`".

## Hook clip to download (main pick)
**Baahubali: The Beginning, the scene where Kattappa recognizes Mahendra (Shivudu).** Kattappa realizes Mahendra is Amarendra Baahubali's son and puts Mahendra's foot on his own head.
- Length: **8–10 sec**, with the clip's own audio and music.
- A face must be on screen at frame 0 (Kattappa or Prabhas). Start the cut as close as possible to the moment of recognition, with no slow build-up.
- Do not use a clip that carries another creator or page watermark (a channel logo is fine).

Why this works: the scene itself is the result. Kattappa instantly recognizes the son as "Baahubali ka beta" without anyone having to tell him. That is inheritance: the son gets the father's identity and power for free.

**Backups**, if you can't find a clean Baahubali clip:
1. **Mohabbatein**, the Amitabh "Parampara, Pratishtha, Anushasan" dialogue: the tradition is passed down to every student.
2. **TMKOC**, Bapuji scolding Jethalal and Jethalal then scolding Tapu the same way: the same behaviour runs from grandfather to father to son (multilevel inheritance).

---

## Script (VO = AI voice Orus, fast and hyped Hinglish)

### 0–8s: HOOK (clip plays with its own audio, no VO)
- **Top text at frame 0:** `Beta ne 0 line likhi... phir bhi papa ki SAARI power?! 🤯`
- **Below the clip, live code that types in:**
  ```java
  class Mahendra extends Amarendra { }   // khaali!
  ```
  Then the ticks pop in one by one:
  `mahendra.talwarChalao()  ✅`
  `mahendra.rajKaro()       ✅`
- **At 3–7s, the company card (second hook):** `Interview favourite: "Inheritance kya hai?" • TCS / Infosys / Accenture`. I'll check this against interview-experience posts and show the CTC with a "~".

### 8–13s: what happened
**VO:** "Kattappa ne ek second mein pehchaan liya: ye Baahubali ka beta hai! Kyunki beta ko papa ki har cheez milti hai... bina kuch kiye. Code mein isi ko kehte hain INHERITANCE!"
- On screen: 👑 Amarendra ➜ 👦 Mahendra, with a ⚔️ talwar and 👑 raj flying from papa to beta.

### 13–22s: the code (big, in the middle of the screen)
```java
class Amarendra {                 // 👑 PAPA (parent)
    void talwarChalao() { ... }
    void rajKaro()      { ... }
}

class Mahendra extends Amarendra { // 👦 BETA (child)
    void shivlingUthao() { ... }   // apna naya kaam ✨
}
```
**VO:** "Papa ki class mein likha hai: talwar chalao, raj karo. Beta ne sirf EK word likha: extends! Bas! Papa ke saare methods beta ke paas free. Aur beta apna naya kaam bhi jod sakta hai: shivling uthao!"
- `extends` glows. The papa methods slide down into the beta box with a "FREE" tag.

### 22–28s: run it live
```java
Mahendra m = new Mahendra();
m.talwarChalao();   // ✅ chala! (papa se aaya)
m.shivlingUthao();  // ✅ chala! (apna)
```
**VO:** "Ab Mahendra ka object banao aur bolo talwar chalao... CHALA! Jabki beta ki class mein ye likha hi nahi tha!"
- Output box: `> ⚔️ Talwar chal gayi!`

### 28–32s: WOW payoff
- **Big text:** `1 word "extends" ➜ 0 copy-paste 🔥`
- **VO:** "Ek word, aur zero copy-paste! Ek line mein yaad rakho: Inheritance matlab baap ki property, beta ko free!"
- **"Ek line mein yaad rakho" card:** `Inheritance = Parent ki cheezein Child ko FREE (extends) 🏰`

### 32–35s: CTA (with the comment bait)
- **Text:** `Java mein 1 beta, 2 papa? Allowed hai ya nahi? 👇 Comment karo`
- **VO:** "Batao comment mein: Java mein ek beta, do papa, allowed hai? Follow karo, next episode: Encapsulation!"
- Show Save / Share / Follow with @pretestpassed.codes and confetti.
- The answer (no, because of the diamond problem) goes in the pinned comment or the next reel. It drives comments.

---

## Fixes from the Polymorphism data
- **Recap:** the AI voice does not repeat what the clip already showed. The voice starts on the code right after the clip ends.
- **Live code:** code runs live under the clip from second 1.
- **Company card:** it appears at 3–7s; it was missing last time.
- **Length:** 35 sec max, against 67s last time.
