# 0006 — prototype (the throwaway-code detour)

Date: 2026-06-19
Status: accepted

## What was taught (Lesson 7)

`prototype` (<span>user-invoked</span>, `disable-model-invocation: true`) = **throwaway code that
answers a question**. The detour off main-flow step 1, bridged in/out by `/handoff`.

**Step zero = pick the branch** (getting it wrong wastes the whole prototype):
- **LOGIC** ("does this state/logic feel right?") → tiny interactive terminal app.
- **UI** ("what should this look like?") → several toggleable variants on one route.
- Ambiguous + AFK → match surrounding code (backend→logic, page→UI), state the assumption.

**Six shared rules:** throwaway+marked · one command · no persistence · skip polish · surface
state · delete-or-absorb.

**LOGIC specifics:** pure portable logic module (reducer / state machine / pure fns / class —
shape from the *question*) + throwaway thin TUI shell that clears + re-renders full frame each
tick (state then shortcuts). Data flows one way: TUI → logic, never back. The module is the
keeper, lifted into real code later.

**UI specifics:** prefer sub-shape A (variants inside an existing page via `?variant=`, real
data/density) over B (throwaway route, last resort). Default 3 variants, cap 5, *structurally*
different not recoloured. Floating switcher: ←/label/→, URL-param (shareable), arrow keys,
hidden in prod.

**When done:** the ANSWER is the only keeper — capture (commit/ADR/issue/NOTES.md) with its
question, then delete or absorb.

## Key insights

- The LOGIC pure-module-behind-thin-shell IS a deep module being prototyped (small interface,
  hidden behaviour) — direct callback to L5. Purity = portability = the validated module lifts
  cleanly into the real codebase.
- The valuable feedback is recombination ("header from B + sidebar from C") or surprise ("that
  shouldn't be possible" = a bug in the *idea*) — not just "B wins."
- SKILL.md→LOGIC.md/UI.md is a clean **progressive-disclosure** example: router file + detail
  file loaded only on the chosen branch.

## Status of the mission

Usage skills: setup ✓ align ✓ plan/build ✓ maintain ✓ map(ask-matt) ✓ prototype ✓.
One usage skill left: **diagnosing-bugs**. Then PHASE 2: writing-great-skills + author/fork one.

## Zone of proximal development (next)

- **Lesson 8 = diagnosing-bugs** — model-invoked discipline; Phase 1 (build a TIGHT, red-capable,
  deterministic, fast, agent-runnable feedback loop) IS the skill, rest is mechanical. 6 phases:
  loop → reproduce+minimise → 3–5 ranked falsifiable hypotheses → instrument (one var, tagged
  logs) → fix+regression test (only at a correct seam) → cleanup+post-mortem. Pairs with the
  seam ideas from L4–L5; "no correct seam = the finding" → hands off to improve-arch.
- Then **Lesson 9 = writing-great-skills** (Phase 2 authoring capstone) → write/fork a real skill.
- Optional: build a real prototype hands-on (TUI state machine or 3-layout UI flip).
