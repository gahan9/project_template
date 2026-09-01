---
name: instagram-reel
license: MIT
aliases:
  - instagram-reels
  - ig-reel
  - portrait-reel
  - cinematic-reel
version: "1.0.0"
description: >-
  Builds catchy brand-promotion Instagram portrait Reels (1080x1920) from a
  source content folder: cinematic VFX opening, shot-to-shot transitions, and
  ending, plus caption and hashtags. Delegates copy to content-marketing-expert.
  Never changes person, face, or valuable attributes unless told explicitly.
  Use when asked for an Instagram reel, IG reel, 9:16 reel, brand promo reel,
  cinematic reel, or a reel from a folder.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
  - "**/*.jpg"
  - "**/*.jpeg"
  - "**/*.png"
  - "**/*.mp4"
  - "**/*.mov"
  - "**/*.webp"
triggers:
  - "instagram reel"
  - "ig reel"
  - "portrait reel"
  - "9:16 reel"
  - "brand promo reel"
  - "cinematic reel"
  - "reel from this folder"
  - "reel caption and hashtags"
delegates_to:
  - content-marketing-expert
metadata:
  authors: [gsaraiya]
  portability: Agent Skills open standard (Cursor, Claude Code, Copilot, Codex, Antigravity)
---

<!-- SPDX-License-Identifier: MIT -->

# Instagram Reel

Turn the media in `<xyz-folder>` into a catchy brand-promotion Instagram
portrait Reel: 1080x1920, cinematic VFX on the open / cuts / close, plus a
caption and hashtags. Copy and SEO come from `content-marketing-expert`. Edit
grammar stays identity-safe.

## Purpose

Produce a shippable Reel pack from a source folder: brief, timed shot list,
VFX spec (opening + every transition + ending), on-screen text, caption, and
hashtags. Prefer an editable spec the user can render; render locally only when
the toolchain is present.

## When to Use

- Instagram Reel, IG Reel, portrait Reel, 9:16 Reel.
- Brand-promotion video from photos and clips in a folder.
- Caption and hashtags for a Reel already storyboarded.
- Cinematic open / cut / close effects on existing footage.

## When NOT to Use

- YouTube Shorts or TikTok as the primary surface - still use this 9:16
  grammar, then re-cut hooks via `content-marketing-expert`.
- Long-form research or blog drafting - `content-marketing-expert` delegates
  that to `content-research-writer`.
- Face swap, beauty retouch, identity restyle, or generating a new person.
- Engagement-bait, fabricated claims, or undisclosed paid promotion. Refuse.

## Identity lock (non-negotiable)

STRICTLY DO NOT CHANGE PERSON/FACE or any valuable arrtibutes unless told explicitely... only play with perception, zoom, cuts, filters, effects and transition effects as needed between across.

Lock unless the user names the change in this turn:

| Locked | Allowed (perception only) |
|--------|---------------------------|
| Face, age, skin, hair, body | Crop, Ken Burns zoom/pan, speed |
| Who is in the frame, head count | Cut, whip, flash, light-leak, grade |
| Logos, product color, brand marks | Filters, grain, bloom, vignette |
| On-source text, tattoos, jewelry | Overlays in the safe area |
| Distinctive clothing / product shape | Motion blur, flares, speed ramps |

No morph, face warp, face replace, beauty smooth, body reshape, logo redraw,
or generative inpaint on a person or product. If a requested effect would
alter identity, drop the effect and say so in one line.

the effects should look as ultra realistic vfx editor artist.

add effects for transition between shots as cinematic as possible, opening effect as well as the ending effect too!

## Instructions

```
Reel Progress:
- [ ] 1. Inventory <xyz-folder>
- [ ] 2. ContentBrief + hooks via content-marketing-expert
- [ ] 3. Sequence shots (hook -> value -> CTA)
- [ ] 4. Spec opening VFX, every cut, ending VFX
- [ ] 5. Identity-lock pass on every shot
- [ ] 6. Caption + hashtags
- [ ] 7. Ensemble review + deliver
```

### 1. Inventory `<xyz-folder>`

`<xyz-folder>` is the source folder the user names (path, `@` mention, or
workspace folder). Do not invent media.

List every still and clip: path, type, duration if video, orientation, and
one-line content (what is visible - not a rewrite of who they are). Skip
unreadable files with a one-line reason.

Pick 4-8 strongest pieces. Prefer motion for the hook, a product or craft
beat in the middle, a group or payoff near the end. Still images are valid
when Ken Burns plus a cinematic grade carries them.

Infer brand voice from filenames, existing copy, overlays, and sibling files
in the folder. If the brand name is not in the folder, ask once.

### 2. Marketing layer

Load `content-marketing-expert` and run its intake through the five-pass
loop for this Reel only (not a multi-platform campaign unless asked).

Defaults when the user is silent:

| Field | Default |
|-------|---------|
| Goal | reach |
| Platforms | Instagram Reels |
| Audience | broad, layman |
| Mode | offline-first hybrid |
| Length | 20-35s |

Emit the ContentBrief before the shot list. Produce three hooks (curiosity,
pain-point, promise) and pick one for the first second.

Claims stay checkable. Placeholder numbers are `TBD-verify`.

### 3. Portrait spec

| Property | Value |
|----------|--------|
| Frame | 1080x1920, 9:16 |
| Frame rate | 30 fps unless source is 24/60 and matching is cleaner |
| Length | 15-90s; 20-35s for a single-idea promo |
| Safe area | No burned-in text in the top 250px or bottom 400px |
| Hook | Motion or a claim in the first 1s - never a logo sting |
| Grade | One look for the whole reel (see [vfx-playbook.md](vfx-playbook.md)) |

Fit landscape sources by center-weighted crop toward the subject. Do not
stretch. Do not letterbox.

On-screen text: <=6 words per beat, high contrast, outside the UI chrome.

### 4. VFX design

Read [vfx-playbook.md](vfx-playbook.md) before writing the shot list.

Every reel gets all three:

1. **Opening effect** on shot 1 (into the hook).
2. **Transition effect** on every shot boundary, cinematic, not a hard cut
   unless the playbook says a smash cut is the beat.
3. **Ending effect** on the last shot (hold, loop-whip, or light-leak to CTA).

Effects are optical and editorial: perception, zoom, cuts, filters,
transitions. They must read as a finishing-artist composite (motion blur that
matches shutter, eased interpolation, light wrap, grain that matches source)
not as a preset sticker.

Name each effect from the playbook. Do not invent a morph-through-face or a
generative restyle and call it a transition.

### 5. Caption and hashtags

Instagram caption, copy-paste ready:

```
<hook line - same promise as the first second>

<body - 2-5 short lines, one idea each>

<one CTA: save, share, or a comment keyword - not a stack>

<hashtags>
```

Hashtags: 3-5, specific over broad. No emoji walls. First line must stand
alone in the feed preview.

### 6. Ensemble review

Score through the five `content-marketing-expert` players (strategist,
educator, formatter, optimizer, amplifier). Formatter floor includes 1080x1920
and the identity lock. A reel that restyles a face does not ship.

### 7. Persist

Write the pack next to the source unless the user names another path:

```
<xyz-folder>/reel/
  brief.md
  shot-list.md
  vfx-spec.md
  caption.md
```

Do not overwrite source media. Rendered MP4, if any, is a new file. Ask
before a `content-marketing-expert` memory shot.

## Output Format

```markdown
## ContentBrief: <slug>
- Goal:
- Platforms: Instagram Reels
- Audience:
- Core promise:
- Mode:
- Constraints: 1080x1920, identity lock, length

## Hooks
A (curiosity):
B (pain-point):
C (promise):
Recommended: <A|B|C> - <one-line reason>

## Folder inventory
| File | Type | Use |
|------|------|-----|

## Shot list (1080x1920, 30fps)
| t | Source | Move | On-screen | VFX |
|---|--------|------|-----------|-----|
| 0.0-1.0 | ... | ... | ... | OPEN: <effect> |
| ... | ... | ... | ... | CUT: <effect> |
| last | ... | ... | ... | END: <effect> |

## Caption
<copy-paste block>

## Hashtags
<3-5 tags>

## Identity lock
- Faces / people unchanged: yes
- Logos / product color unchanged: yes
- Effects used: perception / zoom / cuts / filters / transitions only

## Ensemble review
| Player | Score | Note |
|--------|-------|------|
Equilibrium notes:

## Files written
- <path> - <purpose>
```

## Additional resources

- VFX catalog and optical rules: [vfx-playbook.md](vfx-playbook.md)
- Worked folder walkthrough: [examples.md](examples.md)
