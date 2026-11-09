# STNLab: every implied deadline needs evidence


## STNLab - temporal bounds with attainable schedules

[Live inspector](https://midya8.github.io/stnlab/) · [Source](https://github.com/midya8/stnlab) · [Method and source ledger](https://github.com/midya8/stnlab/blob/main/METHOD.md) · [Case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/stnlab.md)

For tiny hand-written AI plans, inspect every implied time difference: a tight path plus a complete schedule attaining the bound, or an explicit ray proving it unbounded. Negative cycles show exactly why no schedule exists, even away from the anchor. Removing one edge returns an alternate implication path or a complete separating schedule. Eleven editable controls include duplicate edges, zero cycles, free components and a chain with bound 100.

Native Floyd-Warshall/Bellman-Ford generation, independent permutation/edge-product verification and recursive browser search agree. Nine native tests cover exhaustive tiny graphs, seeded networks and strict CLI rejection; real Chrome checks all proof panels at three widths. Six points and twelve constraints, real-valued times, no resource capacity, uncertain durations or execution guarantee. Classic temporal-network theory, not a new optimization algorithm.

## Reproduce

```bash
git clone https://github.com/midya8/stnlab.git
cd stnlab
python -m unittest discover -s tests -v
npm test
bash tools/check_wheel.sh
python -m http.server 8000 --directory docs
```

An edge `[u,v,w]` means `t[v] - t[u] <= w`. The anchor `t0=0` only removes a common translation; negative times are allowed. Inconsistent networks produce no finite-bound or redundancy report. Finite bounds are individually attainable, not necessarily jointly selectable endpoints. Parallel duplicate edges can each be redundant when removed separately without being jointly removable. The browser runs its own solver without an API. The native strict verifier replays complete reports with a separate enumeration algorithm and rejects altered witnesses, unknown keys, duplicate JSON keys and non-finite values.

See the linked method for the seven-source attribution ledger and exact report contract. Synthetic controls are original. No real calendars, private records, paid models, task execution or scalable STNU/dispatchability claim.


## STNLab insertion sensitivity

One proposed temporal constraint, an exact consistency threshold and every changed implied bound. [Source](https://github.com/midya8/stnlab) · [Insertion inspector](https://midya8.github.io/stnlab/insertions.html) · [Contract and source ledger](https://github.com/midya8/stnlab/blob/main/INSERTIONS.md).

Native old-matrix one-edge closure is checked against independent full recomputation. Inspect the old return path, a complete schedule at the feasibility boundary, a candidate-first negative cycle, or a still-unbounded anchored ray. All finite post-insertion bounds include attaining schedules; 41 integer weights are separate alternatives, not accumulated changes.

Ten new synthetic controls include exact-boundary feasibility, a missing return path, a pre-inconsistent base, duplicate/self-loop cases, a six-point threshold outside the input window and a 12-edge base plus candidate. The original inspector remains intact. Seventeen Python tests, six Node/real-Chrome tests and installed-wheel checks cover both families. This is bounded classical temporal reasoning, not event execution, uncertainty handling, a new algorithm or a scalable verifier.
