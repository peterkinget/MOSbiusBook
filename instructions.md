# Publishing Instructions

Peter Kinget

July 31, 2025

- check your branch!

- go to the right folder + launch `venv`:
```
cd /Users/peterkinget/iCloudDrive/BOX/JupyterBook/mosbiusbook
source ../venv-jupyterbook/bin/activate.csh
```

- compile the book:
```
jupyter-book clean . ; jupyter-book build . 
```
- check the result 
```
open _build/html/index.html
```
- upload the new `gh-pages`
```
ghp-import -n -p -c mosbius.org -f _build/html
```
- check the GitHub build process
```
gh run list --workflow=pages-build-deployment --limit 1
```
- when complete, check https://mosbius.org
