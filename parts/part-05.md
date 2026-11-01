
## 6. TROUBLESHOOTING COMMON ISSUES

### "My photos aren't sharp"

1. Shutter speed too low → increase (1/FL equivalent rule × 2 for MFT)
2. IBIS needs a moment to settle → half-press shutter, wait 0.5s, then shoot
3. Subject Detection picked background → use smaller AF zone
4. Lens needs AF fine-tune → not usually needed on mirrorless, but test with a static target
5. Electronic shutter rolling shutter on fast panning → try mechanical shutter
6. C-AF sensitivity too low for subject speed → increase to +1 or +2

### "AF keeps losing my subject"

1. Subject Detection struggling with busy background → switch to single AF point
2. C-AF Sensitivity too high and AF jumps to background → reduce to 0 or -1
3. AF Scanner set too conservatively → try Mode 3
4. Subject too small in frame → get closer or use longer lens; detection needs ~5% frame coverage
5. Backlit subject → AF struggles; reposition or use AF point manually

### "ProCapture isn't working"

1. Must be in a PASM mode, not in a Custom mode (unless ProCapture is saved into that custom mode)
2. Check that ProCapture is enabled in the menu: Camera 2 → ProCapture
3. ProCapture SH2 requires C-AF; SH1 uses S-AF
4. Half-press shutter to start buffering; full press to capture
5. Buffer fills after ~70 frames — release and re-half-press

### "Battery drains too fast"

1. Reduce Quick Sleep Mode to 30 sec
2. Turn off Wi-Fi/Bluetooth when not transferring
3. Disable Live View Boost when not needed
4. Use EVF-only display mode (eye sensor) rather than rear screen
5. Carry at least 2 spare BLX-1 batteries for a full day

---

## 7. TELEGRAM Q&A WORKFLOW

When the user asks camera settings questions via Telegram, follow this workflow:

### Step 1: Identify the Genre
Parse the user's message for genre keywords:
- "landscape" / "scenery" / "long exposure" / "waterfall" / "sunset" / "seascape" → **Landscape**
- "bird" / "BIF" / "birds in flight" / "wildlife" / "nature" / "animal" / "perched" → **Nature/Wildlife**
- "portrait" / "people" / "face" / "person" / "family" / "headshot" → **Portrait**
- "dog" / "pet" / "puppy" / "action" / "running" / "playing" / "canine" → **Dogs/Action**

### Step 2: Identify Sub-Topic
- Specific feature: "Live ND" / "ProCapture" / "Hi-Res" / "Focus Bracketing" / "Subject Detection"
- AF: "autofocus" / "C-AF" / "tracking" / "focus settings" / "sharp"
- General: "settings" / "setup" / "configure" / "what should I use" / "recommend"
- Lens: "which lens" / "lens for" / "best lens"

### Step 3: Compose Answer
Use the settings cards and detailed tables in this skill. Format for Telegram:
- Use plain text (no markdown headers in Telegram)
- Use emoji for visual clarity (📷 🌅 🦅 👤 🐕)
- Keep each answer concise — deliver the quick settings card first, then offer "Want more detail on any specific setting?"
- Always cite provenance: "(Source: Rob Trek/Martin Belan/official OM System guide)"

### Step 4: Deliver to Telegram
Use `send_message(action='send', target='telegram', message='...')`.

### Example Telegram Answer Format

```
🐕 OM-1 Mark II — DOG ACTION SETTINGS

📸 Mode: S (Shutter Priority)
⚡ Shutter: 1/2000s (running) — 1/4000s (fast action)
🔍 AF: C-AF + Dog Subject Detection 🐕
🎯 C-AF Sensitivity: +1
📐 AF Target: Mid-size zone
💨 Drive: SH2 Silent 25fps
⚡ ProCapture SH2: ON (70 pre-frames!)
🔘 Back-button AF: AF-ON button

🎒 Lens: 40-150mm f/2.8 PRO is the workhorse.
   For tighter portraits: 45mm f/1.2 or 75mm f/1.8.

💡 Pro tip: Get down to dog's eye level.
   ProCapture catches the exact jump moment!

Sources: Martin Belan (80-85% keeper rate tested),
Rob Trek action methodology, Mu-43 community.

Need more detail on AF, drive modes, or lens choices?
```

## 8. COMMON PITFALLS

1. **Using 50fps SH2 instead of 25fps** — creates massive culling workload. 25fps captures every moment you need.
2. **Forgetting to turn off Subject Detection for obstructed subjects** — birds in dense foliage confuse AI detection. Switch to single AF point.
3. **Leaving IS on for tripod landscape** — can introduce feedback loop blur. Turn IS OFF when on a solid tripod.
4. **Using Auto ISO with low minimum shutter speed** — set minimum shutter to match your genre (1/125s portrait, 1/2000s action).
5. **Not assigning Subject Detection toggle to a button** — you need to switch detection on/off quickly in the field.
6. **Buying cheap SD cards** — SH2 25fps needs UHS-II V90 cards to clear the buffer fast.
7. **Shooting JPEG only** — the OM-1 RAW files have ~2 stops of highlight recovery headroom.
8. **Using C-AF-TR without understanding Mk II behaviour** — with Subject Detection ON, the Mk II forces C-AF to C-AF-TR automatically.
9. **Not formatting cards after each shoot** — accumulated files slow buffer clearing and increase card failure risk.
10. **Ignoring the histogram** — the EVF/screen lies in bright sunlight. Trust the histogram for exposure.

## Verification Checklist

- [ ] User's genre correctly identified from keywords
- [ ] Quick settings card matches the genre tables in this skill
- [ ] AF settings include Subject Detection type, C-AF Sensitivity, AF Target mode
- [ ] Drive mode and ProCapture correctly specified for action genres
- [ ] Lens recommendations are MFT mount and appropriate for the genre
- [ ] Telegram message formatted with emoji and clear sections
- [ ] Source attribution included where applicable
- [ ] Offer to provide more detail on specific sub-topics

## One-Shot Recipe: Quick Settings for Telegram

```
User message: "What landscape settings for my OM-1 Mark II?"
Agent:
1. Load this skill
2. Compose telegram message from Landscape Quick Settings Card
3. send_message(action='send', target='telegram', message='<formatted landscape card>')
4. In the Telegram message, offer follow-up: "Want detail on Live ND, Hi-Res, or lens choices?"
```

## Reference Sources

This skill is compiled from:
- Phil Norton Photography — OM1-MKII Comprehensive Guide (philnortonphotographyblog.co.uk)
- Mcaughtry.photo — OM-1 Landscape Settings & Spreadsheets (mcaughtry.photo)
- Martin Belan — Dog Subject Detection Testing & Wildlife Settings (martinbelan.com)
- MarcR Photo — OM-1 Bird/Wildlife Settings: Rob Trek vs Steven Ingram Comparison
- Luminescent Photo — Bird & Wildlife Setup Secrets (luminescentphoto.com)
- OM System Official Learn Center — Sports Shooting on OM-1 Mark II
- OM System Official — Download Custom Settings (explore.omsystem.com)
- Ken Rockwell — OM-1 Mark II User's Guide (kenrockwell.com)
- DPReview Forums — OM-1 Mark II user reports and settings discussions
- Mu-43 Community — C-AF problem solving and field experience
- Reddit r/M43 — Community custom mode configurations

## Reference Resources (Manuals, Guides & Sites)

### Official OM System Resources

| Resource | URL | What's There |
|----------|-----|-------------|
| OM-1 Mark II Full Instruction Manual (PDF) | [my.omsystem.com](https://my.omsystem.com/consumer/manuals/cameras/OM-1_Mark_II_MANUAL_EN.pdf) | 566-page official manual — every menu item, every feature, every spec |
| OM-1 Mark II Web Manual (Interactive HTML) | [learning.omsystem.com](https://learning.omsystem.com/OM-1MarkII/zz_html_manual/en/index.html) | Searchable online version of the full instruction manual |
| OM-1 Mark II Camera How-To | [learning.omsystem.com](https://learning.omsystem.com/OM-1MarkII/en/index.html) | Quick-start topic guides: Live GND, Subject Detection AF, Button Assignments, etc. |
| OM-1 Mark II Support & Downloads | [learnandsupport.getolympus.com](https://learnandsupport.getolympus.com/support/om-system-om-1-mark-ii) | Manuals PDF, quick-start guides, software downloads |
| Firmware & Software Downloads | [support.jp.omsystem.com](https://support.jp.omsystem.com/en/support/imsg/digicamera/download/software/) | OM-1 Mark II firmware updates, OM Workspace, OM Capture |
| Manual Download Page (ver1.2) | [download.omsystem.com](https://download.omsystem.com/pages/inst/om1m2/index.html) | All-language PDF manuals for OM-1 Mark II |
| Explore OM System | [explore.omsystem.com](https://explore.omsystem.com/) | Product pages, sample galleries, Test & Wow guides |
| OM System — Test & Wow Landscape | [explore.omsystem.com/gb/en/test-and-wow-landscape](https://explore.omsystem.com/gb/en/test-and-wow-landscape) | Official quick-start guide + settings download for landscape |
| OM System — Test & Wow Macro | [explore.omsystem.com/dk/en/test-and-wow-macro](https://explore.omsystem.com/dk/en/test-and-wow-macro) | Official quick-start guide + settings download for macro |
| My OM System Blog | [my.omsystem.com](https://my.omsystem.com/blog/b/photography-journal_en/posts/my-om-1-custom-settings-for-bird-photography) | Community & official posts — e.g. custom settings for bird photography |

### Comprehensive Third-Party Guides

| Resource | URL | What's There |
|----------|-----|-------------|
| Phil Norton — OM1-MKII Guide | [philnortonphotographyblog.co.uk](https://www.philnortonphotographyblog.co.uk/om-system-om1-mk2-guide) | Full menu walkthrough, custom button setups, custom modes for landscape/BIF/macro |
| Ken Rockwell — User's Guide | [kenrockwell.com](https://www.kenrockwell.com/om/om-1-ii-users-guide.htm) | Concise user's guide covering essential settings, menus, and operation |
| Tony Phillips — Complete Guide | [tonyphillips.org](https://tonyphillips.org/product/om1m2/) | Comprehensive paid guide in PDF/ePub/print — the best help in the world on the OM-1 Mark II |
| Mcaughtry — Landscape Settings | [mcaughtry.photo](https://mcaughtry.photo) | Detailed landscape settings spreadsheets and exposure methodology |
| Martin Belan — Wildlife & Dog Testing | [martinbelan.com](https://martinbelan.com) | Scientific testing of Dog Subject Detection, keeper rates, wildlife settings |
| Luminescent Photo — Bird/Wildlife | [luminescentphoto.com](https://luminescentphoto.com) | Bird and wildlife setup secrets, ProCapture workflow |

### Video Tutorials & YouTube Channels

| Channel / Creator | URL / Search | What's There | Why Watch |
|-------------------|--------------|-------------|-----------|
| **Rob Trek** | [youtube.com/c/RobTrek](https://m.youtube.com/c/RobTrek) | OM System camera tutorials — custom modes, AF setup, settings walkthroughs, button configuration | The most recommended OM System YouTuber across forums (DPReview, Mu-43, Reddit). Known for his OM-1 Mark II custom mode setup guide and AF calibration deep-dives. |
| **OM System Official** — AF Settings | [youtube.com/watch?v=ihDKqa9o6P0](https://www.youtube.com/watch?v=ihDKqa9o6P0) | Official tutorial walking through all AF settings and customisation options | Official source — authoritative guidance straight from OM Digital Solutions |
| **OM System Official** — Handheld High-Res | [youtube.com/watch?v=NIQ6sg3m8ek](https://www.youtube.com/watch?v=NIQ6sg3m8ek) | How to capture 50MP handheld high-res shots | Essential for understanding the Mk II's computational photography features (14-bit, 80MP tripod mode) |
| **OM System Official** — Live Composite | [youtube.com/watch?v=um8J5P4fBNM](https://www.youtube.com/watch?v=um8J5P4fBNM) | Live Composite mode for star trails, light painting, cityscapes | Key tutorial for night/long-exposure computational features |
| **OM System Official** — Focus Stacking | YouTube search: "OM-1 Mark II Focus Stacking Chris McGinnis" | Focus stacking explained with Chris McGinnis | Official deep-dive into focus bracketing/stacking workflow |
| **OM System Official** — Starry Sky AF | [youtube.com/watch?v=oSchZDBNm6Y](https://www.youtube.com/watch?v=oSchZDBNm6Y) | Starry Sky AF for astrophotography | Official guide for astro-specific autofocus feature |
| **Luminescent Photo** — Bird Settings | [youtube.com/watch?v=Adjx7ZOahbc](https://www.youtube.com/watch?v=Adjx7ZOahbc) | Full setup guide for bird and wildlife photography after 2 years of OM-1 use | Highly detailed field-tested settings. Companion to luminescentphoto.com blog |
| **OM-1 Mark II for Video** — Wildlife Filming | [youtube.com/watch?v=lFK32lNLo-o](https://www.youtube.com/watch?v=lFK32lNLo-o) | Video-focused settings for wildlife filming, bird videography | Rare video-specific deep-dive — most guides are stills-focused. Covers C-AF for video, shutter speed matching, codec choice. |
| **Jake Sloan / Fstoppers** — Wildlife Setup | YouTube search: "Jake Sloan OM-1 Mark II Fstoppers" | Why MFT isn't a disadvantage — full wildlife setup breakdown | Honest assessment of MFT trade-offs for wildlife under $10K |
| **Ellie Cartwright** — Videography Skills | YouTube search: "Ellie Cartwright OM-1 Mark II" | Dynamic sequence shooting — Part I of OM-1 Mark II videography series | Professional videographer teaching field techniques on OM System cameras |
| **Gavin Hoey (Gavtrain)** — OM-1 Mark II Features | YouTube search: "Gavin Hoey OM-1 Mark II" | Feature walkthroughs — Live ND, focus stacking, back-button focus | Popular OM System educator. Known for practical, jargon-free explanations. |
| **Robin Wong** — Live ND / Computational | YouTube search: "Robin Wong OM-1 Live ND" | Computational photography tests — Live ND vs real ND filters | Legendary Olympus/OM System blogger. Independent, honest assessments of computational features. |
| **Steven Ingram** — Bird AF Settings | YouTube search: "Steven Ingram OM-1 bird settings" | Bird photography AF configuration, BIF techniques | Alongside Rob Trek, one of the two most-cited AF configuration sources in the community |
| **Peter Forsgård** — OM-1 Tips | YouTube search: "Peter Forsgård OM-1" | Field tests, lens reviews, wildlife shooting with OM System | Active field tester, regularly posts OM-1 Mark II real-world shooting results |
| **Espen Helland** — 2-Year Review | [espenhelland.com/om-1-mark-2](https://espenhelland.com/om-1-mark-2/) | Full review after 2 years of OM-1 Mark II use | Long-term field experience — what works, what doesn't, after years of real shooting |

### Community & Forums

| Resource | URL | What's There |
|----------|-----|-------------|
| DPReview OM-1 Mark II Forum | [dpreview.com/forums](https://www.dpreview.com/forums/) | Real-world user reports, troubleshooting, settings discussions |
| Mu-43 Community | [mu-43.com](https://mu-43.com) | Micro Four Thirds dedicated forum — OM-1 Mk II user experience, C-AF problem solving |
| Reddit r/M43 | [reddit.com/r/M43](https://reddit.com/r/M43) | Community custom mode configs, lens recommendations, field reports |
| OM System Facebook Group | Facebook search: "OM System OM-1 Mark II User Group" | Active user community, real-time Q&A |

### Software & Tools

| Tool | URL | Purpose |
|------|-----|---------|
| OM Workspace | [support.jp.omsystem.com](https://support.jp.omsystem.com/en/support/imsg/digicamera/download/software/) | Free RAW processing from OM System — best for Hi-Res shot processing |
| OM Capture | Same as above | Tethered shooting from computer |
| OM Image Share (OI.Share) | iOS/Android app stores | Transfer images, remote control, geotagging, firmware updates |
| Firmware Updates | [support.jp.omsystem.com](https://support.jp.omsystem.com/en/support/imsg/digicamera/download/software/) | Latest firmware for OM-1 Mark II |

> **Reference:** `references/backup-restore.md` — full OI.Share and OM Workspace backup/restore workflows.

### How to Use These Resources

When the user asks a question I can't fully answer from this skill's knowledge base, I should:

1. Consult the **OM-1 Mark II Web Manual** (interactive HTML) for menu navigation and feature documentation
2. Check **Phil Norton's guide** for custom button and custom mode configuration walkthroughs
3. Use **Ken Rockwell's guide** for quick operational questions (e.g. "how do I set white balance?")
4. Search **DPReview / Mu-43 / Reddit** for community-tested solutions to specific problems
5. Refer to **Mcaughtry / Martin Belan / Luminescent Photo** for genre-specific deep-dives
6. Check the **OM System support page** for firmware updates and official software
7. Use `defuddle parse <url> --markdown` to extract content from any of these URLs for reference
