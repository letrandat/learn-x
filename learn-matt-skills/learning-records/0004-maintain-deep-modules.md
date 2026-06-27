# 0004 — maintain stage (deep modules)

Date: 2026-06-19
Status: accepted

## What was taught (Lesson 5)

The maintain stage — failure mode #4 (ball of mud):
- **codebase-design** (model-invoked vocab skill): glossary (module, interface, implementation,
  depth, seam, adapter, leverage, locality) used exactly, no substitutes. Deep = lots of
  behaviour behind small interface; shallow = interface ≈ implementation. Four principles:
  deletion test, depth-is-interface-not-impl, interface-is-the-test-surface, one-adapter-
  hypothetical-two-real. Rejects depth-as-lines-ratio (rewards padding).
- **improve-codebase-architecture** (user-invoked orchestrator): busiest composition — pulls
  codebase-design (vocab) + Explore (scan) + grilling (design pick) + domain-modeling (capture).
  3 steps: explore (deletion test) → visual HTML report to TEMP dir, not repo (Tailwind+Mermaid,
  before/after cards, strength badges, top rec) → grilling loop on chosen candidate.

## Key insights

- Maintain feeds back into align: sharpens CONTEXT.md + records ADRs → next feature starts
  cleaner. Closes the loop.
- The HTML-report-to-temp pattern == how this teach course's own lessons are built.
- "seam" now unified across Lesson 4 (test boundary) and Lesson 5 (Feathers' definition).

## Status of the mission

**Usage half COMPLETE.** Full daily loop covered: setup ✓ align ✓ plan/slice/build ✓ maintain ✓.
Per Dat's confirmed goal ("both, usage first"), next is PHASE 2 — authoring.

## Zone of proximal development (next)

- **Lesson 6 = writing-great-skills** — how to author skills (frontmatter, progressive
  disclosure, composition, bundled resources). Dat now has 5 dissected skills as worked
  examples to generalise from — ideal timing.
- Then: have Dat write/fork a real skill (capstone).
- Optional experiential detours any time: run grill→prd→issues live, or a real architecture
  review.
