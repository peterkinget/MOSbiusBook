# Workflow: editing and publishing the MOSbius Book

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

Edit, then build and check locally:

```
jupyter-book clean . ; jupyter-book build .
open _build/html/index.html
```

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

To roll back, the previous site is the previous commit on `gh-pages`:
`git log origin/gh-pages` shows the history.

## Setting up a new Mac

```
mkdir -p ~/GitHub && cd ~/GitHub
git clone -b main git@github.com:peterkinget/MOSbiusBook.git
cd MOSbiusBook
python3 -m venv venv_jupyterbook
venv_jupyterbook/bin/pip install -r requirements.txt
```

Needs an ssh key registered with GitHub, and Python 3.12
(`requirements.txt` pins Jupyter Book 1.x; 2.x is a different tool).
