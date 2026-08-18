<!-- SPDX-License-Identifier: MIT -->

# Rebalance Policy

## Tolerance-band mechanics

Default band: rebalance a sleeve/holding when drift exceeds **the tighter
of** ±5 percentage points absolute or ±25% relative to target.

Example: target weight 20%.

```
absolute_band = 20% ± 5pp -> triggers outside [15%, 25%]
relative_band = 20% ± 25% of 20% = 20% ± 5pp -> same in this case
```

Example: target weight 4%.

```
absolute_band = 4% ± 5pp -> triggers outside [-1%, 9%] (floor at 0%)
relative_band = 4% ± 25% of 4% = 4% ± 1pp -> triggers outside [3%, 5%]
```

The relative band is tighter for small target weights — use it, since a 5pp
absolute band on a 4% target would allow the position to more than double
before triggering.

## Cap definitions

State every cap used in a given review; typical defaults if the user has not
specified otherwise (disclose that these are defaults, not the user's
stated policy, unless confirmed):

| Cap | Typical default | Rationale |
|---|---|---|
| Single-name | 20-25% of equity sleeve | Idiosyncratic risk limit |
| Single-sector | 30-35% of equity sleeve | Sector-concentration limit |
| Correlated cluster (pairwise corr >= 0.8) | 35-40% combined | Hidden concentration behind seemingly diversified names |
| Cash floor | User-stated, or 0% if unstated (disclose this) | Liquidity/dry-powder policy is user-specific |

## Trim/Add/Hold/Sell decision table

| Condition | Flag | Notes |
|---|---|---|
| Thesis intact, inside all caps, drift inside band | HOLD | No action |
| Thesis strengthened (new evidence, higher confidence per `trading-analyst`), inside caps, regime gate open | ADD | Size increment per `quant-methods`, respecting caps |
| Position exceeds any cap, regardless of thesis quality | TRIM | Reduce to at or below the cap; state the specific trim size |
| Thesis weakening (confidence downgraded, invalidation condition partially triggered) | TRIM | Reduce ahead of full invalidation, not after |
| Invalidation condition fully triggered (`trade-critic`) | SELL | Full exit; state the specific triggering evidence |
| Regime gate closed, position inside caps, thesis intact | HOLD | De-risking is optional here, not required, but new ADDs are blocked |

## Sequencing rule (worked example)

Portfolio needs to trim Position A (over cap by 8pp) and add to Position B
(under target by 6pp, thesis strengthened, regime gate open), while
maintaining a 5% cash floor currently at 3%.

Order of operations:

1. Trim Position A first — this both resolves the cap breach and raises
   cash.
2. Route enough of the trim proceeds to restore the cash floor to 5% before
   sizing the add (cash floor is maintained throughout, not just at the
   end).
3. Size the add to Position B from the remaining proceeds, capped at the
   smaller of (a) the 6pp drift-to-target and (b) any correlation-cluster
   headroom.
4. If a tax-loss-harvest candidate exists elsewhere in the portfolio and is
   economically equivalent to the Position A trim, evaluate harvesting it
   instead/in addition — state the tax-lot method assumption (FIFO/LIFO/
   specific-ID) explicitly since it changes the realized gain/loss.

## What this policy does not do

It does not place orders. It does not account for user-specific tax bracket,
account type (taxable vs. tax-advantaged), or jurisdiction-specific rules —
state this limitation and recommend the user confirm tax treatment with a
qualified preparer before executing any tax-motivated sequencing.
