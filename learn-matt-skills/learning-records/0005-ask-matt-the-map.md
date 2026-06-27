# 0005 — ask-matt (the map / router)

Date: 2026-06-19
Status: accepted

## What was taught (Lesson 6)

`ask-matt` as the **router** over user-invoked skills — no process, no code, just a map.
`disable-model-invocation: true`; you invoke it on purpose when lost.

New vocabulary: **flow** = a path through the skills. System shape:
- **one main flow** (idea → ship): grill-with-docs → optional prototype detour (bridged
  by /handoff both ways) → branch on multi-session (to-prd → to-issues → implement ×N) or
  implement in place.
- **two on-ramps** that merge onto it: /triage (raw bugs/requests you didn't create) +
  /improve-codebase-architecture (surfaces a deepening idea).
- **standalone**: grill-me (no codebase), teach, writing-great-skills.
- **precondition**: setup-matt-pocock-skills.

Consolidation: placed all 5 previously-learned skills onto this one map — the "daily flow"
from L2–L5 = main flow + one on-ramp.

## Key insights

- **Context hygiene + smart zone (~120k tok):** keep grill→prd→issues in ONE window; don't
  compact/clear until after to-issues. Each /implement starts fresh. This is *why* issues are
  made independent — so each build affords a clean context.
- **handoff vs compact:** handoff forks (→ new session via md file); compact continues (same
  conversation, summarised). Handoff is the bridge into/out of a prototype session.
- **Deep cut — what's absent from the map:** ask-matt routes only *user-invoked* skills.
  `diagnosing-bugs` is model-invoked → a reflex, not a destination → no map entry. Reinforces
  the L1 user/model axis from the other direction. `prototype` IS on the map, but only as a
  detour off step 1.

## Status of the mission

Usage half now fully mapped (ask-matt ties it together). Remaining usage skills to deep-dive:
**prototype** (next), then **diagnosing-bugs**. Then PHASE 2: **writing-great-skills** (authoring
capstone) + write/fork a real skill.

## Zone of proximal development (next)

- **Lesson 7 = prototype** — the throwaway-code detour. Two branches (logic terminal app vs
  toggleable UI variants), 6 shared rules, capture-the-answer-then-delete. Natural follow-on:
  the map named it but didn't open it.
- Then **Lesson 8 = diagnosing-bugs** — Phase 1 (build a tight red-capable feedback loop) IS
  the skill; 6-phase loop. Pairs with the seam/test ideas from L4–L5.
- Then **Lesson 9 = writing-great-skills** (Phase 2 authoring).
- Optional experiential detours: run a live grill→prd→issues, or a real prototype.
