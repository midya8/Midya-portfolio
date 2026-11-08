# LatentLab

A trained Gaussian variational autoencoder whose reconstruction, latent regularization and prior generation can be inspected separately.

- Repository: [midya8/latentlab](https://github.com/midya8/latentlab)
- Derivations: [DESIGN.md](https://github.com/midya8/latentlab/blob/main/DESIGN.md)
- Complete measured report and checkpoints: [examples/demo.json](https://github.com/midya8/latentlab/blob/main/examples/demo.json)

![Six measured equal-axis scatter panels: prior samples and mean reconstructions](https://raw.githubusercontent.com/midya8/latentlab/main/assets/latent-audit.svg)

## The question

If an autoencoder reconstructs held-out inputs well, does sampling its latent prior produce the same data distribution? This tiny experiment makes the distinction visible instead of treating reconstruction error as a generation certificate.

## What I built

A 150-parameter Gaussian VAE, using scalar Python and no array library or autodiff. Both encoder and decoder have a 12-unit tanh hidden layer. The diagonal posterior uses smooth bounded logvariance, and the decoder defines a Gaussian likelihood with fixed standard deviation 0.2. Reparameterized latent samples and analytic Gaussian KL feed a hand-derived backward pass through every weight, bias and logvariance path. Adam includes explicit bias correction.

A strict versioned JSON checkpoint supports detached export/import, reproducible inference and prior sampling. Runtime and tests are dependency-free. Packaging supplies an installed CLI, checked outside the repository checkout.

## What the fixture actually shows

Both arms train on the same 128 synthetic eight-mode points, from identical initialized weights and data/noise RNG streams, for 800 minibatch Adam updates. Neither seed nor checkpoint is selected using held-out outcomes. Another 128 synthetic points are used for evaluation. Negative ELBO uses four held-fixed posterior-noise draws per point, with analytic KL. Prior generation includes independent observation-likelihood noise, not only decoded means.

| Held-out metric | Untrained | Trained beta 0 | Trained beta 1 |
|---|---:|---:|---:|
| Negative ELBO, four-noise MC | 13.5149 | 8.0758 | 1.6600 |
| Analytic posterior KL | 0.3324 | 9.3704 | 2.2073 |
| Posterior-mean MSE / coordinate | 0.44105 | 0.00268 | 0.00281 |
| Prior-sample sliced W2 squared | 0.1138 | 0.0676 | 0.0241 |
| Outside radius 0.3 of all mode centers | 83.59% | 71.09% | 51.56% |

The no-KL arm has slightly lower deterministic reconstruction error yet worse prior-sample distance. Beta 1 improves the measured prior samples, but over half still lie outside the disclosed neighborhoods. These are descriptive results for a single toy run, not proof that one objective always wins. The model's observation noise 0.2 is wider than the fixture jitter 0.06, so the distance diagnostic also reflects likelihood-family mismatch.

## Importance evidence extension

The VAE is unchanged. A separate inference audit computes complete importance witnesses, with latent draws, joint/proposal log densities, normalized weights, log mean weight, mean log weight and ESS. Analytic-KL MC negative ELBO is returned separately because it is not the same finite-sample quantity as negative mean log weight. Only expectation bounds have the IWAE monotonic hierarchy; one random prefix need not improve.

![Importance prefix estimates, exact Gaussian evidence and rare-atom failure control](https://raw.githubusercontent.com/midya8/latentlab/main/assets/importance-audit.svg)

For the trained beta 1 anchor x=(1,0), shared Gaussian-noise prefixes of size 1,4,16,64 give log-evidence estimates -2.0464,0.7106,-0.2701,-0.9271. The true nonlinear evidence is not known. A positive log density is legal, but no finite random row is guaranteed to bound the true log evidence.

A separate linear-Gaussian model has exact log evidence -2.15379530672424. With its exact posterior as proposal, all weights are constant and the 64-draw estimate recovers that value. Four independent Simpson-integral reference settings verify the analytic evidence; this does not turn the nonlinear neural decoder into a linear Gaussian.

The two-atom failure control is stronger than a seed-picked bad run: joint masses are (0.000001,0.999999), proposal masses are (0.999,0.001), and true evidence is 1. With probability (999/1000)^64 = 93.79749638258456%, all 64 draws hit the common proposal atom. ESS is then 64, but log estimate is -13.814510 rather than 0, an underestimate by factor 999,000. Full support is present; nearly all joint mass is simply unseen.

Finite binomial enumeration uses exact rational event probabilities, probability sums and mean evidence estimates. Expected evidence is exactly 1 for every K; expected log estimates for K=1,4,16,64 are about -13.793788,-13.737278,-13.529377,-12.785808. They rise and stay below 0 while remaining far from the truth. Logs and their weighted sums are floating point. High ESS only measures observed weight balance, not missed mass.

The extension adds 15 importance tests and three figure tests, for 43 total. Tests include exhaustive binary IID sequences through K=8, independent normal-density products, extreme-log underflow reports, exact-posterior constants, expected ELBO/posterior-KL identities, nonmutating inference, strict CLI validation and the real neural prefix fixture. The new figure checks all 48 numeric cells/positions, complete witness metadata and an undisplayed log-joint change. The five-module v0.2 wheel reproduces both demos outside checkout; original demo output and original SVG are byte-identical.

See [IMPORTANCE.md](https://github.com/midya8/latentlab/blob/main/IMPORTANCE.md). Standard importance/IWAE formulas credit Burda, Grosse & Salakhutdinov, [Importance Weighted Autoencoders](https://arxiv.org/abs/1509.00519), Section 3 and Theorem 1. This is inference auditing, not IWAE training, a confidence interval, a new estimator, an ESS accuracy certificate or exact neural evidence.

## Verification

The original 25 tests cover independent central differences of every parameter in nine hidden-size/beta settings, a fixed-noise batch derivative, saturated logvariance derivatives, zero-model analytic loss, exact-prior KL, an independently calculated first Adam update, strict checkpoint validation, immutable data, no global RNG effects, deterministic training, and CLI success/failure paths. The unchanged zero-step model deliberately fails the improvement gate; a collapsed origin cloud fails the disclosed distribution diagnostic.

Three visual tests check all 12 metric lines, all 1,536 scatter coordinates and common axes, byte reproduction, complete compressed-report metadata and tampering with an undisplayed checkpoint weight. CI runs tests on Python 3.10-3.13, the actual training demo, SVG check and wheel-installed demo outside checkout. The installed and source runs are compared as complete JSON objects.

## Limits and attribution

Only beta 1 is the ordinary negative-ELBO objective; beta 0 omits KL. Finite-noise evaluation estimates the expected ELBO and is not exact marginal likelihood or a guaranteed realization-wise bound. The posterior is diagonal with bounded variance, output noise is fixed, and there is only one two-dimensional data fixture and default seed. Sliced transport uses 32 deterministic directions; radius 0.3 is a disclosed synthetic diagnostic, not calibrated support estimation. No posterior-collapse, disentanglement, image generation or generalization claim.

Standard variational autoencoding, reparameterization and analytic Gaussian KL are credited to Kingma & Welling, [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114), Sections 2-3 and Appendices B-C. This is an original scalar implementation, synthetic fixture, audit and test suite, not a new algorithm or reproduction of their experiments. MIT.
