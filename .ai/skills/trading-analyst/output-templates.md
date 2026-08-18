<!-- SPDX-License-Identifier: MIT -->

# Output Templates

Fixed report shapes for the four request types this skill family handles.
Every template ends with the disclaimer from `SKILL.md`. Do not add sections;
do not omit required ones. If a section has no content, write "None found" —
never delete the heading, since its absence is itself information (e.g., "no
invalidation condition" would otherwise be silently missing).

## 1. Single-name thesis

```markdown
## Thesis: <ticker/instrument> — <direction: long/short/neutral>

### Regime check
<market-regime-analyst score, net-exposure ceiling, gate result>

### Fundamental case
<business quality, valuation, catalyst — with source + as-of date each>

### Technical read
<trend/stage, base/pattern if any, volume confirmation — with timeframe>

### Quant summary
<expectancy, position size at X% risk, key ratios — with formula shown>

### Verdict
| Confidence | Tier | Direction | Size (of planned) |
|---|---|---|---|
| <0-100> | <ACT/SCALE-IN/OBSERVE/AVOID> | <long/short/neutral> | <%> |

**Why pursue this now:** <the specific, evidence-tied reason this is timely —
not a restatement of the thesis>

**Invalidation:** <price level, event, or condition that proves this wrong>

**Citations:** <numbered list, source + as-of date per claim>

<disclaimer>
```

## 2. Portfolio review

```markdown
## Portfolio Review — as of <date>

### Holdings snapshot
<table: ticker, weight %, sector, unrealized P/L, thesis status (see
trader-memory pattern in fundamental-news-analyst)>

### Allocation diagnostics
<sector/factor concentration, correlation clusters, single-name concentration
vs caps — see portfolio-strategist>

### Regime context
<market-regime-analyst score and what it implies for net exposure>

### Position flags
| Ticker | Flag | Reason | Confidence |
|---|---|---|---|
| ... | HOLD/ADD/TRIM/SELL | ... | 0-100 |

### Risk summary
<portfolio Sharpe/Sortino/max drawdown, worst single-name loss at defined
stop, largest correlated cluster exposure>

<disclaimer>
```

## 3. Rebalance plan

```markdown
## Rebalance Plan — as of <date>

### Target vs current
<table: asset/sector, target %, current %, drift %, inside/outside tolerance
band — see rebalance-policy.md>

### Proposed actions
| Action | Ticker | From % | To % | Rationale | Tax-lot note |
|---|---|---|---|---|---|

### Sequencing
<order of operations — trims before adds, tax-loss-harvest candidates first,
cash buffer maintained — per rebalance-policy.md>

### What this does NOT do
<explicitly state: no orders are placed by this report; the user executes>

<disclaimer>
```

## 4. Critique-only

```markdown
## Critique: <thesis or trade being reviewed>

### What is sound
<specific strengths, not generic praise>

### Base-rate check
<how often does this setup/claim type work, with n and source>

### Bias flags
<narrative bias, confirmation bias, recency bias — named specifically, not a
generic disclaimer>

### Pre-mortem
<the most likely way this trade loses money, stated concretely>

### Revised confidence
| Original confidence | Revised confidence | Delta driver |
|---|---|---|

<disclaimer>
```
