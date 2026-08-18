<!-- SPDX-License-Identifier: MIT -->

# Confidence Calibration

A single 0-100 confidence score accompanies every verdict produced by the
trading-analyst skill family. The score is a **calibration estimate**, not a
probability of profit — it measures how well the stated evidence supports the
stated verdict, given known failure modes (small samples, stale data,
single-source reliance, regime mismatch).

## Inputs

Compute each axis on a 0-100 scale, then combine as specified below. Show the
per-axis scores in the report; never show only the final number.

| Axis | What it measures | 0 (worst) | 100 (best) |
|---|---|---|---|
| **Evidence agreement** | Do quant, fundamental, and technical lenses point the same direction? | All three disagree | All three agree |
| **Evidence count** | How many independent data points support the verdict? | 1 data point | 5+ independent points |
| **Data freshness** | How old is the newest material input? | Stale (>1 quarter for fundamentals, >5 sessions for price/news) | Same-session |
| **Sample size** | For any statistical claim (win rate, pattern hit rate, backtest), is n large enough? | n < 20 events | n >= 100 events, out-of-sample checked |
| **Regime alignment** | Does `market-regime-analyst`'s score support taking risk in this direction? | Regime gate denies risk budget | Regime score strongly favors this direction |

### Combination rule

```
confidence = round(
    0.30 * evidence_agreement
  + 0.20 * evidence_count
  + 0.15 * data_freshness
  + 0.20 * sample_size
  + 0.15 * regime_alignment
)
```

Weights are fixed and disclosed so the score is reproducible and auditable —
never silently reweight axes to reach a target number. If an axis does not
apply to the request (e.g., no statistical claim is made, so "sample size" is
moot), redistribute its weight proportionally across the remaining axes and
say so explicitly in the report.

### Hard floor overrides

Regardless of the weighted formula, apply these overrides in order — the
first one that matches wins:

1. If `market-regime-analyst`'s gate denies risk budget for the direction in
   question, confidence is capped at **30** and the verdict is forced to
   `OBSERVE` or `AVOID`.
2. If the only supporting evidence is a single chart pattern or a single news
   headline with no corroborating data point, confidence is capped at **40**.
3. If a statistical claim's sample size is below 20 events, confidence is
   capped at **35** regardless of how good the hit rate looks — small samples
   are not evidence of an edge (see `quant-methods`).

## Verdict thresholds

| Confidence | Verdict | Meaning |
|---|---|---|
| 80-100 | **ACT** | Evidence agrees across lenses, fresh, adequately sampled, regime-aligned. Full planned size (subject to `portfolio-strategist` caps). |
| 60-79 | **SCALE-IN** | Directionally supported but one axis is weak (e.g., thin sample, partial regime alignment). Reduced initial size with a defined add-trigger. |
| 40-59 | **OBSERVE** | Mixed or incomplete evidence. Document the thesis and the trigger that would upgrade it; take no new risk. |
| 0-39 | **AVOID** | Evidence disagrees, regime-blocked, or a hard-floor override fired. State explicitly what is missing. |

## Anti-patterns

- **Confidence inflation**: rounding 62 up to "high confidence" prose while
  reporting 62 in the table. The prose tone must match the tier, not the raw
  number.
- **Single-axis certainty**: a perfect technical setup with no fundamental or
  regime check cannot exceed the `SCALE-IN` tier (see hard floor override 2).
- **Confidence laundering**: running the same weak evidence through multiple
  skills and treating each skill's agreement as independent confirmation. Only
  count an axis once per underlying data source.
