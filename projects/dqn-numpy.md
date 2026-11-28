# dqn-numpy

Double DQN on CartPole, written from scratch in pure NumPy. The Q-network
is a two-hidden-layer MLP with hand-written backprop, the replay buffer is
a plain ring of arrays, and the environment is integrated from the
equations of motion.

## What the code does

- The loss touches only the selected action's head, so the output-layer
  gradient is a zeroed delta with the TD error on the taken action; the
  gradient is checked against finite differences on every parameter.
- The replay buffer wraps around a fixed ring, and the tests cover both
  the wraparound and that a sample reproduces exactly what was stored.
- The target network hard-syncs every 200 steps, and in the Double DQN
  half the online net picks the action while the target net scores it.
- The environment keeps two failure kinds apart: a pole drop or a cart
  that leaves the track cuts the bootstrap, but the 500-step limit is a
  truncation and the target still bootstraps through it.

## What the results show

The shipped run solves CartPole at episode 389 (mean100 >= 475) and the
greedy policy returns 500.0 +/- 0.0 over 100 fresh episodes.

The repo's second run is the reason the target network exists. The same
recipe with the target network removed never leaves the plateau: it sits
near a mean100 of 264 at episode 300, and its greedy policy fails after
about 8 steps. Same network, same replay, same hyperparameters; the only
difference is where the bootstrap value comes from.

Runs are seed-sensitive: two probe runs with other seeds solved at
episodes 447 and 524. The published numbers also need
`OPENBLAS_NUM_THREADS=1`, because the BLAS reduction order changes which
run you get, the same float-reduction sensitivity the svm-from-scratch
notes document.

## Limits

One task, one architecture, one reward. CartPole is small enough that a
128-wide MLP saturates it; nothing here says anything about scaled-up
control. The eval uses the classic solve criterion (mean100 >= 475 under
an epsilon of 0.01), and the greedy number is the cleaner claim.
