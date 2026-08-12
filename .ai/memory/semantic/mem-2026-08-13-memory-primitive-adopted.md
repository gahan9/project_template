<!-- SPDX-License-Identifier: MIT -->
---
id: mem-2026-08-13-memory-primitive-adopted
type: semantic
title: Agentic memory is a fifth, markdown-only primitive
summary: >-
  Memory lives under .ai/memory/ as five typed markdown stores with no
  runtime dependency, keeping the template a pure configuration scaffold.
created: 2026-08-13T00:00:00Z
updated: 2026-08-13T00:00:00Z
review_after: 2027-08-13
status: accepted
trust: reviewed
classification: public
tags: [architecture, decision, memory]
links: ["[[mem-2026-08-13-template-bootstrap]]"]
supersedes: []
source: ""
spdx: MIT
---

# Agentic memory is a fifth, markdown-only primitive

## Context

The template's four existing primitives (rules, hooks, skills, subagents)
have no way to persist knowledge across agent sessions. Adding one risked
turning a zero-dependency configuration template into an application with a
database and a runtime.

## Decision / Fact

Memory is implemented as a fifth primitive, `.ai/memory/`: plain markdown
notes with strict YAML frontmatter, organized into five cognitive types
(episodic, semantic, procedural, prospective, parametric), openable directly
as an Obsidian vault. No package, no database, no server ships with the
template. A team that outgrows this can add a `src/` indexer later without
changing the note format.

## Consequences

- Retrieval is deterministic and manual (frontmatter, tags, wikilinks) rather
  than embedding-based, matching the template's zero-dependency stance.
- Governance (trust levels, promotion, policy modes) is process, documented
  in `../GOVERNANCE.md`, not code — there is nothing to bypass because there
  is nothing executable.
- Token spend is controlled by convention (`summary` fields, retrieval caps
  in `.ai/hooks-config.json`) rather than by a runtime budget enforcer.

## Links

- [[mem-2026-08-13-template-bootstrap]]
