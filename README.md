# pedro-nunez.github.io

Personal academic website of Pedro Núñez, built with Jekyll and hosted
on GitHub Pages. Content lives in Markdown pages (`*.md`) and data
files under `_data/`; see `CLAUDE.md` for the full build history and
the reasoning behind non-obvious decisions.

## Previewing the site locally

Requires Ruby and Bundler.

```
bundle install
bundle exec jekyll serve
```

Then open <http://127.0.0.1:4000>. The site rebuilds automatically as
you edit files.

## Regenerating the CV PDF

The "PDF version" button on `/cv/` links to `assets/pdfs/cv.pdf`, which
is generated from `_data/cv.yml` via [rendercv](https://rendercv.com) by
`scripts/export_cv_pdf.py`. This is a separate step from the Jekyll
build above — nothing regenerates the PDF automatically, so after
editing `_data/cv.yml` you need to re-run the script by hand and
commit the updated PDF.

One-time setup (requires Python 3; no other system packages needed —
rendercv installs its own Typst typesetting engine via pip):

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

Every time `_data/cv.yml` changes:

```
source .venv/bin/activate   # if not already active
python scripts/export_cv_pdf.py
```

This writes `assets/pdfs/cv.pdf`. See the module docstring at the top of
`scripts/export_cv_pdf.py` for how the script works, and the
`scripts/export_cv_pdf.py` entry in `CLAUDE.md` for why each
section/formatting choice is the way it is.
