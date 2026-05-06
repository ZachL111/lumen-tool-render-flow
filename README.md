# lumen-tool-render-flow

`lumen-tool-render-flow` explores cli tools with a small Python codebase and local fixtures. The technical goal is to package a Python local lab for render analysis with node-edge fixtures, cycle and reachability reports, and documented operating limits.

## Problem It Tries To Make Smaller

I want this repository to be useful as a quick reading exercise: fixtures first, implementation second, verifier last.

## Lumen Tool Render Flow Review Notes

The first comparison I would make is `file span` against `terminal width` because it shows where the rule is most opinionated.

## Working Pieces

- `fixtures/domain_review.csv` adds cases for file span and terminal width.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/lumen-tool-render-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `file span` and `terminal width`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Design Notes

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The Python code keeps the review rule close to the tests.

## Example Run

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Tests

The same command runs the local verification path. The highest-scoring domain case is `baseline` at 214, which lands in `ship`. The most cautious case is `stress` at 152, which lands in `ship`.

## Known Limits

No external service is required. A deeper version would add more negative cases and a clearer boundary around invalid input.
