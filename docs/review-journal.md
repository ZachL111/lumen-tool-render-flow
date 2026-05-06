# Review Journal

The review surface for `lumen-tool-render-flow` is deliberately narrow: one fixture, one scoring rule, and one local check.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its cli tools focus without claiming live deployment or external usage.

## Cases

- `baseline`: `file span`, score 214, lane `ship`
- `stress`: `terminal width`, score 152, lane `ship`
- `edge`: `argument risk`, score 202, lane `ship`
- `recovery`: `report density`, score 172, lane `ship`
- `stale`: `file span`, score 174, lane `ship`

## Note

This file is intentionally plain so the fixture remains the source of truth.
