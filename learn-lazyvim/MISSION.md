# Mission: LazyVim, one feature/plugin at a time

## Why
Dat has used LazyVim for a while and can already edit its config. The goal is to
move from *copy-paste config tweaks* to *confidently reading and modifying* the
plugins LazyVim ships — starting with the ones that touch his daily workflow — so
that when something behaves unexpectedly (e.g. `<leader>ff` showing `node_modules`)
he can reason about the cause and fix it from first principles instead of guessing.

This is an ongoing, à-la-carte mission: Dat will name a specific feature/plugin per
session. Each session should leave him able to fully read the relevant slice of his
own dotfiles.

## Success looks like
- Can read every line of his own `extend-snacks.lua` and explain what it changes vs. the LazyVim default.
- Knows the snacks `setup(opts)` merge model: how `opts` from his file layers onto LazyVim's defaults onto snacks' own defaults.
- Can predict picker behaviour (which files show up) from the `files`/`grep` source options.
- Can add or change a snacks module (or picker source/layout) and know which docs page to check.

## Constraints
- Learns incrementally — one named plugin/feature per session, not a firehose.
- Already fluent in basic LazyVim config (lua plugin spec files, `opts` tables, keymaps).
- Materials live in `/Users/dat/ws/repos/learn-x/learn-lazyvim` and should print well.

## Out of scope (for now)
- Writing a Neovim config from scratch / leaving LazyVim.
- Plugin development in Lua (authoring a plugin).
- Every one of snacks' 28 modules — only the ones present in Dat's config or that he asks about.
