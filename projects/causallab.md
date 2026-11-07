# CausalLab

[Repository](https://github.com/midya8/causallab) · [Model and algorithm](https://github.com/midya8/causallab/blob/main/DESIGN.md)

## Problem

A strong association does not say what replacing a mechanism would do. Even a complete observed joint can agree under two different causal mechanisms that disagree about actions and counterfactuals. The missing information is an assumption, not a decimal place.

## Built

- Exact finite structural-causal-model enumeration with categorical exogenous noise and topologically ordered deterministic truth tables.
- Separate observational, post-intervention and factual-evidence counterfactual queries. Shared exogenous assignments are reused across factual/action worlds, not independently redrawn.
- Strict JSON and CLI, SHA-256 model identity, full query joints, finite rare log masses, explicit impossible support and bounded posterior noise-world traces.
- 38 tests, independent rational references including all 64 tiny Boolean mechanism pairs, a reproducible eight-bar SVG and Python 3.10..3.13 CI. Standard-library runtime only.

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

## Run locally

```sh
python -m unittest discover -s tests -v
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
