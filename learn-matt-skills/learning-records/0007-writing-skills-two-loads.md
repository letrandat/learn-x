# 0007 — writing-great-skills I: predictability & the two loads

Date: 2026-06-19
Status: accepted

## Context

Dat chose to jump to **writing-great-skills** (Phase 2 authoring capstone) ahead of the
planned Lesson 8 = `diagnosing-bugs`. Respected — diagnosing-bugs deferred, not dropped.
This opens the "author your own" arm of the mission.

The skill is big (8 sections, self-described "all reference"). Teaching as a 4-part arc, not
one lesson. Lesson 8 = the foundation.

## What was taught (Lesson 8)

**Thesis:** a skill exists to *wrangle determinism out of a stochastic system*.
**Predictability** = same *process* every run, NOT same output (brainstorm predictably diverges).
Root virtue; every other lever serves it.

**The flip:** L1's user/model axis, now from the author's seat. The `description` field *is* the
axis — keep it → model-invoked; delete it → user-invoked. No third state.

**The two loads (the central tradeoff):**
- **Context load** — paid by the *model*; description in the window every turn (tokens + attention);
  brake on more model-invoked skills.
- **Cognitive load** — paid by the *human*; remembering it exists + when to reach for it (you are the
  index); NOT to be zeroed (price of human agency); brake on more user-invoked skills.

**Invocation rule:** model-invocation ONLY when the agent must reach it itself (or another skill must);
else user-invoked, pay no context load. Asymmetry: a description only *adds* agent reach — model =
user-AND-agent, never agent-only.

**Reachability rides the description:** other skills can only fire model-invoked skills → shared
reference often lives in one. **Router skill** = cure for piled cognitive load (ask-matt is one;
hints, can't fire them).

## Key insights

- Authoring ≈ repeatedly choosing *which of two loads to pay*. Everything later (disclose / split /
  word choice) is this same tension reapplied.
- Strong ZPD bridge: Dat already *read* the L1 axis as a user; this just hands him the pen.
- Glossary now has an "Authoring" section (predictability, context load, cognitive load, router skill)
  — authoritative going forward.

## Status of the mission

Phase 1 usage: setup ✓ align ✓ plan/build ✓ maintain ✓ map ✓ prototype ✓.
Outstanding usage skill: **diagnosing-bugs** (deferred).
Phase 2 authoring arc: **Part I ✓** (this) · II–IV ahead · then fork/write a real skill.

## Zone of proximal development (next)

- **Lesson 9 = Part II: information hierarchy** — the ladder (in-skill step → in-skill reference →
  external reference behind a context pointer) + **progressive disclosure** + **co-location** +
  **branch** as the cleanest disclosure test. Completion criterion (clarity vs demand) likely belongs
  here or splits into its own beat.
- **Lesson 10 = Part III: leading words** (the signature/gem idea — ties to lesson, tracer bullets,
  red, tight; recruits pretraining priors). Highest-leverage, most non-obvious.
- **Lesson 11 = Part IV: pruning + 5 failure modes** (premature completion, duplication, sediment,
  sprawl, no-op) → then hands-on **fork/write a real skill** against one of Dat's repos.
- Still owed from Phase 1: **diagnosing-bugs** whenever Dat wants to circle back.
