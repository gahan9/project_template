<!-- SPDX-License-Identifier: MIT -->

# Source Hierarchy

When sources conflict, rank by tier and state which tier won. Never blend
conflicting numbers into an average without disclosing that a conflict
existed.

## Tier 1 — Primary filings and official releases

Company filings (10-K/10-Q/8-K, prospectuses, or local-market equivalents),
official press releases, regulator filings/approvals, and exchange
announcements. Highest weight; cite the specific filing, section, and date.

## Tier 2 — Named data providers and market data

Named financial-data providers, exchange-published data, and official
economic-data releases (with the release date, since these are frequently
revised — cite the vintage). Second-highest weight; state the provider name
and as-of date/timestamp.

## Tier 3 — Reputable financial press with named reporting

Named, mainstream financial publications reporting with attribution (not
anonymous), and analyst research notes when the analyst/firm is named.
Usable for catalyst context and sentiment, weighted below Tier 1/2 for hard
numbers — cross-check any specific figure against Tier 1/2 before treating it
as confirmed.

## Tier 4 — User-supplied documents and screenshots

Documents, CSVs, or chart images the user pastes directly. Treat as
authoritative for *what they show* (state exactly what is visible) but flag
if they cannot be independently corroborated — note this explicitly in the
confidence calculation (`trading-analyst/confidence-calibration.md`,
evidence-count axis).

## Tier 5 — Unnamed/social/rumor

Anonymous social posts, unnamed "sources familiar with the matter," and
unverified rumors. Never presented as fact. May be mentioned as "market
chatter" only with an explicit flag that it is unverified, and it must not
by itself raise confidence above the single-evidence-point cap in
`trading-analyst/confidence-calibration.md`.

## Conflict-resolution rule

1. Tier 1 beats Tier 2 beats Tier 3 beats Tier 4 beats Tier 5 for hard
   numbers.
2. If two sources at the **same tier** conflict, state both values, both
   as-of dates, and flag the discrepancy rather than picking one silently —
   this itself lowers the evidence-agreement axis of the confidence score.
3. A Tier 3-5 claim that contradicts a Tier 1/2 fact is not "additional
   color" — it is wrong, and should be labeled as such once the higher-tier
   source is confirmed current.
