<!-- SPDX-License-Identifier: MIT -->

# Formula Reference

Worked examples for every formula in `SKILL.md`. Numbers are illustrative,
not recommendations.

## Expectancy

```
E = (win_rate * avg_win) - (loss_rate * avg_loss)
```

Example: 45 closed trades, win_rate = 0.44 (20 wins), avg_win = $340,
loss_rate = 0.56 (25 losses), avg_loss = $210.

```
E = (0.44 * 340) - (0.56 * 210) = 149.6 - 117.6 = $32.00 per trade
```

n = 45 → above the n >= 20 floor, but below n = 100 → report as provisional.

## Fixed-fractional position size

```
shares = (account_equity * risk_per_trade_pct) / (entry_price - stop_price)
```

Example: $50,000 equity, 1% risk budget, entry $82.00, stop $78.50.

```
risk_$ = 50,000 * 0.01 = $500
shares = 500 / (82.00 - 78.50) = 500 / 3.50 = 142 shares
```

## Fractional Kelly

```
f* = (b*p - q) / b        where q = 1 - p
```

Example: estimated win probability p = 0.55, payoff ratio b = 1.8 (win/loss).

```
q = 0.45
f* = (1.8*0.55 - 0.45) / 1.8 = (0.99 - 0.45) / 1.8 = 0.30
```

Applying **1/2 Kelly**: `0.30 * 0.5 = 15%` of risk capital allocated to this
edge — never the full 30%. Always disclose both `f*` and the applied
fraction.

## Volatility annualization

```
sigma_annual = sigma_period * sqrt(periods_per_year)
```

Example: daily stdev of returns = 1.8%, 252 trading days/year.

```
sigma_annual = 0.018 * sqrt(252) = 0.018 * 15.87 = 28.6%
```

## Sharpe / Sortino / Calmar

```
Sharpe  = (mean_return - risk_free) / stdev_return                 [annualized]
Sortino = (mean_return - risk_free) / downside_deviation            [annualized]
Calmar  = annualized_return / abs(max_drawdown)
```

Example: annualized return 14%, risk-free 4.5%, annualized stdev 22%, max
drawdown -18%.

```
Sharpe = (0.14 - 0.045) / 0.22 = 0.43
Calmar = 0.14 / 0.18 = 0.78
```

State the lookback (e.g., trailing 3-year monthly returns) alongside the
number — the same Sharpe label means nothing without it.

## Max drawdown

```
drawdown_t = (equity_t / peak_equity_to_t) - 1
max_drawdown = min(drawdown_t) over the series
```

Report the trough date, the peak date it fell from, and — if applicable — the
recovery date and the number of periods to recover.

## Hurst exponent (rescaled range, simplified)

For a return series of length N, split into subsequences, compute the
rescaled range R/S for each, and regress `log(R/S)` on `log(n)`; the slope is
H. Interpretation:

| H | Behavior |
|---|---|
| < 0.5 | Mean-reverting |
| ≈ 0.5 | Random walk (no memory) |
| > 0.5 | Trending / persistent |

Treat estimates from fewer than ~100 observations as noise-dominated; report
the sample size alongside H.

## Half-life of mean reversion

Fit `delta_x_t = alpha + beta * x_(t-1) + epsilon_t` where `x` is the
deviation from the rolling mean (or the cointegration residual for a pair).

```
half_life = -ln(2) / ln(1 + beta)
```

Example: beta = -0.08 from the AR(1) fit.

```
half_life = -0.693 / ln(0.92) = -0.693 / -0.0834 = 8.3 periods
```

A negative or near-zero `beta` implies no measurable mean reversion — report
this outcome rather than forcing a half-life number.

## ADF stationarity test

Report the ADF test statistic and the critical value at the 5% significance
level for the sample size; state explicitly whether the null hypothesis of a
unit root (non-stationarity) is rejected. A cointegration or mean-reversion
thesis without a passed ADF test is a hypothesis, not a validated edge.

## Correlation and concentration

```
cluster_weight = sum(weight_i for i in holdings where pairwise_corr >= 0.8)
```

Example: three holdings each correlated >= 0.85 pairwise, weights 15%, 14%,
11% → cluster_weight = 40%, reported even though no single holding exceeds a
20% cap.

## Walk-forward validation shape

```
for each rolling window (train_start, train_end, test_start, test_end):
    fit parameters on [train_start, train_end]
    evaluate (no refitting) on [test_start, test_end]
    record out-of-sample metric
aggregate out-of-sample metrics across all windows
```

Report the aggregated out-of-sample metric, not the best single window's
result — cherry-picking one window is a form of overfitting.
