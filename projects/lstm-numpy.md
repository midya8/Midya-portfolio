# lstm-numpy

A character-level LSTM with backprop through time derived and coded by
hand in NumPy, gate by gate. No autograd, no framework. The gradient
check tests are what made the hand-written math trustworthy: the first
version of the cell cached the post-update hidden state where the
backward pass needed the pre-update one, and only the finite-difference
check caught it.

The repo trains on two synthetic corpora and reports next-char cross
entropy against an interpolated 3-gram baseline:

| corpus | LSTM NLL | 3-gram NLL |
|--------|----------|------------|
| sentences | 0.404 | 0.798 |
| parens    | 1.336 | 1.733 |

The headline result is the balanced-paren check. Every training string
on the parens corpus balances, so samples can be scored mechanically:
the LSTM produces balanced strings 97.5 percent of the time (195 of 200
at temperature 0.8) while the n-gram manages 28.5 percent, because an
n-gram cannot count. LSTM samples read as well-formed arithmetic:
`(((4+6)*(7*3))+5)`.

On sentences the model learned word shapes and the plural agreement
rule, with the occasional overreach (`fishs sleep`).

![loss curves](https://raw.githubusercontent.com/midya8/lstm-numpy/master/assets/fig_loss.png)
