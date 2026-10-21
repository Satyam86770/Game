---
name: "raw-to-final"
description: "Turn raw talking-head takes (or an already-merged master) into a finished reel: cut retakes with zero-gap joins, then add voice-synced motion graphics, logos, calendar/globe/timer visuals, news cards, B-roll, SFX, music and grade."
---

# Raw to final 2

Two phases in one run:
- **Phase A (merge):** cut out repeated/failed takes and join the final take of every sentence into one clean master. Only cut, split, delete and merge here. **Skip Phase A** when the user gives one already cut and merged video; it is the master.
- **Phase B (edit):** edit the master into a finished video with motion graphics, B-roll, self-made animation clips and images, news cards, logos, sound design and colour, all **synced to the words actually spoken** and factually correct.

The core pipeline runs locally with **FFmpeg** and **Python** (Pillow, NumPy, OpenCV, onnxruntime, scipy). **Use anything you can download or install** whenever it helps: pip/npm packages, GitHub repos and release files, model weights, fonts, CLIs. First check what is reachable from this workspace (a quick `curl -sS -o /dev/null -w '%{http_code}'` per host, `pip download`/`npm view` for a package). If a source is blocked because it needs permission or a sign-in the user can give (a GitHub repo that needs access via `add_repo`, a connector that needs connecting or re-auth, a site behind a login, a tool approval), **ask the user**: they are happy to grant access or sign in. Only when a source is truly unreachable (network allowlist, no way to grant it) say so in one line and use the next option. Never pretend a download or install worked. Never overwrite or modify the user's original files; always work on copies.

Work in a task list. Narrate little. Report blockers immediately. Reply in the user's language (this user often writes Hindi/Hinglish; answer in the same).

## The rules learned from past edits (read first)

1. **Sync to the real voice, never to the script.** The speaker often says something different from the written script (different wording, extra lines, lines skipped). Always transcribe the actual audio and time every graphic from those spoken words. Graphics timed to a script drift by seconds after the first 20–30 s; that was the main complaint.
2. **Show only what is said.** Every card, tag or animation must match a line she actually speaks, at the moment she speaks it. Never add cards for script lines she didn't say (e.g. company names or claims from the plan doc that never appear in the audio). If something useful was left unsaid, mention it to the user instead of showing it.
3. **No burned-in captions/transcript by default.** This user prefers no running captions. Use big on-screen text cards for key words instead. Add a caption track only if the user asks for one.
4. **Big text after the intro.** On a 1080-wide frame, full-frame text cards use about 70–120 px type (never the 30–45 px chip size). Use both the **top zone** (above the head) and the **chest zone** (below the chin, above the bottom safe area), never over the face.
5. **Crop, zoom and colour are allowed** on the raw footage; never change what she says or its order.
6. **Use the user's B-roll where it fits**, and **make your own short animation clips and images** for concept lines (details in B4d and B4e).
7. **Verify before every full render**: stills at every event, plus Whisper spot-checks of key timings (B7).
8. **Show it, don't just type it.** When she says a date, a place, a duration, a company/app, a number or a time of day, turn it into a small animated visual (calendar, globe/map zoom with a pin, running timer/clock, official logo card, counter, day-cycle), not a plain text chip. Text alone is for words that have no natural picture. Full catalogue in B4f.
9. **Zero-gap joins.** The user wants no audible gap or stutter between kept sentences: no pause longer than ~0.1 s at a join, no half-word of the next take left at the end of a cut, no word said twice across a join (A2 step 6b).

---

## 0. Inputs and setup

1. **Get the footage.** Use attached files. A Windows/Mac path the user types (e.g. `C:\Users\...`) is on their computer: use the device bridge if it is connected, otherwise ask them to attach the file. Never pretend to have a file. Copy every input into the project before working.
2. **Confirm inputs:**
   - Clip order. The user says which clip is 1st, 2nd, ... (often by duration). Match with ffprobe durations. Never order by filename or creation time. A single clip that contains retakes inside it is normal; the same rules apply within it.
   - Reference script (optional). It may be a Google Doc link with a `?tab=t.xxxx` id: read it with the Google Docs connector; the result is large JSON, so save it and extract only that tab with Python (walk `tabs` / `childTabs`, match `tabProperties.tabId`, join `textRun.content` of paragraphs and table cells). Use the script for code, data and intent, never for timing (rule 1).
   - Platform / aspect (9:16 Reel/Short or 16:9). Infer from the footage if obvious; ask only if not.
   - Optional reference videos, B-roll clips, images, logo, brand colours, handle (e.g. @channel).
3. **Toolchain check:** `ffmpeg -version`, `ffprobe -version`, `python3 -c "import PIL, numpy, cv2, scipy, onnxruntime"`, and `ffmpeg -hide_banner -filters` for the filters you need (`overlay`, `xfade`, `sidechaincompress`, `loudnorm`, `zscale`/`tonemap`). If something is missing, install it (`pip install --break-system-packages <pkg>`, `npm install`, a GitHub release or repo, a static build); if every route is blocked, say so in one line and continue with what exists. List installed fonts with `fc-list` (Inter Display, Lora, DejaVu Sans Mono and Noto Color Emoji are usually present) and copy the ones you use into `assets/other/`.
4. **Smoke test:** render 3 s (colour source + one Pillow PNG overlay + a sine tone) to MP4, verify with ffprobe, delete it.
5. **Project layout:**

```text
videos/<project>/
├── assets/source/      raw clips (copies)
├── assets/reference/   reference videos or REFERENCES.md
├── assets/broll/       user B-roll clips, images, screenshots (copies)
├── assets/news/        NEWS.md (sources, excerpts, dates), article screenshots
├── assets/logos/       official logo files + LOGOS.md (where each came from)
├── assets/other/       fonts, map data, synthesised music and SFX
├── ASSETS.md           every external or generated asset, its source and licence
├── merge/              Phase A: wavs, silence maps, transcripts, edl.json, segments, master
├── BRIEF.md            goal, audience, platform, must-haves
├── STYLE.md            style analysis from references
├── STORYBOARD.md       timed plan of every visual and its reason
├── build/              transcripts, words.json, times.py, edit.py, audio.py, mix.sh, stills/
└── renders/            previews and versioned finals (name_v1.mp4, name_v2.mp4, ...)
```

---

## Phase A: merge the final takes

### A1. Take-selection rules (core logic)
1. For each sentence, find every attempt across all clips.
2. The **final take** is the last attempt that is followed by the next new sentence (or the end of the clip) and is not attempted again later. If a later clip starts by repeating a sentence, the later version wins.
3. Drop false starts, half sentences, breaths, whispers, and anything said between takes ("ek baar aur", "ruko").
4. If a line is rephrased, the last version still wins. Flag it so the user can swap.
5. If no single take is complete, join the first half of the last full attempt to a later take that completes the ending, cutting at a word boundary. Flag it.
6. Keep a sentence spoken only once as it is. When listing it to the user, write it out in full (no "…").
7. Keep intentional silences that belong to the content (e.g. a 5-second "find the bug" wait); they are not gaps to cut.

### A2. Workflow
1. **Probe** each clip: codec, profile, pix_fmt, color_transfer/primaries (iPhone is often HEVC Main10 HLG BT.2020), fps (29.97 vs 30), rotation side-data, keyframe interval.
2. **Audio:** `ffmpeg -i clip -ac 1 -ar 16000 merge/vN.wav`.
3. **Silence map:** RMS dB in 10 ms frames, smooth over 5 frames, threshold = 12th percentile + 9 dB, runs ≥150 ms = gaps between utterances. Inside long utterances find micro-gaps (≥60 ms below -50 dB; -38/-32 dB for word boundaries).
4. **Transcribe** each utterance with the Whisper setup in **T1** below (Hindi/Hinglish). Transcribe each silence-bounded utterance separately with ±0.1 s padding to avoid hallucinations.
5. **EDL** (`merge/edl.json`): one (clip, start, end, text) per kept sentence in script order. Pad ~0.12 s before and ~0.18 s after speech, never into a neighbouring utterance.
6. **Verify before encoding:** render an audio-only concat of the EDL and re-transcribe each piece. The joined text must read as one clean script: no repeated or missing lines. Compare against the reference script line by line. **Whisper hides repeats on long windows** (it collapses or hallucinates them), so check every sentence of more than ~4 s in two halves, and transcribe each join on its own (~1.2 s before to ~1.0 s after).
6b. **Join audit (rule 9).** For every join, look at the 10 ms RMS dB profile ±0.4 s around it and fix these three faults:
   - **Leaked onset of the next word.** A cut that ends mid-way into the next word of the old take leaves a stub ("…nahi karta *bal*" + "*balki* users…", "follow kar lo *and*" + "*And* comments…"). Find the dip between the last kept word and the next onset (the frame where dB rises sharply, e.g. -50 → -25) and end the segment inside that dip, ~10–30 ms before the onset. Prove it by decoding `[seg_start, new_end]` (the next word must be absent) and the joined pair (the word must appear exactly once).
   - **Leftover gap.** Measure silence below -50 dB on both sides of each join (trailing silence of segment i plus leading silence of segment i+1; breaths at -50…-60 dB count as gap). If the total is more than ~0.12 s, trim the end so ≤0.04 s of trailing silence remains and the start so ≤0.03 s of leading silence remains. Never trim into a soft consonant onset (ph/s/h): check the dB curve and re-transcribe the join afterwards.
   - **Double word.** If the same word ends one take and starts the next ("and" + "And", "balki" + "balki"), keep only one.
   After trimming, re-encode only the changed segments and rebuild the master. Snap starts so the kept lead is not lost: compute `a2 = ceil(a*fps - 1e-3)/fps` and choose `a` exactly on a frame boundary, otherwise ceil jumps one frame (33 ms) later and can clip an onset. Then run the join audit again on the new master: every join ≤ ~0.12 s of silence and a clean transcript.
7. **Encode low-memory, one segment at a time** (never feed all 4K inputs into one filter graph):
   - Snap start to a source frame: `a2 = ceil(a*fps - 1e-3)/fps`; `nf = round((b-a2)*30)`.
   - `ffmpeg -ss a2 -i clip -map 0:v:0 -vf fps=30 -frames:v nf` with the source codec family and colour tags, e.g. for HLG HEVC: `-c:v libx265 -preset fast -pix_fmt yuv420p10le -profile:v main10 -x265-params crf=14:colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc -color_primaries bt2020 -color_trc arib-std-b67 -colorspace bt2020nc -tag:v hvc1 segNN.mov` (for SDR H.264 sources use libx264 crf 14 with matching tags). Frame-exact cuts need a re-encode because keyframes are ~1 s apart.
   - Audio as one continuous WAV: per segment `-ss a2 -t nf/30`, apad/atrim to exactly nf/30, 20–30 ms afade in/out, then concat.
   - Concat video segments with the concat demuxer `-c:v copy`, mux the WAV as AAC 192k, `+faststart` → `merge/master.mov`.
   - 4K x265 runs ~1.7 fps on 2 cores; run long encodes in the background.
8. **Check the master:** video and audio durations match, full decode with `-f null` is clean, transcribe the final audio once more (sentence by sentence, long ones in halves), run the join audit (6b), grab a few frames.
9. **Checkpoint:** send the user the master and list every kept line in full, flagging judgement calls (rephrased lines, stitched takes). If the user is present, wait for an OK or swaps before Phase B. If unattended, proceed with the best reading and say so at the top.

Phase A don'ts: no graphics, captions, music, colour, flips or crops; don't change resolution, codec family, bit depth or HDR (autorotate to upright is fine; say so).

---

## T. Transcription and word timing (used by both phases)

### T1. Whisper
In order of preference: local faster-whisper/openai-whisper; **Whisper ONNX** from `https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-turbo.tar.bz2` (~560 MB; a direct curl download from GitHub usually works even when PyPI is blocked; download it without asking and keep it in `~/models/` for reuse); a connected tool (VideoDB `upload_media` → `generate_transcript`, needs a public URL); a transcript the user provides. Never fall back to timing graphics from the script alone (rule 1).

Decoding the sherpa ONNX export yourself with onnxruntime:
- Encoder input `mel` (1, n_mels, 3000) → outputs `n_layer_cross_k/v`. Decoder inputs `tokens`, `in_n_layer_self_k_cache/v_cache` shaped (n_text_layer, 1, 448, n_text_state), `n_layer_cross_k/v`, `offset`; outputs `logits` and the updated caches. Metadata holds `sot`, `eot`, `transcribe`, `no_timestamps`, `all_language_codes`/`all_language_tokens`, `n_mels` (128 for turbo).
- Log-mel: pad audio to 30 s, reflect-pad 200, Hann window 400, hop 160, power spectrum, drop the last frame (3000 frames), slaney mel filters (slaney norm), log10, clamp to max-8, (x+4)/4.
- Greedy decode from `[sot, lang(hi), transcribe]` plus `no_timestamps` (or allow timestamp tokens ≥ no_timestamps+1 at 0.02 s per step for segment times). Suppress sot/transcribe/language tokens; stop at eot. Tokens file = base64 bytes per id; join bytes, then UTF-8 decode.
- Turbo int8 takes ~6 s per decode on 2 cores (the encoder always sees 30 s).
- Hinglish comes out as Devanagari mixed with English words. For anything shown on screen, romanize to Hinglish by hand in the speaker's own spelling style (e.g. "dhyan se dekho", "chhota", "khatam"), one romanized token per Whisper token, so the timings carry over.

### T2. Word-level timestamps (the method that fixed sync)
1. Split the voice into speech segments at pauses (50 ms RMS, -33 dB threshold, merge gaps ≤100 ms, drop blips <100 ms). Transcribe each segment (T1) → reference words per segment.
2. **Prefix sweep** per segment: decode audio `[seg_start-0.08, t]` for t stepping by 0.35 s to the segment end. Align each hypothesis (minus its last, possibly cut word) to the reference words with a fuzzy-similarity DP (normalise nukta/anusvara, difflib ratio) to get how many reference words are complete. The first t at which word k is complete gives its end ≈ t − 0.175 s. Keep the count monotonic. Cost: ~14 s per step; ~60 s of speech takes ~40 min, so run it in the background and build graphics meanwhile.
3. **Smooth clusters.** Sweep ends come in clusters (several words share one end). Use each cluster's last word as an anchor (cumulative syllables → time), add (0, seg_start) and (1, seg_end), and interpolate every word boundary by syllable count between anchors.
4. Write `build/words.json` (romanized word, start, end, segment index). Derive every event time in `build/times.py` by word lookup, e.g. `T_LOOP = wt('loop', after=39)`; never hard-code seconds.
5. **Spot-check** 4–6 key events: decode `[seg_start, T-0.1]` (word must be absent) and `[seg_start, T+0.45]` (word present). Fix any that fail before rendering.
6. Digital-silence pauses (a deliberate wait) are exact anchors: find them from the waveform.

---

## Phase B: edit the master into the final video

Input is `merge/master.mov` (or the user's already-merged video) plus word timestamps for **that exact file** (T2). Never re-cut or reorder content in this phase.

### B1. Analyse
1. Contact sheet of the master (`fps=1/N,scale=320:-1,tile=6x4`). Find the face/head box on a gridded frame (OpenCV Haar cascades may be missing from the build; then read it off the grid by eye) and compute where the chin lands at every zoom level you plan to use.
2. Map the content from the **actual transcript**: hook, problem/topic, key facts or claims, explanation steps, proof, payoff, CTA. Tie each to word timestamps. Diff the transcript against any script and note every line that was changed, added or skipped.
3. **Classify the video type:** coding/technical explainer, news/current-event (an outage, a court ruling, a launch, a policy, a market event, anything that "just happened"), or general talking head. A video can be both. The type decides which gates below apply.
4. **List every company, product, app or organisation she names.** Each gets its official logo on the word that names it (B4c); a text name tag is only the last fallback.
4b. **List every visualisable fact she says** (rule 8): dates, places/countries/cities, durations and time spans, times of day, counts, money, percentages, speeds, sizes, before/after states, "down/failed/blocked", "whole day/night". Each gets a visual from the B4f catalogue on the word that says it.
5. **Reference videos** (if given): files, or `vidiq_watch_shortform_content` for Instagram/TikTok links. Write `STYLE.md`: pacing (visual changes per 10 s), hook style, text-card system, type hierarchy, motion-graphics vocabulary and density, B-roll rhythm, transitions, zoom rhythm, colour look, sound-design rhythm, safe zones. Mark each trait adopt / adapt / skip with a reason. Recreate the style principles in original graphics; skip the creator's own brand pieces (signature end cards, handles, logos). With no references, use a clean educational-shorts style.
6. **Inventory user B-roll:** ffprobe each clip (duration, rotation side-data; phones often store portrait as landscape + rotation, and ffmpeg autorotates on decode), make a contact sheet of each, write a one-line description, and note which spoken line each could illustrate.

### B2a. Correctness gate: coding/technical content
Before drawing anything:
- Solve the problem yourself. Write the solution in the language the video uses and **run it** on the example from the video plus edge cases. Every code line shown on screen must come from this tested code (or, for a "find the bug" video, from the buggy code with the bug verified by running it, e.g. confirming the infinite loop).
- Dry-run the on-screen example step by step (pointer positions, comparisons, branches) and save it as `build/dryrun.json`. Every animation frame must match it.
- Verify every claim said or shown: complexities, technique names, numbers. If the speaker says something wrong, don't silently "fix" the visual to contradict the audio; flag it to the user.
- Spell the example data exactly as the speaker uses it.

### B2b. News gate: news/current-event content
Whenever the speaker talks about a real event, find the real reporting and show it as a **news card** (B4b) while she is talking about it.
1. **Find the sources.** Pull the event, names, numbers and dates from the transcript, then WebSearch (use `extended` mode for events from the last few days) and WebFetch the articles. Prefer original and reputable sources: the company's or authority's own statement/status page, court/government sites, wire services and major outlets. Pick one primary article per claim; use a second source to confirm key numbers.
2. **Match the article to what she says.** For each news beat, choose the 1–3 sentences of the article that best match the sentence she is speaking. Never invent, merge, or reword text and present it as the outlet's wording. If no real article supports a claim, don't make a card for it: flag it to the user, or use a clearly self-written "KEY FACTS" summary card with no outlet name.
3. **Check facts against the audio.** If what she says conflicts with the reporting, flag it to the user before rendering.
4. **Keep excerpts short**, always with the outlet name and date.
5. **Record everything** in `assets/news/NEWS.md`: outlet, headline, URL, publish date, the exact excerpt shown, and which timestamps it covers.
6. **Optional article screenshot** via a browser tool, cropped, as a brief insert.

### B3. Storyboard (STORYBOARD.md + build/times.py)
A timed list of visuals; each has a purpose (explain, prove, emphasise, contrast, retention) and is anchored to the spoken word that triggers it (rule 2). Delete anything without a purpose. Aim for a visual change every 2–3 s.

**Coding explainer vocabulary (split-screen layout):**
- 9:16 split: a light-blue dotted panel on top (~880 px) holding a dark code-editor card (traffic-light dots, file name, line numbers, syntax colours, ~33 px monospace), the speaker reframed in the bottom panel (~1040 px) with a thin dark seam. Keep the split for the **whole explanation, up to the line where she finishes the fix**, then cut to full frame with a quick white flash and a whoosh.
- Title pill above the card that changes with the beat: hook ("AI ka code. 1 bug. 5 sec.") → countdown ring over a deliberate silent wait (5→1, ticks, a scanning highlight over the code, nothing revealed) → "Bug mila?" → "BUG: l = mid" (red, monospace) → "Interviewer: Fix kaise karoge?" → "FIX: l = mid + 1" (green).
- Bug line: red highlight, bold red text and a wavy underline on the word that names the bug, with a small shake; pulse it again when she re-explains it; it turns green on the words of the fix.
- Example data as boxes with indices: show "?" boxes on "array", fill each value on the word that says it; pointers (`l`, `r`, `mid`, combined "l, mid") as labelled arrows popping on the words that set them; a bounce when a pointer "stays"; short side tags on their words ("target = 4", "2 < 4", "l = 0 phir se", "∞ INFINITE LOOP" red, "found → index 1" green).
- Brute force briefly with complexity and ❌; optimal with ✅; complexity badge on the words that say it.

**News vocabulary:** news card (B4b) on the first words about the event with the highlight sweeping as she reads; official logo (B4c) on the word that names the company; dates, places, durations and numbers as animated visuals (B4f); a small "Source: <outlet>, <date>" tag.

**Hook pattern for an event ("<date> ko <place> me <apps> <duration> tak down"):** calendar flips to the date → globe spins to the place and zooms in with a pin → the calendar and globe shrink into small corner badges that stay up for the rest of the hook → logo cards pop in one by one as each app is named → a timer counts up to the duration in the chest zone → on the failure words the logos grey out with red ✕ badges and a short shake → the company's big official logo on its name → a day-cycle or similar visual on "poore din"/"whole day". The same pattern works for any "when + where + what + how long" opening.

**Full-frame talking part (after the split), big text (rule 4):**
- Top-zone cards (centre y ≈ 380 on 1920): white or dark rounded cards, 70–110 px heavy sans (e.g. "Bina check kiye" / "SUBMIT? ❌" appearing word by word).
- Chest-zone cards (centre y ≈ 1330–1370): stamps such as a rotated "REJECTED" (~130 px, red border), kept below the chin at the current zoom.
- Punch-in zooms (1.0 → 1.1 → 1.2) on emphasis words, centred on the face.
- Outro: a large follow card with the handle (~1.45× chip size) on the words that ask to follow, then a large two-line question card ("Kitne second me / find kiya? 👇") on the comment ask, in the top zone.

Keep all timing in `times.py` from word lookups; the compositor reads it, so a change is one edit plus one re-render.

### B4. Build the pieces
- **Compositor:** one Python script (`build/edit.py`) that reads the master as raw RGB frames from an ffmpeg pipe (decoded at 1.2× output size for zoom headroom, with the colour grade in the decode filter), composes each frame with Pillow (cards pre-rendered once, animated per frame with ease-out / back-out springs and pop-in scale), and pipes RGB to an ffmpeg libx264 encoder. It also has a `stills t1,t2,...` mode for review. A 72 s 1080×1920 render takes ~6–7 min on 2 cores (heavier per-pixel visuals such as the globe add more; render two halves in parallel); run it in the background and wait for completion with a Monitor/until-loop.
- **Text cards and pills:** heavy sans (Inter Display Black/ExtraBold) for emphasis, an italic serif (Lora) for soft connectors, monospace for code tokens like `l = mid`; yellow accent, red for negative words, green for fixes; soft drop shadows. Lay text out on a shared baseline (`anchor='ls'`) so mixed fonts line up. Emoji via Noto Color Emoji (`embedded_color=True`, size 109 then scale). Pillow RGBA drawing replaces pixels instead of blending: draw semi-transparent shapes on a small layer and `alpha_composite` it.
- **Captions (off by default, rule 3):** if the user asks for them, build from `words.json` (1–3 words per chunk, emphasis words big and coloured, the rest small italic), placed below the face and never overlapping a card or news panel.
- **Zooms/reframes:** animated crop+scale on emphasis words, centred on the face box; never crop out the face.
- **Transitions:** hard cuts with a 0.1 s white flash plus a whoosh between sections; slide-ins for scene changes inside animations.
- **Colour:** if the master is HLG/HDR, tone-map to SDR BT.709 (`zscale=t=linear:npl=100,format=gbrpf32le,tonemap=hable,zscale=p=709:t=709:m=709:r=tv,format=yuv420p`, or the `colorspace` filter if zscale is missing) and say so. Then a light look, e.g. `eq=contrast=1.05:saturation=1.08:gamma=0.985,colorbalance=rs=0.015:bs=-0.02`.

### B4b. News card (split-screen read-along highlight)
- **Split screen.** The speaker stays visible in one part of the 9:16 frame and a solid news panel takes the other part, roughly 45–50% of the height. Default: panel at the **bottom**, speaker reframed into the top half (face fully visible). If the face sits low or the user asks, put the panel at the **top**. For 16:9, use a side panel (~45% width).
- **Divider:** a thin accent-coloured line (3–5 px). **Panel:** near-black slate, generous padding, safe zones respected.
- **Source label** at the top of the panel: the outlet's official logo file if obtained per B4c, otherwise the outlet name in clean bold text; date below.
- **Article text:** the excerpt in white, centred, ~34–42 px on a 1080-wide frame, 5–9 lines.
- **Read-along highlight:** an amber/orange (or brand-colour) box sweeps behind the text being spoken, line by line, driven from word timestamps; already-read lines stay highlighted. If she paraphrases, highlight the sentence she is talking about for that span.
- **Motion:** panel slides in (~0.3 s ease-out) with a soft whoosh, text fades up, highlight sweeps; panel slides out when she moves on.
- **Accuracy:** card text must match `NEWS.md` character for character; outlet and date must be right.

### B4c. Logos, characters, music and other third-party assets
**Where official logo files usually come from** (anonymous `git clone --depth 1 --filter=blob:none --sparse <repo>` then `git ls-tree -r --name-only HEAD | grep -i <name>` and `git sparse-checkout set --no-cone /path/file.svg` works even when PyPI/npm and Wikimedia are blocked):
- `gilbarbara/logos` (logos/*.svg: microsoft, microsoft-teams, microsoft-onedrive, google, aws, meta, …), `homarr-labs/dashboard-icons` (svg/ and png/: app icons such as microsoft-outlook, microsoft-teams, onedrive, slack, notion, …), `simple-icons/simple-icons` (one-colour brand marks; some brands like Microsoft are removed there), the company's press/brand kit, Wikimedia Commons, or a file from the user.
- When a brand has several icon generations, use one consistent generation across all logos in the same scene.
- Render SVG to PNG at ~800 px height with Playwright Chromium (strip `width`/`height`, set `style="height:800px;width:auto"`, `element.screenshot(omit_background=True)`), keep them in `assets/logos/`, and record repo, path and date in `LOGOS.md`.
- A logo may be animated as a whole (pop, slide, scale, fade, grey-out, a ✕ badge beside it). Pieces cropped from the official file may pop in one after another (e.g. Microsoft's four squares, then the wordmark slides in), as long as the final frame is the unaltered official logo.

Decide per asset, in this order, and record each decision in `ASSETS.md` (asset, source URL, licence/terms, where used):
1. **Free to use as-is → use it.** CC0/public domain or a licence that allows this use (check the actual licence page).
2. **Real company/product/outlet logos → the official file, never a redrawn look-alike.** Get it from the sources above, the company's press/brand kit, the Wikimedia Commons file (check its licence/trademark note), or a file the user supplies. Keep proportions and colours, give it clear space, use it only to identify the company being discussed, pop it on the word that names it. Don't recolour, distort or combine it. If no official file can be obtained, use a clean text name tag (company name in bold in a pill) and tell the user. Logos that appear naturally in the user's own B-roll (e.g. her office) are fine as filmed.
3. **Not free → create an original in the same spirit:** music synthesised with a similar mood and tempo (no copied melody); B-roll and illustrations drawn in Python or via a connected image tool; original characters (never a known character, even restyled). Never put a real company's name or logo inside an invented visual so that it looks like their official screen.
4. **Screenshots of real things** (a status page, a post, an article headline) may be shown briefly as evidence, cropped, with a source tag.

### B4d. User B-roll
1. Pick the clip(s) that best show the line being spoken (e.g. "Google me kaam karte hue…" → walking into the Google building, then working at a laptop next to the logo). Skip clips that don't match the line (scenery, feet, lobbies) and say which you skipped.
2. Cut short pieces: an establishing beat of ~1.2–1.5 s, then the most relevant shot for the rest of the line. Start exactly on the first word of the line; end when the next idea starts.
3. Extract frames at 30 fps, scaled/cropped to 1080×1920 (autorotated), with the same light grade as the master; add a slow push-in (1.0 → 1.07).
4. Full-screen replace the speaker (her voice continues), with a white flash + whoosh in, a bottom gradient, and one big lower-third that names the point (e.g. "Software Engineer" ~70 px white over "@ Google" ~120 px yellow), clear of the bottom safe area.
5. Record each clip used, with in/out points, in `ASSETS.md`.

### B4e. Self-made animation clips and images
For a line that states a concept or a conclusion (e.g. "AI code likhta hai, lekin final approval engineer deta hai… isliye aaj bhi DSA important hai"), make a short full-screen animated clip (4–6 s) instead of plain talking head, timed scene by scene to the words; her voice continues underneath.
- Background: dark navy-to-indigo gradient with a faint dot grid.
- Original illustrations drawn in Pillow: a friendly AI robot (rounded head, glowing eyes, antenna, "AI" chest plate) that bobs; an engineer avatar (white circle, dark silhouette with glasses, yellow "Engineer" label); code-editor cards whose code types in character by character with a cursor; a green rotated "APPROVED ✓" stamp that slams in (scale 1.8 → 1) on "approval"; big bouncing letters ("D S A" ~330 px, staggered 80 ms) and a slam-in "IMPORTANT" pill on their words; a binary tree that grows node by node with the binary-search path lighting up yellow; users → servers diagrams with moving packets, a slow server in red, traffic re-routing to healthy servers, a restart spinner.
- Scene titles at ~80–100 px, kept within 1000 px width (shrink if it would clip).
- Each scene change lands on its trigger word, slides in over ~0.3 s, and has its own SFX (whoosh, pop, thud, chime).
- Prefer these self-made clips over stock; if a connected image or video generator is available and clearly better for the idea, use it and record it in `ASSETS.md`.

### B4f. Visual catalogue: show facts as animations (rule 8)
Draw these in Pillow/NumPy per frame (all original, no third-party art). Trigger each on the word that says it; pop in with a back-out spring (~0.35–0.4 s); add the SFX in brackets. Put them in the top zone (above the head) or the chest zone (below the chin), at a size that reads on a phone (cards ~300–860 px wide).
- **Date → calendar** (tick per page): a tear-off desk calendar card (red header with month, big day number ~230 px, weekday · year line, binder rings). Pages flip quickly from a few days before to the spoken day (≈0.1 s per page, old page flies up and fades), landing with a small bounce on the day. Compute the weekday in code (`datetime.date(y,m,d).strftime('%A')`). After its line it shrinks (~0.35 s ease) into a small corner badge (scale ~0.4) and stays while the event is still being described.
- **Place → globe zoom + pin** (whoosh, ding on highlight, swish on zoom, pop on pin): an orthographic globe rendered per pixel from **Natural Earth** country polygons (public domain; sparse-clone `nvkelso/natural-earth-vector`, file `geojson/ne_50m_admin_0_countries.geojson`). Draw an equirectangular world texture (~12 px/deg) plus a high-res regional texture (~70 px/deg) of the area, with land, ocean and borders; sample with the inverse orthographic projection; add sphere shading and a rim light while small. Sequence: globe pops in (~R 255 px) → rotates to the place's lon/lat (~0.6 s) → the country fills in an accent colour on the word that names it → zooms (R ×12 exponentially, ~0.8 s) into a round lens with a white ring → a dark teardrop pin (contrasting with the highlighted fill) drops with a bounce, a pulse ring, and a "<PLACE>" pill above it. Cache the final zoomed frame and only resize it afterwards (a full-res render costs ~0.6 s). Later it shrinks into a corner badge (map + small label; hide the pin at badge size). For a city, use admin-1/populated-places data and pin the city.
- **Duration / time span → running timer** (thud, then soft ticks while counting): a card with an analog stopwatch (crown, 12 ticks, hour + red minute hands, a red filled sector growing) and a digital counter that eases from 00h 00m to the real value in ~1 s (e.g. 10h 51m), with a label in her words underneath (e.g. "≈ 11 GHANTE"). Show the exact sourced value plus her rounded phrase; never show a number that contradicts the source.
- **Start–end times / "poora din" / "raat bhar" → day-cycle sky** (swish, sparkle, ding at night): a rounded card with a sky gradient (dawn → noon → dusk → night), a sun moving along an arc from the start time to the end time with a glow, then a moon and stars; a ground strip with the start/end time labels (e.g. "07:40" … "18:31 UTC"); a title pill on the card's top edge with her phrase.
- **Company / app names → official logo cards** (pop per logo): white rounded cards (~300 × 300 px) with the logo (~150 px) and the name in bold below, one per name as she says it, in a row in the top zone. A big standalone brand on its own emphasis ("Microsoft jaisi company") gets a large logo card (~860 px wide, the logo ~175 px tall).
- **Down / failed / blocked → failure state** (error buzz): the affected logo cards desaturate to ~85% grey, a red ✕ badge (white outline) pops on each corner with a 0.08 s stagger and a short horizontal shake, plus an "APPS DOWN"-style pill. **Fixed / back → recovery state** (chime): colour returns, a green ✓ badge.
- **Numbers / money / percentages / counts → counter** (tick then pop): the number counts up from 0 with ease-out, a unit label, and a small bar or icon row (e.g. users × N) filling up.
- **Before vs after / comparison → split card** with two columns, left greyed, right highlighted; **growth/decline → mini line or bar chart** drawing itself.
- **Steps / process → numbered step dots** (1 2 3) with the active one highlighted, or a full-screen animation (B4e).
- **Status / health → status lights**, a heartbeat line, server icons going red/green.
Pick the visual that matches the meaning of the words she says, not decoration; one visual per idea; let each one leave (~0.25 s fade) before the next idea or move into a badge.

### B5. Composition rules
- Never cover the face or the UI/board element being discussed. Check the chin position at each zoom level; chest-zone cards sit below it.
- 9:16 safe zones: no text in the top ~8%, bottom ~15%, or the right-edge button strip.
- Never flip or mirror footage. Never change content order.

### B6. Sound
- Copyright-free audio per B4c, usually synthesised in code (NumPy → WAV): a lo-fi bed (~88 BPM, soft pad, keys arpeggio, bass, light drums), whoosh, pop, click, tick, low buzz, chime, thud, riser. Record each in `ASSETS.md`.
- SFX on visual events only, each placed at the same `times.py` time as its visual: pointer = click, value pop = pop, bug/mismatch = low buzz, fix/✅ = chime, stamp = thud, section/B-roll/animation cut = whoosh, countdown = tick per second with a riser into it; calendar page = tick, globe = whoosh/swish, pin = pop, timer = thud + soft ticks, failure ✕ = buzz. Keep pops quiet (SFX around -20 dB under the voice).
- Duck the music under the voice with `sidechaincompress` (voice as sidechain); lift the music during deliberate silent waits so the pause doesn't feel dead. Clean the voice (highpass 80 Hz, light `afftdn`, gentle compression). Final loudness ≈ -14 LUFS, true peak -1 dB (two-pass `loudnorm`, linear). The voice must stay clearly on top.

### B7. Review, fix, render
1. Before any full render, export stills at every storyboard event (and a few between) and tile them for review. Check:
   - each visual appears on the word that triggers it and matches what is said (compare against `words.json`);
   - nothing is shown that she didn't say;
   - face/UI never covered; text big enough, not clipped at frame edges, inside safe zones;
   - algorithm frames match `dryrun.json`; code on screen matches the tested code;
   - news cards: text matches `NEWS.md`, outlet/date correct, highlight on the spoken line;
   - logos are official files (text tags only if no file could be found, and say so); B-roll matches its line; animation scenes land on their words;
   - every date, place, duration, company and number she says has its B4f visual on its word, and the values match the sources (weekday computed, durations exact).
2. Run the Whisper spot-checks from T2 step 5 for the key events. If the master was re-cut after events were timed, remap every event through source time (`new = new_seg_start + (old_src_time - new_src_start)`) instead of re-guessing, then spot-check a few in the changed sentences.
3. Fix every issue and re-check. Send a preview to the user when they are present.
4. Final render to `renders/<name>_vN.mp4` (new version number each round; never overwrite the previous one): libx264 `-crf 17–18 -preset slow -pix_fmt yuv420p`, BT.709 tags, AAC 192k, `-movflags +faststart`, 1080×1920 for Reels. Verify with ffprobe (duration equals master, audio present) and a full decode `ffmpeg -v error -i out.mp4 -f null -`, then grab frames from the final file at key events.
5. Deliver with SendUserFile. Summarise briefly in the user's language: what changed since the last version, visuals with their trigger words, B-roll used and skipped, self-made clips, news sources (outlet, headline, link, date), logos and assets (from `ASSETS.md`), anything flagged, and an offer to nudge any moment by seconds. If the user asks how long a render will take, check real progress (output file sizes, elapsed time) and give an honest estimate.

## Don'ts (whole skill)
- Don't time graphics from a script; time them from the transcribed voice.
- Don't show cards, names or claims she didn't say.
- Don't burn in captions unless the user asks.
- Don't use small text in the full-frame part; don't put text over the face or chin.
- Don't overwrite or modify the user's originals; don't overwrite earlier renders.
- Don't order clips by filename or creation time over what the user says.
- Don't show code, pointer steps or complexities you haven't run or dry-run.
- Don't show a news card for anything you couldn't find real reporting for, and never put made-up or reworded text under an outlet's name.
- Don't redraw or imitate a real logo or known character; use the official file, a text name tag, or an original design.
- Don't show a date, place, duration or company as a plain text chip when a B4f visual fits.
- Don't leave gaps over ~0.1 s, half-words or doubled words at any join.
- Don't use non-free music, footage or images as-is; make an original with the same feel instead.
- Don't copy a reference creator's brand pieces (end cards, handles, logos).
- Don't add decoration without a purpose.
- Don't skip a better tool just because it needs a download, a permission or a sign-in: if pip, npm, GitHub or a model file is reachable, use it; if it needs the user's permission or login, ask them. Only fall back when the source is truly unreachable, and say so.