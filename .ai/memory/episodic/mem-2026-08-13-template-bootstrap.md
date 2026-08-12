<!-- SPDX-License-Identifier: MIT -->
---
id: mem-2026-08-13-template-bootstrap
type: episodic
title: Agentic memory primitive added to the template
summary: >-
  The template gained a fifth primitive for agentic memory with five typed
  stores, a governance model, and two reporting skills.
created: 2026-08-13T00:00:00Z
updated: 2026-08-13T00:00:00Z
review_after: 2026-09-13
status: accepted
trust: reviewed
classification: public
tags: [template, bootstrap, memory]
links: ["[[mem-2026-08-13-memory-primitive-adopted]]"]
supersedes: []
source: ""
spdx: MIT
---

# Agentic memory primitive added to the template

## Context

The template had four primitives (rules, hooks, skills, subagents) and no
mechanism for an agent to persist knowledge across sessions.

## What Happened

A fifth primitive, `.ai/memory/`, was added: five typed memory stores
(episodic, semantic, procedural, prospective, parametric), a schema
(`SCHEMA.md`), a governance model (`GOVERNANCE.md`), a token budget
(`.ai/hooks-config.json` `memory` block), a curator skill, and two reporting
skills for weekly summaries and roadmap review.

## Follow-ups

- Replace this seed note and the other seed notes with real content as the
  project grows. The schema and folder structure should stay.

## Links

- [[mem-2026-08-13-memory-primitive-adopted]]
