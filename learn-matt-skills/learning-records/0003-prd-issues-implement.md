# 0003 — plan → slice → build chain

Date: 2026-06-19
Status: accepted

## What was taught (Lesson 4)

The three skills that turn alignment into merged code:
- **to-prd** — synthesises conversation into a PRD (NO interview — the deliberate complement
  of grill-with-docs). Steps: explore w/ glossary + ADRs → sketch fewest/highest test seams
  (confirm with user) → write PRD + publish tagged `ready-for-agent`. Bans file paths/snippets
  (decisions age slow, code ages fast).
- **to-issues** — breaks PRD into vertical slices = tracer bullets (cut through ALL layers,
  demoable on their own; NOT horizontal). Prefactor first ("make the change easy, then make
  the easy change"). Quiz user on granularity/deps, iterate to approval, publish in dependency
  order tagged `ready-for-agent`.
- **implement** — 5-line build conductor; uses tdd at pre-agreed seams; typecheck + single
  tests often, full suite at end; then /review; commit.

## Key insights

- The **setup config threads through all three** — each opens "run /setup if not provided."
  Concrete payoff of Lesson 2.
- `ready-for-agent` is the **handoff token** carried the whole length of the line.
- The line is a funnel narrowing ambiguity: conversation → PRD → slices → code.

## Zone of proximal development (next)

Daily-flow loop now fully covered (setup ✓, align ✓, plan/slice/build ✓). Options:
- **maintain stage** — `improve-codebase-architecture` + `codebase-design` (failure mode #4,
  ball of mud). Natural to close the loop.
- **experiential** — run the real line (grill → to-prd → to-issues) on a small feature against
  Dat's local-markdown tracker.
- **authoring arm** — begin `writing-great-skills` (Dat's confirmed phase 2). Could pair with
  the maintain stage or come after.

Recommend: Lesson 5 = maintain stage (closes the usage loop), then pivot to authoring.
