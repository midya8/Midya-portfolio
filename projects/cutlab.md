# CutLab

Exact binary energy, flow and all minimum-cut witnesses.

[Live inspector](https://midya8.github.io/cutlab/) · [Source and reproduction](https://github.com/midya8/cutlab) · [Method, sources and limits](https://github.com/midya8/cutlab/blob/main/METHOD.md)

## The problem

A supplied binary energy can couple decisions strongly enough that choosing the best unary or stopping at a one-flip local minimum gives the wrong answer. A graph-cut solver should expose why its global answer is optimal, and should not report one cut as the only answer when several labels are ambiguous.

## What is built

CutLab reduces signed rational unary and asymmetric submodular pair tables to a directed s-t network. Every pair entry is reconstructed, every terminal shift is retained, and every assignment satisfies original energy = offset + cut capacity. Non-submodular pairs are refused rather than clipped. Exact original-energy enumeration remains visible as an independent tiny reference.

The inspector shows every deterministic shortest augmenting path, residual bottleneck and complete edge-flow state. A six-augmentation fixture actually needs a reverse variable arc to cancel earlier flow. Every cut then exposes capacity minus flow = outgoing residual slack. Matching feasible flow and cut prove optimality.

The residual SCC graph recovers the whole forward-closed family of minimum cuts and forced/free labels. Free does not mean independently selectable: tied agreement has two free variables but only two optimal masks. The zero six-variable graph has all 64 assignments optimal.

## Controls that can fail

- Strict best single-flip search starts at mask 0 with energy 2. Both one-flip neighbors cost 3, so it stops. Mask 3 has energy 0. Flow 1 plus offset -1 certifies that optimum.
- Unary-only chooses energy 5 in a separate coupling control, while two exact tied minima cost 3. Gap 2 is labeled as an incomplete baseline, not a solver benchmark.
- Negative costs, asymmetric and rational tables, disconnected ties, forced/free mixtures, zero capacities, zero slack, a refused non-submodular pair and ten seeded signed networks remain available.

## Verification

21 Python tests pass on 3.10-3.13: 250 independently enumerated original-energy cases, 160 every-cut slack audits, full augmentation replay, conservation/capacity, independent reachability/SCC, optimum-family and lattice checks, 100 positive-scaling/offset controls and 80 variable relabelings. Counts inside tests are controls, not extra test functions.

24 complete native and independent BigInt reports agree on 24,624 exact scalar leaves. Actual Chrome checks 570 cut records, 56 flow states, 73 pair reductions, 180 residual records and 50 local states, plus 87 terminal rows, 449 SVG edges and 4,166 node colors. Summaries, all optimum-family fields, invalid/stale clearing and export are checked. Full 320/390/1280 layouts are inspected; graph and tables scroll rather than shrinking labels.

An installed wheel reproduces all 24 reports and both CLI routes with four module origins checked outside the checkout. The published CI runs the Python matrix, deterministic audit regeneration, Node/Chrome and wheel reproduction.

## Boundaries

This is established binary submodular inference and maxflow/mincut, not a new algorithm. All inputs are original synthetic costs, at most six binary variables and finite rational costs. Exhaustive family verification is exponential. There is no trained model, real-image segmentation, predictive validation, speed/memory benchmark, multilabel or higher-order method, or machine-checked formal proof. Non-submodular refusal is under the supplied label coding, not a claim about all possible transformations. Native JSON is stricter than browser JSON.parse on duplicate keys, float index tokens and byte versus character limits.

Theory is attributed to Kolmogorov-Zabih, flow/cut lecture notes and the established Picard-Queyranne cut-family background. The method distinguishes a historical scan from readable theorem support and identifies the Springer erratum as an erratum. No external dataset, figure or implementation is copied.

[Back to projects](README.md)


## Exact affine unary response paths

[Open the exact response-path inspector](https://midya8.github.io/cutlab/path.html) · [Source and method](https://github.com/midya8/cutlab/blob/main/PATH.md)

Vary binary unary costs with a rational parameter and retain the complete optimum family on every closed region, open cell and breakpoint, including point-only optima and persistent ties. Every assignment keeps its affine line and every line comparison keeps its exact inequality. Independent graph-cut audits check all boundary and cell witnesses.

18 synthetic controls retain 214 assignment lines, 6,084 inequalities and 92 full flow/cut witnesses. Mixed-sign slopes include a label that leaves and returns: no nested-label or scalable parametric-maxflow guarantee is claimed. The inspector enumerates all 2^n assignments for at most six variables. Original flow/cut functionality and tests remain.
