# AlignLab: know what you optimized

A policy can solve its reward objective and still lose utility. AlignLab attaches the standard finite-action Gibbs optimum and a KL-budget frontier to a preference-based alignment experiment, so optimizer error and reward quality are separate questions.

[Live inspector](https://midya8.github.io/alignlab/) · [Source](https://github.com/midya8/alignlab) · [Equations, schema and limits](https://github.com/midya8/alignlab/blob/main/FRONTIER.md) · [Implementation PR](https://github.com/midya8/alignlab/pull/2)

## The original experiment stays attached

The dependency-free Python experiment fits a linear Bradley-Terry reward model on 800 noisy preference pairs over 120 synthetic response feature vectors. It evaluates 150 held-out pairs from that same response pool, not new tasks or new styles. A second model fits 800 utility-independent pairs. Latent utility is available only because this synthetic fixture defines it; it is not an input to reward training or optimization.

The original softmax policy ascends `J = E_p[r] - beta KL(p||q)` over six styles. All original training, data, evaluation, gradients, gate thresholds and 15 original tests remain unchanged. The inspector retains all 201 states of the learned, no-KL and noise-control runs plus two explicitly additional stiff-KL controls: 1,005 states, no best-state replacement.

## A concrete separation between questions

For positive beta and fixed finite support, `p*_i ∝ q_i exp(r_i/beta)` and `J(p*) - J(p) = beta KL(p||p*)`. The inspector shows every action's reference/current/optimal probability, the gap identity, 13 beta samples, 33 budget samples and full trajectories. Optional supplied utilities are shown separately, never used to choose the optimum.

The original noise-control run finishes with an objective gap about 4e-15, yet synthetic utility is 1.8548647, below the reference's 2.0375. Its optimizer is doing its job for a poor reward. The original learned-reward run reaches utility 4.5704247; its finite-policy optimum has utility about 4.5768334. These are descriptive results of one seeded six-action fixture, not causal attribution, generalization or deployment evidence.

For a supplied KL budget the implementation brackets and bisects a dimensionless reward tilt. It exposes computed KL/tilt brackets, a numerical dual reward value and a numerical duality gap. At zero beta, reward ties are weighted by the reference; zero-reference actions remain outside the finite-KL domain. Below-resolution budgets and unresolved near ties are explicit statuses and gaps in the plotted frontier, not silently declared optima.

Two additional beta-50 runs keep their entire large-step failure and smaller-step trajectory visible. Their final objective gaps are about 89.859927 and 2.87e-9. They do not replace the original three runs or identify a general optimizer mechanism.

## Reproduced numbers, not repaired training

Earlier published prose was stale. The unchanged current original code gives learned reward 3.4641183 to 6.2462098, synthetic utility 2.0375 to 4.5704247, noise-control utility 1.8548647, KL 1.0750099 and entropy .7167496. The no-KL run gives KL 1.7510340 and entropy .0407255. Older prose said utility 4.6154, control 2.5800 and KL 1.0216; those are not regenerated results. The repository preserves a full old/current table and corrects the prose rather than tuning training to it.

## Independent implementations and installed reproduction

Python and JavaScript independently evaluate 35 complete report witnesses and all 1,005 trajectory audits. Tests include independent 80-digit Decimal Gibbs optima, 100-digit near-reference divergence terms, random gap identities, finite simplex-grid lower-bound controls, ties, underflow, support restrictions, subnormal references and unresolved near ties.

47 Python tests run across Python 3.10-3.13, including all 15 original tests unchanged. Four substantive Node/actual-Chrome tests check all 201 learned UI states, all five runs, ten arithmetic controls, 64-action Unicode-label bounds, strict JSON, invalid-state non-revival, exports, clipboard outcomes, keyboard operation and 320/390/1280 layouts. Full frozen archive and browser-data regeneration is checked, not just selected totals.

An isolated installed wheel imports nine modules and runs all four CLI commands outside the checkout. It retrains both original reward models and reconstructs all original vectors, pairs, weights, scores, report and all 1,005 states. Complete retraining uses 1e-11 abs/rel for runtime/libm differences; frozen report/audit comparisons use 1e-12. Same-runtime reconstruction equals the unchanged original report exactly. No original tolerance or gate is weakened.

## Limits and attribution

The standard Gibbs variational formula is tractable because every action is enumerated. This is not DPO training, PPO, a language model, a scalable substitute for sequence optimization, or a new alignment algorithm. The browser shows finite sampled curves, not the entire continuum. Stable shifted arithmetic, supported log probabilities and a cancellation-aware KL formula reduce numerical problems but do not certify rounded-device arithmetic. Computed brackets and dual values are not outward-rounded certificates.

Methods are attributed in [FRONTIER.md](https://github.com/midya8/alignlab/blob/main/FRONTIER.md), including the [DPO reward-policy mapping](https://arxiv.org/html/2305.18290), [finite Gibbs formula and reference-weighted tie limit](https://lihanqing1997.github.io/notes/reinforcement-learning/entropy-regularized-reinforcement-learning/) and [numerical analysis of log-sum-exp/softmax](https://academic.oup.com/imajna/article/41/4/2311/5893596). Synthetic utility is not a measured human outcome; reward optimality alone proves no safety or generalization claim.
