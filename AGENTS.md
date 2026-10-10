# Notes for AI agents

The MOSbius Book is a Jupyter Book (1.x) published at https://mosbius.org
(GitHub Pages, `gh-pages` branch, custom domain via CNAME).
Source: git@github.com:peterkinget/MOSbiusBook.git, branch `main`.

- `WORKFLOW.md`: how to build, save and publish; setting up a new Mac.
- `TODO.md`: the book's to-do list (not published).

## Working rules

- Plan and ask before acting; the owner wants to be careful.
- Commit locally, but ask before `git push`.
- Never run `ghp-import` or modify `gh-pages` unless the owner explicitly asks
  in that session.
- Moving or renaming pages changes public URLs. The short links (`555.html`,
  `crew.html`, `blinky.html`, ... via `html_extra_path` in `_config.yml`)
  are redirects to chapter pages and must keep working.
- Only files listed in `_toc.yml` are built (`only_build_toc_files: true`);
  drafts like `experiment_DSM1/` stay unpublished until added there.
- Owner's shell is zsh, with `noclobber` set: `>` will not overwrite an
  existing file. Python env folder is `venv_jupyterbook/` (not hidden).

## Migration out of iCloud: remaining steps (remove when done)

Done 2026-10-10: clone, cleanup, venv, build checked against the live site,
default branch set to `main`, old branches resolved.

1. [done 2026-10-10] Published from the new clone (gh-pages 3c2edd1);
   mosbius.org and the short links checked.
2. [done 2026-10-10] iCloud folder renamed to
   `~/BOX/JupyterBook/mosbiusbook_ARCHIVE_do_not_edit`.
3. Set up the Mac mini per `WORKFLOW.md`.
