# ddpm-mini

Repo: https://github.com/midya8/ddpm-mini

A denoising diffusion probabilistic model built with nothing but NumPy: the
denoiser is a small MLP with hand-written backprop, trained with an
eps-prediction objective on a cosine noise schedule over two 2D toy
distributions (two moons and a spiral). Sampling supports the ancestral DDPM
update and DDIM with eta 0 or 1.

The interesting part is measurement. Each run gets scored with two two-sample
checks against held-out data: 1-NN label accuracy, where 0.5 means generated
and real points are statistically indistinguishable, and an RBF-kernel MMD.
At 16,000 steps the stochastic samplers score 0.50 to 0.58 on both datasets.
The deterministic DDIM update does not: with a denoiser this small its error
compounds along a fixed trajectory and the samples drift off the manifold
(1-NN 0.95 on moons, 0.99 on spiral), which the sample grid in the README
makes visible.

Nine tests cover the schedule bounds, forward-process moments, backprop
shapes, DDIM determinism and metric sanity.
