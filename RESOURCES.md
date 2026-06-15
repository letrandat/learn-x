# Resources

High-trust, official sources. **Paste these at your LLM when it gets syntax wrong.**

## Primary (official — trust these)
- **Marpit Markdown syntax** — https://marpit.marp.app/markdown
  Slide separation, the three directive scopes, fragmented lists. The canonical syntax page.
- **Marpit Directives** — https://marpit.marp.app/directives
  Full directive list, global vs local vs spot (underscore), front-matter form.
- **Marpit Image syntax** — https://marpit.marp.app/image-syntax
  Resizing, background images (`bg`), split backgrounds, filters. *The single best page to hand an LLM for image bugs.*
- **Marp Core (README)** — https://github.com/marp-team/marp-core
  Adds themes (default/gaia/uncover), math (KaTeX/MathJax), emoji, `<!-- fit -->` auto-scaling, `size` directive.
- **Marp CLI (README)** — https://github.com/marp-team/marp-cli
  Export to HTML/PDF/PPTX/PNG, watch/server/preview modes.
- **Marp for VS Code** — https://github.com/marp-team/marp-vscode
  Live preview + export inside the editor. Easiest way to *see* the LLM's output.

> Note: marpit.marp.app pages are JS-rendered SPAs — WebFetch can't read them. For
> raw text, use the GitHub repos (`marp-team/marpit/docs/*.md`) instead.

## Tooling
- **Marp web editor (no install)** — https://web.marp.app/
  Paste markdown, see slides instantly. Best feedback loop for checking LLM output.

## Community (wisdom — test your skills)
- GitHub Discussions: https://github.com/orgs/marp-team/discussions
- Tag `marp` on Stack Overflow: https://stackoverflow.com/questions/tagged/marp

## Verification log
- `marp: true` front-matter requirement confirmed via marp-vscode README + multiple guides (2026-06-15).
- Built-in themes confirmed as default/gaia/uncover (NOT "gaudy") via marp-core README (2026-06-15).
- Directive scopes & image syntax pulled from raw marpit docs on GitHub (2026-06-15).
