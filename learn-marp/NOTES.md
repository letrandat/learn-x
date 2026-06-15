# Notes

## Teaching preferences

- Telegraphic, minimal tokens. Noun-phrases fine. Skip pleasantries in lessons.
- Wants overview-level fluency, fast. Not a completionist.
- Goal is _editorial_ skill (spot & correct LLM output), not authoring from scratch.

## Working notes

- Mission is knowledge-heavy + a "failure-mode pattern library." Skills come via
  spot-the-bug drills rather than open authoring.
- Best feedback loop for him: paste LLM output into https://web.marp.app/ and eyeball.
- Keep a running "LLM failure modes" list — this IS the deliverable. Lives in the
  cheat sheet reference doc.

## Tooling (confirmed 2026-06-15)

- Node: ✓ LibreOffice: ✗ → default `--pptx` (images) only; no `--pptx-editable`.
- Local package.json has ONLY `@marp-team/marpit` (engine, no themes/export).
  Steer to `npx @marp-team/marp-cli@latest …`, or `npm i -D @marp-team/marp-cli`.

## Likely future lessons (ZPD ladder)

1. ✅ Mental model + deck anatomy + top failure modes (lesson 0001)
2. ✅ MD→PPTX lifecycle + LLM prompting harness (lesson 0002 + reference 0002)
3. ✅ Full worked example: notes → deck → pptx (lesson 0003 + examples/)
4. Directive scopes deep-dive (global/local/spot) — the #1 LLM confusion
5. Images & backgrounds drill (bg, split, fit vs contain)
6. Get him to run preview/export for real; debug browser-not-found if it arises
7. Generate a deck from HIS own notes → he practices the review step

## Unknowns to resolve

- His preferred Marp surface: CLI vs VS Code vs web editor?
