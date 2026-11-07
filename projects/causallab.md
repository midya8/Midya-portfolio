# CausalLab

[Repository](https://github.com/midya8/causallab) · [Model and algorithm](https://github.com/midya8/causallab/blob/main/DESIGN.md)

## Problem

A strong association does not say what replacing a mechanism would do. Even a complete observed joint can agree under two different causal mechanisms that disagree about actions and counterfactuals. The missing information is an assumption, not a decimal place.

## Built

- Exact finite structural-causal-model enumeration with categorical exogenous noise and topologically ordered deterministic truth tables.
- Separate observational, post-intervention and factual-evidence counterfactual queries. Shared exogenous assignments are reused across factual/action worlds, not independently redrawn.
- Strict JSON and CLI, SHA-256 model identity, full query joints, finite rare log masses, explicit impossible support and bounded posterior noise-world traces.
- 90 tests, independent rational references including all 64 tiny Boolean mechanism pairs, three reproducible audit SVGs and Python 3.10..3.13 CI. Standard-library runtime only.

The model's graph, functional tables and noise distributions are supplied. This does **not** infer causal structure or effects from an observational dataset.

## Constructed confounding reversal

The first fixture enumerates 100 equally weighted noise assignments. Context Z affects action X and outcome Y. The action is more common in the favorable context but lowers outcome probability within both contexts.

| Outcome probability | X=0 | X=1 | Difference |
|---|---:|---:|---:|
| Observed conditional | .42 | .68 | +.26 |
| Supplied-model intervention | .60 | .50 | -.10 |
| Observed conditional, Z=0 | .90 | .80 | -.10 |
| Observed conditional, Z=1 | .30 | .20 | -.10 |

Backdoor adjustment using the supplied Z distribution matches intervention enumeration. This is a synthetic counterexample, not an empirical treatment effect, sampled population or policy recommendation.

## Same observations, different mechanisms

Both two-world models have X=U with U~Bernoulli(.5). One has Y=X; the other Y=U. Their observed joint is identical: half its mass at (0,0), half at (1,1).

Yet P(Y=1 given do(X=1)) is 1 in the direct model and .5 in the common-input model. Given factual X=0,Y=0, the probability that Y would be 1 under X=1 is **1 versus 0**. Factual evidence fixes U=0; changing X does not redraw U. The same observational joint cannot settle these queries without further structural assumptions.

No seed or budget search is involved. The demos exhaust the complete finite worlds; they illustrate semantics and non-identifiability, not a general automatic effect-identification method.

## Identical action marginals, different cross-world response types

The multi-world API/CLI abducts one factual noise posterior, then evaluates 1..4 named action scenarios jointly on every retained assignment. It does not multiply marginals or draw new independent noise. Combined output and trace caps are checked before evaluation.

Two supplied models use independent equiprobable U,V and X=V. Stable has Y=U; flip has Y=X xor U. Both have a uniform observed (X,Y) joint and P(Y=1 | do(X=x))=.5 under either action, yet the shared-noise response joints differ:

| (Y0,Y1) | Stable | Flip | Naive product |
|---|---:|---:|---:|
| (0,0) | .50 | .00 | .25 |
| (0,1) | .00 | .50 | .25 |
| (1,0) | .00 | .50 | .25 |
| (1,1) | .50 | .00 | .25 |

Y0/Y1 mean Y under do(X=0)/do(X=1) on the same noise assignment. Factual X=0,Y=0 gives (0,0) for stable and (0,1) for flip. These joints are structural assumptions not determined by the matching observations or single-action marginals. No monotonicity, empirical benefit or injury claim is made. An independent rational reference checks all 64 tiny Boolean mechanism pairs; tests also verify scenario marginals, repeated-world coupling, traces and actual joint/trace-cap boundaries. A second eight-bar SVG embeds the complete models and traces.

## Sharp bounds instead of choosing a coupling

`response_bounds(p0,p1,monotone=False)` considers every binary response joint with the two supplied point action marginals. The one free cell t=P(Y0=1,Y1=1) ranges from max(0,p0+p1-1) to min(p0,p1). Each bound includes a joint witness that attains it; mixtures of the two witnesses cover all feasible joints. Exact rational fraction strings accompany rounded display numbers.

| Action marginals | Helped, unrestricted | Harmed, unrestricted | Mean effect | Helped, monotone | Harmed, monotone |
|---|---|---|---:|---:|---:|
| .50/.50 | [0,.50] | [0,.50] | .00 | .00 | .00 |
| .25/.75 | [.50,.75] | [0,.25] | +.50 | .50 | .00 |

The stable/flip mechanisms attain the equal-marginal endpoints. Adding monotonicity Y1>=Y0 rules out flip; the matching marginals do not establish that assumption. Positive mean effect alone still permits negative unit responses. Incompatible monotonicity errors, and zero-probability conditioning rates are explicitly undefined. Bounds also cover changed/unchanged fractions, effect variance, covariance, sufficiency and necessity.

An independent rational reference enumerates all 165 denominator-eight response joints across 81 marginal pairs and checks exact extrema with/without monotonicity. Every named witness is checked for feasibility and attainment. Tiny exact fractions remain present when float display underflows. This is exact for supplied binary-float values, not decimal text or empirical causal truth. These are feasible-coupling ranges for assumed point action marginals, not confidence intervals or uncertainty propagation for unknown marginals. A third SVG shows all 24 joint-mass segments in six attaining witnesses.

## Run locally

```sh
python -m unittest discover -s tests -v
python -m causallab bounds --p0 .25 --p1 .75 --monotone
python -m causallab bounds-demo > /tmp/bounds-demo.json
python examples/render_bounds.py /tmp/bounds-demo.json --check
python -m causallab multiworld-demo > /tmp/multiworld-demo.json
python examples/render_multiworld.py /tmp/multiworld-demo.json --check
python -m causallab joint examples/response_flip.json --scenarios examples/scenarios.json --evidence X=0,Y=0 --trace
python -m causallab demo > /tmp/causal-demo.json
python examples/render_demo.py /tmp/causal-demo.json --check
python -m causallab query examples/confounded.json --query Y --evidence X=1
python -m causallab query examples/confounded.json --query Y --do X=1
python -m causallab counterfactual examples/common.json --query Y --evidence X=0,Y=0 --do X=1 --trace
```

An ordinary `query` treats evidence as post-action; the counterfactual command treats it as factual in the original model. Contradictory post-action evidence is an error, not quietly reinterpreted as a counterfactual.

## Limits and attribution

Exhaustive discrete enumeration in floating point, not symbolic exactness or certainty about the model. At most 65,536 Cartesian noise worlds, 12 endogenous nodes, 16,384 total truth-table entries and 4,096 query rows, with a tighter trace-output preflight. Possible rare events may have underflowed stored probability but finite logs; impossible evidence errors explicitly.

No learned causes, graph discovery, automatic do-calculus identification, continuous/cyclic model, soft intervention, empirical confidence interval, medical advice or fairness certificate. No private data, GPU or paid API.

Independent implementation of standard SCM intervention and abduction/action/prediction semantics, referenced to Judea Pearl's [author-hosted R-485 report](https://ftp.cs.ucla.edu/pub/stat_ser/r485.pdf), section 2 and equation 3 (2019 draft; 2021 handbook chapter). The repository supplies its own tables, code, tests and figure; no source text, code, data or figures copied. MIT license.
