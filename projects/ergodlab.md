# ErgodLab

Exact stationary policy sensitivities, independently checked against directed spanning trees, with a Poisson-bias and temporal reward-variance audit.

- Repository: [midya8/ergodlab](https://github.com/midya8/ergodlab)
- Runtime: Python 3.10+, standard library only
- Verification: 26 tests; reproducible SVG; exact four-module wheel demo outside checkout

![Exact stationary reward audit](https://github.com/midya8/ergodlab/raw/main/assets/stationary-audit.svg)

## The question

A policy changes both its immediate reward distribution and the states it visits. Long-run reward and reward-sum variance cannot generally be read from one-step quantities alone.

## Two exact counterexamples

In the occupancy fixture, state rewards are 0 and 1 and are independent of the action. At the policy anchor, the controlled transition is `[[1/2,1/2],[1/4,3/4]]`, stationary distribution `[1/3,2/3]`, average reward `2/3` and stationary derivative `[-1/18,1/18]`. Freezing that distribution gives immediate-reward gradient zero; the true average-reward gradient is `1/18`.

Two separate symmetric chains with state rewards 0/1 have equal one-step stationary reward variance `1/4`. Staying in the same state with probability `7/8` gives asymptotic reward-sum variance per step `7/4`. Deterministic alternation gives zero. The alternating chain has period two: exact stationary block-sum variance is zero for even lengths and `1/4` for odd lengths. The figure shows all lengths 1..16 and both exact limits on the same axis. These are prescribed analytical fixtures, not training results or benchmark trials.

## What was built

The anchored policy is proportional to `weight(s,a)*exp(feature(s,a) dot theta)`, with fixed transitions/rewards and theta evaluated at zero. Exact pivoted linear solves return stationary distributions and derivatives. A structurally independent directed spanning-tree product/quotient rule returns the same values and every derivative. The controlled chain must be irreducible; periodicity is computed and reported, not silently ruled out.

A centered Poisson solve returns `h`, satisfying `(I-P)h=r-rho` and `mu h=0`. The average-reward gradient is checked in both forms:

```text
d rho = (dmu) r + mu dr = mu dr + mu (dP) h
```

For every positive state/action/next-state edge, the report returns the centered martingale increment `D=R-rho+h(next)-h(state)` and its nonnegative variance contribution. Its stationary second moment is the asymptotic variance of centered reward sums per step. Exact conditional first/second-moment dynamic programs return every finite-block variance through the requested length, without enumerating exponentially many paths. [The full derivation](https://github.com/midya8/ergodlab/blob/main/DESIGN.md) covers action/transition-dependent rewards, boundary effects and periodic chains.

## Independent checks

26 tests cover 25 analytic two-state transition settings, 16 exact policy-weight gradient settings, nine multi-state/two-coordinate determinant and finite-difference references, and explicit path enumerations through four steps for all three fixtures. Additional checks cover the alternating chain through length 32, period-three chains, IID action rewards, zero-asymptotic-variance telescoping edge rewards, feature/reward/state/action transformations, five-state complete-graph tree counts, reducible refusal, strict CLI/schema/file bounds, input/output/RNG isolation and every SVG point/limit geometry.

Input is a versioned JSON model with 1..5 states, 1..4 actions and 1..3 shared coordinates. Rational probabilities/rewards are bounded, transition rows sum exactly to one, and duplicate keys/booleans/floats/malformed shapes are rejected. The independent tree reference checks at most 1,280 parent assignments. The wheel and SVG need no external runtime dependency.

## Attribution and boundaries

Stationary sensitivities, directed spanning-tree formulas, Poisson equations and martingale decompositions are standard. The repository cites Aldous and Fill Section 9.2, Glynn and Infanger's Poisson-equation framework, and Greensmith, Bartlett and Baxter's average-reward policy-gradient context. Code, finite fixtures, bounded derivations, tests and figure are original implementations; no external code or dataset is copied. MIT licensed.

This is not GPOMDP, a learned policy, a sampled gradient estimator, a confidence interval, a mixing-rate or CLT result, arbitrary reducible-chain inference, or a claim about large-scale RL. Reward-sum variance is not policy-gradient estimator variance. Exact arithmetic checks the supplied model's calculations, not its realism.
