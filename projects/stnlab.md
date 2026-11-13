# STNLab: temporal constraints, bounds and repairs

[Live inspector](https://midya8.github.io/stnlab/) · [Source](https://github.com/midya8/stnlab) · [Method and sources](https://github.com/midya8/stnlab/blob/main/METHOD.md)

STNLab checks small temporal networks: whether their constraints fit together, which time differences they imply, what one extra constraint changes, and which edge removals repair a conflict. Each answer comes with a path, a complete schedule or a negative cycle that can be checked independently.

## Four inspectors

| Question | Inspector | Evidence |
| --- | --- | --- |
| Is the plan consistent, and how tight is each bound? | [Temporal bounds](https://midya8.github.io/stnlab/) | Attaining schedules, unbounded rays, negative cycles and single-edge redundancy checks. |
| What would one new constraint change? | [Insertion sensitivity](https://midya8.github.io/stnlab/insertions.html) | Exact consistency threshold, boundary schedule, changed bounds and candidate-first contradiction. |
| Can hidden time points be removed without losing their consequences? | [Existential projection](https://midya8.github.io/stnlab/projection.html) | Retained bounds, full extensions, rejection paths and counterexamples to naive deletion. |
| What are all the minimal conflicts and repairs? | [Conflicts and repairs](https://midya8.github.io/stnlab/conflicts.html) | Complete conflict/correction sets, deletion schedules, restoration cycles and hitting-set duality. |

An edge `[u,v,w]` means `t[v] - t[u] <= w`. The anchor `t0=0` removes only a common translation; negative real times are allowed. The public base input accepts up to six points and twelve edges. A proposed insertion can be a thirteenth edge, and derived projection witnesses can exceed the public input windows.

## What is checked

Native Floyd-Warshall and Bellman-Ford generation is checked by independent permutation/edge-product enumeration. The browser uses separate recursive path search. The current suite has 31 Python tests and 12 Node/Chrome tests. Isolated installed-wheel checks cover 11 base, 10 insertion, 12 projection and 10 conflict controls through both module and console entry points, outside the checkout. Chrome checks proof panels at 320, 390 and 1280 pixels.

These are original synthetic controls, not real plans or a speed benchmark. Runtime code, controls, tests and attribution are unchanged by this prose review.

## Important distinctions

- Finite bounds are individually attainable. Picking several endpoints independently need not produce one valid schedule. Duplicate edges can each be redundant when removed alone without being jointly removable.
- Insertion compares one candidate at a time against an immutable base. The distance-matrix update is quadratic; the exhaustive certificate generation and checker are not. The 41-weight sweep contains alternatives, not accumulated updates. [Insertion contract](https://github.com/midya8/stnlab/blob/main/INSERTIONS.md).
- Projection restricts the closed network, not the original edge list. Retained values must fit jointly and extend to a full original schedule. A hidden inconsistent component still makes the projection empty. [Projection contract](https://github.com/midya8/stnlab/blob/main/PROJECTION.md).
- Minimal means no proper subset has the same conflict or repair property. It does not mean smallest cardinality. All original edges are removable; there are no hard constraints or weighted repair priorities. [Conflict contract](https://github.com/midya8/stnlab/blob/main/CONFLICTS.md).

This is bounded classical temporal reasoning. It does not handle resources, uncertain durations, task execution or real calendar changes, and it makes no new-algorithm or scalable-solver claim. The browser needs no API or paid model.

## Reproduce

```bash
git clone https://github.com/midya8/stnlab.git
cd stnlab
python -m unittest discover -s tests -v
npm test
bash tools/check_wheel.sh
python -m http.server 8000 --directory docs
```

The linked method and family contracts preserve the original attribution ledgers and report schemas.
