# AlignLab: what the comparisons leave open

A reward optimizer can do its job while the preference data leaves its target open. AlignLab makes those two questions visible. The new inspector shows which reward ratios a comparison graph fixes, which policies still fit it, and when the supplied probabilities contradict a scalar reward model.

[Preference inspector](https://midya8.github.io/alignlab/identification.html) · [Original optimizer inspector](https://midya8.github.io/alignlab/) · [Source](https://github.com/midya8/alignlab) · [PR #3](https://github.com/midya8/alignlab/pull/3)

## Same preferences, different policies

Take four items with a uniform reference policy. We know that A beats B with probability 2/3 and C beats D with probability 2/3. That fixes the merit ratios within each pair, but says nothing about how the two pairs compare.

Give each pair an independent merit scale between 1 and 4. Every scale choice preserves both observed preferences. Yet the first pair's policy mass can range from 1/5 to 4/5. With supplied utility (1,0,0,0), expected utility ranges from 2/15 to 8/15. These are exact fractions, not estimates.

Adding the exact population comparison p(B > C)=1/2 joins the graph and fixes the policy up to a common scale. One noisy win would not do that. The inspector takes population probabilities, not finite win counts.

## What it computes

The Python producer propagates Bradley-Terry merit ratios from one anchor per connected component. It then checks every edge. Contradictory inputs return a closed cycle whose odds product differs from 1, with no policy family or feasible scale dimension.

For consistent inputs, the beta-1 Gibbs policy is proportional to reference probability times merit. A common merit scale cancels; separate component scales change component mass. The conditional policy within each component stays fixed.

The inspector enumerates every corner of the supplied scale box. It shows all action and component mass ranges, every item-pair probability range, supplied-utility extremes, and the complete policies that attain them. Duplicate policies and all ties are kept. With at most six components, there are at most 64 corners.

This enumeration is enough for the reported objectives. Hold all but one scale fixed and the objective has the form (a*s+b)/(c*s+d), with a positive denominator. Its derivative cannot change sign, so moving that scale to an endpoint cannot worsen an extremum. Repeat for each coordinate. The proof and full schema are in [IDENTIFICATION.md](https://github.com/midya8/alignlab/blob/main/IDENTIFICATION.md).

## Checks that do not just trust the producer

A separate Python reference enumerates every simple path and rebuilds the whole report. The browser has its own BigInt fractions, JSON parser, path search and corner enumeration. Neither calls the producer to get an answer.

- 12 full controls retain 107 corner records. They cover inconsistent and redundant cycles, isolated items, no edges, fixed bounds, constant utility, skew references, tiny positive 2^-128 reference mass and all 64 corners.
- 65 Python tests retain all 47 earlier tests. New checks cover every report-leaf edit, every four-item support graph, 100 consistent random graphs and 100 arbitrary-odds graphs.
- Eight Node/actual-Chrome tests retain all four earlier tests. They compare every report field, select all 107 corners, check 36 layouts, invalidate stale results after a real edit and verify two actual JSON downloads.
- An installed wheel runs every audit/verify round trip outside the checkout. It also reconstructs the old learned fixture, original gates, 35 floating witnesses and all 1,005 trajectory states.

The bounds are assumptions, not confidence intervals. Utility is a supplied evaluation axis, not inferred human utility. Beta is fixed at 1 to keep the arithmetic rational. Reference probabilities must be positive. General beta and finite-sample MLE fitting belong to different contracts. In particular, connected undirected comparison support identifies population merit ratios; it does not guarantee a finite MLE from a directed win graph.

## The original experiment is still here

The original dependency-free experiment fits a linear Bradley-Terry reward model on 800 noisy pairs over 120 synthetic response feature vectors. It evaluates 150 held-out pairs from the same pool, not new tasks or styles. A second model fits 800 utility-independent pairs. The fixture supplies latent utility, but training and optimization cannot see it.

A categorical policy over six styles ascends reward minus beta times KL to its reference. All original training, data, gradients, gates and 15 original tests are unchanged. The original learned, no-KL and noise-control runs keep all 201 steps. Two additional stiff-KL controls bring the total to 1,005 states; the large-step failure is kept, not replaced with a better result.

The noise-control policy ends about 4e-15 from its reward optimum, yet its synthetic utility is 1.8548647, below the reference's 2.0375. The learned-reward policy reaches 4.5704247; its finite-policy optimum is about 4.5768334. These are results of one seeded fixture, not causal evidence or a generalization claim.

The older optimizer inspector shows every action's reference, current and optimal probability, the standard gap identity, 13 beta samples, 33 budget samples and full trajectories. Supplied utility is shown separately. Tiny budgets and unresolved near ties remain explicit failures to resolve, not claimed optima. The beta-50 controls keep final gaps of about 89.859927 and 2.87e-9 without claiming that this pair of runs explains a general optimizer mechanism.

## Corrected prose, unchanged training

Earlier README numbers were stale. The original code gives learned reward 3.4641183 to 6.2462098, utility 2.0375 to 4.5704247, noise-control utility 1.8548647, KL 1.0750099 and entropy .7167496. Without KL, the final KL is 1.7510340 and entropy .0407255. The older prose had utility 4.6154, control utility 2.5800 and KL 1.0216. The [old/current table](https://github.com/midya8/alignlab/blob/main/FRONTIER.md) keeps the discrepancy visible. Training was not tuned to match the prose.

The earlier 47 Python tests and four Node/Chrome tests remain in the current suite. They cover 35 full floating reports, all 1,005 trajectory audits, independent 80/100-digit controls, ties, underflow, reference support and unresolved near ties. Installed retraining uses 1e-11 abs/rel tolerance for runtime/libm differences; frozen report and audit checks use 1e-12. The original tolerances and gates are unchanged.

## What not to conclude

This is a finite synthetic lab, not DPO training, PPO, a language model or a safety certificate. Exact preference geometry is separate from the floating optimizer calculations. Numerical brackets and dual values in the older inspector are not outward-rounded certificates. Sampled curves are not the whole continuum.

Bradley-Terry identification and the Gibbs mapping are standard results, not new methods. Six primary papers and official documentation are cited with the derivations in [IDENTIFICATION.md](https://github.com/midya8/alignlab/blob/main/IDENTIFICATION.md). The older [FRONTIER.md](https://github.com/midya8/alignlab/blob/main/FRONTIER.md) also links the DPO mapping, reference-weighted tie limit and softmax numerical analysis. A solved reward objective alone says nothing about safety or preferences beyond the supplied comparisons.
