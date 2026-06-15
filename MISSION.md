# Mission

**Dat wants to:** Understand Marp (Markdown Presentation Ecosystem) well enough to
**direct and course-correct an LLM** that generates slide decks for him.

## Why
He will not hand-author decks. He'll prompt an LLM to produce Marp markdown.
The LLM in use is assumed **low-reasoning / low-intelligence**, so it will make
predictable mistakes. Dat's job is to be the *editor-in-chief*: spot the broken
output, know the correct syntax, and point the model at the right docs.

## What success looks like
- Can read a Marp `.md` file and tell at a glance if it's well-formed.
- Knows the handful of directives that matter and how global/local/spot differ.
- Has a mental list of "things dumb LLMs get wrong in Marp" and the fix for each.
- Knows which official doc page to paste at the LLM when it's stuck.

## Scope (deliberately narrow)
- NOT building custom CSS themes from scratch (yet).
- NOT deep Marpit internals.
- Focused on: anatomy of a deck, directives, images/backgrounds, export, and
  LLM failure modes.

## Constraints
- Prefers minimal-token, telegraphic teaching.
- Wants overview-level fluency fast, not exhaustive mastery.
