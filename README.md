<!-- SPDX-License-Identifier: MIT -->

# AI-Ready Project Template

A portable, **GitHub template** repository that ships a single source of truth
for AI coding-assistant configuration. Author your rules, hooks, skills, and
subagents once in `.ai/`, then generate platform adapters for **Claude Code,
Cursor, GitHub Copilot, OpenAI Codex, and Google Antigravity**.

Everything here is generic and free of proprietary project, company, or product
names — fork it, rename `your_package`, and start building.

## Why this template

- **One source of truth.** No copy-paste drift across five tools' config files.
- **Five composable primitives.** Rules, hooks, skills, subagents, and agentic
  memory, each with a clear home and a clear contract.
- **Deterministic guardrails.** Hooks block `.env` access, lint on edit, scan for
  secrets/SPDX, and forecast token cost — independent of which assistant runs.
- **Portable skills.** Skills follow a universal format (`.ai/SKILL-FORMAT.md`)
  and are translated to each platform by `setup-adapters.py`.
- **Persistent, typed memory.** `.ai/memory/` gives agents durable, markdown-only
  memory across sessions — episodic, semantic, procedural, prospective, and
  parametric — openable directly as an Obsidian vault.

## The five primitives

```mermaid
flowchart TD
  subgraph canonical [".ai/ — single source of truth"]
    RULES["rules/*.md"]
    HOOKS["hooks/*.py + hooks-config.json"]
    SKILLS["skills/<name>/SKILL.md"]
    SUBS["subagents/*.md"]
    MEM["memory/ (5 typed stores)"]
  end
  GEN["setup-adapters.py + setup-links.py"]
  canonical --> GEN
  GEN --> CUR[".cursor/ (rules, agents, hooks.json)"]
  GEN --> CLA[".claude/ (CLAUDE.md, agents, settings.json)"]
  GEN --> COP[".github/copilot-instructions.md"]
  GEN --> COD["AGENTS.md (root) — Codex"]
  GEN --> ANT[".antigravity/instructions.md"]
```

| Primitive | Lives in | Purpose |
|-----------|----------|---------|
| **Rules** | `.ai/rules/*.md` | Always-on conventions that constrain every change |
| **Hooks** | `.ai/hooks/*.py` | Deterministic guardrails fired on tool/agent events |
| **Skills** | `.ai/skills/<name>/SKILL.md` | Reusable, trigger-activated capability modules |
| **Subagents** | `.ai/subagents/*.md` | Composite agents that delegate to one or more skills |
| **Memory** | `.ai/memory/` | Durable, typed, markdown-only agent memory across sessions |

## Repository layout

```
.ai/                      # Canonical source (edit here)
├── AGENTS.md             # Central instructions + index
├── SKILL-FORMAT.md       # Universal skill format spec
├── rules/                # python, security, git-commits, pr-budget, testing
├── hooks/                # guard-env, ensure-uv-env, lint, review, estimate, runner
├── hooks-config.json     # Budget / review / lint tunables
├── skills/               # portable skills (see table below)
├── subagents/            # composite subagents
├── memory/               # Agentic memory: 5 typed stores, schema, governance
├── setup-adapters.py     # Generates platform adapters
└── setup-links.py        # Links .ai/skills into .cursor/skills

# Generated adapters (do not edit by hand; regenerate instead):
AGENTS.md                 # OpenAI Codex + Google Antigravity entry
.cursor/                  # rules/*.mdc, agents/*.md, hooks.json
.claude/                  # CLAUDE.md, agents/*.md, settings.json
.github/copilot-instructions.md
.antigravity/instructions.md
```

## Quick start

1. **Use this template** on GitHub (or clone it) and rename `your_package`
   placeholders to your project name.
2. **Install tooling** (Python 3.11+ and [`uv`](https://github.com/astral-sh/uv)):
   ```bash
   pip install uv
   uv sync   # once you add a pyproject.toml
   ```
3. **Generate adapters** for every platform:
   ```bash
   python .ai/setup-adapters.py
   ```
4. **(Cursor only)** Expose skills to native discovery:
   ```bash
   python .ai/setup-links.py
   ```
5. Edit canonical files in `.ai/`, then re-run `setup-adapters.py`. Never edit the
   generated adapter files directly.

## Platform support matrix

| Platform           | Primary Config                    | Hooks                   | Skills            |
|--------------------|-----------------------------------|-------------------------|-------------------|
| Cursor             | `.cursor/agents/*.md`             | `.cursor/hooks.json`    | Reads SKILL.md    |
| Claude Code        | `.claude/CLAUDE.md`               | `.claude/settings.json` | Read tool         |
| GitHub Copilot     | `.github/copilot-instructions.md` | N/A                     | Inline summary    |
| OpenAI Codex       | `AGENTS.md` (root)                | N/A                     | Section headers   |
| Google Antigravity | `.antigravity/instructions.md`    | Slash commands          | Multi-agent       |

## Available AI skills

| Skill | Trigger phrases | Purpose |
|-------|-----------------|---------|
| `principal-engineer` | architecture, scalability, ROI, security, GPU | ROI/scale/security/licensing gates, GPU compute, packaging |
| `ai-engineer` | pipeline node, agent graph, confidence threshold, LLM call | Rule-based-first routing, structured outputs, gateway client |
| `backend-architect` | service layout, connector, transport, config, state | Package layout, async connectors, settings management |
| `clean-code` | readability, clarity, simplicity, story flow | Reader-mindset readability and abstraction-value review |
| `devops-automator` | CI/CD, Docker, deployment, secrets, pipeline | Container images, pipeline gates, secret hygiene |
| `code-reviewer` | code review, PR review, review this diff | 16-point checklist, commit hygiene, config↔docs parity |
| `test-quality-evaluator` | run tests, coverage, quality scoring, calibration | Test execution, quality matrix, regression and calibration |
| `memory-curator` | remember this, write a memory note, record this decision, add to the backlog | Write/dedupe/promote/prune notes in `.ai/memory/`, staleness sweeps |
| `contribution-summary` | weekly summary, contribution report | Weekly summary from git history + memory, no vendor dependency |
| `roadmap-review` | roadmap review, milestone confidence | Confidence-scored feedback on `.ai/memory/prospective/roadmap.md` |

## Available subagents

| Subagent | Composes | Use for |
|----------|----------|---------|
| `reviewer` | code-reviewer, clean-code | End-to-end review of a diff or PR |
| `architect` | backend-architect, principal-engineer | Design and scalability decisions |
| `release-engineer` | devops-automator, test-quality-evaluator | Build, test, and ship readiness |
| `memory-steward` | memory-curator, code-reviewer | Memory hygiene with a review-ready diff |

## Hooks

Hooks live in `.ai/hooks/` and are wired into Cursor (`.cursor/hooks.json`) and
Claude Code (`.claude/settings.json`). They are cross-platform and stdlib-only.

| Hook | Fires on | Effect |
|------|----------|--------|
| `guard-env-files` | file read/write | Blocks access to `.env*` (fail-closed) |
| `ensure-uv-env` | shell exec | Verifies a `uv`-managed venv is active |
| `lint-changed-files` | file edit | `ruff` + `mypy` on changed lines (non-blocking) |
| `post-test-review` | shell exec (tests) | SPDX + secret scan (+ standards in `full` mode) |
| `pre-agentic-estimate` | prompt submit | Token-cost forecast with a budget gate |

Tune behavior in `.ai/hooks-config.json` or via environment overrides:

| Variable | Effect |
|----------|--------|
| `AI_HOOK_REVIEW_MODE=off` | Disable post-test review |
| `AI_HOOK_REVIEW_MODE=full` | Enable the full standards pass |
| `AI_HOOK_LINT_ENABLED=0` | Disable lint-on-edit |
| `AI_HOOK_BUDGET_MAX=10` | Raise the cost-approval threshold |

## Agentic memory

`.ai/memory/` gives agents durable, session-spanning memory with no runtime
dependency — plain markdown notes with strict frontmatter, openable directly
as an Obsidian vault.

| Type | Answers | Lifecycle |
|------|---------|-----------|
| Episodic | What happened, and when? | Cheap to write, short-lived, unverified by default |
| Semantic | What is true? | PR-reviewed before it counts as fact |
| Procedural | How do we do this? | Stabilizes into a `.ai/skills/` entry once proven |
| Prospective | What must happen next? | Local backlog/roadmap; optional GitHub Issues mirror |
| Parametric | What do we assume the model knows? | A single register, not a note store |

Start with `.ai/memory/README.md` (the contract), `.ai/memory/SCHEMA.md` (the
frontmatter fields), and `.ai/memory/GOVERNANCE.md` (trust levels, promotion,
policy modes). Retrieval budgets live in the `memory` block of
`.ai/hooks-config.json`. Write and curate notes with the `memory-curator`
skill; generate weekly summaries and roadmap feedback with
`contribution-summary` and `roadmap-review`.

## Conventions

Project rules are modular under `.ai/rules/`: `python.md`, `security.md`,
`git-commits.md`, `pr-budget.md`, `testing.md`, and `memory.md`. See
`.ai/AGENTS.md` for the full index.

## License

First-party content is MIT — see [LICENSE](LICENSE). First-party skills declare
`license: MIT` in their `SKILL.md` frontmatter, and other first-party source and
docs carry an `SPDX-License-Identifier: MIT` header.

Some skills under `.ai/skills/` are vendored from upstream projects and retain
their original licenses (e.g. Apache-2.0). Their provenance, license files, and
any modifications are recorded in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
