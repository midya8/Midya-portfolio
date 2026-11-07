# AlignLab: preference-based alignment from scratch, with the KL bill shown

RLHF in one paragraph: collect pairwise preferences, train a reward model to predict them, then push a policy toward higher reward while a KL penalty keeps it near a reference policy. AlignLab implements exactly that chain in dependency-free Python - and because the policy is categorical over six response styles, every expectation, KL, and gradient is computed in closed form. Nothing hides behind sampling noise, so every number in the README is the number the code produced.

## The fixture

Six response styles over five interpretable features (helpful, correct, verbose, polite, toxic). A latent utility scores them; pairwise preferences are drawn from the Bradley-Terry model `P(a beats b) = sigmoid(u_a - u_b)` with a seeded RNG. The reward model never sees the latent utility - only the noisy pairs.

## Reward model

Linear, `r(x) = w . phi(x)`, trained on 800 pairs with the hand-derived gradient of `-log sigmoid(r_w - r_l)`: `dL/dw = -(phi_w - phi_l) * sigmoid(-(r_w - r_l))`. Holdout accuracy 0.7800 on 150 fresh pairs. That number is bounded by design: labels are sigmoid-noisy, so even the Bayes-optimal ranker falls short of 1.0, and the gate is pinned at an achievable 0.75 instead of a flattering perfect score. A control model trained on utility-independent labels lands at 0.4333 on this finite fixture - utility-independent labels are expected near chance on average, and 0.4333 is this fixture's outcome.

## Alignment with exact KL accounting

The policy is a softmax over the six styles. Alignment ascends `J = E_pi[r] - beta * KL(pi || ref)` where:

```
dE/dtheta_k  = pi_k (r_k - E_pi[r])
dKL/dtheta_k = pi_k ((log pi_k - log ref_k) - KL)
```

Both terms finite-difference verified in the suite. On the fixture: expected learned reward 2.1297 to 4.2520; **true latent utility 2.0375 to 4.6154**; KL paid 1.0216.

## Why the negative control is the load-bearing number

"Policy improved under the learned reward" is easy - any monotone direction in feature space does that. AlignLab's control aligns an identical policy to the noise-trained reward model: true utility moves only 2.0375 to 2.5800, and the `--max-control-gain` gate fails CI if the control ever buys more than 0.2. On this fixture the gain tracks preference signal rather than the optimization machinery; one seeded control is a fixture comparison, not a general proof that signal alone causes improvement.

## What the beta=0 ablation shows

Without the KL term the policy collapses onto the argmax-reward style: entropy 0.0136 vs 0.7701, KL 1.7781 vs 1.0216. The `--min-nokl-kl` gate keeps this demonstrated. One measured practitioner note: with a stiff KL coefficient, fixed-step ascent overshoots into the collapsed corner - the KL gradient vanishes as a style's probability approaches zero, so it never recovers. The suite's large-beta test uses a stable step size, and the dynamic is documented rather than smoothed over.

## Scope

No PPO, no transformers, no sampled rollouts - the alignment mechanics are the point, and the README says what real RLHF adds. 15 unit tests, fully offline, CI across Python 3.10-3.13.

- Repo: [midya8/alignlab](https://github.com/midya8/alignlab)
