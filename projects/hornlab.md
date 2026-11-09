# HornLab


## HornLab: a circle is not a proof

[Live inspector](https://midya8.github.io/hornlab/) · [Source and tests](https://github.com/midya8/hornlab) · [Method and sources](https://github.com/midya8/hornlab/blob/main/METHOD.md)

Bounded positive propositional Horn inference with synchronous derivation rounds and every indexed rule decision. Compare the least model with every classical and supported model: a supported circular assignment need not have a derivation. Inspect an atomic countermodel for each non-entailed query and every inclusion-minimal initial-fact support, including its deletion failures and all seed subsets. Not entailed does not mean classically false.

Independent Python bitsets and JavaScript sets match 210 full reports; a separate native set/truth-table checker replays the complete report. Ten original controls, exhaustive two-atom programs, seeded tests, installed-wheel reproduction and actual Chrome record checks. Six atoms/eight rules, no negation or variables; established semantics, not a new algorithm or production rule engine.

## Method boundaries

Facts are fixed seeds. Empty-body rules can derive atoms with empty seed support. Duplicate indexed rules remain distinct achievers. Synchronous closure does not chain through a new atom until the next round. Models satisfy all implications; support is a separate equality test and may admit unsupported-by-derivation cycles. Minimal supports are relative only to the given initial facts with rules held fixed.

The native checker uses explicit sets, enumerates every truth assignment and tests all proper seed subsets, separate from the bitset generator and its immediate-deletion test. They share validation. This is bounded exhaustive evidence, not a formal proof or a signed certificate. JSON export is unsigned, and the browser generator is not an independent verifier.

## Reproduce

```sh
python -m unittest discover -s tests -v
npm test
bash tools/wheel_smoke.sh
python -m hornlab examples/cycle.json --output /tmp/horn.json
python -m hornlab --verify /tmp/horn.json
```

See the repository METHOD.md for six inspected sources, exact schema, the ten controls and validation limits. No external model, API or paid service.
