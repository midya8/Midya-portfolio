# RobustLab: exact linear threat-set audits

[Source repository](https://github.com/midya8/robustlab)

A high clean accuracy does not certify a classifier against an explicit adversarial input budget. RobustLab makes that distinction measurable for a small class where the inner attack problem can actually be solved: binary affine scores under L1, L2 and L-infinity balls.

## The result, including the cost

Both arms train from zero on the same 30 fixed synthetic rows for 4,000 updates with rate 0.1 and L2 coefficient 0.001. The only changed training setting is the L-infinity radius, 0 versus 0.30. There is no test-driven stopping, seed search or checkpoint selection.

| Training | Shifted holdout clean accuracy | Strict robust accuracy at radius 0.30 | >=75% robust gate |
|---|---:|---:|---|
| Ordinary logistic | 100% | 20% | Fail |
| Robust logistic | 80% | 80% | Pass |

The 30-row holdout is a different supplied factorial grid, not independent random samples. A strong coordinate has one of five signs reversed; a smaller coordinate always aligns with the label but can be overwhelmed by the stated perturbation radius. The robust objective mostly uses the strong coordinate and accepts its exceptions. Both clean accuracy and the robust model's small nonzero second weight remain visible.

This is a constructed descriptive comparison, not an image benchmark or a universal claim about the cost of robustness.

## Mechanism and evidence

For signed margin `y*(w.x+b)`, the worst margin in an Lp ball is the clean margin minus epsilon times the dual weight norm. The implementation returns the actual perturbation attaining that margin: a signed coordinate vertex for L1, an opposite weight direction for L2, and a signed corner for L-infinity. It also returns the attacked coordinates, attained signed margin and zero-margin radius.

The robust logistic objective puts this worst margin inside softplus, with a separate explicit quadratic weight regularizer. Hand-derived selected subgradients are checked against central finite differences away from kinks, and against convex subgradient inequalities at zero/tied weights. The optimizer is fixed-step full-batch descent, not an asserted exact minimizer.

The initial 35 tests include independent rational corner enumeration over 240 small model/label configurations, separate L1-vertex references, an L2 3-4-5 identity and 10,000-direction circle check, corner-enumerated logistic loss, exact first optimizer update/final objective, boundary ties, zero weights, monotone radius sweeps, scaling-invariant radii, resource preflight and strict CLI errors. Four figure tests inspect every bar and curve coordinate, unchanged full metadata and byte reproduction. A standalone wheel runs the same demo outside the source directory.

The generated SVG displays both gate directions and both fixed-model radius sweeps. Its metadata retains the full unchanged fixture, fit settings/checkpoints, models and train/holdout attacks. Sweep summaries avoid repeated row arrays; the audit API recovers witnesses at any chosen radius.

## Run it

```sh
python -m robustlab demo
python -m robustlab audit examples/model.json examples/data.json --norm l2 --epsilon 0.4
python -m robustlab fit examples/data.json --norm linf --epsilon 0.3 --steps 1000
python -m unittest discover -s tests -v
PYTHONPATH=. python examples/render_audit.py --check
```

Dependency-free Python 3.10+, with CI on Python 3.10-3.13. No network, paid API, model download or GPU is required.

## Boundaries and attribution

The original training and all-real audit threat domain has no clipping, boxes or preprocessing; the separate box API below instead requires explicit bounds. The bias is fixed. Coordinates and epsilon are used as supplied, so feature units matter. Strict robustness requires worst signed margin >0; a boundary tie fails conservatively even when the +1 prediction rule gets that label right. A failed strict flag is not necessarily a label-flipping witness.

The identity is exact in real arithmetic but evaluated in ordinary floats, not interval/outward-rounded arithmetic. No nonlinear or multiclass certificate, adaptive attack suite, distributional generalization, calibrated uncertainty or production security guarantee is claimed. Fixed-step descent can oscillate at norm kinks and carries no convergence claim.

Independent implementation of standard norm duality and robust linear logistic training, following [Kolter/Madry's tutorial](https://adversarial-ml-tutorial.org/adversarial_ml_slides_parts_2_3.pdf) and [the logistic inner problem, Theorem 2 of arXiv:2208.09449](https://arxiv.org/html/2208.09449v3). All code, tests, synthetic rows and diagrams are original. MIT licensed.

## Exact rational boundary certificates

A separate `exact_audit` API and `exact-audit` / `exact-demo` CLI make the float limitation actionable for L1 and L-infinity balls. They interpret each validated input as its actual stored binary float, not an exact decimal literal. Scores, dual norms, radii, worst/attained margins, perturbations and attacked coordinates are reduced numerator/denominator strings. Certificate flags use integer signs, not rounded decimal views. The float audit is retained beside the exact result, with explicit disagreements.

A selected boundary fixture has float worst margin approximately +2.081668171e-17 but rational worst margin approximately -2.775557562e-18, so its float strict flag is true while its exact flag is false. Another cancellation fixture has the reverse strict-flag disagreement, and a dyadic exact-zero control fails both strict flags. The first case is the first match from a documented finite decimal grid search; these are selected edge cases, not prevalence measurements. The original trained demo is byte-identical.

The exact audit preflights at most 4,096 row-coordinate products before fraction conversion. It rejects L2 explicitly because general directions/margins can be irrational. An exact rational result certifies the stated mathematical linear function and real-valued threat ball, not a separately rounded inference or attack pipeline. Rounding the rational witness can change a near-boundary result.

Seventeen additional arithmetic/API/CLI tests check independent rational vertex/corner minima across 156 model/label/norm configurations, serialized witness feasibility and attained scores, both rounding-disagreement directions, exact binary input semantics, prediction disagreements, zero/tied weights, the executed work-cap boundary and subnormal-squared underflow. Four new figure tests verify six displayed result flags, numeric signs, scope text, metadata, reproduction and rejection of changed records. That increment brought the suite to 56 tests and two SVGs; the box increment below brings it to 80 tests and three SVGs. The wheel's exact demo also runs identically outside the source directory.

```sh
python -m robustlab exact-demo
python -m robustlab exact-audit examples/model.json examples/data.json --norm linf --epsilon 0.1
PYTHONPATH=. python examples/render_exact.py --check
```

Exact float-to-rational conversion follows [Python's Fraction documentation](https://docs.python.org/3/library/fractions.html). All added code, numeric fixtures and diagrams are original.

## Box intersection: an optimal witness, not a clipped candidate

The new `box_audit` API solves L1/L-infinity balls intersected with supplied per-coordinate bounds. It requires clean inputs inside those bounds and returns exact rational primal movement plus a matching dual gain bound. The L1 problem is bounded fractional knapsack; L-infinity separates by coordinate. L2 is explicitly unsupported here. Neither existing training nor the all-real audits change.

A direct dyadic fixture makes the failure mode concrete: weights `(4,1)`, bias `-1/4`, point `(1/16,3/4)`, positive label and unit box. At L1 radius `5/8`, clipping the old all-real attack leaves margin `+1/2`. The actual minimum is `-1/16`, attained by movements `(-1/16,-9/16)`. The positive clipped candidate cannot prove robustness. Exact primal and dual gains both equal `13/16`, with zero gap. Under L-infinity, independent adverse-direction clipping is optimal.

Twenty new tests include a separate full orthant-polytope vertex oracle on 468 configurations, certificate/witness reconstruction, asymmetric/degenerate/nonbinding boxes, zero/tied weights, saturated budget, subnormals, isolation, actual 4,096-product execution and preflight/strict CLI checks. Four new figure tests cover 36 points, six polylines, full metadata and exact reproduction. Total suite: 80 tests and three SVGs. The new fixture was hand-specified without parameter search; it says nothing about prevalence or neural-network security.

```sh
python -m robustlab box-demo
python -m robustlab box-audit examples/model.json examples/data.json examples/bounds.json --norm l1 --epsilon 0.3
PYTHONPATH=. python examples/render_box.py --check
```

Bounds and inputs mean exact stored binary floats. The cap is 4,096 row-coordinate products, checked before rational conversion; each bounds JSON file uses the existing strict 1 MiB parser. No box-constrained training or separately rounded execution guarantee is claimed. See the [full derivation and dual inequalities](https://github.com/midya8/robustlab/blob/main/DESIGN.md) and [Duke's standard fractional-knapsack formulation](https://courses.cs.duke.edu/spring20/compsci330/lecture15scribe.pdf). All new code, synthetic data, test references and figures are independent implementations.
