# Linked List Cycle — Amazon SDE-1 reel with the "Ghoomar" gorilla hook (~74s)

**Hook (0–8.5s): the user's clip**, a gorilla spinning round and round to "Ghoomar ghoomar...", ending dizzy on the floor.
Source 0.6–9.13s, cropped to 720x720 (y=270) and shown in a 1000x1000 pink frame with the original song.
The voiceover plays over the clip with the song ducked: *"Cycle wali linked list mein, end node dhoondhne ghuse...
toh bas aise hi ghoomte rahoge! Ghoomar, ghoomar! End node kabhi milega hi nahi!"*

**How the hook ties to the concept (concept running live):**
- **Top text:** "AMAZON ne poocha! 💰 ~44 LPA 😳" + "🔍 END node dhoondhne ghuse... 🌀".
- **While the gorilla climbs down the rope:** "➡️ head se list mein ENTER...". The dot walks 1→2→3.
- **While it spins:** "🌀 Ghoomar ghoomar... chakkar #k". The dot keeps looping 3→4→5→6→3, the back edge pulses, and the terminal shows
  `while(node.next!=null) node=node.next;` with "chakkar #k 🌀" and "END? ❌ kabhi nahi!".
- **When it falls dizzy (≈7.2s):** "😵 END node? 🤷 kabhi nahi mila!" with a thump SFX.

**After the hook:** Amazon card at ~8.7s, then the same body as the Amazon reel: normal vs cycle, HashSet ❌ REJECTED, Floyd race, O(n)/O(1), then Ek line + Follow.
Twist section dropped. Page source: `linked-list-cycle-ghoomar-src/reel.html`.
