---
name: quant-methods
license: MIT
aliases:
  - quant-analyst
  - risk-math
version: "1.0.0"
description: >-
  Quantitative foundation for trading decisions — expectancy, fractional
  Kelly position sizing, volatility and vol-targeting, correlation and
  concentration math, mean-reversion diagnostics (Hurst, half-life, ADF),
  risk-adjusted return metrics, and walk-forward validation to detect
  overfitting before any statistical edge claim is trusted.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
triggers:
  - "position size"
  - "kelly criterion"
  - "expectancy"
  - "sharpe ratio"
  - "sortino"
  - "max drawdown"
  - "volatility target"
  - "correlation"
  - "mean reversion"
  - "half life"
  - "walk forward"
  - "is this overfit"
  - "backtest"
delegates_to:
  - trading-analyst
  - trade-critic
---

# Quant Methods

## Purpose

Provide the deterministic mathematical layer every other trading skill relies
on. No verdict from `technical-chart-analyst`, `fundamental-news-analyst`, or
`portfolio-strategist` is complete until it passes through the relevant
formula here with the calculation shown. This skill exists to stop trading
advice from being vibes with numbers attached.

## When to Use

- Sizing a position (fixed-fractional, volatility-adjusted, or Kelly).
- Computing or reporting a risk-adjusted return metric (Sharpe, Sortino,
  Calmar) or drawdown statistic.
- Testing whether a price series is trending or mean-reverting (Hurst,
  half-life, ADF).
- Validating a backtest or a claimed historical edge before it is trusted.
- Measuring correlation/concentration for a portfolio decision.

## When NOT to Use

- Choosing the store/engine for a data pipeline that runs these calculations
  — that is `backend-architect`/`database-architect`.
- Deciding *what* to size or rebalance — that is `portfolio-strategist`; this
  skill only supplies the math it consumes.

## Instructions

### Expectancy and edge

1. Expectancy per trade: `E = (win_rate * avg_win) - (loss_rate * avg_loss)`.
   An edge claim with no expectancy computation is not a claim, it is an
   opinion.
2. Require **n >= 20** closed trades/events before reporting a win rate at
   all, and flag n < 100 as "provisional — sample too small for high
   confidence" per `trading-analyst/confidence-calibration.md`.
3. State whether the sample is in-sample or out-of-sample. In-sample-only
   expectancy claims are downgraded automatically (see hard rejects below).

### Position sizing

4. **Fixed-fractional**: `shares = (account_equity * risk_per_trade_pct) /
   (entry_price - stop_price)`. Risk-per-trade default ceiling: 1-2% of
   equity per idea unless the user states a different risk budget.
5. **Volatility-adjusted**: size inversely to recent realized volatility (e.g.
   ATR-based) so each position contributes roughly equal risk:
   `shares = (target_risk_$) / (ATR_n * multiplier)`.
6. **Fractional Kelly**: `f* = (b*p - q) / b` where `p` = win probability,
   `q = 1-p`, `b` = win/loss payoff ratio. Never recommend full Kelly — cap at
   **1/4 to 1/2 Kelly** by default; full Kelly's variance is unfit for a
   single-strategy, estimation-error-prone input. Show `f*` and the fraction
   applied.
7. Every sizing output states the stop price and the dollar/percent risk it
   implies — a size without a stop is a hard reject (see `trading-analyst`).

### Volatility and risk-adjusted return

8. Realized volatility: annualize as `sigma_annual = sigma_daily *
   sqrt(252)` (or the appropriate periods-per-year for the sampling
   frequency). State the lookback window used (e.g., 20-day, 63-day).
9. Sharpe: `(mean_return - risk_free) / stdev_return`, annualized consistently
   with the return frequency. Sortino: same numerator, denominator uses only
   downside deviation. Calmar: `annualized_return / |max_drawdown|`.
10. Max drawdown: the largest peak-to-trough decline in cumulative equity;
    report both the % depth and the recovery time if the series has since
    recovered, or state "not yet recovered."

### Mean reversion vs trend diagnostics

11. **Hurst exponent**: H < 0.5 suggests mean-reverting, H ≈ 0.5 suggests
    random walk, H > 0.5 suggests trending/persistent. Treat H estimates from
    < 100 observations as unreliable.
12. **Half-life of mean reversion**: from an OU/AR(1) fit,
    `half_life = -ln(2) / ln(1 + beta)` where `beta` is the AR(1) coefficient
    on the deviation from the mean. Report the confidence interval, not a
    point estimate alone, when the fit is noisy.
13. **ADF (Augmented Dickey-Fuller)** test for stationarity before trusting
    any mean-reversion or pairs/cointegration thesis; report the test
    statistic and whether it rejects the unit-root null at the 5% level.

### Correlation and concentration

14. Use rolling-window correlation (not full-history) for current portfolio
    decisions; state the window. A single full-sample correlation hides
    regime-dependent decoupling.
15. Concentration: report both single-name weight and the largest correlated
    cluster's combined weight (e.g., "3 holdings, 0.85+ pairwise correlation,
    sum to 40% of portfolio" is a concentration risk even if no single name
    exceeds a cap).

### Backtest validity and overfitting

16. Any backtest claim must state: sample period, in-sample vs out-of-sample
    split method, number of parameters tuned, and number of independent
    trials run to find the result (the more trials, the more likely the
    result is noise — multiple-testing correction or at minimum disclosure is
    required).
17. Prefer **walk-forward validation** (rolling train/test windows) over a
    single in-sample fit. A strategy that only works on one static historical
    slice is not validated.
18. Red flags that must be surfaced, not hidden: parameter count approaching
    trade count, performance that collapses out-of-sample, and curve-fit
    entry/exit rules with no economic rationale (see `trade-critic`).

### Hard Rejects

| Violation | Reason |
|---|---|
| Win rate or expectancy reported with n < 20 | Statistically meaningless |
| Full Kelly sizing recommended | Estimation error + variance make full Kelly unsafe for live capital |
| Sharpe/Sortino/Calmar reported without stating the annualization convention and lookback | Non-reproducible, non-comparable |
| Backtest edge claimed with no out-of-sample or walk-forward check | Overfit by construction |
| Correlation computed on full history and applied to a current decision without a rolling check | Ignores regime-dependent correlation breakdown |
| Position size given with no stop price | Sizing formula is undefined without a stop |

## Output Format

- Show the formula, the inputs, and the computed result — never the result
  alone.
- State the lookback window, sample size, and in-sample/out-of-sample status
  for every statistical claim.
- Flag any hard-reject condition explicitly rather than silently omitting the
  unsupported claim.

## References

- `formulas.md` — full formula reference with worked numeric examples.
- `trading-analyst/confidence-calibration.md` — how sample size feeds the
  confidence score.
- `trade-critic` — the overfitting/base-rate red-team pass this skill feeds.
- Methodological inspiration (concepts only, no code copied — see
  `THIRD_PARTY_NOTICES.md`): agiprolabs/claude-trading-skills (MIT) — Kelly
  criterion, cointegration/mean-reversion diagnostics, walk-forward
  validation; tradermonty/claude-trading-skills (MIT) — position-sizer risk
  discipline.
