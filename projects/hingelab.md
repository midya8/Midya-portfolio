# HingeLab

Exact rational ReLU regions and class-change topology.

[Live inspector](https://midya8.github.io/hingelab/) · [Source](https://github.com/midya8/hingelab) · [Reviewed implementation](https://github.com/midya8/hingelab/pull/1)

## The question

If a network's nearest decision boundary is distance one away, is a closed perturbation ball of radius one robust? The answer depends on which class owns the boundary. For margin(x) = x, HingeLab assigns class 1 at margin ≥ 0. From x = 1, the opposite-class set [-2, 0) is open at zero. Distance one is only an infimum, so the closed ball is robust. From x = -1, the opposite-class set [0, 2] includes zero, and the same radius contains an actual adversary.

An isolated tie makes the point sharper: margin(x) = -|x| has class 1 only at x = 0. A continuous curve and two sampled points can miss that entire opposite class. The inspector retains the singleton rather than smoothing it away.

## What is built

- Forward exact affine-interval propagation through one or two ReLU hidden layers. Every interior preactivation root splits its interval.
- Python Fraction and normalized browser BigInt arithmetic. All decision logic, roots, coefficients, sets and distances are rational; only SVG coordinates are rounded.
- Complete cells with canonical open-interior activation masks, including hidden kinks cancelled in the scalar output.
- Exact opposite-class intervals with explicit endpoint flags; per-cell zero witnesses; exact domain Lipschitz constant from the largest absolute slope.
- Distance infimum, whether a minimum is attained, the nearest actual adversary when one exists, and a witness inside the requested radius when the closed ball is not robust.
- Eight controls, custom JSON, region-by-region selection, exact evidence export, stale clearing and visible input errors.

## Why the checker is different

The independent checker enumerates every hidden activation mask, builds its affine forms, intersects the rational phase inequalities and checks the entire region list. It handles overlapping weak phase constraints at zero by imposing the canonical inactive convention on zero interiors.

It then splits the true domain into every endpoint/root atom and intervening open interval, directly evaluates the network there, and checks the reported opposite-class union, distance, attainment and radius witness. Since the sign is constant on each derived atom, this is finite exact exhaustion, not a sampled-grid argument. The checker imports neither the forward generator nor its set-construction routine. Shared input parsing and direct point evaluation are explicit, not described as unrelated implementations.

## Evidence on published main

Main 52871cd2298909dec76496dabbdf34c4408606c7 is exact across all 24 source files. Feature, PR, main and Pages checks are green. Fresh main reruns pass 12 tests on each Python 3.10-3.13, including 200 seeded two-layer networks, generator-disabled checks and forged evidence. The exact Python/BigInt tests compare 144 complete reports. Four Node/Chrome tests pass. A fresh wheel outside the checkout reproduces eight controls through module and console and rejects forged reports.

Live Chrome checks all 54 region selections over 24 full reports at 320/390/1280, plus download, stale clearing and malformed input. All five deployed assets match main. All 24 main/deployed screenshots match pixel for pixel; responsive phone and desktop conditional result regions were visually inspected.

- [Main CI](https://github.com/midya8/hingelab/actions/runs/42701542385)
- [Pages deployment](https://github.com/midya8/hingelab/actions/runs/42701592331)

## Deliberate bounds

One scalar input, one scalar margin, one or two hidden layers of width 1..3: at most six hidden neurons and 64 oracle masks. The generator has at most 16 forward cells. Every parameter, endpoint, reference and radius is an integer-valued number or rational string with absolute reduced value ≤ 32 and reduced denominator ≤ 1,024. The reference must be inside the declared closed domain.

Zero-set entries are per-cell witnesses and can repeat shared roots; they are not a minimal union. The opposite-class union is canonical and keeps its topology. The domain is part of the claim: robustness outside it is not checked. Exact arithmetic applies to the declared rational network, not to an unprovided floating-point model.

## Attribution and nonclaims

This is a bounded educational implementation of established piecewise-affine analysis, not a new verification algorithm. Sotoudeh and Thakur's *Computing Linear Restrictions of Neural Networks* (NeurIPS 2019) develops exact line restrictions for broader networks. Bunel et al.'s JMLR 2020 work studies branch-and-bound verification. HingeLab does not implement or benchmark those full systems. Six primary source notes and the exact contract are in the repository.

No training, model import, image classifier, high-dimensional certificate, speed/accuracy benchmark, paid API or private dataset. Browser-generated custom evidence becomes independently checked only when the Python checker accepts its downloaded JSON.
