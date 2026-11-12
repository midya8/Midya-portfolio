# CutLab

CutLab minimizes a supplied binary energy over at most six variables. Two inspectors show why a fixed-cost answer is optimal and how the complete optimum family changes when unary costs vary. Python uses exact rational arithmetic; the browser has an independent BigInt implementation.

[Flow/cut inspector](https://midya8.github.io/cutlab/) · [Response-path inspector](https://midya8.github.io/cutlab/path.html) · [Source and reproduction](https://github.com/midya8/cutlab) · [Fixed-cost method](https://github.com/midya8/cutlab/blob/main/METHOD.md) · [Path method](https://github.com/midya8/cutlab/blob/main/PATH.md)

## Fixed costs: retain the reduction and the certificate

Signed rational unary costs and asymmetric submodular pair tables become a directed s-t network. The report reconstructs every pair entry and retains all terminal shifts. For every assignment, original energy equals offset plus cut capacity. Non-submodular pairs are refused rather than clipped.

Every shortest augmenting path, bottleneck and complete edge-flow state remains visible. A six-augmentation control needs a reverse variable arc to cancel earlier flow. Each cut exposes capacity minus flow as outgoing residual slack; a feasible flow and an equal-capacity cut certify the minimum. Independent original-energy enumeration checks the answer on these small inputs.

The residual SCC graph gives the whole forward-closed family of minimum cuts, including forced and free labels. Free does not mean independently selectable: tied agreement has two free variables but only two optimal masks. The zero six-variable graph has all 64 assignments optimal.

## When local choices fail

Strict best single-flip search starts at mask 0 with energy 2. Both neighbors cost 3, so it stops, although mask 3 has energy 0. Flow 1 plus offset -1 certifies that optimum. Dropping the offset would give the wrong energy.

In a separate coupling control, unary-only picks energy 5 while two tied minima cost 3. Its gap of 2 is an explicitly incomplete baseline, not a solver benchmark. Negative and rational costs, asymmetric tables, disconnected ties, forced/free mixtures, zero capacities and ten seeded signed networks remain available.

## Affine unary response paths

Keep pair costs fixed and make each unary cost affine in a rational parameter. The path inspector retains every assignment's line and intersects its exact inequalities against all competitors. It shows closed optimal regions, open-cell families and breakpoint ties, including assignments optimal only at a single point and ties that persist across an interval.

The default path has open-cell masks 7, 0 and 1, with breakpoints 1/4 and 2. One label leaves and returns. Arbitrary signed slopes therefore do not inherit nested-label guarantees from source-sink-monotone parametric flow algorithms. This implementation enumerates all assignments; it is not scalable parametric maxflow.

The 18 synthetic path controls retain 214 assignment lines, 6,084 inequalities and 92 full flow/cut witnesses at boundary points or cell midpoints. A midpoint solve alone would not establish an entire region; the complete inequality intersection does.

## Verification and reproduction

The current suite has 30 Python tests, including all 21 original fixed-cost tests, and six Node/actual-Chrome tests. The CI Python matrix covers 3.10-3.13. Counts within a test are controls, not additional test functions.

Fixed-cost checks include 250 independent dense-energy cases, 160 every-cut slack audits, augmentation replay, conservation, capacity, independent reachability/SCC checks, full optimum families, 100 scaling/offset controls and 80 relabelings. The 24 Python/BigInt reports agree on 24,624 exact scalar leaves. Chrome checks the rendered cut, flow, reduction, residual and local-search records, SVG labels and colors, export, invalid/stale clearing and 320/390/1280 containment.

Path checks include 120 independent path oracles, 50 endpoint-inequality audits, 40 objective transformations, 40 parameter reversals and 60 concave active-slope checks. The 18 full Python/BigInt path reports agree on 90,732 exact scalar leaves. Chrome checks all 214 lines, 6,084 inequality rows, 92 point/cell summaries with flow reports, region tables and envelope geometry. Floating plot coordinates never choose an optimum.

From the source checkout:

```sh
python -m pip install .
python -m unittest discover -s tests -v
PYTHONPATH=. python tools/build_audits.py
PYTHONPATH=. python tools/build_paths.py
npm test
sh tools/wheel_smoke.sh
python -m cutlab examples/demo.json --output /tmp/cutlab.json
python -m cutlab examples/path.json --path --output /tmp/path.json
```

Node 22+ and Chrome are needed for browser checks. The isolated wheel check reproduces all 24 fixed-cost and 18 path reports, compares console/module CLI output for both workflows and checks five module origins outside the checkout.

## Limits and attribution

This implements established binary submodular inference and maxflow/mincut, not a new algorithm or a trained model. Inputs are original synthetic costs with at most six binary variables. Family and path enumeration are exponential. There is no real-image segmentation, predictive validation, speed/memory benchmark, multilabel or higher-order method, or machine-checked formal proof. Non-submodular refusal applies under the supplied label coding, not every possible transformation.

Native JSON rejects duplicate keys and bounds UTF-8 bytes; browser JSON.parse keeps the last duplicate and bounds characters. Their index-number parser differences are documented in the source method. Arithmetic is exact, but drawing geometry is approximate.

The source credits Kolmogorov-Zabih, standard flow/cut references and Picard-Queyranne cut-family structure, and records the assumptions of parametric-flow sources separately. It distinguishes a historical scan from readable theorem support and identifies the Springer erratum as an erratum. No external dataset, figure or implementation is copied. Implementation and synthetic controls: Midya Rahmani.

[Back to projects](README.md)
