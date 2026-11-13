# Notes for Claude

## Instagram channel (use in every reel/video)
- Handle: **@pretestpassed.codes**
- Link: https://www.instagram.com/pretestpassed.codes
- Always use this exact handle for the on-screen watermark and in the end-of-video
  follow CTA (profile card / "Follow karna mat bhoolna"). Do not use `@PretestPassed`.

## Reel style
- Reference style: dark gradient, top progress bar, handle watermark, step pills,
  real-life analogy, "Ek line mein yaad rakho", Save/Share/Follow CTA with confetti.
- Voice: see "DEFAULT VOICE" below (ElevenLabs **Bunty**). Older Puck/Orus voices are retired.
- Example build: `reels/array-vs-linkedlist-src/`.

## Watermark: keep it minimal (user rule)
- The user REJECTED the tiled and moving anti-copy watermark ("video bekar lag rha"). Do not add it.
  Only the small top "@pretestpassed.codes" handle stays.

## Old voice (RETIRED Nov 13 2026, kept only for re-editing old reels)
- Old Gemini setup, do NOT use for new reels:
  - Model: **gemini-2.5-flash-preview-tts only**, voice **Orus**.
  - Prompt prefix: "Say in a fast, high-energy, hyped, fun young Indian Hinglish Instagram tech reel creator voice,
    punchy with dramatic pauses (pronounce English tech words like SQL, index, pointer, binary search clearly): ".
  - Post-processing: silence-trim, then **atempo=1.07**, then loudnorm I=-16.
- Do not mix in 3.1 or 3.8 model lines. If the 2.5 quota is exhausted (10/day, resets 08:00 UTC), wait for the reset.

## VIRAL HOOK FORMULA (mandatory for every new reel — user rule, data-backed)
Public plays (Nov 2026):

| Reel | Plays |
|---|---|
| Binary Search game (24s, real people) | 2.9M |
| Google SDE advice | 666K |
| **Indexing AI-voice reel** (`Indexing_SQL_AI_Voice_Reel.mp4`, 71s) | **245K** |
| Projects advice (face) | 174K |
| LL traversal | 7.1K |
| Auth vs Authz | 3K |
| Cycle detection | 3.2K |
| GROUP BY vs Window (Kokilaben) | 961 |
| 3-way handshake | 199 |
| HashMap / username-taken 3D (83s, no human or movie clip, Insta-logo first frame) | 309 (day 1) |

The viral Indexing reel used the SAME template, AI voice (Orus) and length as the flops, so those are NOT the cause.
What actually differed:
1. **The hook shows a visible RESULT that triggers "ye itna fast/kaise?!"** The scene literally IS the outcome
   (Robot finds 1 Bhajan Lal among lakhs → query runs live 12 rows → 1 row • 0.003 sec).
   Flops used a joke or metaphor that needs the topic already known ("Sorry = SYN", "Ghoomar = cycle", "Paani = node.next").
   If a label is needed to make the clip mean the concept, reject the clip.
2. **Broad curiosity topic.** Pick everyday "how does X work?" questions (Google search speed, UPI double-tap,
   WhatsApp ticks, feed loading) where the concept is the ANSWER. Do not lead with syllabus topics
   (handshake, cycle detection, GROUP BY) as the hook.
3. **End with a WOW number payoff** ("10 lakh rows → sirf 20 steps!") that people share.
4. **A recognizable clip that plays long enough with its own audio** (~8–12s of iconic dialogue), with the live concept overlay below it.
5. **Company + CTC card is the SECOND hook (≈3–8s), never the first.** Use reported CTC with "~" and a source.
6. **Keep it focused: one idea and one payoff.** Aim for 30–60s, and drop detours (extra approaches, twists) unless essential.
7. **Posting:** at most 1 reel per day, never 2 the same day. Never use clips carrying another creator's watermark.
8. **Every reel that went viral had a human face or an iconic movie clip in the very first second**
   (binary-search duo, Google office, Rajinikanth, creator face). Pure animation reels (Auth, HashMap 3D) flopped even with a good hook.
   Open on a face or iconic clip, not on a logo or animation. Use Instagram Trial Reels to test 2–3 hook variants before a full post.
9. **Owner insights (vidIQ, connected Nov 2026): SKIP RATE is the gate.**

   | Reel | Plays | Skip rate | Avg watch |
   |---|---|---|---|
   | Indexing | 246K | **30%** | 19.9s (28%); 3,002 shares; 4,294 saves |
   | LL traversal | 7.2K | 42% | |
   | Cycle | 3.4K | 55% | |
   | GROUP BY | 990 | 69% | |
   | Auth | 3K | 79% | |
   | HashMap 3D | 520 | **77%** | 8.5s (10%); 0 shares |
   | Missing number (3 Idiots) | 3.1K (day 1) | 52% | 10.5s (19%); frame 0 = back of a head + label "Rank List = ARRAY" |
   | Polymorphism (Ninja Hattori, 67s) | 5.3K (day 1) | 42% | 10.8s (16%); 32 shares, 25 saves; no CTC card; AI recap of the clip after 8s; "OOPs in 30 sec" pill on a 67s reel |
   | House Robber LC198 (3D night-robbery story, 80s) | 4.1K (first hours) | 39% | **26.5s (33%)**, best avg watch so far; 42 saves; greedy robber gets caught, then the DP solution. Story format = keep. |

   Frame-0 text must be a curiosity QUESTION with a number ("Lakhs mein se 1... 1 second mein?! 🤯"), never a concept label ("Rank List = ARRAY").
   Target skip rate < 35%. The HashMap reel spent 0–4.5s on a logo and typing before the "taken" result.
   The payoff text and a face/iconic clip must be on screen at FRAME 0 (no intro, no logo animation).
   Check insights with vidiq_instagram_owner_insights (platformAccountId 39687719547542292).
10. **Self-check before rendering:** in the first 2s, does a non-coder see a result and ask "kaise?"? If not, redo the hook.

## DEFAULT VOICE FOR ALL REELS (user rule, Nov 13 2026: "ye ai voice hamesa yaad rakhna")
- ALWAYS use the ElevenLabs Voice Library voice **"Bunty - Punchy, Crisp and Reel King"**
  (voice_id `FZkK3TvQ0pjyDmT8fzIW`, model `eleven_multilingual_v2`). It matched the user's reference reel 10/10.
- Reference sample: `reels/voice/Bunty_Reference_Sample.mp3` (Missing Number reel voiceover).
- Write scripts in Devanagari with English tech words in Latin (e.g. "इस array में एक number missing है").
- The user is on the ElevenLabs FREE plan, so the API refuses library voices (402). Workflow:
  1. Write the script to `reels/<Topic>_Bunty_Script.txt`.
  2. Ask the user to generate it on elevenlabs.io (Text to Speech, voice Bunty, Multilingual v2) and attach the MP3.
  3. Use the attached MP3 as one VO track; get word timestamps with faster-whisper (language='en' + romanized
     initial_prompt) for captions and animation keys; fix caption spellings by hand.
  If the user upgrades to a paid plan, call the API directly (api.elevenlabs.io, header xi-api-key: `proxy-injected`).
- No background music in these reels (user adds music); keep the sound effects.
- Fallback only if the user explicitly says so: ElevenLabs premade Liam (`TX3LPaxmHKxFdv7VOQHJ`).
