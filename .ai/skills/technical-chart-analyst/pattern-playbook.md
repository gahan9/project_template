<!-- SPDX-License-Identifier: MIT -->

# Pattern Playbook

Named structural patterns, their required conditions, and the base rate
caveat that must accompany every one of them (see `trade-critic` for how base
rates factor into confidence).

## Stage model (four-stage)

| Stage | Description | Key evidence |
|---|---|---|
| 1 — Basing | Sideways range after a decline; volatility contracting | Price crossing a flattening long moving average repeatedly, volume declining |
| 2 — Advancing | Persistent uptrend | Higher highs/higher lows; price above a rising moving average; volume expands on up moves |
| 3 — Topping | Sideways after an advance | Increasing volatility, failed breakouts, volume expanding on down moves |
| 4 — Declining | Persistent downtrend | Lower highs/lower lows; price below a falling moving average |

Only Stage 1 → Stage 2 transitions and continuation setups within Stage 2 are
higher-quality long candidates. A "breakout" attempted from Stage 3 or 4
structure is lower quality by definition — state this explicitly.

## Volatility contraction pattern (VCP-style base)

**Required conditions** (all four, or the pattern is "not yet confirmed"):

1. Prior uptrend or basing structure precedes the contraction.
2. Each successive pullback within the base is shallower than the last
   (progressively tighter swings).
3. Volume dries up as the range tightens, then expands on the breakout
   attempt.
4. A definable breakout price (top of the range/prior pivot high) and
   invalidation price (below the most recent contraction low) both exist.

**Base rate caveat**: even well-formed contraction patterns fail a material
fraction of the time (varies by market regime — failure rates rise sharply
in Stage 3/4 regimes per `market-regime-analyst`). Never state a contraction
pattern's implied success rate without a named source and sample size; if
none is available, state "base rate unknown — treat as directional bias, not
a probability."

## Flag / pennant (continuation)

- A brief, shallow, roughly parallel-channel pullback after a sharp
  directional move, on declining volume. Breakout in the direction of the
  prior move, confirmed by volume expansion. Invalidation: a close back
  inside the channel against the implied direction.

## Range / rectangle

- Horizontal support and resistance tested at least twice each. Breakout
  direction is not presumed — score both directions until volume or a
  fundamental catalyst confirms one. Invalidation: a close back inside the
  range after a breakout attempt (a "failed breakout," which is itself
  actionable information about the opposite direction).

## Distribution top (structural, not a single-day event)

- Increasing volatility, multiple failed rally attempts, volume expanding on
  down days and shrinking on up days, while `market-regime-analyst`'s
  distribution-day count is elevated. Requires multiple confirming sessions,
  not one down day — see the hard reject on single-day regime calls in
  `market-regime-analyst`.

## What is NOT a pattern

- A single candlestick shape with no surrounding structural context.
- Any "pattern" whose boundaries were drawn after the fact to fit the
  outcome (hindsight pattern-fitting) — boundaries must be statable *before*
  the outcome is known, i.e., reproducible from the data alone.
