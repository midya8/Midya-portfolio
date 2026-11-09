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
