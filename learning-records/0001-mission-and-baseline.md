# 0001 · Mission set + baseline

**Date:** 2026-06-15
**Status:** active

## Context
First session. Dat wants Marp overview-level fluency specifically to **direct and
correct an LLM** that generates slide decks — assumed low-reasoning model. He is the
editor, not the author.

## Baseline (assumed)
- Comfortable with Markdown and CLIs generally.
- No prior Marp-specific knowledge assumed.

## Decision
Framed the whole track as a *failure-mode pattern library* rather than authoring practice.
Lesson 0001 teaches: (1) three-layer model (Marpit / Marp Core / Marp CLI), (2) deck
anatomy (`marp: true` front-matter + `---` rulers), (3) directive scopes (global/local/
spot underscore) as the #1 LLM bug, plus a 4-question spot-the-bug quiz.

## Key insight to preserve
The mission makes *spot-the-bug* the core skill. Lessons should lean on diagnosis drills
("what's wrong with this snippet?") over open authoring. The running "LLM failure modes"
table in the cheat sheet (reference 0001) is the central deliverable — grow it over time.

## Open questions / next ZPD
- Does Dat use Marp via VS Code, CLI, or web editor? (affects export lesson) — unknown.
- Likely next lesson: directive-scope deep dive OR images/backgrounds drill.
