# ScanLab

Exact affine prefix scans and input-gated state-space derivatives, with
algorithmic span kept separate from real arithmetic work and floating behavior.

![Affine/scan/convolution/gradient audit](https://raw.githubusercontent.com/midya8/scanlab/main/assets/scan-audit.svg)

## Mechanism

- Diagonal affine pairs compose in temporal order. A reduction/reconstruction
  inclusive scan retains every operand, interval, pair and dependency depth.
- Fixed diagonal LTI recurrence equals direct causal convolution, with the
  nonzero-initial-state boundary term and skip connection explicit.
- A separate sigmoid input-gated recurrence exposes every forward state and
  hand-derived parameter/input/initial-state adjoint. Streaming carries state
  across chunk boundaries without changing causal outputs.

## Results and controls

The exact 16-token, two-state fixture uses 26 pair compositions. Unit vector
composition/apply span is 7 versus recurrence span 16, but scalar
multiplications rise from 32 to 136 and additions from 32 to 84. These are
actual DAG counts on supplied pairs, not runtime, GPU/FLOPs or fraction bit
complexity. Both paths execute serial Python.

The floating cancellation control writes [1e16,1,-1e16,1] with decay 1. The
sequential final state is 1, scan is 0 and exact rational result is 2. The input
gate control gives final f(2x)-2f(x) about 0.20243342, so one fixed linear
convolution cannot represent that model on all inputs. Neither failing control
is turned into a tolerance-based success.

30 tests include 729 scalar composition cases, 264 length/width cases against
an independent product expansion, 120 fixed LTI models, 123 independent gradient
probes, all 64 streaming partitions, full DAG/count checks and strict invalid
inputs. The 16 displayed gradient probes have maximum central-difference error
about 8.419e-12. Stable float reductions make full JSON/SVG artifacts reproducible
across the tested Python versions; the explicit cancellation failure remains.

## Boundaries

Supplied tiny affine tables, width 1..8 and length 0..128. Rational algebra and
float sigmoid arithmetic are separate paths. Finite differences validate
fixtures, not all derivatives. Streaming state is fixed width, but retained
trace/output memory still grows with length. No learned-task quality, general
long-context memory, GPU speed, FFT, HiPPO or Mamba/S4 implementation claim.
Seven prior sources are attributed; this is not a new scan algorithm.

- [Repository](https://github.com/midya8/scanlab)
- [Equations, counters, sources and limitations](https://github.com/midya8/scanlab/blob/main/NOTES.md)
