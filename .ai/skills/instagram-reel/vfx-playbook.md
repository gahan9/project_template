<!-- SPDX-License-Identifier: MIT -->

# VFX playbook - perception only

Cinematic finishing for Instagram portrait Reels. Every recipe below is
optical or editorial. None of them rewrite a person, a face, or a product.

the effects should look as ultra realistic vfx editor artist.

add effects for transition between shots as cinematic as possible, opening effect as well as the ending effect too!

## Optical floor (every effect)

Treat the timeline like a finishing artist, not a transition pack:

- **Shutter-matched motion blur.** At 30 fps, 180-degree shutter is ~1/60.
  Whip and smash-zoom kernels follow the pan/zoom vector. No isotropic blur.
- **Eased interpolation.** Ease-in-out or ease-out on zooms and pans. Linear
  Ken Burns reads as a slideshow.
- **One grade.** Lifted blacks, restrained highlights, mild vignette, grain
  that matches the noisiest source clip. Do not recolor skin, hair, product
  paint, or logos.
- **Light wrap and bloom.** Flares and leaks sit in screen/add space; they
  wrap over highlights, they do not stamp a PNG sticker.
- **Edge-only chromatic.** If used, a few pixels at the frame edge on a fast
  whip. Never on irises or teeth.
- **Hold the identity lock.** If an effect needs a warp mesh, face landmarks,
  or inpaint, it is illegal in this skill. Pick another recipe.

## Opening effects (pick one)

Apply on shot 1, covering the first 8-20 frames (hook window is 1 second).

| Name | What the viewer feels | How (perception only) |
|------|-----------------------|------------------------|
| Smash-zoom in | Thrown into the scene | Exponential zoom 1.0 -> 1.35-1.55, slight downward pan, radial streak in the last 6 frames |
| Anamorphic leak-in | Cinema open | Horizontal streak flare from off-frame, intensity peaks ~0.25s then decays; source still sharp |
| Film-gate flash | Print-roll start | 2-4 frame white/amber overexposure + grain settle, then the grade |
| Whip-in | Arriving mid-motion | Directional motion blur from one edge, resolves to a locked Ken Burns |
| Crash-zoom + bloom | Hero beat | Fast ease-out zoom, highlight bloom on speculars only, no skin smooth |
| Silhouette match | Mystery then reveal | Start tight/dark on a non-face shape (instrument, doorway, product), zoom out to the locked frame |

Never open on a static logo card. Motion or a claim first.

## Shot-to-shot transitions (pick per cut)

Use a different recipe when two adjacent cuts would otherwise match. Hold
each transition to 6-12 frames unless the beat is a smash cut (1-2 frames).

| Name | Use when | How |
|------|----------|-----|
| Whip pan | Energy, location change | Directional blur along the intended pan; incoming shot blurs in from the opposite side |
| Optical flash | Color or product change | Sinusoidal add of 80-140 (8-bit) over 6-10 frames; incoming shot flashes down from the peak |
| Match-cut on motion | Same gesture, new clip | Cut on a shared direction or shape (strum, walk, pan). Do not morph faces to match |
| Smash zoom through | Entering a space | Outgoing zoom-in + radial streak; incoming continues the zoom and eases out |
| Light-leak dissolve | Softer emotional beat | Warm/cool elliptical leak, Gaussian-blurred, screen-blended; no identity warp |
| Speed ramp | Highlight a micro-moment | Ease into 0.4-0.6x, hold 8-12 frames, ramp out. Do not retiming-warp faces |
| Dip-to-color | Chapter change | 4-8 frames through black or a brand accent color, not through a generated face |
| Push-pull | Two stills | Outgoing zooms in while incoming zooms out (or the reverse), 10-12 frames |
| Smash cut | Joke, impact, beat drop | 0-2 frames, no blend. Use sparingly so the other cuts stay cinematic |

Illegal as a "transition": face morph, flow-warp across a person, style
transfer, swapping who is in the shot, recoloring a branded product.

## Ending effects (pick one)

Last 12-24 frames, then a hold the viewer can loop.

| Name | What it does | How |
|------|--------------|-----|
| Slow push-out + hold | Resolve | Zoom 1.12 -> 1.0, vignette up slightly, freeze last frame 8-12 frames |
| Leak to CTA | Brand close | Light leak climbs, badge/CTA already in the safe area, leak peaks as text holds |
| Freeze + Ken Burns out | Poster beat | Freeze on the payoff still, slow zoom out, no new people |
| Loop whip | Infinite scroll | Whip in the same direction as the open so frame 0 can replay; no smash-to-black |
| Film-burn hold | Editorial close | Warm overexposure + grain, settle on the CTA still |

Pair the ending with the opening: whip-in pairs with loop whip; smash-zoom in
pairs with slow push-out; leak-in pairs with leak to CTA.

## Grade (global, identity-safe)

A typical cinematic promo grade, applied after crop/zoom:

- Soft S-curve on luma (do not crush faces into silhouette unless the source
  already is).
- Slight warm highlight, slight cool in deep shadows - stop if product color
  or skin hue shifts enough to notice.
- Vignette 0.3-0.4 strength, not a tunnel.
- No frequency separation, no skin blur, no eye-whitening, no teeth whitening.

## On-screen type

Lower-third or badge in the vertical safe area (below the top 250px, above
the bottom 400px). One accent bar, two lines max. Fade or slide with the
shot; do not cover faces.

## Audio (notes only unless asked to mix)

Whoosh on whips, a short optical "hit" on flashes, music ducked 2 dB under
any VO. Do not invent licensed tracks. If no audio is in `<xyz-folder>`,
ship the picture spec and mark audio `TBD`.
