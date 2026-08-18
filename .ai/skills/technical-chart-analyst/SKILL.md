---
name: technical-chart-analyst
license: MIT
aliases:
  - chart-analyst
  - technical-analyst
version: "1.0.0"
description: >-
  Chart-expertise skill for multi-timeframe trend structure, stage analysis,
  base/contraction patterns, volume confirmation, and support/resistance —
  including reading pasted chart images. Confirms or contradicts the
  fundamental thesis; never treated as sufficient evidence alone.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
triggers:
  - "read this chart"
  - "chart pattern"
  - "support and resistance"
  - "is this a good entry"
  - "breakout"
  - "trend structure"
  - "volume confirmation"
delegates_to:
  - quant-methods
  - trading-analyst
---

# Technical Chart Analyst

## Purpose

Read price structure across timeframes — trend stage, base/contraction
patterns, and volume — as one input among several, never as the sole basis
for a call. Chart reading is pattern recognition with a documented failure
rate; this skill exists to keep that failure rate visible (via base rates in
`trade-critic`) rather than presenting pattern-matching as certainty.

## When to Use

- A user pastes or references a price chart (image, CSV, or described
  levels) and wants a structural read.
- Evaluating entry/exit timing for a thesis already established by
  `fundamental-news-analyst` or `market-regime-analyst`.
- Confirming or contradicting a fundamental catalyst with price action.

## When NOT to Use

- As the sole justification for a trade recommendation — combine with
  `fundamental-news-analyst` and `market-regime-analyst` per the
  persona-consistency check in `trading-analyst`.
- Intraday/tick-level market-microstructure questions this skill does not
  model (order flow, market making) — say so rather than guessing.

## Instructions

### Multi-timeframe structure first

1. Establish the **higher timeframe** trend context before the entry
   timeframe (e.g., weekly trend before daily setup). A daily "breakout"
   against a weekly downtrend is a lower-quality signal — state this
   explicitly rather than ignoring the conflict.
2. Classify trend stage using a four-stage model: **Stage 1** (basing,
   sideways after a decline), **Stage 2** (advancing, higher highs/higher
   lows, price above rising moving averages), **Stage 3** (topping,
   sideways after an advance), **Stage 4** (declining, lower highs/lower
   lows). State which stage and the evidence (moving-average slope,
   swing-structure) for the classification.

### Base and contraction patterns

3. A valid base/contraction pattern requires: (a) a prior uptrend or
   basing structure to contract from, (b) progressively tighter price
   swings or a defined range, (c) volume drying up during the contraction,
   and (d) definable boundaries (a specific breakout level and a specific
   invalidation level). A pattern missing any of (a)-(d) is "not yet
   confirmed" — say so rather than forcing a label onto ambiguous structure.
4. State the specific breakout trigger price and the specific invalidation
   price for every pattern called. These two numbers feed
   `quant-methods`'s stop-based position sizing directly.

### Volume confirmation

5. A breakout on below-average volume is a lower-confidence signal — apply
   the confidence-calibration hard floor (single-evidence-point cap) unless
   corroborated by a second independent signal (fundamental catalyst,
   regime alignment).
6. A pattern breaking down on rising volume while the market regime is
   deteriorating is a stronger confirmation of weakness than the same move
   in isolation — cross-reference `market-regime-analyst`.

### Support, resistance, and indicator discipline

7. Identify support/resistance from actual prior price reaction (swing
   highs/lows, prior consolidation ranges, round-number/psychological
   levels only when they coincide with real reaction), not from arbitrary
   lines.
8. Use **no more than three indicators**, and only non-redundant ones (e.g.,
   do not stack RSI with Stochastic — both measure similar momentum; pick
   one momentum, one trend, one volume indicator if three are used at all).
   State why each indicator used adds information the others do not.

### Reading a pasted chart image

9. When given a chart image: state what timeframe and instrument it appears
   to show, describe the visible trend stage, any pattern boundaries, and
   volume behavior, and flag explicitly anything illegible (axis labels,
   exact price levels) rather than inventing precise numbers from an
   unclear image.
10. Never state a precise numeric price level read from an image with high
    confidence if the image resolution or labeling makes it genuinely
    ambiguous — say "approximately" and note the uncertainty.

### Hard Rejects

| Violation | Reason |
|---|---|
| A pattern call with no stated breakout and invalidation price | Not usable for sizing; unfalsifiable |
| Treating a single chart pattern as sufficient evidence for a full-size trade | Violates the multi-lens persona-consistency check in `trading-analyst` |
| Inventing precise price levels from an illegible chart image | Fabricated precision |
| Ignoring a higher-timeframe trend conflict | Systematically overstates lower-timeframe signal quality |
| Stacking >3 or redundant indicators to manufacture false confirmation | Indicator redundancy is not independent evidence |

## Output Format

- Higher-timeframe context → stage classification with evidence → pattern
  (if any) with breakout/invalidation levels → volume read → indicator notes
  (if used) → explicit confidence-relevant caveats (image ambiguity, volume
  quality, timeframe conflict).

## References

- `pattern-playbook.md` — named base/contraction pattern definitions and
  volume-confirmation checklists.
- `quant-methods` — consumes the breakout/invalidation levels for sizing.
- `market-regime-analyst` — the trend/breadth context this skill's
  stage-classification should agree or conflict with, explicitly.
- Methodological inspiration (concepts only, no code or text copied — see
  `THIRD_PARTY_NOTICES.md`): tradermonty/claude-trading-skills (MIT) —
  stage analysis and volatility-contraction pattern discipline, weekly-chart
  technical-analyst workflow.
