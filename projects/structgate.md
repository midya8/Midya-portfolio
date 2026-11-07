# StructGate

Grammar-constrained generation built from scratch in pure Python, with conformance and constraint cost both measured.

## Problem

Structured output is usually asserted, not verified: "the model returns JSON" until it does not. StructGate builds the constraint machinery itself - an incremental validator that knows exactly which tokens are legal next - and measures both sides of the trade: what masking guarantees (conformance rate) and what it costs (distribution distortion).

## Approach

- **Exact legal-token sets** - a stack-based JSON state machine answers `allowed()` for any prefix: objects, arrays, strings with escapes, the full number grammar, literals, whitespace. It matches Python's json module on 32 adversarial cases in the suite, and snapshots/restores state for exact queries.
- **Closed-schema layer** - required keys in a fixed order, typed slots (string/number/bool), no additional keys; the same masking loop then produces records that parse and conform, with key order and types enforced during generation.
- **Exact distribution to mask** - an order-3 character n-gram with add-k smoothing; probabilities come straight from counts, so the mask's effect is measured against ground truth, never an approximation.
- **The cost in nats** - masking renormalizes the distribution to the legal set; -ln(Z) per step is exactly KL(p || p_masked), reported per mode.

## Verification

- 33 unit tests cover validator-against-stdlib agreement, exact allowed sets per grammar position, snapshot determinism, schema key-order/type/extra-key rejection, a pinned number/whitespace boundary regression, pinned fixture numbers, and both sides of every CLI gate.
- Fixture results (40 seeded draws per mode): grammar-constrained valid JSON 40/40, schema-constrained conforming 40/40, unconstrained control 3/40; mean mask cost 1.3496 nats/step (grammar), 0.8209 (schema).
- `bash examples/demo.sh` runs fully offline and asserts both gate sides; CI runs the suite across Python 3.10-3.13.
- The unconstrained control is gated from above (`--max-unconstrained-rate`) so a fixture change cannot silently stale the comparison.

Bounds worth stating: the char-level n-gram is a toy model by design - it exists to be exact, not fluent, and nothing here claims language-model quality. The schema layer covers flat closed records with three slot types; nested schemas, unions and optional fields are future work. KL cost is measured against this model's own unconstrained distribution.

## Links

- Repository: [midya8/structgate](https://github.com/midya8/structgate)
