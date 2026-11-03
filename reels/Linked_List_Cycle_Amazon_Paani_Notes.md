# Linked List Cycle — Amazon SDE-1 reel with the Bhool Bhulaiyaa "PAANI!" hook (~77s)

Same body as `Linked_List_Cycle_Amazon_Notes.md`. The twist section is dropped to keep the reel shorter.

**Hook (0–7s): the user's clip**, Akshay Kumar & Rajpal Yadav "Paani" scene from Bhool Bhulaiyaa (2007).
Cuts from the source: 0–1.45 (warning), 3.4–3.9 ("PAANI!"), 3.9–6.0 (jump), 7.45–9.0 ("PAANI!" + jump), 10.6–12.0 ("PAANI!" + jump).
These are cropped to 720x720 and shown in a 1000x1000 framed window, with the original audio.

**How the hook ties to the concept (concept running live):**
- **Top text:** "AMAZON ne poocha! 💰 ~44 LPA 😳" + "🔁 Ye LOOP kabhi khatam nahi hota!".
- **On every "PAANI!":** the pill `💧 "PAANI!" = node.next` appears, then `🦘 Same jump DOBARA! #k 🔁`.
- **Under the clip:** a mini cycle list 1→2→3→4→5→6→3. The dot runs one full loop per "PAANI!". A "LOOP LIVE" terminal
  `while(node!=null) node=node.next;` shows "loop #k" and "null? ❌ kabhi nahi!".

**VO c1 (new, trimmed):** "Ye loop kabhi khatam hi nahi hota... bilkul cycle wali linked list ki tarah!" The rest is c2–c7 and c9 from the Amazon reel.
