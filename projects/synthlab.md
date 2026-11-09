# SynthLab


### SynthLab: counterexample-guided bit-vector program synthesis


**Fits the examples. Fails the function.** A learner chooses the cheapest grammar expression fitting known examples; an exact finite verifier returns the first wrong input. Inspect every iteration, eliminated candidate, complete truth table and evaluation tree. Full-domain semantic signatures safely deduplicate programs without using the target; a separate verifier enumerates every raw ordered grammar tree to check bounded completeness and canonical minimum cost.

Ten synthetic controls separate example agreement, exact finite correctness and minimum AST-node cost inside the explicit grammar. Eight native tests run on Python3.10-3.13, including512 Boolean target/grammar pairs and2764 raw trees at each of three widths; four Node/actual-Chrome tests audit30 reports,90 iterations,903 candidate signatures and3420 expression probes. Installed module+console reproduction runs outside the checkout. Classical CEGIS/enumeration credited. No novel algorithm, unbounded synthesis, cvc5 integration or production-code benchmark claim.

[Live inspector](https://midya8.github.io/synthlab/) · [Source](https://github.com/midya8/synthlab) · [Grammar, proof boundary and sources](https://github.com/midya8/synthlab/blob/main/CONTRACT.md)

## Technical case study

The frontier covers pure unsigned1..3-bit expressions built from0/1/x/y and selected add/and/neg/not/xor operators through AST node cost5. All operations are total and fixed-width. The complete target table is supplied, so this is an inspectable finite CEGIS replay rather than hidden-service query learning.

Canonical representatives use minimum node cost then ASCII prefix-expression order. Full-domain equivalence is a congruence for these pure total operators; replacing an equivalent subtree cannot worsen cost. The certificate verifier independently enumerates the raw grammar rather than trusting quotient construction. Exhaustion proves only absence through the bound.

The browser exposes each candidate and input probe, with subtree costs and values, example membership, verifier counterexamples and complete eligibility/elimination lists. Offline CLI certificates have strict parsing and atomic output. No API key, runtime dependency, private data or paid service.
