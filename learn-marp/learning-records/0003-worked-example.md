# 0003 · Full worked example (notes → PPTX)

**Date:** 2026-06-15
**Status:** active

## Context
Dat chose "full worked example" as the next lesson. Confirmed tooling: **Node yes,
LibreOffice no** → default `--pptx` (image route) only; `--pptx-editable` off the table.

## Workspace move
Dat relocated the whole workspace to `repos/learn-x/learn-marp`. All future paths use
that base. (Old `repos/learn-marp` should be considered dead.)

## Local-setup gotcha discovered
His `package.json` installs only `@marp-team/marpit` (the low-level engine) — which has
**no built-in themes and no export**. The deck uses `theme: gaia` (a marp-core theme) and
needs marp-cli to export. Lesson 0003 steers him to `npx @marp-team/marp-cli@latest …`
which bundles marp-core, sidestepping the issue. Flagged `npm i -D @marp-team/marp-cli`
as the local-install alternative.

## Artifacts produced
- examples/01-raw-notes.md, 02-outline.md, deck.md (an 8-slide Redis-cache pitch).
- Lesson 0003: walks raw→outline→md→review→preview→pptx, incl. a before/after showing the
  two classic bugs (invented theme `corporate`, missing `_` on `class: lead`) and the fix.

## Key insight reinforced
The teachable skill is *review*, not authoring: spot invalid theme + missing underscore,
then issue a targeted fix prompt. Lesson centers a concrete before/after diff on exactly that.

## Next ZPD
- Get him to actually run the preview/export (watch for "browser not found" errors).
- Or a directive-scopes drill to make the underscore rule automatic.
- Offer: generate a second deck from his OWN notes so he practices review on fresh output.
