---
name: portfolio-strategist
license: MIT
aliases:
  - portfolio-manager
  - rebalance-advisor
version: "1.0.0"
description: >-
  Portfolio-level allocation, concentration/correlation review, and
  rebalance planning — target weights, tolerance-band vs calendar
  rebalancing, sector/correlation caps, trim/add/hold decisions, tax-aware
  sequencing, and cash as an explicit position. Consumes the regime gate
  and never sizes above it.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
triggers:
  - "portfolio review"
  - "rebalance"
  - "asset allocation"
  - "should I trim"
  - "diversification"
  - "concentration risk"
  - "cash allocation"
delegates_to:
  - market-regime-analyst
  - quant-methods
  - trade-critic
---

# Portfolio Strategist

## Purpose

Own the portfolio-level decision layer: given current holdings, a stated (or
inferred) target allocation, and the regime gate from
`market-regime-analyst`, produce a rebalance plan and per-position
hold/add/trim/sell flags. Single-name conviction from
`fundamental-news-analyst` / `technical-chart-analyst` never overrides
portfolio-level risk limits — concentration and correlation caps are
enforced here regardless of how good any one thesis looks.

## When to Use

- Reviewing an existing portfolio's allocation, concentration, and risk.
- Producing a rebalance plan (trim/add sequencing) toward target weights.
- Deciding whether a new idea fits within existing concentration/sector/
  correlation limits before it is sized.
- Answering "how much cash should I be holding right now."

## When NOT to Use

- Building the single-name thesis itself — that is `fundamental-news-analyst`
  / `technical-chart-analyst`; this skill consumes their conclusions.
- Computing the underlying risk math (Sharpe, correlation, Kelly) — that is
  `quant-methods`; this skill applies the math to allocation decisions.

## Instructions

### Target allocation and drift

1. State the target weights (asset class, sector, or single-name, as
   applicable) — if the user has not specified targets, ask, or use a
   stated risk-budget default (e.g., equal-weight sector caps) and disclose
   the assumption explicitly rather than inventing "reasonable" targets
   silently.
2. Compute drift per holding/sleeve: `drift = current_weight -
   target_weight`. State both the absolute and relative drift (5 points on
   a 10% target is a much bigger relative move than 5 points on a 40%
   target).

### Tolerance-band vs calendar rebalancing

3. Default to **tolerance-band** rebalancing (rebalance when drift exceeds a
   stated band, e.g., ±5 percentage points absolute or ±25% relative,
   whichever is tighter) over fixed-calendar rebalancing, since band-based
   rebalancing reacts to what actually happened rather than an arbitrary
   date. State which policy is in effect and why, per
   `rebalance-policy.md`.
4. Do not recommend a rebalance trade for drift inside the stated band —
   unnecessary turnover has a cost (fees, taxes, bid/ask) that must be
   weighed explicitly, not ignored.

### Concentration, sector, and correlation caps

5. Enforce explicit caps and state them: e.g., single-name cap, single-
   sector cap, and a correlated-cluster cap computed via
   `quant-methods`'s rolling correlation method. A thesis exceeding a cap is
   flagged for TRIM regardless of conviction — state this trade-off
   explicitly rather than silently overriding the cap.
6. Treat cash as an explicit position with its own target weight and
   rationale (dry powder for `market-regime-analyst` risk-off periods,
   near-term liquidity need, or a stated opportunity-cost tradeoff) — never
   an unexamined residual.

### Position-level flags

7. Assign each holding one of **HOLD / ADD / TRIM / SELL**, each with a
   named reason: thesis intact (HOLD), thesis strengthened and under cap
   (ADD), over a cap or thesis weakening (TRIM), thesis invalidated per
   `trade-critic`'s invalidation condition (SELL).
8. A flag must never contradict `market-regime-analyst`'s current gate — do
   not flag ADD for new risk when the gate is closed; TRIM/SELL/HOLD flags
   remain valid regardless of the gate (de-risking is always permitted).

### Rebalance sequencing

9. Sequence trades: trims/sells before adds (raises cash and confirms real
   capacity before committing new risk); tax-loss-harvest candidates
   considered before tax-gain realization when economically equivalent
   alternatives exist; maintain the stated cash-buffer target throughout the
   sequence, not just at the end. Full detail in `rebalance-policy.md`.
10. State explicitly that no order is placed by this report — the output is
    a plan for the user to execute (see the Hard Rejects on order placement
    in `trading-analyst`).

### Hard Rejects

| Violation | Reason |
|---|---|
| Recommending ADD for new risk when the regime gate is closed | Overrides the fail-closed risk gate |
| A rebalance/trim recommendation with no stated target or band | Non-reproducible; arbitrary |
| Ignoring a breached concentration/correlation cap because conviction is high | Portfolio risk limits are structural, not conviction-overridable |
| Recommending a rebalance trade for drift inside the stated tolerance band | Manufactures unnecessary turnover/cost |
| Treating cash as a residual with no stated target or rationale | Cash is a position; it needs a thesis too |

## Output Format

Use the "Portfolio review" or "Rebalance plan" templates in
`trading-analyst/output-templates.md`. Every plan states the sequencing
rationale and the explicit "no orders are placed" disclosure.

## References

- `rebalance-policy.md` — tolerance-band mechanics, cap definitions, and the
  full trim/add/hold decision table with worked examples.
- `market-regime-analyst` — supplies the net-exposure ceiling this skill must
  respect.
- `quant-methods` — supplies correlation, concentration, and risk-adjusted
  return math.
- `trade-critic` — validates invalidation conditions behind every SELL flag.
- Methodological inspiration (concepts only, no code or text copied — see
  `THIRD_PARTY_NOTICES.md`): tradermonty/claude-trading-skills (MIT) —
  portfolio-manager rebalancing review, Kanchi-style forced-review triggers,
  drawdown circuit breaker; agiprolabs/claude-trading-skills (MIT) —
  portfolio analytics and risk-management sizing controls.
