# kalman-numpy

A constant-velocity Kalman filter, an RTS smoother, and an EM fit of the
process and measurement noise, written from scratch in NumPy.

The model is linear and the state is [x, y, vx, vy]. A target follows
constant velocity with small random noise on the velocity; measurements
are noisy positions. The filter must track, the smoother must do better
using the whole record, and the EM routine must recover the noises that
generated the data starting from a deliberately bad guess.

## What the code does

- The filter keeps the covariance in Joseph form
  `(I-KH)P(I-KH)' + KRK'`, which stays positive definite even after
  hundreds of updates. Each step reports the normalized innovation
  squared (NIS) and the log-likelihood increment.
- The smoother is the standard RTS backward pass, and it also returns
  the cross covariances `Cov(x_t, x_{t+1} | all data)`, which the EM
  update needs and which most textbook implementations quietly skip.
- EM is Shumway and Stoffer's, using those cross covariances for the
  Q update. It starts from `Q = I` and `R = 9I`, far from the truth,
  and still climbs monotonically to the right neighborhood.

## Verification, not vibes

Every claim is checked against a second, independent computation:

- The filter's log-likelihood over a 15-step run matches a direct
  evaluation on the joint Gaussian of all states and measurements,
  built from the unconditional covariance chain and one slogdet.
  Agreement is exact to 1e-6 relative. This check caught nothing in the
  end, which is itself information: the likelihood depends only on the
  position block of the covariance, so a filter can get the likelihood
  right while the velocity block is wrong.
- The smoothed covariances match a Schur complement on the same joint,
  to machine precision, for every step.
- The smoothed cross covariance `Cov(x_t, x_{t+1}|Y)` matches its
  exact value `C_t P_{t+1|T}` at every step of a short run.
- On long runs the mean NIS sits at 1.9, and a two-dimensional
  chi-square expects 2.0. An earlier version of the model hit a mean in
  the hundreds, which is how the first bug below was found.

## Results (T=300, q=0.02, r=1.0)

| quantity | value |
| --- | --- |
| raw measurement RMSE | 1.388 |
| filter RMSE | 0.929 |
| smoother RMSE | 0.515 |
| mean NIS | 1.91 |
| EM learned velocity noise | 0.0205, 0.0187 (true 0.02, 0.02) |
| EM learned measurement noise | 0.786, 0.815 (true 1.0) |

A velocity kick of 1.5 at t=150, unmodeled by the filter, costs little:
the track lags for a dozen steps and settles back to 0.91 RMSE after
the kick, 0.54 for the smoother.

## Two bugs worth writing down

The first one came from a one-line shorthand. Writing the process noise
as `Q[2:, 2:] = q` sets the whole velocity block, cross terms included,
so vx and vy get perfectly correlated noise. The filter's covariance
then collapses along the [1, -1] direction. Position gains look normal,
tracking looks fine for a while, and then the track drifts hundreds of
units while the NIS climbs past ten thousand: the differential part of
every innovation, where x and y disagree, is treated as impossible and
gets almost no gain. The fix is a diagonal velocity block, now built by
`process_cov` so the mistake cannot be made the same way again.

The second one was the smoother cross covariance. A first
implementation used `C_t (P_{t+1|T} - P_{t+1|t})`, which produces a
negative position-velocity cross covariance, impossible for this model.
The correct form is `C_t P_{t+1|T}` with
`C_t = P_{t|t} F' P_{t+1|t}^{-1}`. The exact-joint test pins it.

A third trap lived in the verification itself: the joint covariance of
the state sequence must come from the unconditional chain starting at
P0, not from the filter's measurement-conditioned covariances. Using
the conditioned ones conditions on the data twice, and the resulting
"exact" reference disagrees with everything while looking rigorous.

## Limits

Linear model with known F and H, no maneuver detection, and the EM
estimate of the measurement noise runs about 20 percent low on 300
samples because of the initial transient. Nothing here uses scipy or
filterpy.
