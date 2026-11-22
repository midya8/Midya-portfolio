# realnvp-numpy

A RealNVP normalizing flow written entirely in NumPy, coupling layers
included, with backprop derived by hand in every module. No PyTorch, no
JAX, no autograd of any kind.

Why a flow: unlike a GAN or a VAE, the training objective is the exact
data likelihood, so the loss itself is a comparable, meaningful number.
The repo reports held-out NLL against a diagonal Gaussian baseline on the
same train split, and scores 600 samples per model with the same 1-NN
separability and RBF MMD checks as [ddpm-mini](https://github.com/midya8/ddpm-mini).

Results at 12,000 steps (four coupling layers, hidden width 64): held-out
NLL 1.758 on two moons and 1.716 on the spiral, against Gaussian baselines
of 2.834 and 2.846. 1-NN accuracy 0.499 on moons and 0.537 on the spiral,
where 0.5 means the two point sets are indistinguishable to a 1-NN
classifier.

The interesting debugging was all in the hand-written gradients: the
input gradient through the first layer, the tanh derivative on the scale
path, and the identity pass-through of the masked half in the inverse
direction all had bugs that only showed up under finite-difference
gradient checking, which is exactly why the tests exist.

![samples](https://raw.githubusercontent.com/midya8/realnvp-numpy/master/assets/samples_spiral.png)
