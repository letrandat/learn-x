# Baseline: confident LazyVim user; learning snacks à la carte

Dat has used LazyVim "for a while" and is already fluent in plugin-spec files, `opts` tables, and keymaps. He learns one named feature/plugin per session — don't pre-build a curriculum. First topic: **snacks**, grounded in his own `extend-snacks.lua`.

**Established prior knowledge:** can edit config and read Lua plugin specs. Do NOT re-teach plugin-spec basics.

**Misconception corrected (live, this session):** he expected the snacks `files` picker to always hide `node_modules`. Real rule: hiding gitignored files depends on `ignored=false` AND the `fd` backend, which only honours `.gitignore` *inside a git repo*. In a non-git dir (`~/.config/opencode/`) it leaked. Fix: explicit `exclude = { "node_modules", ".git" }` on `files`/`grep` sources. This is high-value — it predicts future confusion about picker filtering and the defaults `hidden`/`ignored`.

**Implications for next sessions:** the "snacks defaults → LazyVim defaults → your opts" merge model landed as the core mental tool; reuse it. Candidate next topics he hasn't covered: snacks layouts/presets in depth, the terminal module, or how LazyVim binds keys to picker sources. Wait for him to name one. No evidence yet that the quiz/merge model is *retained* — revisit with a spaced retrieval question next session.
