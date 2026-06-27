# Working notes — learn-lazyvim

## How Dat likes to learn
- À la carte: he names one feature/plugin per session. Don't pre-build a curriculum ahead of his ask.
- Already comfortable with LazyVim plugin-spec files, `opts` tables, keymaps. Don't re-teach the basics of "what is a plugin spec".
- Ground every lesson in **his actual dotfiles** (`repos/dotfiles/nvim/.config/nvim/`), not generic examples. Quote his real config.
- Telegraphic communicator; keep prose tight, lead with the concrete.

## Teaching style for this workspace
- Each lesson = one tightly-scoped win, tied to a file he already has open.
- Use the shared `assets/styles.css` + `assets/quiz.js`. Lua snippets get hand-applied syntax spans (`.kw/.str/.num/.com/.ann`).
- Prefer a "default vs. his override vs. effect" framing — the merge model is the recurring mental tool.

## Source-fetch gotcha
- GitHub `blob/` URLs return only page chrome to WebFetch. Always fetch `raw.githubusercontent.com/.../main/docs/<x>.md`.

## Context that seeded this workspace
- Session opened right after fixing `<leader>ff` showing `node_modules` in `~/.config/opencode/` (a non-git dir). Root cause: `fd` only honours `.gitignore` inside a git repo; fix added `exclude = { "node_modules", ".git" }` to the snacks `files`/`grep` sources. Lesson 0001 builds on this live example.
