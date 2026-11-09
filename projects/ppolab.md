# PPOlab

A PPO implementation that makes reset boundaries, credit assignment and numerical replay limits inspectable.

- Repository: [midya8/ppolab](https://github.com/midya8/ppolab)
- Live: [Boundary and policy inspector](https://midya8.github.io/ppolab/)
- Method: [BOUNDARIES.md](https://github.com/midya8/ppolab/blob/main/BOUNDARIES.md)
- Reviewed change: [Fix timeout credit leakage and add independent audits](https://github.com/midya8/ppolab/pull/1)

## The real problem

A time limit is not necessarily a terminal state. The original training collector reset on time-limit truncation, but recorded only true failures as done. Its GAE calculation then used the next episode's reset value and carried that episode's advantage backward. A tail-value unit test did not exercise the collector's internal reset.

The corrected collector saves each actual post-step state and value before reset. Training now uses two masks: genuine termination suppresses bootstrap, while either termination or truncation cuts the recursive advantage trace. A documented seven-array compatibility adapter uses reward augmentation at truncation; raw rewards and flags live in the explicit transition API. The original model, optimizer, loss, physics and GAE helper remain unchanged.

## Working implementation

The live page runs both tanh hidden layers and both heads from all 4,675 original checkpoint parameters, with scalar JavaScript and the original Euler equations. All 30 initial states from the full 20-episode historical evaluation and ten-episode original gate are available, with every scalar path step, frame selection, play/pause and complete JSON export. Custom state simulation is actual policy inference and physics, not prerecorded frames or a model API.

Editable strict JSON exposes ten GAE fixtures: four complete actual trajectories and six labeled controls, retaining all 186 transitions. Tables show reward, actual successor value, both masks, TD residual, advantage, value target, the old reset bug and a wrong terminal-mask control. A signed contribution heatmap and complete residual table show where each advantage gets its credit, including exact zeros across resets.

Sixteen PPO fixtures cover advantage signs and ratios, including a complete tiny original-network batch. Every loss term, selected clip branch and output derivative is visible. All 57 finite-difference stencils expose left/right slopes. Four cross a clip kink and are explicitly not counted as ordinary central-gradient failures. A ratio outside the clip interval can still have active policy gradients; entropy/value gradients and full policy KL are separate questions.

## Evidence, including the failure of exact replay

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
