---
name: om1-mark2-settings
description: "Use when the user asks about OM System OM-1 Mark II settings — landscape, nature/wildlife, portrait, dog/action, C1-C4 custom modes, Live ND/GND, autofocus, plus photography theory."
version: 1.5.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [photography, om-system, om1-mark2, camera-settings, landscape, wildlife, portrait, dogs, action, theory]
    triggers:
      - "OM-1"
      - "OM1 Mark II"
      - "OM System settings"
      - "camera settings for landscape/wildlife/portrait/dogs"
      - "Live ND"
      - "ProCapture"
---

# OM System OM-1 Mark II — Settings Skill

Knowledge lives in `references/om1-mark2.md`; this file is the entry point.

## Use when

- The user asks for settings on the OM-1 Mark II for landscape, nature/wildlife,
  portrait, or dog/action photography.
- The user asks about C1-C4 custom modes, Live ND, Live GND, High Res Shot,
  ProCapture, subject detection AF, or menu configuration.
- The user wants a quick settings cheat sheet (Telegram or email).
- The user asks about photography theory: exposure triangle, light, colour,
  composition, artistic vision.

## Pattern

1. Read `references/om1-mark2.md` for the full detail — specs, per-genre setting
   tables, custom-mode recipes, troubleshooting, pitfalls, theory.
2. Answer in the user's format: settings cards for Telegram, dark-theme HTML for
   email, plain lists for CLI.
3. The guide is the source of truth for this camera; do not invent menu names.

## Restore to Hermes

```bash
cp references/om1-mark2.md ~/.hermes/skills/user_skills/camera-gear/references/
```

(or install this directory as a standalone skill under `~/.hermes/skills/user_skills/`)
