# PPOlab: training boundaries and exact policy audits

A NumPy PPO trainer and separate inspectors cover CartPole episode boundaries and exact clipped-objective policy faces. The rational optimizer exposes every optimal policy for a supplied single-state problem, without selecting one preferred update. Constructive dual bounds, independent global replay and a BigInt browser distinguish objective clipping from a hard probability-ratio box. The original trainer, checkpoint, boundary fix and numerical replay audit remain intact.

- Repository: [midya8/ppolab](https://github.com/midya8/ppolab)
- Live: [Boundary and policy inspector](https://midya8.github.io/ppolab/)
- Method: [BOUNDARIES.md](https://github.com/midya8/ppolab/blob/main/BOUNDARIES.md)
- Reviewed change: [Fix timeout credit leakage and add independent audits](https://github.com/midya8/ppolab/pull/1)

## Exact clipped-objective policy faces

For the centered supplied control p=(1/10,9/10), A=(9,-1), epsilon=1/5, the best clipped score is 9/25. Imposing an actual hard ratio box on that same objective lowers the optimum to 1/5, a strict 4/25 gap. Every unconstrained optimizer has q0 in [7/25,1]; exact total variation ranges from 9/50 to 9/10, with both endpoints attained. A positive exact optimal family approaches a zero-probability vertex, proving unbounded old-to-new KL without rounded logarithms. A separate forced-zero control has no fully supported exact optimizer, which is not confused with an unbounded family inside an empty set.

The rational producer solves a separable concave objective using coordinate supporting-line bounds. Zero dual gap identifies every optimizer as a box-simplex face. It retains all vertices, attainable marginal ranges, nearest/farthest TV witnesses and every dual knot. The independent native verifier never imports the optimizer: it enumerates every clipped cell's vertices and checks the original min expression before replaying every certificate leaf. A separately written browser BigInt engine reproduces the complete evidence.

The current suite has 64 Python tests (all 50 earlier tests unchanged) and seven Node/actual-Chrome tests (all four earlier tests unchanged). New checks cover 351 exhaustive signed-advantage reports, denominator-24 simplex controls, six-action/tiny-probability cases, permutations/positive scaling, all-leaf tampering, strict schemas and the unchanged NumPy loss with correctly old-probability-weighted batches. Actual Chrome visits 135 policy selectors, 60 layouts and 2,658 exact table cells, clears stale results on trusted edits, and downloads two real JSON Blobs for native regeneration and independent replay. Both earlier and extension installed-wheel gates reproduce outside checkout.

This is a full old-policy expectation at one supplied state with 2–6 actions. It does not model empirical minibatches, shared neural parameters, entropy/value losses, dynamics, optimizer trajectories or new training performance. Closed-simplex optima can have zeros; finite softmax logits cannot. The clipping limitation is established PPO mathematics, not a new algorithm or a new failure benchmark.

[Exact policy-face inspector](https://midya8.github.io/ppolab/clip.html) · [Proof, schema, sources and reproduction](https://github.com/midya8/ppolab/blob/main/CLIP_FACE.md). The standard objective and caveats are attributed to Schulman et al., OpenAI Spinning Up and prior PPO analyses. Earlier boundary and policy inspector retained below.

The counts below describe the retained boundary-audit stage. The current
64-Python/seven-Node suite includes those tests.

## Collector reset bug

A time limit is not necessarily a terminal state. The original training collector reset on time-limit truncation, but recorded only true failures as done. Its GAE calculation then used the next episode's reset value and carried that episode's advantage backward. A tail-value unit test did not exercise the collector's internal reset.

The corrected collector saves each actual post-step state and value before reset. Training now uses two masks: genuine termination suppresses bootstrap, while either termination or truncation cuts the recursive advantage trace. A documented seven-array compatibility adapter uses reward augmentation at truncation; raw rewards and flags live in the explicit transition API. The original model, optimizer, loss, physics and GAE helper remain unchanged.

## Network, physics and estimator inspectors

The live page runs both tanh hidden layers and both heads from all 4,675 original checkpoint parameters, with scalar JavaScript and the original Euler equations. All 30 initial states from the full 20-episode historical evaluation and ten-episode original gate are available, with every scalar path step, frame selection, play/pause and complete JSON export. Custom state simulation is actual policy inference and physics, not prerecorded frames or a model API.

Editable strict JSON exposes ten GAE fixtures: four complete actual trajectories and six labeled controls, retaining all 186 transitions. Tables show reward, actual successor value, both masks, TD residual, advantage, value target, the old reset bug and a wrong terminal-mask control. A signed contribution heatmap and complete residual table show where each advantage gets its credit, including exact zeros across resets.

Sixteen PPO fixtures cover advantage signs and ratios, including a complete tiny original-network batch. Every loss term, selected clip branch and output derivative is visible. All 57 finite-difference stencils expose left/right slopes. Four cross a clip kink and are explicitly not counted as ordinary central-gradient failures. A ratio outside the clip interval can still have active policy gradients; entropy/value gradients and full policy KL are separate questions.

## Boundary-audit checks and trajectory differences

- 50 Python tests on 3.10-3.13, retaining all 18 original tests and original checkpoint/results/images.
- Four Node/actual-Chrome tests compare all 26 complete reports and 12,408 numbers, all contribution rows, four actual JSON exports, invalid-state clearing, keyboard/playback, custom-state errors and 320/390/1280 layouts.
- Independent 80-digit Decimal residual sums check all 186 GAE rows. The unchanged NumPy loss and gradients independently check the scalar PPO audit.
- Node and Chrome check the entire network and one-step physics on all 14,871 original observations, with original greedy decisions preserved at those fixed inputs. The reference Node maximum normalized one-step error is about 1.01e-15; the supported threshold is 1e-11.
- This does not imply trajectory equivalence. The reference free-running scalar paths differ on 377 actions and reach a maximum absolute state-coordinate difference of about 0.59337, while all 30 return lengths happen to match. Long unstable dynamics amplify tiny NumPy/scalar reduction differences, and Chrome can differ from Node. New scalar paths are labeled as such, not passed off as the original trajectories.
- Isolated installed reproduction outside checkout verifies eight module origins, all complete reports, full original 20-episode evaluation, corrected short-timeout training, both JSON commands and the real training CLI.
- A corrected seed-0 full rerun reproduces the historical final return display of 493.6 +/- 27.7. It is one run, not evidence of a training improvement or a new speed benchmark. No original measured artifact was replaced.

## Limits and attribution

PPO, GAE and CartPole are standard methods, not new algorithms. A 500-step replay is not a universal solve or safety guarantee, and PPO clipping is not a hard KL constraint. Time-limit bootstrap assumes an external cutoff of a continuing task; a genuine finite-horizon ending needs different semantics and a time-aware state. Value estimates can be wrong even when the estimator arithmetic is correct. Finite differences across kinks are not ordinary derivatives. All inputs, bounds, branch conventions and cross-runtime tolerances are documented.

[BOUNDARIES.md](https://github.com/midya8/ppolab/blob/main/BOUNDARIES.md) attributes the GAE paper, Time Limits in Reinforcement Learning, Gymnasium documentation, OpenAI Spinning Up, Costa Huang's implementation checklist and the clarified Stable Baselines3 terminal-observation discussion. The SB3 issue was a caller misunderstanding, not evidence SB3 has this repository's bug.
