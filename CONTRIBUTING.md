# Contributing to DataLens

Thanks for picking this up! DataLens is the starter repo for the
freeCodeCamp/NHCarrigan Summer 2026 Cohort sprint phase. The goal is a real,
working PR you can point to - not a toy exercise - so treat this like any
other open-source repo.

## Claiming an issue

1. Browse [open issues](../../issues) and find one that matches your skill
   level (`difficulty:easy`, `difficulty:medium`, `difficulty:hard`) and
   interest area (`area:analysis`, `area:cli`, `area:tests`, `area:docs`,
   `area:notebook`).
2. Comment on the issue to claim it (something as simple as "claiming this"
   is fine). Only claim one issue at a time so others have a chance to pick
   things up.
3. **You have 48 hours from claiming to open a PR.** If you go quiet and
   don't open a PR (even a draft one) within that window, the issue will be
   released for someone else to claim. This isn't a punishment - it just
   keeps issues from sitting locked while people are busy. Comment on the
   issue if you need more time and a maintainer will usually extend it.
4. If an issue is already claimed, look for another one, or ask in the
   cohort Discord about opening a related follow-up issue.

## Setting up locally

```bash
git clone <your fork URL>
cd datalens
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

This installs `pandas`, `matplotlib`, `click`, `pytest`, and the `datalens`
package itself (editable), which also gives you the `datalens` CLI command.

## Running tests locally

```bash
pytest
```

Please run the full test suite before opening a PR. If you're adding a new
function to `datalens/cleaning.py` or `datalens/analysis.py`, add tests for
it in the matching `tests/test_*.py` file - PRs that only touch the CLI
layer (`datalens/cli.py`) don't need CLI-level tests beyond the existing
smoke tests, but new *logic* should live in the package and be tested there.

## Opening a PR

- Keep PRs focused on a single issue.
- Reference the issue you're closing (e.g. `Closes #12`) in the PR
  description.
- Make sure `pytest` passes locally - CI will also run it automatically on
  your PR (see `.github/workflows/ci.yml`).
- Add or update a docstring for any new public function.
- If your change affects CLI usage, update the examples in `README.md`.

## Code style

Nothing fancy required - just try to match the style already in the file
you're editing (type hints on function signatures, docstrings with `Args`/
`Returns`/`Raises` sections, no in-place `DataFrame` mutation where a
function can return a new one instead).

## Questions

Ask in the cohort Discord. If something in this repo is confusing or the
setup steps don't work for you, that's useful signal - open an issue about
the docs (`area:docs`) rather than suffering in silence.
