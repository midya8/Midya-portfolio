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

35 tests include independent rational corner enumeration over 240 small model/label configurations, separate L1-vertex references, an L2 3-4-5 identity and 10,000-direction circle check, corner-enumerated logistic loss, exact first optimizer update/final objective, boundary ties, zero weights, monotone radius sweeps, scaling-invariant radii, resource preflight and strict CLI errors. Four figure tests inspect every bar and curve coordinate, unchanged full metadata and byte reproduction. A standalone wheel runs the same demo outside the source directory.

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

The threat domain is all real coordinates, with no clipping, boxes or preprocessing. The bias is fixed. Coordinates and epsilon are used as supplied, so feature units matter. Strict robustness requires worst signed margin >0; a boundary tie fails conservatively even when the +1 prediction rule gets that label right. A failed strict flag is not necessarily a label-flipping witness.

The identity is exact in real arithmetic but evaluated in ordinary floats, not interval/outward-rounded arithmetic. No nonlinear or multiclass certificate, adaptive attack suite, distributional generalization, calibrated uncertainty or production security guarantee is claimed. Fixed-step descent can oscillate at norm kinks and carries no convergence claim.

Independent implementation of standard norm duality and robust linear logistic training, following [Kolter/Madry's tutorial](https://adversarial-ml-tutorial.org/adversarial_ml_slides_parts_2_3.pdf) and [the logistic inner problem, Theorem 2 of arXiv:2208.09449](https://arxiv.org/html/2208.09449v3). All code, tests, synthetic rows and diagrams are original. MIT licensed.
