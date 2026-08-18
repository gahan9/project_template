---
name: market-regime-analyst
license: MIT
aliases:
  - regime-gate
  - market-breadth-analyst
version: "1.0.0"
description: >-
  Determines current market regime (risk-on/neutral/risk-off) from breadth,
  trend participation, distribution-day-style risk counting, and cross-asset
  macro ratios. Emits a 0-100 regime score and a net-exposure ceiling that
  fail-closed gates every downstream trade or sizing recommendation.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
triggers:
  - "market environment"
  - "market regime"
  - "is the market healthy"
  - "risk on or risk off"
  - "market breadth"
  - "should I be adding risk"
  - "distribution days"
delegates_to:
  - trading-analyst
  - portfolio-strategist
---

# Market Regime Analyst

## Purpose

Answer "how much risk is the environment allowing right now?" before any
single-name analysis happens. This skill implements the highest-value
structural idea in disciplined trading practice: **risk budget is decided
before candidates are found, not after.** Its output is a fail-closed gate,
not a suggestion — `trading-analyst` must not emit entry or sizing advice for
a direction this gate denies.

## When to Use

- Start of any multi-step trading analysis (thesis, portfolio review,
  rebalance) — this is always the first skill in the chain.
- A direct question about market health, breadth, or "should I add risk."
- Re-checking regime status after a market-moving event (FOMC, CPI, a large
  index move) before acting on a pending idea.

## When NOT to Use

- Single-name technical or fundamental analysis in isolation — those are
  `technical-chart-analyst` / `fundamental-news-analyst`; this skill supplies
  their risk-budget context, not their content.

## Instructions

### Inputs (use what is available; state what is missing)

1. **Breadth**: % of a broad index's constituents above their 200-day moving
   average, advance/decline trend, and new-highs-vs-new-lows trend. Source
   from a pasted CSV, chart image, or named public dataset with an as-of
   date.
2. **Trend participation**: % of constituents in a confirmed uptrend
   structure (see `technical-chart-analyst`'s stage definitions) vs. in
   distribution.
3. **Distribution-day-style risk count**: count of high-volume down closes
   (e.g., -0.2% or worse on above-average volume) in the trailing ~25
   sessions for the relevant index; more counts = more institutional
   selling pressure.
4. **Cross-asset macro ratios**: risk-on/risk-off proxies such as
   growth-vs-value relative strength, credit spreads direction, or a
   volatility index level/trend, when available.
5. If none of the above is available, say so explicitly and default the
   regime score to neutral (50) with a `LOW_DATA` flag — never infer a
   score from vibes.

### Scoring (0-100, deterministic)

6. Compute a 0-100 composite from the available inputs, weighting each
   available axis roughly equally, and disclose the weights actually used
   when an axis is missing (redistribute weight, do not silently zero-fill).
   Anchor points:
   - 80-100: broad-based uptrend, low distribution count, breadth expanding.
   - 55-79: constructive but mixed — some distribution or narrowing breadth.
   - 30-54: caution — rising distribution count, breadth deteriorating,
     defensive rotation visible.
   - 0-29: broad deterioration, high distribution count, breadth collapsing.
7. Show the sub-scores per axis, not only the composite.

### Net-exposure ceiling (the gate)

8. Map the composite score to a net-exposure ceiling and an explicit
   ACT/SCALE-IN/OBSERVE/AVOID directional gate for **new long risk**:

   | Score | Net-exposure ceiling | New-long gate |
   |---|---|---|
   | 80-100 | Up to full planned exposure | Open |
   | 55-79 | Reduced (e.g., 60-75% of planned) | Open, smaller size |
   | 30-54 | Defensive (e.g., 25-40% of planned) | New entries require SCALE-IN sizing only |
   | 0-29 | Cash-priority | Closed — `AVOID` for new long risk |

9. This ceiling is an input to `portfolio-strategist`'s sizing and to every
   `trading-analyst` verdict's confidence hard-floor override (see
   `trading-analyst/confidence-calibration.md`). It does not by itself force
   closing existing positions — that is a `portfolio-strategist` decision
   informed by this gate plus position-level thesis status.
10. Re-run this check whenever the request's data is stale (>5 sessions old)
    before relying on a prior score.

### Hard Rejects

| Violation | Reason |
|---|---|
| Assigning a regime score with no stated inputs or as-of date | Unauditable |
| Skipping this gate before issuing new-entry or sizing advice | Violates fail-closed risk ordering |
| Treating a single day's move as a regime change | One data point is noise, not a regime signal |
| Silently zero-filling a missing axis instead of disclosing reduced weighting | Hides the real confidence of the score |

## Output Format

- Per-axis sub-scores → composite score → net-exposure ceiling → explicit
  new-long gate (Open / Open-smaller / SCALE-IN-only / Closed).
- State data recency and any `LOW_DATA` flag prominently, before the score.

## References

- `trading-analyst/confidence-calibration.md` — how this gate feeds the hard
  floor override.
- `portfolio-strategist` — consumes the net-exposure ceiling for sizing.
- `technical-chart-analyst` — supplies the trend-participation/stage
  definitions this skill counts against.
- Methodological inspiration (concepts only, no code or text copied — see
  `THIRD_PARTY_NOTICES.md`): tradermonty/claude-trading-skills (MIT) —
  breadth/uptrend-ratio analysis, distribution-day monitoring, "risk before
  candidates" exposure coaching.
