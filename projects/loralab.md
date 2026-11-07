# LoRALab: low-rank adaptation from scratch, measured honestly

Low-rank adaptation (LoRA) fine-tunes a frozen model by learning a small low-rank update to a weight matrix instead of the whole matrix: `W' = W + B @ A`, where `A` is `r x d_in` and `B` is `d_out x r`. LoRALab implements the whole thing - forward pass, hand-derived gradients through `A` and `B`, merge-back, and the evaluation harness - in dependency-free Python, and measures the trade-off rather than asserting it.

## The fixture

A linear classifier over hashed bag-of-words trains on a synthetic topic distribution A. Distribution B uses disjoint vocabulary, so the base model's accuracy on B collapses: 1.0000 on A, 0.4444 on B. Adapting to B is then a real task, not a formality.

## What gets measured

Every adaptation configuration reports three numbers, because any two alone flatter the method:

- **Accuracy on B** - did adaptation work?
- **Trainable-parameter share** - what did it cost relative to full fine-tuning?
- **Retention on A** - what did adapting disturb?

On the checked-in fixture, pinned in tests:

| method | acc on B | retention on A | params | share |
|---|---|---|---|---|
| base (no adaptation) | 0.4444 | 1.0000 (on A) | 387 | - |
| lora r=1 | 0.9333 | 0.7333 | 131 | 33.9% |
| lora r=2 | 1.0000 | 0.7556 | 262 | 67.7% |
| lora r=4 | 1.0000 | 0.7778 | 524 | 135.4% |
| lora r=8 | 1.0000 | 0.7778 | 1048 | 270.8% |
| full fine-tune | 1.0000 | 0.9556 | 387 | 100.0% |

The headline: a rank-2 adapter matches full fine-tuning accuracy on the shifted distribution while training 67.7% of the parameters. The honest footnote, kept in the README and the tests: on this fixture the adapters retain *less* accuracy on the original distribution than full fine-tuning does. That is a measured property of this fixture and optimizer, not a general claim about LoRA, and it stays visible because cherry-picking the favorable column would be easy and wrong.

## Merge equivalence, bounded correctly

An adapter in production is usually merged into the base weights: `W' = W + B @ A`. Algebraically `(W + B @ A) x = W x + B (A x)`; in floating point the two association orders differ. LoRALab measures the difference instead of declaring it zero: max abs logit diff ~1e-14 on the fixture, with a test that pins the diff below 1e-12 and a second assertion that it is nonzero. The claim is exact algebra and approximate arithmetic - which is the true statement, and the only kind worth pinning in CI.

## Gates in both directions

```bash
python -m loralab gates --min-base-drop 0.3 \
    --min-adapted-accuracy 0.95 --max-rank2-param-share 0.7 \
    --max-merge-diff 1e-12
```

`--min-base-drop` fails if the fixture's distribution shift stops being real (without it, every other gate can pass vacuously); the achievable set above passes; `--max-rank2-param-share 0.5` fails because rank-2 costs 67.7%. The demo asserts both sides.

## Scope

The base model is a linear classifier, not a transformer; the adaptation mechanics - frozen base, low-rank factors, merge equivalence, cost and retention accounting - are model-shape-independent, and the README says so. 14 unit tests, fully offline, CI across Python 3.10-3.13.

- Repo: [midya8/loralab](https://github.com/midya8/loralab)
