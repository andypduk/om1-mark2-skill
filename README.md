# OM System OM-1 Mark II — Hermes skill backup

Private backup of the Hermes skill *OM System OM-1 Mark II — Ultimate Settings Guide & Photography Theory*.

The live copy lives at `/root/.hermes/skills/user_skills/camera-gear/references/om1-mark2.md`
inside the `camera-gear` skill. This repository is the off-machine backup.

## What's in here

| Path | What it is |
|---|---|
| `om1-mark2.md` | The full guide, assembled from `parts/` (regenerated automatically on push) |
| `parts/part-01.md` ... `part-05.md` | The guide in five sequential chunks — the source of truth in this repo |
| `skill/SKILL.md` | Drop-in Hermes skill wrapper (frontmatter + index) |
| `build.sh` | `cat parts/part-*.md > om1-mark2.md` — run locally if the workflow ever fails |
| `.github/workflows/assemble.yml` | Concatenates the parts into `om1-mark2.md` on every push to `main` |

## Contents of the guide

1. System prompt / persona and trigger phrases
2. Core knowledge graph and response guardrails
3. Camera key specifications
4. Photography theory and art (exposure triangle, light, colour, composition, vision)
5. Custom mode C1-C4 recommendations
6. Genre settings — landscape, nature/wildlife, portrait, dog/action
7. Universal best practice, troubleshooting, common pitfalls
8. Telegram Q&A workflow and one-shot settings recipes
9. Reference sources and resources

## Restore

```bash
git clone git@github.com:andypduk/om1-mark2-skill.git
cd om1-mark2-skill
./build.sh                      # rebuild om1-mark2.md if needed
cp om1-mark2.md ~/.hermes/skills/user_skills/camera-gear/references/om1-mark2.md
```

Or install as a standalone skill:

```bash
mkdir -p ~/.hermes/skills/user_skills/om1-mark2-settings/references
cp skill/SKILL.md ~/.hermes/skills/user_skills/om1-mark2-settings/
cp om1-mark2.md ~/.hermes/skills/user_skills/om1-mark2-settings/references/
```

Version: 1.5.0 (as recorded in the guide frontmatter).
