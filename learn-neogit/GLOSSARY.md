# Neogit & Git CLI Glossary

Consistent terms for this workspace. Adhere to these in all lessons and records.

## Git concepts

**Working tree**:
The directory on your filesystem where you edit files. Git tracks changes here.

**Index / Staging area**:
The intermediate area between your working tree and the repository. Changes must be staged (added to the index) before they can be committed.
_Avoid_: Staging cache, pending area

**Commit**:
A snapshot of the index at a point in time. Each commit has a SHA hash, an author, a timestamp, and a message.

**HEAD**:
The commit your working tree is currently based on. Usually points to the tip of a branch. A "detached HEAD" means it points directly to a commit instead.

**Ref**:
A named pointer to a commit. Branches, tags, and HEAD are all refs.

**Remote**:
A named reference to another repository (usually on a server). Conventionally called `origin`.

**Upstream**:
The remote branch that your local branch tracks. Used by `git pull` and `git push` to know where to fetch from / push to.

## Neogit concepts

**Status buffer**:
The main neogit view. Shows HEAD, untracked files, unstaged changes, staged changes, stashes, unpushed/pulled commits, and recent commits. Every section maps to a `git` CLI concept.

**Popup**:
A transient menu in neogit opened by a mnemonic key (e.g. `c` for commit, `b` for branch). Lists available actions, arguments, and options for that git operation.

**Hunk**:
A contiguous block of changed lines in a file. neogit lets you stage/unstage individual hunks or even lines within a hunk.

## Staging workflow

**Index (staging area)**:
The intermediate layer between your working tree and commits. Changes must be staged (added to the index) before committing.

**Staging**:
Adding changes to the index. In neogit: <kbd>s</kbd> (stage item), <kbd>S</kbd> (stage all), <kbd>C-s</kbd> (stage all including untracked).
CLI equivalent: <code>git add</code>, <code>git add .</code>, <code>git add -A</code>

**Unstaging**:
Removing changes from the index while keeping them in the working tree. In neogit: <kbd>u</kbd> (unstage item), <kbd>U</kbd> (unstage all).
CLI equivalent: <code>git restore --staged &lt;file&gt;</code>

**Hunk**:
A contiguous block of changed lines. Stage/unstage individual hunks with <kbd>Tab</kbd> to expand, then <kbd>s</kbd> or <kbd>u</kbd>.
CLI equivalent: <code>git add -p</code> (interactive patch mode)

## Neogit keybinding patterns

**Popups** (single mnemonic keys, opened from status buffer):
- `c` — Commit popup
- `b` — Branch popup
- `P` — Push popup
- `p` — Pull popup (note: lowercase)
- `f` — Fetch popup
- `m` — Merge popup
- `r` — Rebase popup
- `Z` — Stash popup
- `v` — Revert popup
- `A` — Cherry-pick popup
- `X` — Reset popup

**Status buffer actions** (single keys):
- `s` — Stage item under cursor
- `u` — Unstage item under cursor
- `S` — Stage all unstaged
- `U` — Unstage all staged
- `x` — Discard (danger: loses changes)
- `<tab>` — Toggle expand/collapse section or hunk
- `$` — Show command history
- `1`-`4` — Set section depth
- `<cr>` — Open file under cursor
