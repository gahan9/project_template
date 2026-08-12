<!-- SPDX-License-Identifier: MIT -->
---
id: mem-2026-08-13-backlog
type: prospective
title: Local work backlog
summary: >-
  Table-form backlog of pending work. Source of truth for prospective
  memory; rows optionally mirror to GitHub Issues per GOVERNANCE.md.
created: 2026-08-13T00:00:00Z
updated: 2026-08-13T00:00:00Z
review_after: 2026-09-13
status: accepted
trust: reviewed
classification: public
tags: [backlog, prospective, template]
links: []
supersedes: []
source: ""
spdx: MIT
---

# Local work backlog

This file is the source of truth for pending work. Use it whether or not
this project also tracks issues on GitHub — see `../GOVERNANCE.md` for the
optional, one-directional mirror to `.github/ISSUE_TEMPLATE/backlog-item.yml`.

## Columns

- `id` — short kebab-case identifier, unique within this file.
- `title` — one line.
- `type` — `bug`, `feature`, `chore`, or `roadmap`.
- `priority` — `p0` (drop everything) through `p3` (someday).
- `status` — `open`, `in-progress`, `blocked`, or `done`.
- `owner` — free text; blank if unassigned.
- `issue` — GitHub Issue URL if mirrored, blank otherwise.
- `note` — link to a `prospective/mem-*.md` note if the item needs more than
  a one-line description.

## Backlog

| id | title | type | priority | status | owner | issue | note |
|----|-------|------|----------|--------|-------|-------|------|
| example-001 | Replace seed memory notes with real project content | chore | p2 | open | | | |
| example-002 | Wire a schema validator once a `src/` package exists | feature | p3 | open | | | [[mem-2026-08-13-write-a-memory-note]] |

Delete the two example rows once real backlog items exist.
