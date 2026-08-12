<!-- SPDX-License-Identifier: MIT -->
---
id: mem-2026-08-13-write-a-memory-note
type: procedural
title: How to write a new memory note
summary: >-
  Copy the template for the target type, fill required frontmatter per
  SCHEMA.md, keep the summary under 40 words, and link related notes.
created: 2026-08-13T00:00:00Z
updated: 2026-08-13T00:00:00Z
review_after: 2027-08-13
status: accepted
trust: reviewed
classification: public
tags: [procedure, memory, onboarding]
links: []
supersedes: []
source: ""
spdx: MIT
---

# How to write a new memory note

## Purpose

Produce a schema-conformant note without re-reading `SCHEMA.md` every time.

## Preconditions

- You know which of the five types the note belongs to (see
  `.ai/memory/README.md` if unsure).

## Steps

1. Copy `.ai/memory/templates/<type>.md` into the matching type folder.
2. Rename the file to `mem-YYYY-MM-DD-slug.md` using today's date and a short
   kebab-case slug.
3. Fill `id` with the same value as the filename stem (no extension).
4. Fill every required field from `SCHEMA.md`. Do not invent new fields.
5. Write `summary` last, after the body — it should compress the body, not
   restate the title.
6. Add wikilinks to related notes in both `links:` (frontmatter) and the
   `## Links` section (body).
7. Leave `trust: unverified` unless you are the reviewer promoting this note
   in the same change — see `.ai/memory/GOVERNANCE.md`.

## Verification

The note opens cleanly in Obsidian (or any markdown+YAML viewer) with no
frontmatter parse errors, and every wikilink in `links:` resolves to an
existing note.

## Graduation Criteria

This procedure is simple and unlikely to graduate into a standalone skill on
its own; it is a candidate to be folded into `memory-curator`
(`.ai/skills/memory-curator/SKILL.md`) instead, which already automates it.

## Links

- [[mem-2026-08-13-template-bootstrap]]
