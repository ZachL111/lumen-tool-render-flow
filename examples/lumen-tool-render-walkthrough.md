# Lumen Tool Render Flow Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | file span | 214 | ship |
| stress | terminal width | 152 | ship |
| edge | argument risk | 202 | ship |
| recovery | report density | 172 | ship |
| stale | file span | 174 | ship |

Start with `baseline` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

If `stress` becomes less cautious without a clear reason, I would inspect the drag input first.
