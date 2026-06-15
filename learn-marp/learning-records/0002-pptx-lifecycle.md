# 0002 · MD → PPTX lifecycle + LLM prompting

**Date:** 2026-06-15
**Status:** active

## Context
Dat asked for the full lifecycle from notes → Marp markdown → browser preview → PPTX,
and how to prompt an LLM through it. His self-described model: gather context → generate
md → preview → pptx.

## What he already had right
~80%. He understood the broad pipeline and the browser-preview verification step.

## Two corrections taught (the non-obvious bits)
1. **Separate "outline" from "Marp syntax."** A low-reasoning model must lock a plain-text
   slide outline (step 3) BEFORE generating Marp (step 4). Conflating thinking + formatting
   is where weak models fail. This was the missing step in his model.
2. **PPTX is rasterized images by default.** `marp --pptx` = each slide a background image,
   not editable text. `--pptx --pptx-editable` is experimental, needs LibreOffice, lower
   fidelity, and drops presenter notes. This decision belongs in step 1 (the spec).

## Artifacts produced
- Lesson 0002 (deck-lifecycle): 7-step pipeline with who-does-what, stage prompts, PPTX trap table.
- Reference 0002 (llm-deck-prompt): reusable RULES BLOCK + per-stage prompts + review
  checklist + export commands + "which doc to paste" map. This is now his working harness.

## Next ZPD
- A full worked example (real notes → finished deck) would consolidate.
- Possible: speaker/presenter notes lesson; getting `--pptx-editable` working on his Mac
  (LibreOffice install). Unknown whether he has Node/LibreOffice installed — ask before
  the export-heavy lesson.
