# 0001 — Skills mental model + the setup skill

Date: 2026-06-19
Status: accepted

## What was taught

First two lessons of the course:
- **Lesson 1** — mental model: skill = composable markdown prompt; the user-invoked vs
  model-invoked axis; the composition rule (flat orchestration); the four failure modes;
  the daily flow (grill → prd → issues → tdd → maintain).
- **Lesson 2** — `setup-matt-pocock-skills` dissected: file anatomy, frontmatter contract,
  the three per-repo configs (issue-tracker / triage-labels / domain), and the design
  principles worth stealing (config-as-markdown, teach-don't-assume, one-decision-at-a-time,
  defaults-from-evidence, idempotent writes, confirm-before-write).

## Key insight to carry forward

The setup skill is a *worked example* of how every good skill is built. Frame future
skills against it: explore → present → confirm → write, with judgement at each step.

## Zone of proximal development (what to teach next)

Dat confirmed end goal: **both, usage first then authoring.** Path:
- **Lesson 3 (next):** hands-on — run `setup-matt-pocock-skills` on a real repo, read the
  three configs it writes.
- **Lesson 4:** `grill-with-docs` — alignment + `CONTEXT.md` (Matt's flagship, failure modes 1 & 2).
- **Lesson 5:** trace the daily flow end-to-end (`to-prd` → `to-issues` → `tdd`).
- **Later (authoring arm):** `writing-great-skills` + dissect a second skill for reinforcement,
  then Dat forks/writes one.

## Correction (Dat caught this)

Original daily-flow diagram put `/tdd` at the build stage. Wrong altitude: the build
orchestrator is **`/implement`** (user-invoked) — it drives the PRD/issues, then calls
`/review` and commits, *reaching for* `tdd` + `diagnosing-bugs` (model-invoked) as
disciplines. Great live demonstration of the composition rule. Lesson 1 diagram + glossary
fixed. Note: README's user-invoked list omits `implement`, but its frontmatter has
`disable-model-invocation: true`, so it is user-invoked — a gap in Matt's own docs.

## Notes

- Mission "done" criteria still my inference — refine as we go.
