# LazyVim / snacks.nvim Resources

## Knowledge

- [snacks.nvim — README & module list (folke)](https://github.com/folke/snacks.nvim)
  Canonical index of all 28 snacks modules and how `setup(opts)` enables them. Use for: "what modules exist", "is X part of snacks", the per-module `enabled = true` model.
- [snacks.nvim — picker docs](https://github.com/folke/snacks.nvim/blob/main/docs/picker.md) ([raw](https://raw.githubusercontent.com/folke/snacks.nvim/main/docs/picker.md))
  Authoritative reference for sources, finders, and per-source options (`hidden`, `ignored`, `follow`, `exclude`, `cmd`, `args`) plus layouts. Use for: any picker behaviour question (why a file shows/hides, layout sizing). NOTE: fetch the *raw* URL — the GitHub blob page returns only chrome.
- [snacks.nvim — terminal docs](https://raw.githubusercontent.com/folke/snacks.nvim/main/docs/terminal.md)
  Reference for `Snacks.terminal.toggle`, `win.style = "terminal"`, float vs split behaviour. Use for: the `terminal` block in `extend-snacks.lua`.
- [LazyVim docs — Snacks integration & default keymaps](https://www.lazyvim.org/)
  How LazyVim wires snacks in as its default picker/dashboard/etc., and which keys (`<leader>ff`, `<leader>/`) map to which source. Use for: connecting a keymap to the snacks source behind it.

## Wisdom (Communities)

- [r/neovim](https://www.reddit.com/r/neovim/)
  High-signal, heavily-moderated. Use for: config critique, "is this the idiomatic way", picker/snacks edge cases.
- [folke/snacks.nvim — Discussions / Issues](https://github.com/folke/snacks.nvim/discussions)
  Straight from the maintainer and power users. Use for: confirming undocumented options, reporting/searching real bugs.
- [LazyVim — GitHub Discussions](https://github.com/LazyVim/LazyVim/discussions)
  Use for: LazyVim-specific override patterns and "how do I change the default for X".

## Gaps
- No single authoritative page maps *every* LazyVim default keymap → snacks source. The picker docs + `:LazyExtras` / `<leader>sk` (search keymaps) in-editor fill this; record findings in the glossary as they surface.
