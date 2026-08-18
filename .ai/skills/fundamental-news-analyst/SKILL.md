---
name: fundamental-news-analyst
license: MIT
aliases:
  - fundamental-analyst
  - news-analyst
version: "1.0.0"
description: >-
  Fundamental research and news-reaction analysis — business quality and
  valuation screens, catalyst classification, and the reaction-to-news
  failure test (price ignoring favorable news signals crowded positioning).
  Every claim cites a source and an as-of date.
platforms:
  cursor: true
  claude: true
  copilot: true
  codex: true
  antigravity: true
scope:
  - "**/*.md"
triggers:
  - "fundamental case"
  - "is this a good business"
  - "valuation"
  - "earnings"
  - "what did the news mean"
  - "catalyst"
  - "why did the stock not react"
delegates_to:
  - quant-methods
  - trading-analyst
---

# Fundamental & News Analyst

## Purpose

Build the business-quality and catalyst case for an instrument, and read the
market's *actual reaction* to news as a signal in its own right. A stock that
fails to rally on genuinely good news is not "efficient market noise" — it is
often evidence of crowded positioning or a thesis already priced in. This
skill treats that failure-to-react pattern as first-class evidence, not an
afterthought.

## When to Use

- Building or reviewing a fundamental thesis (quality, valuation, growth,
  balance sheet).
- Interpreting a specific news event's likely and actual market impact.
- Deciding whether a rally/selloff on news confirms or contradicts a held
  thesis.
- Screening candidates on quality/valuation/dividend criteria.

## When NOT to Use

- Reading price structure/patterns absent a fundamental question — that is
  `technical-chart-analyst`.
- Macro regime/breadth questions — that is `market-regime-analyst`.

## Instructions

### Business quality and valuation

1. State the specific metrics used (e.g., revenue growth trend, margin
   trend, return on invested capital, debt/EBITDA, free cash flow
   conversion) with the reporting period and source (filing, named data
   provider) for each — never a quality judgment with no metric behind it.
2. Valuation is always **relative**: state the multiple used (P/E, EV/EBITDA,
   P/FCF, P/B — pick the one appropriate to the business model), the peer or
   historical-range comparison, and the as-of date of both. A multiple with
   no comparison point is not a valuation judgment.
3. For dividend-oriented theses: state the payout ratio, dividend growth
   streak/rate, and free-cash-flow coverage — a yield alone does not
   establish sustainability.

### Catalyst classification

4. Classify every catalyst into a named type (earnings beat/miss, guidance
   change, M&A, regulatory/FDA-style approval, analyst
   upgrade/downgrade, contract win, product launch, macro/rate-sensitive
   event, insider transaction, short-interest/squeeze dynamic) — an
   unclassified "there was news" is not actionable.
5. State the catalyst's *expected* durability: is this a one-time repricing
   or does it change the multi-quarter earnings trajectory? A beat-and-raise
   quarter changes the trajectory; a one-off legal settlement usually does
   not.

### The reaction-to-news failure test

6. When a name has genuinely favorable news (a clear beat, a clear positive
   catalyst) and the price reaction is flat or negative, treat this as a
   distinct, citable signal: **crowded positioning** or **thesis already
   priced in**, not noise. State the news, the expected reaction direction,
   and the actual reaction, side by side.
7. Conversely, a muted reaction to *bad* news in a name that was heavily
   shorted or under-owned can indicate exhausted selling pressure — apply
   the same side-by-side comparison in the other direction.
8. This test requires the news to be genuinely one-directional in
   expectation (a clean beat, not a mixed report) — do not apply it to
   ambiguous or mixed news where "expected reaction" itself is unclear; say
   so instead.

### Screening discipline

9. When screening a universe (e.g., "find quality dividend growers"), state
   every filter criterion and threshold used, and how many candidates passed
   at each stage (a funnel), so the result is reproducible.
10. Screens produce **candidates for further research**, not verdicts — a
    passed screen still requires the catalyst/valuation/technical checks
    above before it reaches a confidence score.

### Citation discipline

11. Every fact traces to a named source type and an as-of date: a company
    filing (10-K/10-Q/8-K or local equivalent), a named data provider, a
    pasted document/screenshot the user supplied, or a specifically named
    public report. "Reportedly" or "it's said that" with no named source is
    not a citation — flag such claims as unverified rather than presenting
    them as fact.
12. Rank sources by the hierarchy in `source-hierarchy.md` when sources
    conflict; state which source won and why.

### Hard Rejects

| Violation | Reason |
|---|---|
| A quality/valuation judgment with no named metric or comparison point | Unauditable |
| A catalyst left unclassified as "news happened" | Not actionable; no durability assessment possible |
| Applying the reaction-to-news failure test to ambiguous/mixed news | The test requires an unambiguous expected direction |
| A claim sourced only to "reportedly" / unnamed rumor presented as fact | Unverifiable; must be flagged, not asserted |
| A screen's pass/fail criteria not fully disclosed | Non-reproducible |

## Output Format

- Business quality metrics (with source + date) → valuation (with
  comparison + date) → catalyst classification and durability → reaction-to-
  news comparison (if applicable) → source ranking notes if sources
  conflicted.

## References

- `source-hierarchy.md` — source-tier ranking and conflict-resolution rule.
- `trade-critic` — where confirmation-bias and narrative-bias checks on this
  skill's output happen.
- Methodological inspiration (concepts only, no code or text copied — see
  `THIRD_PARTY_NOTICES.md`): tradermonty/claude-trading-skills (MIT) —
  news-reaction-failure analysis (Jason Shapiro contrarian methodology
  step 2), value/dividend-growth screening discipline, earnings-reaction
  scoring.
