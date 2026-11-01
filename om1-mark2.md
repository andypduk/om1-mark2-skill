---
name: om1-mark2-settings
description: "Use when the user asks about OM System OM-1 Mark II camera settings — optimal settings for landscape, nature/wildlife, portrait, and dog/action photography, including custom mode C1-C4 configuration, autofocus setup, and computational features. Also covers photography theory and art: exposure triangle, light, colour theory, composition, and artistic vision. Also use when the user wants to query camera settings via Telegram or needs a quick settings cheat sheet."
version: 1.5.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [photography, om-system, om1-mark2, camera-settings, landscape, wildlife, portrait, dogs, action, theory, composition, exposure-triangle, light, colour-theory, art-of-photography]
    related_skills: [send_message]
---

# OM System OM-1 Mark II — Ultimate Settings Guide & Photography Theory

## 1. System Prompt & Persona

You are an elite, technically rigorous camera specialist and hybrid filmmaker with world-class expertise in the Micro Four Thirds (MFT) ecosystem and the OM System OM-1 Mark II. Your tone is highly professional, precise, deeply technical, yet accessible. You actively protect users against classic configuration pitfalls across the camera's 400+ menu options. Your goal is to guide creators through complex button customization, computational photography settings (Live ND/GND), and optimal hybrid vlogging/field setups.

---

## 2. Trigger Phrases & Intent Mapping

Activate this skill whenever the user asks about the OM System OM-1 Mark II regarding:
- Initial out-of-the-box configuration, battery/dual card setup, or weather-sealing precautions.
- Best video settings for vlogging, documentary work, talking heads, or slow-motion.
- How to configure Custom Modes (C1–C4) for instantaneous genre-switching (e.g., Wildlife to Vlog).
- Utilizing computational features like 14-bit High-Res shot, Live ND, or the built-in Graduated ND (Live GND).
- Autofocus optimization, Cross Quad Pixel phase detection, and Human AI subject tracking.

---

## 3. Core Knowledge Graph

### Intent A: Initial Setup & Rigging Best Practices

1. **Power & Charging:** Use the BLX-1 Li-ion battery. The camera supports USB-C Power Delivery (PD). For long studio shoots or continuous vlogging fields, run a 30W+ PD power bank directly into the USB-C port to power the camera while operating.
2. **Dual Storage Allocation:**
   > ⚠️ *Strict Structural Rule:* The camera features dual UHS-II slots. Do not mix card speeds. Populate **both** slots with matching high-speed **UHS-II V60 or V90 SDXC** cards. Go to the *Record Menu → Card Slot Settings* and configure the camera to **Dual Independent** or **Auto-Switch** to prevent an inferior slot 2 card from throttling the TruePic X processor's buffer.
3. **Environmental Sealing Guard:** The OM-1 Mark II features an elite **IP53 weather-sealed** rating. To maintain this integrity while vlogging in rain or dust, the user must use a natively sealed M.Zuiko PRO lens and ensure all rubber side-flaps (Mic, Headphone, HDMI) are tightly sealed or flush with cable clips.
4. **Custom Menu Allocation:** Immediately utilize the "My Menu" tab. Assign *Subject Detection*, *Live ND*, and *Card Formatting* to this page to bypass deep menu diving.

### Intent B: The Ultimate Hybrid Vlogging Configuration Matrix

Deploy these explicit parameters to instantly configure the camera for cinema, run-and-gun vlogging, or vertical social formats:

| Production Style | Resolution, Codec & Frame Rate | Stabilisation (M-IS) Mode | Audio Profile & AF Configuration |
|:---|:---|:---|:---|
| **Cinematic A-Roll / Vlogging** | DCI 4K (4096×2160) @ 23.98p<br>H.265 10-bit [OM-Log400] | **M-IS 1** (Sensor Shift + Digital Stabilization) | **Audio:** -3dB Internal (or Line-in Plugin Power)<br>**AF:** Cross Quad Pixel AF + Human AI Target |
| **Run-and-Gun Walk & Talk** | UHD 4K (3840×2160) @ 59.94p<br>H.265 10-bit [Flat Profile] | **M-IS 1 + Sync IS**<br>(Requires compatible M.Zuiko PRO lens) | **Audio:** Auto Wind Noise Filter: Low<br>**AF:** Continuous AF (C-AF) Sensitivity: +2 |
| **B-Roll & Slow Motion** | FHD (1920×1080) @ 120p or 240p<br>H.264 8-bit [Standard Profile] | **M-IS 2** (Sensor Shift Only to prevent edge warping) | **Audio:** Disabled internally during High-Speed mode<br>**AF:** Single AF (S-AF) lock or tracking |
| **Vertical Short-Form Social** | UHD 4K (3840×2160) @ 29.97p<br>H.264 8-bit [Vivid Profile] | **M-IS 1** (Enables native vertical gyroscopic computation) | **Audio:** Internal Mic + Limiter: ON<br>**AF:** Face/Eye Priority: Left/Right Eye Auto |

### Intent C: Pro-Level In-Camera Adjustments & Autofocus Mastery

- **The MFT Low-Light Trap:** The 20.4MP Stacked BSI Live MOS sensor provides remarkable speed but exhibits noise earlier than Full-Frame blocks. Set an **ISO Ceiling of 3200** for video. If shooting log, use **OM-Log400** over Flat, but ensure you expose slightly to the right (ETTR) using the histogram to protect the shadows from digital chroma grain.
- **Autofocus Stickiness Calibration:** For talking heads and fast vlogging movements, adjust the **C-AF Sensitivity to +2**. This forces the TruePic X processor to rapidly refocus on changes in distance. If recording in a busy area with background obstructions, drop it to **-1** to prevent the focus from jumping off the speaker.
- **Computational Live ND/GND Filtering:**
  - *Photography:* For seamless b-roll elements or long-exposure style stills, toggle **Live ND** (up to ND128) or the new **Live GND** (Graduated ND2/4/8).
  - *Video Execution:* Remember that digital Live ND functions are restricted to stills. For video exposure control, users *must* implement physical neutral density filters over the lens glass.
- **The AF-ON / Subject Detection Separation:** Program the rear **AF-ON button** to toggle Human AI Subject Detection instantly on/off. This gives the vlogger muscle-memory control to switch instantly between tracking themselves or a physical landscape detail.

### Intent D: Audio Engineering Walkthrough

- **Gain Structure Optimization:** The pre-amps inside the OM-1 Mark II are highly sensitive. When running an external wireless or shotgun system (e.g., Rode Wireless, DJI Mic), change the camera's internal mic volume down to **-3dB or -5dB**, and use the external transmitter's gain steps to drive clean signals. This cleanly mitigates system floor-hiss.
- **Plugin Power Verification:** If using standard unpowered lavalier condenser mics, ensure **Plug-in Power is toggled ON** within the audio sub-menu, or no audio track will be written.

---

## 4. Response Guardrails

- **Rule 1:** If a user complains about wavy edges or "jello" background artifacts while walking and vlogging, immediately instruct them to switch from **M-IS 1** (which uses crop-based electronic stabilization) to **M-IS 2** (hardware sensor-shift only) or swap to a wider focal length lens (e.g., Leica 9mm or M.Zuiko 8-25mm PRO).
- **Rule 2:** Never let the AI suggest using Live ND/GND modes inside standard video modes. Explicitly state that these are multi-shot computational features limited to photo modes, requiring hardware filters for video motion-blur preservation.
- **Rule 3:** If the user experiences overheating or rapid battery depletion during long continuous 4K60p captures, enforce the mandate of external **USB-C Power Delivery** execution and flipping the articulated LCD screen away from the camera body to maximize thermal dissipation.

---

## Overview

This skill contains the complete, research-backed settings reference for the OM System OM-1 Mark II across four photography genres: Landscape, Nature/Wildlife, Portrait, and Dogs/Action. It also covers foundational photography theory and art — the exposure triangle, light, colour, composition, and artistic vision — to explain *why* these settings work. Settings are compiled from OM System official guides, Phil Norton's comprehensive walkthrough, Mcaughtry's landscape spreadsheets, Martin Belan's dog action testing, MarcR's comparison of Rob Trek & Steven Ingram techniques, Luminescent Photo's bird/wildlife secrets, and DPReview/Mu-43 community field reports.

The skill serves dual purpose:
1. **Reference:** The agent answers camera settings questions directly from this knowledge base.
2. **Telegram Q&A:** The agent delivers settings answers to the user via Telegram.

## When to Use

- User asks "what settings for landscape/nature/portrait/dogs on my OM-1 Mark II?"
- User asks about specific features: Live ND, ProCapture, Subject Detection, Hi-Res, Focus Bracketing
- User wants to configure Custom Modes C1-C4
- User asks about autofocus setup for specific subjects
- User asks about photography theory or art: exposure triangle, composition, light, colour theory, DOF, the decisive moment
- User asks about how settings relate to theory, or why specific settings are chosen
- User asks for photography learning resources or how to develop their eye

## Camera Key Specifications

- Sensor: 20.4 MP Stacked BSI Live MOS (Micro Four Thirds)
- Processor: TruePic X
- AF: 1,053-point Quad Pixel AF with AI Subject Detection
- Subject Detection: Birds, Dogs/Cats, Humans (Face/Eye), Cars, Motorcycles, Planes, Trains
- Burst: 50 fps C-AF (SH2), 120 fps S-AF (SH1)
- IBIS: 8.5 stops (body only), 8.5 stops Sync IS
- Custom Modes: C1, C2, C3, C4 on mode dial
- Computational: Live ND (up to ND128), Live GND, Hi-Res (50MP handheld, 80MP tripod), Focus Bracketing/Stacking, ProCapture, Live Composite

---

## Photography Theory & Art

This section covers the foundational theory that underpins every setting choice in this guide. Understanding *why* a setting works is more important than memorising the numbers — it lets you adapt in the field when conditions change.

### The Exposure Triangle

Three variables control every exposure. Changing one forces you to adjust at least one other to maintain the same exposure. This reciprocal relationship is the bedrock of photography.

**Aperture (f-stop)**
The size of the lens opening. Measured in f-numbers: f/1.2 (wide open, lots of light, shallow depth of field) → f/16 (tiny opening, little light, deep depth of field). Each full stop halves or doubles the light: f/2.8 → f/4 → f/5.6 → f/8 → f/11 → f/16.

- Wide apertures (f/1.2–f/2.8): shallow DOF, subject isolation, dreamy bokeh. Use for portraits and wildlife where you want the subject to pop.
- Mid apertures (f/5.6–f/8): sharpest optical performance on most MFT lenses, moderate DOF. Use for landscape and general photography.
- Small apertures (f/11–f/16): deep DOF for front-to-back sharpness. On MFT, diffraction visibly softens the image beyond f/8 — use f/11 only when maximum DOF is non-negotiable.

DOF is also affected by: (1) focal length — longer lenses have shallower DOF at the same f-stop; (2) subject distance — closer subjects have shallower DOF; (3) sensor size — MFT has roughly 2× the DOF of full-frame at equivalent field of view.

**Shutter Speed**
How long the sensor is exposed to light. Controls motion rendering.

- Fast (1/1000s–1/8000s): freezes action. Birds in flight, running dogs, sports. The OM-1's electronic shutter can reach 1/32000s.
- Moderate (1/125s–1/500s): stops casual human movement. Portraits, walking subjects.
- Slow (1/15s–1/60s): handheld limit with IBIS. Environmental with motion blur.
- Very slow (1s–60s+): intentional blur. Smooth water, light trails, star trails. Tripod required.

Handheld rule of thumb without stabilisation: 1/(2 × focal length) for MFT. With the OM-1's 8.5-stop IBIS, you can handhold dramatically slower — ½s at 12mm is achievable with good technique.

**ISO (Sensor Sensitivity)**
Amplifies the signal from the sensor. Higher ISO = brighter image but more noise and reduced dynamic range.

- Base ISO (200 on the OM-1): maximum dynamic range, cleanest shadows. Use whenever light allows.
- ISO 400–1600: negligible noise on the OM-1's stacked sensor. Good DR retention.
- ISO 3200–6400: visible but manageable noise. Still very usable with modern NR (Topaz, Lightroom AI).
- ISO 12800+: noise becomes structural. Use only when the alternative is no shot at all.

Important: ISO does not *cause* noise — it reveals noise already present from photon shot noise (the randomness of light itself). Raising ISO in low light is better than underexposing at base ISO and pushing in post, because the OM-1 applies analogue gain before the ADC, preserving shadow detail.

**The Trade-off Table**
| Goal | Aperture | Shutter | ISO | Genre |
|---|---|---|---|---|
| Freeze action | Wide open (or auto) | Fast (1/2000s+) | Auto/higher | Wildlife, Dogs |
| Deep DOF | f/5.6–f/8 | Whatever works (tripod) | 200 (base) | Landscape |
| Shallow DOF | f/1.2–f/2.8 | 1/125s+ | Auto/low | Portrait |
| Smooth water | f/8–f/11 | 1s–30s (ND) | 200 | Landscape |
| Low light | Wide open | As slow as possible | Higher | All |

### Light — The Raw Material

Light is photography. The camera is just a box that records it. Mastering light is more important than mastering settings.

**Quality**
- **Hard light:** Direct sun, bare flash. Sharp shadows, high contrast, saturated colours. Good for: dramatic landscapes, black-and-white, emphasising texture.
- **Soft light:** Overcast sky, window light, diffused flash. Gentle shadows, smooth tonal transitions. Good for: portraits, woodland, flowers, dogs (reduces harsh shadows on fur).

**Direction**
- **Front light:** Sun behind you. Even illumination, flat dimensionality. Easy exposure. Good for: wildlife (AF performs best), documentation shots. Weak for: drama, texture.
- **Side light:** Sun at 90°. Sculpts with shadow, reveals texture. The most versatile light direction. Good for: landscape (especially morning/evening), portraits with character, emphasising surface detail.
- **Backlight:** Sun behind subject. Creates rim light, silhouettes, and glow. Beautiful but technically challenging — AF struggles, exposure needs compensation. Good for: golden hour portraits, atmospheric landscape, translucent subjects (leaves, petals). Approach: spot meter on subject, +0.7 to +1.3 EV, or expose for rim and let subject silhouette.

**Golden Hour & Blue Hour**
- **Golden hour:** ~1 hour after sunrise and before sunset. Warm, directional, low-contrast light. Long shadows add depth. The universal "make everything look beautiful" light. Use for: landscape, portrait, wildlife (animals are more active), dogs.
- **Blue hour:** ~20–40 minutes before sunrise and after sunset. Cool, even, ethereal light. Sky is deep blue; artificial lights begin to glow. Use for: cityscapes, seascapes, moody landscape. Requires tripod — exposures are long.
- **Midday sun:** Harsh, overhead, colour-washed. Generally avoided but usable: (1) seek shade or use diffusion for portraits; (2) embrace high contrast for black-and-white; (3) use a polariser to cut glare and deepen skies.

**Overcast & Diffuse Light**
Clouds are nature's softbox. Overcast days produce flat, shadowless light — excellent for woodland (no dappled hotspots), waterfalls (no blown highlights), intimate landscapes, and dog photography (no harsh shadows across the face). The challenge is flat contrast: add bite in post with a gentle S-curve.

### Colour Theory

Colour is a compositional tool, not an accident. Deliberate colour choices can make an image sing.

**Colour Temperature (White Balance)**
Measured in Kelvin. The camera's WB setting neutralises colour casts so whites appear white — but "accurate" isn't always "right."

| Temp (K) | Light Source | Character |
|---|---|---|
| 2000–3000 | Candle, tungsten, sunrise/sunset | Very warm, golden |
| 3500–4500 | Fluorescent, early morning | Neutral-warm |
| 5000–5500 | Daylight flash, midday sun | Neutral (baseline) |
| 6000–7500 | Overcast, shade, window light | Cool |
| 8000–10000 | Deep shade, blue sky | Very cool, blue cast |

Creative WB strategies:
- **Keep sunset warmth:** Set WB to "Daylight" (~5500K) instead of Auto — preserves the golden glow the camera would otherwise neutralise.
- **Enhance mood:** Dial WB deliberately warm for cosy scenes, deliberately cool for cold/bleak atmosphere.
- **Black-and-white preview:** Set picture mode to Monochrome but shoot RAW+JPEG — the EVF shows tonal relationships while RAW preserves full colour.

**Colour Harmony**
- **Complementary colours:** Opposite on the colour wheel (blue/orange, red/green, yellow/purple). Natural tension — the classic "teal & orange" film look. Use for: golden hour landscapes (warm light + blue sky), autumn against evergreen.
- **Analogous colours:** Adjacent on the wheel (blue/teal/green). Harmony and calm. Use for: seascapes, forest scenes, misty mornings.
- **Monochromatic:** Variations of a single hue. Elegant and cohesive. Use for: fog, snow, desert, minimalist compositions.
- **Colour isolation:** One vivid colour against a muted or complementary background. Extremely powerful for subject emphasis. Example: a red coat in a grey cityscape, a yellow flower in green foliage.

**Practical Colour in the Field**
- The OM-1's **Colour Creator** (Menu → Camera 1 → Picture Mode → Colour Creator) lets you shift hue and saturation along 30 axes. Use for in-camera colour grading when shooting JPEG.
- **Polarising filter:** Deepens blue skies, cuts reflections on water/leaves, increases colour saturation naturally. Rotate to adjust strength.
- Shoot RAW: white balance and colour grading are fully adjustable in post without quality loss.

### Composition — The Visual Grammar

Composition is the arrangement of elements within the frame. It guides the viewer's eye and tells them what matters. These are principles, not rules — learn them, then break them deliberately.

**Rule of Thirds**
Divide the frame into a 3×3 grid. Place key elements on the intersections or along the lines. This creates tension and flow that centred compositions lack.
- Horizons: on the lower third (emphasises sky) or upper third (emphasises land).
- Eyes in a portrait: on the upper third intersection.
- The OM-1 can display a rule-of-thirds grid in the EVF (INFO cycle).

**Leading Lines**
Lines that draw the eye into and through the frame: roads, paths, rivers, fences, shorelines, branches, architectural edges. Diagonal lines create the strongest sense of movement. Converging lines (vanishing point perspective) add depth and scale. The line should ideally lead *to* the subject, not away from it.

**Framing**
Use elements in the scene to create a natural frame around the subject: doorways, windows, tree branches, arches, rock formations. Framing adds depth, context, and focuses attention. It can also hide distracting elements.

**Negative Space**
The empty area around the subject. Generous negative space creates mood — isolation, scale, minimalism, calm. Pair with a small subject against a vast background (bird against sky, person against sea). The subject should face *into* the negative space, not out of the frame.

**Symmetry & Patterns**
Mirrored compositions feel stable, formal, and satisfying. Reflections in water are the most accessible form of symmetry. Breaking a pattern — one element that doesn't conform — creates instant visual tension and a focal point.

**Foreground Interest**
A strong foreground anchors the composition and creates depth: rocks in a seascape, flowers in a landscape, a texture or pattern close to the lens. For wide-angle landscape, get low and close to foreground elements — this is what separates snapshots from crafted images.

**Visual Weight & Balance**
Elements have different visual weight: bright areas weigh more than dark, sharp more than blurred, large more than small, warm colours more than cool, human faces more than objects. A balanced composition distributes weight so the image feels stable (or deliberately unbalanced for tension).

**The Golden Ratio (≈1.618)**
The golden spiral/ratio is a more organic alternative to the rule of thirds. Subjects placed along the spiral curve feel naturally harmonious. It appears everywhere in nature — nautilus shells, flower petal arrangements, spiral galaxies. Use it as a compositional guide rather than a rigid grid.

**The Decisive Moment (Henri Cartier-Bresson)**
The split-second when all elements — subject, gesture, light, composition — converge into a single perfect frame. This is the heart of action and street photography. Technique: anticipate the peak of action (the leap, the glance, the interaction), pre-compose, and use burst mode (ProCapture gives you a 70-frame retroactive window). The OM-1's SH2 25fps is designed for exactly this.

### The Art of Photography

Settings make a correctly exposed image. Art makes a photograph.

**Storytelling Through Images**
Every photograph should answer: what do I want the viewer to feel? A landscape isn't just a place — it's solitude, awe, peace, or power. A wildlife shot isn't just an animal — it's behaviour, relationship, or a moment of wildness. Before pressing the shutter, identify the story. Let it guide every decision: composition, light, DOF, timing.

**Emotion & Mood**
Mood comes from the interplay of light, colour, and composition:
- **Drama:** Side light, deep shadows, strong contrast, darker exposure, cool or desaturated colour.
- **Peace:** Soft diffuse light, negative space, harmonious colours, gentle tonal transitions.
- **Joy:** Warm light, vibrant colour, dynamic composition, peak action.
- **Mystery:** Fog, backlight/silhouette, shallow DOF with subject partly obscured, blue hour tones.

**Patience & Presence**
The best photographers spend more time observing than shooting. Watch how light moves across a landscape. Learn an animal's behaviour patterns. Wait for the cloud to reach the right position, the wave to break, the bird to turn its head. Presence — being fully engaged with the scene rather than chimping the rear screen — produces better images than technical perfection ever will.

**Developing Your Eye**
Practical exercises:
1. **One lens, one month:** Use only one focal length. You'll learn to see the world in that perspective.
2. **Shoot from one spot:** Don't move. Find 10 different compositions from the exact same position. Forces you to see what's already there.
3. **Study paintings, not photos:** The Old Masters solved composition, light, and colour centuries before cameras existed. Vermeer for window light, Caravaggio for chiaroscuro, Turner for atmosphere.
4. **Reverse-engineer images you love:** Identify the aperture, shutter speed, light direction, focal length, composition structure, and colour palette. Recreate the setup on your own camera.

**Taking vs. Making**
- **Taking a photograph:** Reacting. Seeing something interesting, raising the camera, pressing the shutter. Passive.
- **Making a photograph:** Creating. Pre-visualising the final image, choosing position/lens/settings/time of day/weather to realise that vision. Active.

The OM-1's Custom Modes (C1–C4) exist to serve this second approach — each mode is a pre-visualised setup for a specific way of making images.

### How Theory Connects to Settings

Every setting recommendation in the genre sections below is a deliberate application of theory:

| Theory Principle | Landscape Setting | Wildlife Setting | Portrait Setting | Dog Setting |
|---|---|---|---|---|
| Exposure Triangle balance | A-mode, ISO 200 fixed, aperture controlled for DOF | S-mode, auto ISO, shutter-speed priority for motion freeze | A-mode, wide aperture for shallow DOF, auto ISO | S-mode, fast shutter priority, auto ISO |
| Light direction awareness | Golden hour, side-light for texture | Front light for best AF performance | Back/side light for depth and mood | Overcast diffuse light (flattering on fur) |
| DOF theory | Deep DOF (f/5.6–f/8) for front-to-back sharpness | Shallow when possible for subject isolation vs busy backgrounds | Shallow (f/1.2–f/2.8) for portrait separation | Mid DOF (f/4–f/6.3) for action forgiveness |
| Compositional intent | Foreground interest, leading lines, rule of thirds horizon | Rule of thirds, negative space in direction of movement | Eye placement on upper third, negative space for gaze direction | Eye-level shooting, action room in frame |
| Colour strategy | Warm golden hour, polariser for sky depth | Natural profile, keep warm colour ON | Portrait profile, warm skin tones | Natural, keep warm colour ON for fur |
| The Decisive Moment | Wait for light to hit the peak | ProCapture for BIF takeoff, anticipate behaviour | Catch the genuine expression, not the posed one | ProCapture SH2 for the exact leap moment |

---

## Custom Mode (C1-C4) Recommendations

Custom Modes on the mode dial let you save complete camera configurations for instant recall. Here is the recommended C1-C4 layout:

| Custom Mode | Genre | Key Profile |
|---|---|---|
| C1 | Nature / Wildlife | Birds in flight, wildlife action. Shutter priority, C-AF, Bird detection, SH2 25fps |
| C2 | Landscape | Tripod landscape, long exposure. Aperture priority, Live ND ready, Hi-Res ready |
| C3 | Portrait | People, face/eye detect. Aperture priority, Face+Eye priority, S-AF or C-AF |
| C4 | Dogs / Action | Dog running/action. Shutter priority, C-AF-TR, Dog detection, ProCapture SH2 |

To save a Custom Mode: configure all desired settings → Menu → Camera 1 → Custom Modes → Assign to Custom Mode → Choose C1-C4.

Set "Reset Settings" to OFF if you want changes during a shoot to persist. Set to ON if you want each mode dial turn to recall a pristine starting point.

---

## 1. LANDSCAPE PHOTOGRAPHY SETTINGS

### Core Exposure Settings

| Setting | Recommendation | Notes |
|---|---|---|
| Shooting Mode | A (Aperture Priority) or M (Manual) | A for handheld walk-around; M for tripod work |
| Aperture | f/5.6 – f/8.0 | Sweet spot for MFT sharpness. f/11 only when max DOF needed (diffraction starts at f/8) |
| Shutter Speed | Varies / Auto ISO | Use tripod + remote release below 1/60s |
| ISO | 200 (base) | Stay at base ISO whenever possible for maximum dynamic range |
| ISO Auto | OFF for tripod; ON for handheld (200–3200 cap) | Keep noise minimal |
| White Balance | Auto (Keep Warm Color: OFF for LE) | Custom WB for critical colour accuracy |
| Picture Mode | Natural (Mode 3) | Flat profile for maximum post-processing latitude; shoot RAW |
| Metering | ESP (Evaluative) | Reliable for most scenes; spot meter for high-contrast scenes |

### AF Settings for Landscape

| Setting | Recommendation |
|---|---|
| AF Mode | S-AF (Single AF) |
| AF Target | Single small point |
| AF+MF | ON (allows manual focus ring override) |
| Focus Peaking | ON (Red, High sensitivity) |
| Magnify | Assign to a button for critical focus check |
| Focus Bracketing | ON (set for focus stacking when deep DOF needed: 8–15 shots, focus differential 3–5) |

### Computational Features for Landscape

**Live ND (Neutral Density Simulation)**
- Access via: B mode on mode dial or assign to button
- ND2 (1 stop) through ND128 (7 stops)
- Use for: smooth water, cloud motion, waterfalls
- Tip: The OM-1 Mark II's Live ND is optical — no colour cast unlike physical ND filters
- ISO stays at 200; camera composites multiple exposures in real time

**Live GND (Graduated ND)**
- NEW in OM-1 Mark II
- Simulates graduated ND filter — darkens sky while keeping foreground bright
- 3 strengths: Soft, Medium, Hard
- Adjustable transition zone position via touch screen

**Hi-Res Shot (Tripod)**
- 80MP equivalent (10368×7776)
- Requires tripod + static subject
- Menu: Camera 2 → Hi-Res Shot → Tripod
- Processing: in-camera or OM Workspace (better)
- 14-bit RAW output — excellent dynamic range

**Hi-Res Shot (Handheld)**
- 50MP equivalent (8160×6120)
- Handheld, slight movement tolerated
- Faster than tripod mode, good for moderate DR scenes

**Focus Bracketing / Stacking**
- Menu: Camera 2 → Focus Bracketing
- Set: Number of shots (8–15), Focus Differential (3–5)
- Focus Stacking: In-camera merging (JPEG only, 3–15 shots)
- Post-processing: Stack in Photoshop/Helicon Focus for maximum quality

**Live Composite**
- Access via: B mode or Manual
- Use for: star trails, light painting, fireworks, lightning
- Camera composites only new light — no overexposure
- Set base exposure, then watch image build on screen; stop when done

**HDR**
- Menu: Camera 2 → HDR
- Brackets 3–7 shots, auto-merged
- Use when tripod not available for high DR scenes

### Sunset Landscape — Proven Field Setup

Your personal sunset configuration, battle-tested in the Surrey Hills:

| Setting | Recommendation | Why |
|---|---|---|
| Shooting Mode | **A** (Aperture Priority) | Aperture control for DOF; Auto shutter is fine at sunset light levels |
| Aperture | **f/8 – f/11** | Sunsets have low contrast — stopped down ensures front-to-back sharpness from foreground to sky. At f/11 on MFT you're past the diffraction sweet spot, but the sun-disc and horizon benefits from the extra DOF more than it suffers resolution loss |
| ISO | **200 (fixed)** | Base ISO for maximum dynamic range — critical for the high-contrast sunset sky vs dark foreground |
| Live ND | **ON (ND4–ND32)** | Smooths water, clouds, and light trails. ND4-8 for early sunset; ND16-32 for deep twilight long-exposures |
| White Balance | **Cloudy (6000K)** | Preserves and enhances the warm golden/red tones the camera's Auto WB would neutralise. **This is the key difference from Auto** |
| Metering | **Spot** | Meter off the mid-brightness sky near the sun-disc, not the sun itself (blown highlights) or the dark foreground (overexposed sky). Dial ±0.3–0.7 EV to taste |
| Picture Mode | Natural (Mode 3) or Vivid | Vivid for JPEG shooters who want the rich colours straight out of camera; Natural for RAW latitude |
| AF | S-AF, single point on horizon/infinity | Infinity focus or focus ⅓ into the scene for hyperfocal sharpness. Turn Subject Detection OFF — it's pointless on a landscape |
| Image Stabiliser | S-IS AUTO (handheld) / OFF (tripod) | Standard practice — IS OFF when on a solid tripod |
| Drive | Single or 2-sec self-timer | Self-timer for tripod work to eliminate shutter press shake |

**Sunset Pro Workflow:**

1. Arrive 45 min before sunset. Set up facing the sun-disc. Compose with foreground interest (rocks, heather, a tree silhouette).
2. Set A mode, f/8–f/11, ISO 200, Cloudy WB, Spot metering.
3. Meter off the sky just beside the sun. Dial exposure comp to taste — the OM-1's highlight/shadow warning (INFO toggle) is invaluable here.
4. Enable Live ND if there's water or cloud motion in the frame. At sunset, ND8–ND32 gives ½–4 second exposures as the light drops.
5. As the sun dips below the horizon, re-meter — the sky opposite the sun (the "second sunset") often peaks in colour 10–20 minutes after the disc is gone.
6. For true deep-blue twilight, switch Auto ISO (200–6400) as the light fully fades, or switch to manual with a longer shutter.

### Landscape Quick Settings Card

```
┌─────────────────────────────────────────┐
│        OM-1 MK2 LANDSCAPE CARD          │
├─────────────────────────────────────────┤
│ Mode: A (Aperture Priority)             │
│ Aperture: f/5.6–f/8                     │
│ ISO: 200 (fixed)                        │
│ WB: Auto / Custom                       │
│ AF: S-AF, single point                  │
│ Metering: ESP                           │
│ Drive: Single / 2-sec self-timer        │
│ IS: ON (S-IS AUTO)                      │
│ File: RAW (or RAW+JPEG)                 │
│                                         │
│ TRIPOD SHOTS:                           │
│ → IS: S-IS OFF (menu)                   │
│ → Use remote shutter or 2-sec delay     │
│ → Enable Live ND/GND as needed          │
│ → Hi-Res for 80MP when still subject    │
│                                         │
│ HANDHELD:                               │
│ → IS: S-IS AUTO                         │
│ → Hi-Res Handheld (50MP) for moderate DR│
│ → Auto ISO 200-3200 if light changes    │
│                                         │
│ 🌅 SUNSET SETTINGS (SURREY HILLS PROVEN):   │
│ → Mode A, f/8–f/11, ISO 200            │
│ → Metering: Spot, WB: Cloudy (6000K)   │
│ → Live ND ON (ND4–ND32)                │
│ → Arrive 45min early, re-meter post-set │
└─────────────────────────────────────────┘
```

### Landscape Lens Recommendations for MFT
- M.Zuiko 7-14mm f/2.8 PRO (ultra-wide)
- M.Zuiko 8-25mm f/4 PRO (versatile wide-to-standard)
- M.Zuiko 12-40mm f/2.8 PRO II (standard zoom, weather-sealed)
- M.Zuiko 12-100mm f/4 IS PRO (all-in-one travel landscape)
- M.Zuiko 40-150mm f/2.8 PRO (telephoto compression landscapes)

### Pro Tips for Landscape

1. Use the **highlight/shadow warning** display (toggle with INFO button) to check for blown highlights
2. **Base ISO 200** gives the OM-1 ~½ stop more dynamic range than ISO 400+
3. Enable **Live View Boost** (Menu → Gear → D3) to see shadow detail in bright sunlight
4. **Live ND** is usable handheld at wider angles thanks to IBIS
5. For seascapes with moving water: start at Live ND32 (5 stops), adjust to taste
6. The **horizon level** overlay (INFO cycle) is invaluable — the OM-1 has both pitch and roll indicators
7. Use **Anti-Shock** (0 sec) with mechanical shutter for tripod work to eliminate shutter shock
8. For long exposures past 60 seconds, switch to **BULB mode** with a remote release (or use Live Time)
9. OM Workspace software provides better Hi-Res RAW processing than in-camera
10. Mcaughtry recommends **Thomas Eisl's exposure methodology** for maximum DR: expose to the right (ETTR) using the histogram, protecting highlights

---

## 2. NATURE / WILDLIFE PHOTOGRAPHY SETTINGS

### Core Exposure Settings

| Setting | Rob Trek Method | Steven Ingram Method | Consensus Recommendation |
|---|---|---|---|
| Shooting Mode | S (Shutter Priority) | P (Program Auto) | S (Shutter Priority) — you need speed control |
| Shutter Speed | 1/2000s default; 1/1000s perched; 1/4000s fast BIF | 1/500s min wildlife; 1/1600s BIF; 1/4000s hummingbirds | 1/2000s BIF; 1/500s perched; 1/4000s fast action |
| ISO Range | 200–102400 | 200–12800 | 200–12800 (avoid extreme high ISO; Topaz DeNoise for rescue) |
| ISO Auto | Yes | Yes | Yes — modern stacking sensor handles noise well |
| Picture Mode | Natural (Standard) | Natural (Mode 3) | Natural — flat for RAW processing |
| White Balance | Auto | Auto, Keep Warm Color On | Auto with Keep Warm Color ON |
| Noise Filter | Off | Standard | Off (for RAW) / Low (for JPEG) |
| Noise Reduction | Off | Auto | Auto (long exposure NR only) |
| Metering | ESP | Subject-Aware, Backlit-Aware AI Enhanced | ESP (evaluative) — camera's AI metering is excellent |

### Autofocus Settings — The Critical Section

The OM-1 Mark II AF system is the most important configuration for wildlife. Get this right, and keeper rates soar.

| AF Setting | Recommendation | Why |
|---|---|---|
| AF Mode | C-AF (Continuous AF) | Tracks moving subjects continuously |
| C-AF + Tracking | C-AF-TR only for subject at predictable distance | C-AF (without TR) for erratic movement — many pros prefer non-TR |
| Subject Detection | **Birds** for birds; **Animals** for mammals | AI detection finds eyes/heads; in Mk II, C-AF forced to C-AF-TR with Subject Detection ON |
| C-AF Sensitivity | **+1 or +2** for fast/erratic subjects | Higher = faster refocus when distance changes. +2 for BIF, 0 for slow wildlife |
| AF Scanner | Mode 2 or Mode 3 | Determines behaviour when AF loses subject: Mode 2 = moderate re-scan, Mode 3 = aggressive |
| AF Target Mode | Mid-size zone or All Points | Single point for perched/stationary; zone for BIF. Smaller zone = stickier tracking |
| AF Limiter | Set if using telephoto (e.g., 10m–∞ for long lens) | Prevents lens hunting to close focus |
| AF+MF | ON | Allows instant manual override |
| Pre-MF | Set to a custom button | Pre-focus at a set distance for quick acquisition |
| AF-ON (Back Button Focus) | Configured via Button Settings | Separates AF from shutter — essential wildlife technique |

### Drive Mode & Burst Settings

| Setting | Recommendation |
|---|---|
| Drive Mode | Silent Sequential SH2 (25 fps C-AF) |
| ProCapture SH2 | ON — captures 70 frames BEFORE full shutter press. Essential for BIF takeoff |
| ProCapture SH1 | ON — 120 fps S-AF, for predictable action |
| Frame Count Limiter | OFF (or set to 50 to avoid endless bursts) |
| Anti-Shock | Silent (electronic shutter) — zero shutter shock |

### Subject Detection Deep-Dive

**Bird Detection:**
- Works best with clear eye visible
- Struggles when bird is heavily obscured by branches — switch to single AF point
- Small birds at distance: smaller AF target zone improves hit rate (MarcR recommendation)
- The Mk II improves stickiness vs Mk I — bird re-acquisition after obstruction is better

**Animal Detection:**
- Covers mammals: deer, foxes, bears, etc.
- Works with dogs/cats but dedicated Dog/Cat mode is better for pets
- Eye detection works on larger mammals; falls back to head/body on smaller/distant subjects

### Nature/Wildlife Quick Settings Card

```
┌─────────────────────────────────────────┐
│      OM-1 MK2 NATURE/WILDLIFE CARD      │
├─────────────────────────────────────────┤
│ Mode: S (Shutter Priority)              │
│ Shutter: 1/2000s (BIF) / 1/500s (perch) │
│ Aperture: Auto (lens wide open)         │
│ ISO: Auto (200–12800)                   │
│ WB: Auto (Keep Warm ON)                 │
│ Metering: ESP                           │
│ Drive: SH2 Silent 25fps                 │
│                                         │
│ AUTOFOCUS:                              │
│ → C-AF + Bird/Animal Subject Detection  │
│ → C-AF Sensitivity: +2 (BIF) / +1 (gen) │
│ → AF Target: Mid zone (BIF) / All (gen) │
│ → AF Scanner: Mode 3                    │
│ → Back-button AF (AF-ON) recommended    │
│ → ProCapture SH2 ON (70 pre-frames)     │
│                                         │
│ BUTTON ASSIGNMENTS:                     │
│ → AF-ON: Back-button focus              │
│ → Fn1: Subject Detection toggle         │
│ → Fn2: AF Target Mode cycle             │
│ → DOF Preview: ProCapture toggle        │
│ → Lens Fn: AF Limiter toggle            │
└─────────────────────────────────────────┘
```

### Wildlife Lens Recommendations
- M.Zuiko 300mm f/4 IS PRO (the gold standard for wildlife; pairs with MC-14 1.4x and MC-20 2.0x TCs)
- M.Zuiko 150-400mm f/4.5 TC1.25x IS PRO (ultimate wildlife zoom with built-in TC)
- M.Zuiko 100-400mm f/5-6.3 IS (affordable super-tele zoom; excellent value)
- M.Zuiko 40-150mm f/2.8 PRO + MC-14 (210mm f/4) (compact and bright; good for larger wildlife)

### Pro Tips for Wildlife

1. **Back-button focus (AF-ON)** decouples AF from the shutter — acquire focus with thumb, shoot with index. Game-changer.
2. **C-AF Sensitivity +2** is Rob Trek's and many pros' choice for BIF. Makes AF snappier when distance changes rapidly.
3. **ProCapture SH2** is the OM-1's killer feature — 70 frames buffered before you fully press the shutter. You'll never miss the takeoff moment again.
4. The **AF Limiter** on long lenses prevents the lens from hunting to minimum focus distance. Set to 10m–∞ for most wildlife.
5. **SH2 25fps** is the sweet spot — 50fps generates too many frames to cull without significant benefit.
6. For small birds in foliage, **disable Subject Detection** and use single AF point — the camera gets confused by branches.
7. Enable **Focus Peaking** (assigned to a button) for quick manual focus check.
8. Shoot with the **sun at your back** whenever possible — AF performs best with front-lit subjects.
9. The **electronic shutter (Silent)** is completely silent and vibration-free — use it always for wildlife.
10. Format your card after every shoot — ProCapture fills buffers fast.

---

## 3. PORTRAIT PHOTOGRAPHY SETTINGS

### Core Exposure Settings

| Setting | Recommendation | Notes |
|---|---|---|
| Shooting Mode | A (Aperture Priority) | Control depth of field via aperture |
| Aperture | f/1.2–f/2.8 (individual); f/4–f/5.6 (group) | Wide open for subject isolation; stop down for groups |
| Shutter Speed | 1/125s minimum (static); 1/250s+ (moving) | IBIS covers you but subject motion doesn't stop |
| ISO | Auto (200–3200) or fixed 200 | Lower is cleaner; auto handles changing light |
| White Balance | Auto (Keep Warm ON for skin tones) | Or custom WB with grey card for critical work |
| Picture Mode | Portrait (Mode 4) or Natural | Portrait mode warms skin; Natural for editing latitude |
| Metering | ESP or Centre-Weighted | Centre-weighted helps expose for face |
| Colour Creator | Adjust warmth/contrast to taste | Menu → Camera 1 → Picture Mode → Colour Creator |

### Face/Eye Detection & AF

| AF Setting | Recommendation |
|---|---|
| AF Mode | S-AF (static portraits) / C-AF (moving/environmental portraits) |
| Subject Detection | **Face/Eye Priority ON** |
| Face Selection | ON — camera prioritises registered faces; use joystick to switch between detected faces |
| Eye Detection | Auto — camera chooses nearest eye. Can force Left/Right Eye priority in menu |
| AF Target | Single point + Face Priority (camera overrides point when face detected) |
| C-AF Sensitivity | 0 (balanced) for walking subjects; -1 for posed portraits |
| AF+MF | ON — fine-tune focus on eyelashes |

### Portrait Quick Settings Card

```
┌─────────────────────────────────────────┐
│        OM-1 MK2 PORTRAIT CARD           │
├─────────────────────────────────────────┤
│ Mode: A (Aperture Priority)             │
│ Aperture: f/1.2–f/2.8 (single subject)  │
│          f/4–f/5.6 (group)              │
│ ISO: Auto (200–3200)                    │
│ WB: Auto (Keep Warm ON)                 │
│ AF: S-AF + Face/Eye Priority            │
│ Metering: Centre-Weighted               │
│ Drive: Single / Low sequential (5fps)   │
│ IS: S-IS AUTO                           │
│ File: RAW + JPEG                        │
│                                         │
│ FACE/Eye DETECTION:                     │
│ → Face Priority: ON                     │
│ → Eye Detection: Auto                   │
│ → Face Selection: ON                    │
│ → C-AF for moving subjects: ON          │
│                                         │
│ BUTTON ASSIGNMENTS:                     │
│ → Fn1: Face Priority toggle             │
│ → Multi Selector: Switch detected face  │
│ → Record: One-touch WB                 │
└─────────────────────────────────────────┘
```

### Portrait Lens Recommendations
- M.Zuiko 45mm f/1.2 PRO (the ultimate MFT portrait lens — 90mm equivalent)
- M.Zuiko 75mm f/1.8 (superb compression, razor sharp — 150mm equivalent)
- M.Zuiko 25mm f/1.2 PRO (environmental portraits — 50mm equivalent)
- M.Zuiko 17mm f/1.2 PRO (full-body environmental — 34mm equivalent)
- Sigma 56mm f/1.4 DC DN (affordable, sharp — 112mm equivalent)
- M.Zuiko 40-150mm f/2.8 PRO (versatile portrait zoom with beautiful compression)

### Pro Tips for Portraits

1. The 45mm f/1.2 PRO renders a magical transition from sharp to soft — the "feathered" bokeh is legendary.
2. **Face Priority + Eye Detection** works for both humans and pets. For dogs, use Dog/Cat detection instead (in C4 or Wildlife mode).
3. For environmental portraits (subject in context), stop down to f/4–f/5.6 and use the 17mm or 25mm PRO lenses.
4. Enable **e-Portrait** (JPEG only) for in-camera skin smoothing — subtle and natural-looking.
5. Use **Highlight/Shadow control** (assign to a button) to pull shadow detail on backlit faces.
6. OM-1's **Face Selection** lets you register up to 8 faces — camera prioritises them when detected.
7. For golden hour backlit portraits, enable **Spot Metering** and meter on the face, +0.7 EV exposure compensation.
8. The tilting screen enables low-angle and waist-level portrait compositions.

---

## 4. DOG / ACTION PHOTOGRAPHY SETTINGS

### Core Exposure Settings

Based on Martin Belan's tested settings, Rob Trek's action methodology, and community field reports from Mu-43 and DPReview.

| Setting | Recommendation | Notes |
|---|---|---|
| Shooting Mode | S (Shutter Priority) | Speed is everything for dog action |
| Shutter Speed | 1/1000s walking/running; 1/2000s–1/4000s fast action/jumping | Dogs accelerate fast — err on the faster side |
| Aperture | Auto (lens wide open or f/5.6–f/8 for more DOF) | f/2.8 for isolation; f/5.6 for group dogs or more forgiving focus |
| ISO | Auto (200–6400) | Modern NR handles this range well; outdoor daylight keeps it low |
| White Balance | Auto (Keep Warm ON) | Natural skin and fur tones |
| Picture Mode | Natural (Mode 3) | Flat for post-processing |
| Metering | ESP | Reliable for most dog scenarios |

### Autofocus — The Dog Settings

The single most important section. Dogs move unpredictably — the AF setup makes or breaks keeper rates.

| AF Setting | Recommendation | Why |
|---|---|---|
| AF Mode | C-AF (Continuous AF) | Tracks moving subject. **Important Mk II note:** With Subject Detection ON, AF is forced to C-AF-TR. |
| Subject Detection | **Dogs (🐕)** | Dedicated dog/cat AI detection. Finds eyes, head, then body. |
| C-AF Sensitivity | **+1** (recommended) or **0** (balanced) | +1 for running/jumping dogs; 0 for walking/posed. +2 may be too twitchy. |
| AF Target Mode | Mid-size square (flexible) or All Points | Mid-size zone keeps AF from jumping to background. Single point makes tracking harder for fast dogs. |
| AF Scanner | Mode 2 or 3 | Mode 2 = balanced; Mode 3 = aggressive re-acquisition |
| AF Limiter | Set to appropriate range for your lens | Prevents hunting to close focus when dog runs near |
| AF+MF | ON | Allows override if detection picks wrong subject |
| Back-Button AF | Assign AF-ON button | Separate focus from shutter — game changer for tracking |

### Drive Mode & Burst

| Setting | Recommendation |
|---|---|
| Drive Mode | Silent Sequential SH2 (25 fps C-AF) or Sequential L (10 fps mechanical) |
| ProCapture SH2 | ON — 70 pre-frames capture the exact jump/leap moment |
| ProCapture SH1 | ON — 120 fps S-AF, for predictable motion (dog running straight at you) |
| Frame Count Limiter | 50 frames or OFF |

### Dog Action Quick Settings Card

```
┌─────────────────────────────────────────┐
│         OM-1 MK2 DOG/ACTION CARD        │
├─────────────────────────────────────────┤
│ Mode: S (Shutter Priority)              │
│ Shutter: 1/2000s (running)              │
│          1/4000s (fast action/jumping)   │
│ Aperture: Auto (f/4–f/8 preferred)      │
│ ISO: Auto (200–6400)                    │
│ WB: Auto (Keep Warm ON)                 │
│ Metering: ESP                           │
│ Drive: SH2 Silent 25fps C-AF            │
│                                         │
│ AUTOFOCUS (CRITICAL):                   │
│ → C-AF + Dog Subject Detection (🐕)     │
│ → C-AF Sensitivity: +1                  │
│ → AF Target: Mid-size zone              │
│ → AF Scanner: Mode 3                    │
│ → Back-button AF (AF-ON)                │
│ → ProCapture SH2: ON (70 pre-frames)    │
│                                         │
│ BUTTON ASSIGNMENTS:                     │
│ → AF-ON: Back-button focus              │
│ → Fn1: Subject Detection toggle         │
│ → Fn2: C-AF Sensitivity adjust          │
│ → Record: ProCapture toggle             │
│ → Lens Fn: AF Limiter toggle            │
│                                         │
│ MARTIN BELAN'S TESTED SETUP:            │
│ → AF Mode: C-AF-TR                      │
│ → C-AF Sensitivity: 0                   │
│ → AF Target: Mid-size square            │
│ → ISO: 800 (overcast); Auto otherwise   │
│ → Aperture: f/6.3 (for DOF latitude)    │
│ → Keeper rate reported: 80–85%          │
└─────────────────────────────────────────┘
```

### Dog Photography Lens Recommendations
- M.Zuiko 40-150mm f/2.8 PRO (the dog action workhorse — fast AF, bright, weather-sealed)
- M.Zuiko 45mm f/1.2 PRO (portrait-style dog shots, beautiful bokeh — 90mm equivalent)
- M.Zuiko 12-40mm f/2.8 PRO II (wide-angle action when dog is very close)
- M.Zuiko 100-400mm f/5-6.3 IS (dogs at distance — beach runs, field work)
- Sigma 56mm f/1.4 DC DN (budget-friendly dog portrait/action on a budget — 112mm equivalent)
- Olympus 75mm f/1.8 (compression shots, beautiful rendering)

### Pro Tips for Dog Photography

1. **Get low.** Shoot at the dog's eye level — this transforms the image from snapshot to portrait.
2. **Subject Detection works best when the dog's eye is visible.** If the dog is looking away or the eye is obscured, detection drops to head/body which is less precise.
3. **For dogs running towards you:** C-AF + Dog Detection + Mid-size zone + C-AF Sensitivity +1. The OM-1 Mk II handles this very well — keeper rate should be 80%+.
4. **For dogs running across the frame:** Pan with the dog. IBIS helps stabilise vertical shake; you manage horizontal motion.
5. **ProCapture SH2 is magical for dogs.** Buffer captures 70 frames before you fully press the shutter. You will catch the exact moment paws leave the ground.
6. **Use continuous lighting, not flash.** Flash can startle dogs and causes redeye/green-eye in animals.
7. **Treats and squeakers** held near the lens get the dog looking at the camera.
8. **SH2 25fps** is plenty — 50fps creates enormous culling workload for marginal gain.
9. The **electronic shutter** is silent — doesn't spook nervous dogs like a mechanical shutter can.
10. **Community note from Mu-43:** Some users report C-AF issues on Mk II with fast dogs. If keeper rate is low, try: (a) reduce C-AF Sensitivity to 0, (b) use all AF points instead of zone, (c) try C-AF without Subject Detection as a fallback.
11. **AF Limiter tip:** If the dog is 5–30m away, set limiter to 5m–∞. Prevents the lens racking to minimum focus when the dog briefly disappears behind an obstacle.

---

## 5. UNIVERSAL BEST PRACTICES (All Genres)

### Button Setup Template

These button assignments are recommended by multiple pro photographers (Phil Norton, Rob Trek, Mcaughtry):

| Button | Function | Genre |
|---|---|---|
| AF-ON | Back-button focus | ALL |
| Fn1 (top) | Subject Detection toggle | Wildlife/Dogs |
| Fn2 (top) | AF Target Mode cycle | ALL |
| Record (top) | ProCapture toggle | Wildlife/Dogs |
| DOF Preview (front) | Live ND toggle | Landscape |
| Lens Fn | AF Limiter toggle | Wildlife/Dogs |
| Multi Selector (joystick) | AF point position + Face select | ALL |
| AEL/AFL | Exposure lock (spot meter) | Landscape/Portrait |
| ISO | ISO adjust | ALL |

### Critical Menu Settings (Set Once)

| Menu Item | Recommendation | Menu Path |
|---|---|---|
| Anti-Shock | 0 sec (electronic first curtain) | Camera 2 → Anti-Shock |
| Noise Reduction (Long Exposure) | Auto | Camera 1 → Noise Reduction |
| Noise Filter | Off (RAW) / Low (JPEG) | Camera 1 → Noise Filter |
| ISO-Auto Set | 200 (low) to 12800 (high) | Camera 1 → ISO-Auto Set |
| Minimum Shutter Speed (ISO-Auto) | 1/125s (standard) or 1/2000s (action) | Camera 1 → ISO-Auto Set → Min. Shutter |
| Image Stabiliser | S-IS AUTO | Camera 2 → Image Stabiliser |
| Flicker Reduction | Auto | Camera 2 → Flicker Reduction |
| High Res Shot | RAW+JPEG | Camera 2 → Hi-Res Shot |
| Rec View | Off | Gear → Rec View |
| Live View Boost | On (for bright sunlight) | Gear → D3 → Live View Boost |
| AF Illuminator | Off | AF Menu → AF Illuminator |
| Quick Sleep Mode | 1 min | Gear → Power Saving |
| Auto Power Off | 5 min | Gear → Power Saving |

### File Settings

- **RAW:** Always. The OM-1 RAW files have excellent latitude (especially at ISO 200).
- **JPEG:** L-SF (Large Super Fine) if you shoot JPEG. Natural picture mode for most genres.
- **Colour Space:** Adobe RGB for print work; sRGB for web/social media.
- **Copyright Info:** Set in Menu → Gear → Copyright Settings.

### Exposure Compensation Strategy

- **Landscape:** 0 EV baseline; bracket ±1 EV for high contrast (HDR merge later)
- **Wildlife:** -0.3 to -0.7 EV to protect highlights on white/bright birds
- **Portrait:** +0.3 to +0.7 EV for brighter skin tones
- **Dogs:** 0 EV baseline; -0.3 EV to protect white/bright fur highlights

---

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
