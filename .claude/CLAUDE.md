<!-- SPDX-License-Identifier: MIT -->

# Project — Claude Code Instructions

> Auto-generated from `.ai/`. Run `python .ai/setup-adapters.py` to regenerate.

Read `.ai/AGENTS.md` for the full configuration and `.ai/rules/` for project rules.

## Skills

| Skill | Description | Source |
|-------|-------------|--------|
| `ai-engineer` | AI/LLM application engineer for agent and graph pipelines — rule-based first, LLM only below a confi | `.ai/skills/ai-engineer/SKILL.md` |
| `backend-architect` | Service and package architecture for Python backends — transport layer, async connectors with timeou | `.ai/skills/backend-architect/SKILL.md` |
| `clean-code` | Code readability and craft advocate drawing on Robert C. Martin's Clean Code and Software Craftsmans | `.ai/skills/clean-code/SKILL.md` |
| `code-reviewer` | Structured 16-point code review for commits and PRs — reviewability budget, commit hygiene, style/SO | `.ai/skills/code-reviewer/SKILL.md` |
| `devops-automator` | CI/CD pipelines, Docker containers, deployment, and secrets hygiene — reproducible builds, minimal i | `.ai/skills/devops-automator/SKILL.md` |
| `principal-engineer` | Brutally honest Principal Engineer. Gates every change on ROI, scalability, licensing, and security. | `.ai/skills/principal-engineer/SKILL.md` |
| `principal-uefi-engineer` | Principal UEFI/firmware engineer for EDK II projects across x86 and ARM. Use when designing, reviewi | `.ai/skills/principal-uefi-engineer/SKILL.md` |
| `test-quality-evaluator` | Testing and evaluation specialist — runs pytest, designs unit/integration/ regression tests, and sco | `.ai/skills/test-quality-evaluator/SKILL.md` |

## Subagents

| Subagent | Description | Source |
|----------|-------------|--------|
| `architect` | Design and scalability decisions for backend services and AI pipelines. Combines structural package/ | `.ai/subagents/architect.md` |
| `release-engineer` | Build, test, and ship readiness. Combines CI/CD and container automation with test execution and qua | `.ai/subagents/release-engineer.md` |
| `reviewer` | End-to-end review of a diff or pull request. Combines the structured 16-point review with a deep rea | `.ai/subagents/reviewer.md` |

To use a skill or subagent, read its source file and follow the instructions.
