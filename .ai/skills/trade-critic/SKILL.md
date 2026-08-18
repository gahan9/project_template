---
name: trade-critic
license: MIT
aliases:
  - red-team-trade
  - signal-postmortem
version: "1.0.0"
description: >-
  Red-team pass applied to every thesis before delivery — base-rate and
  sample-size checks, narrative/confirmation/recency bias flags, a
  pre-mortem of the most likely loss path, and a mandatory, specific
  invalidation condition. The final gate before any trading-analyst output.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
triggers:
  - "critique this trade"
  - "what am I missing"
  - "play devil's advocate"
  - "why might this be wrong"
  - "postmortem"
  - "second opinion"
delegates_to:
  - quant-methods
  - trading-analyst
---

# Trade Critic

## Purpose

Be the skeptical second opinion every thesis must survive before it is
delivered. This skill's job is to find the strongest reason the thesis from
`fundamental-news-analyst`, `technical-chart-analyst`, or
`portfolio-strategist` is wrong — not to rubber-stamp it. A thesis that
cannot state its own best counter-argument and a concrete invalidation
condition is not ready to ship.

## When to Use

- Immediately before any `trading-analyst` verdict is finalized (this is the
  last step in the composed workflow — see `.ai/subagents/trading-desk.md`).
- A user explicitly asks for a critique, second opinion, or "what am I
  missing."
- Reviewing a closed trade's outcome to extract a lesson (postmortem).

## When NOT to Use

- As a substitute for building the original thesis — this skill critiques,
  it does not originate the fundamental/technical/quant case.

## Instructions

### Base-rate check

1. For any claim of the form "setups like this tend to work," demand: the
   named base rate, its sample size, and its source. If no base rate is
   available, state "base rate unknown" explicitly rather than letting the
   claim stand unchallenged — this itself should cap confidence per
   `trading-analyst/confidence-calibration.md`.
2. Compare the claimed edge against the honest base rate for random/no-edge
   outcomes where relevant (e.g., a pattern with a claimed 65% win rate is
   less impressive if the underlying instrument rallies 55% of all
   comparable periods regardless of pattern).

### Sample-size check

3. Apply `quant-methods`'s n >= 20 floor and n >= 100-for-confidence
   guidance explicitly; state the actual n behind every statistical claim
   in the thesis being critiqued, and downgrade confidence if the thesis
   omitted it.
4. Flag "cherry-picked window" risk: does the supporting data span multiple
   market regimes (per `market-regime-analyst`), or only one favorable
   stretch?

### Bias flags (name the specific bias, not a generic disclaimer)

5. **Confirmation bias**: did the thesis selectively cite only the evidence
   supporting the desired direction while omitting contrary evidence that
   was available? Name the specific omitted evidence if identifiable.
6. **Narrative bias**: is the thesis driven by a compelling story ("this
   company will definitely win because...") without the story being
   reducible to the quantitative/fundamental/technical evidence actually
   presented? A good narrative is not evidence.
7. **Recency bias**: is the thesis overweighting the most recent data point
   or the most recent regime, ignoring a longer, more representative
   sample?
8. **Anchoring**: is a price target anchored to an arbitrary reference (a
   prior all-time high, a round number) rather than derived from the
   valuation/technical method actually used?

### Pre-mortem

9. State the single most likely way this specific trade loses money —
   concretely (e.g., "guidance disappoints next quarter and the stock gaps
   below the stated stop," not "the market could go down"). A generic
   pre-mortem is not a pre-mortem.
10. Cross-check the pre-mortem scenario against `market-regime-analyst`'s
    current gate — is the regime itself a live risk to this thesis?

### Mandatory invalidation condition

11. Every thesis reaching this skill must have (or be assigned here, if
    missing) a specific, falsifiable invalidation: a price level, an event,
    or a data threshold that — if it occurs — means the thesis was wrong
    and the position should be reduced or closed. "I'll reassess if things
    change" is not an invalidation condition.
12. State the invalidation as an input to `portfolio-strategist`'s SELL
    flag definition, not as a separate, disconnected note.

### Revised confidence

13. Output a revised confidence score alongside the original, with the
    specific driver of any change (e.g., "sample size n=14, below the n>=20
    floor — capped at 35" or "no contrary evidence found, no revision").
    Never revise silently — always show original vs. revised.

### Hard Rejects

| Violation | Reason |
|---|---|
| A thesis passed through with no stated invalidation condition | Non-falsifiable; violates the mandatory-invalidation rule |
| A pre-mortem that only restates generic market risk | Not a pre-mortem; provides no decision-relevant information |
| Letting an unsupported base-rate claim stand unchallenged | Fails the base-rate check |
| Revising confidence without stating the specific driver | Non-auditable |
| Treating a compelling narrative as evidence on its own | Narrative bias by definition |

## Output Format

Use the "Critique-only" template in `trading-analyst/output-templates.md`
when critique is the whole request; otherwise append the base-rate,
bias-flag, pre-mortem, and revised-confidence sections to whichever template
the parent request used.

## References

- `quant-methods` — supplies the sample-size and base-rate math this skill
  applies.
- `market-regime-analyst` — the regime context every pre-mortem must
  cross-check.
- `portfolio-strategist` — consumes this skill's invalidation condition for
  the SELL flag.
- Methodological inspiration (concepts only, no code or text copied — see
  `THIRD_PARTY_NOTICES.md`): tradermonty/claude-trading-skills (MIT) —
  signal-postmortem review framework, edge-strategy-reviewer overfitting and
  sample-size critique.
