# Workflow: editing and publishing the MOSbius website

Live site: https://mosbius.org (served by GitHub Pages from the `gh-pages` branch)
Source: https://github.com/peterkinget/MOSbiusBook (branch `main`)

The working copy lives in `~/GitHub/MOSbiusBook`, **outside iCloud**.
Each Mac has its own clone; GitHub is what keeps them in sync.
(iCloud sync corrupts git repos and creates "file 2.md" duplicates.)

## Every work session

```
cd ~/GitHub/MOSbiusBook
source venv_jupyterbook/bin/activate
git status                               # check your branch!
git pull                                 # get changes made on the other Mac
```

Edit, then build and preview locally:

```
jupyter-book clean . ; jupyter-book build .
cd _build/html && python3 -m http.server 8765    # Ctrl-C to stop
```

Open http://127.0.0.1:8765/ in a browser. (Opening `_build/html/index.html`
directly as a file does not work in Safari: it blocks the style sheets.)

Save the source to GitHub:

```
git status                               # review what changed
git add -A
git commit -m "short description of the change"
git push
```

## Publish to the live site

Only after the local build looks right, and from `main`:

```
ghp-import -n -p -c mosbius.org -f _build/html
```

- `-n` adds `.nojekyll`, `-p` pushes, `-c` writes the `CNAME` file
  (without it the custom domain breaks), `-f` force-replaces `gh-pages`.

Check the deployment, then the site:

```
gh run list --workflow=pages-build-deployment --limit 1
```

When it is complete, check https://mosbius.org and a few short links
(e.g. https://mosbius.org/555.html, https://mosbius.org/crew.html).

Then tag the release (see below) and record it in the table.

## Versions and tags

Every publish is a commit on `gh-pages`, and every source change a commit on
`main`, so all versions are kept. Releases worth going back to get a pair of
annotated git tags: one on the `main` commit the site was built from, and
`-html` on the `gh-pages` commit that was published.

| Tag (source on `main`) | Tag (HTML on `gh-pages`) | Published | What |
| --- | --- | --- | --- |
| `site-v1` (`48d45b4`) | `site-v1-html` (`70e3b50`) | 2025-07-31 | MOSbius Twist Classic (V1) website; live until 2026-10-10. Planned archive at `mosbius.org/v1/` |

To tag a new release right after publishing (replace `NAME`):

```
git fetch origin
git tag -a NAME -m "description" main
git tag -a NAME-html -m "description" origin/gh-pages
git push origin NAME NAME-html
```

`git tag -n1` lists the tags with their descriptions.

### Look at an old version locally

Without touching the live site, e.g. for `site-v1-html`:

```
rm -rf /tmp/oldsite && mkdir /tmp/oldsite
git archive site-v1-html | tar -x -C /tmp/oldsite
cd /tmp/oldsite && python3 -m http.server 8766    # open http://127.0.0.1:8766/
```

To rebuild an old version from source instead: `git worktree add /tmp/oldsrc site-v1`,
then build in `/tmp/oldsrc` (and `git worktree remove /tmp/oldsrc` afterwards).

### Roll the live site back

Point `gh-pages` at an older published commit and push; the newer versions
stay in the history:

```
git fetch origin
git push -f origin site-v1-html^{commit}:gh-pages    # or any gh-pages commit hash
```

Then check the deployment as above. To go forward again, publish as usual.

### Publishing an archived version under a subfolder (e.g. /v1/)

Prepared, not active yet. To serve the V1 website at `mosbius.org/v1/` next to
the current site, add it to the build before publishing:

```
jupyter-book clean . ; jupyter-book build .
mkdir -p _build/html/v1
git archive site-v1-html | tar -x -C _build/html/v1
rm -f _build/html/v1/CNAME _build/html/v1/.nojekyll
ghp-import -n -p -c mosbius.org -f _build/html
```

The V1 pages use relative links, so they work unchanged in the subfolder
(tested locally 2026-10-10). Once this is active, do it at every publish,
otherwise the next publish removes `/v1/` again.

## Setting up a new Mac

```
mkdir -p ~/GitHub && cd ~/GitHub
git clone -b main git@github.com:peterkinget/MOSbiusBook.git
cd MOSbiusBook
git fetch --tags
python3 -m venv venv_jupyterbook
venv_jupyterbook/bin/pip install -r requirements.txt
```

Needs an ssh key registered with GitHub, and Python 3.12
(`requirements.txt` pins Jupyter Book 1.x; 2.x is a different tool).
