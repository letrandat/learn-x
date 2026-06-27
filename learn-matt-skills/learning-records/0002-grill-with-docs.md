# 0002 — grill-with-docs (the flagship)

Date: 2026-06-19
Status: accepted

## Context

Dat completed Lesson 2 AND ran `setup-matt-pocock-skills` hands-on himself: `/Users/dat/ws`
now has `docs/agents/{domain,issue-tracker,triage-labels}.md` (local-markdown tracker) and a
`## Agent skills` block in `/Users/dat/ws/CLAUDE.md`. So the planned "Lesson 3 = run setup
hands-on" is already done — collapsed it.

## What was taught (Lesson 3)

`grill-with-docs` as a pure orchestrator (3-line body) composing two model-invoked players:
- **grilling** — relentless, tree-structured interview; one question at a time; always
  recommends an answer; explores code before asking. Fixes failure mode #1.
- **domain-modeling** — the *active* discipline: five moves (challenge / sharpen / scenarios
  / cross-ref code / inline update); writes `CONTEXT.md` (opinionated glossary, `_Avoid_`
  lists, no impl detail) + ADRs (one paragraph, three-gate test). Fixes failure mode #2.
- **lazy creation** as the connecting discipline.

## Key insight

Best live example yet of the composition rule: a user-invoked conductor whose entire value
is sequencing two reusable disciplines. Reinforces Lesson 1's axis.

## Zone of proximal development (next)

- **Strongly recommended:** run a *real* grilling session on something Dat is actually
  planning (experiential > expository for this skill).
- Then **Lesson 4** = the plan→slice→build chain: `to-prd` → `to-issues` → `implement`/`tdd`,
  ideally end-to-end on the same artefact from the grilling session.
- Authoring arm still later (writing-great-skills), per confirmed "both, usage first."
