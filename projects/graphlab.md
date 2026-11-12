# GraphLab: graph convolution and fixed-model audits

GraphLab trains a two-layer graph convolutional network on a small synthetic graph, with masked training labels, validation-only checkpoint selection and matched feature-only and scrambled-graph controls. For a fixed model, it audits input gradients, single-edge deletions and complete joint-edge deletion sets. The joint audit recomputes normalization for every set and shows where adding singleton effects gives the wrong class prediction.

[Source repository](https://github.com/midya8/graphlab) · [Design contracts](https://github.com/midya8/graphlab/blob/main/DESIGN.md)

![Synthetic graph and expressivity audit](https://raw.githubusercontent.com/midya8/graphlab/main/assets/graph-audit.svg)

## Joint-edge deletion

51 Python tests retain all 42 original tests. Independent dense/bitmask checks cover 180 seeded graph/model cases; 70-digit Decimal checks all 16 counterexample sets. Python/JavaScript agree on 46 complete reports and 559 subsets. Actual NumPy checks all 559 logit vectors, max difference 8.88e-16. Five Node/Chrome tests cover 24 responsive views, 568 subset selections and six natively replayed trusted downloads. An isolated wheel checks seven module origins and all nine commands via both entrypoints. Original trained GCN/MLP/scrambled results, centroid/final controls and both figures reproduce unchanged.

The original joint-deletion release in source PR1 passed all 16 latest feature/PR jobs and merged with prior history intact. All 44 merged files and five deployed assets match the tested source. Merged-main CI and Pages passed after enabling the repository's Pages source. Full deployed Chrome workflow passes. Twenty of 24 unmasked captures are byte-identical in pixels; the other four differ only on one 150-pixel table-border line, with identical layout/content. The four differences were inspected, not masked. Actual desktop and phone graphs, values and complete tables were inspected. This is a bounded binary64 fixed-model sensitivity census, not a causal effect, learned robustness improvement, new algorithm, formal real-arithmetic certificate or scale claim. Original edges only, with self loops retained. Chosen two-class margins stay separate from all-class predictions. Established GCN and formal graph-verification literature are credited.

The hand-set counterexample uses four scalar features [-4,-4,6,6] and five original edges. Its baseline class-1 minus class-0 margin is 0.5534180126. All five single deletions preserve class 1. Removing e1=(0,2) and e3=(1,2) produces margin -0.6666666667 and class 0. Singleton extrapolation predicts +0.3151513784 instead; the residual is -0.9818180451. Of all 16 empty/single/pair sets, five change the class. The stronger minimum-margin pair e1/e2 has margin -1.0606601718 and remains visible. This fixture was found by a disclosed tiny integer search, not a held-out experiment or trained-model quality result.

The Python producer reuses the original sparse fixed-model forward evaluator but independently constructs each perturbed edge list and recomputes every degree. A separate dense checker uses full adjacency/matrix products and bitmask enumeration. JavaScript uses its own dense engine and recursive subset generation. A numerical NumPy matmul reference checks logits, with a separate tolerance for discrete near-tie decisions. High-precision Decimal checks the developed counterexample. None is presented as a formal proof of every accepted real-valued input.

A preflight call count sums binomial coefficients for all cardinalities through min(k,m). Native limits permit k=0..8 and 1..65,536 forwards; an oversized request fails before any model forward. The original 483-edge graph at k=2 exceeds the cap, while k=1 fits. No candidate restriction is silently substituted. The page supports 12 nodes/edges, four input/hidden/class dimensions and at most 4,096 calls. Empty input edges retain one empty subset, and self loops always remain.

Every report records all target logits, selected margin, signed change, singleton sum and residual. Budget summaries keep minimum/maximum margin witnesses, largest residual and all-class prediction-change counts. Lowest class index wins evaluated exact ties. Choosing two margin classes does not hide another class that wins. The multiclass control shows a negative selected margin while baseline class 2 stays unchanged. MLP identity propagation and all-zero ties remain explicit controls.

The browser invalidates all old outputs and disables downloads on edits. Six trusted JSON downloads are independently replayed by native sparse Python. Reports are unsigned and attest only to consistency with their embedded input, not source authenticity or real-world truth. The ordinary CLI/page JSON parsers do not reject duplicate keys. No cross-language exact tie guarantee, runtime comparison, edge-addition/rewiring, causal importance or robustness-accuracy score is claimed.

[Live inspector](https://midya8.github.io/graphlab/) · [Full contract, commands and seven-source ledger](https://github.com/midya8/graphlab/blob/main/JOINT.md)

The single-edge and input-gradient sections below describe the original 42 tests, retained within the current 51-test suite.

## What the graph changes

Message passing changes which information a node prediction can use. This implementation makes that context, the label masks, checkpoint choice and failure cases inspectable. A high fixture accuracy is not enough without stating how the graph was made and which nodes were visible.

## The model

For undirected binary adjacency A and added self loops:

```
S = D^(-1/2) (A + I) D^(-1/2)
H = ReLU(S X W0)
P = softmax(S H W1)
```

Sparse neighbor lists apply the symmetric normalized operator. It is **not row normalization**; irregular-graph row sums need not equal one. Isolated nodes retain their own features through a self loop. A feature-only MLP uses identity propagation with the same parameterization, initialization, parameter count and update budget.

Cross-entropy gradients use training nodes only. Validation labels can select a checkpoint, including initialization, but never enter the training gradient. Test labels are passed as `None` during fitting. Test **features and graph edges remain visible**: this is transductive node evaluation on one graph, not unseen-graph, unseen-node or temporal generalization. Prediction accepts only features/edges, never labels.

[DESIGN.md](https://github.com/midya8/graphlab/blob/main/DESIGN.md) records equations, masks, selection, bounds and strict artifacts.

## Measured development fixture

Seed 41: 96 nodes in two equal class communities, 4 noisy features, 483 edges. Each coordinate has class mean -0.25 or +0.25, noise SD 1. Edges are sampled with probability 0.2 within a class and 0.015 across classes. Thus **graph construction deliberately carries class signal**. Split: 8 training + 8 validation + 32 test nodes per class. The complete node lists are in demo JSON.

Each neural arm has 72 weights, shared seed 13, Adam learning rate 0.03 and 300 updates. Validation cross-entropy selects each arm independently among initialization and every update, with earliest ties retained. No test labels select a checkpoint. The scrambled graph uses seed 47 to relabel the same graph while keeping features/labels fixed: it preserves the graph's degree multiset and structure, not each original node's degree or feature alignment.

| Neural arm | Selected update | Selected train acc. | Selected validation acc. | Selected test acc. | Selected test CE | Last-update test acc. / CE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| GCN | 300 | 1.0000 | 1.0000 | 0.96875 | 0.060893 | 0.96875 / 0.060893 |
| Feature-only MLP | 1 | 0.6250 | 0.9375 | 0.34375 | 0.848734 | 0.484375 / 8.140771 |
| Scrambled-graph GCN | 0 | 0.3750 | 0.5625 | 0.515625 | 0.693328 | 0.546875 / 2.749939 |

A separate **train-only nearest-class-centroid** feature control fits 8 numbers with no validation selection and gives test accuracy **0.484375**. Balanced constant predictions give 0.5 on this balanced test set. The neural controls are not suppressed when a later checkpoint has higher test accuracy: both selected and last checkpoints are shown.

The feature MLP's excellent small-validation accuracy does not transfer to this test split; validation selection is no guarantee of representative evaluation. These are descriptive fixture results, not causal contributions or a general GCN ranking. Validation selection and the centroid control were added after inspecting the initial fixed-budget arms and their overfit losses. This is a **development fixture**, not an untouched benchmark or a multi-seed study. No architecture or seed sweep was run.

## Original tests and an architecture limitation

The original 42 tests cover every parameter of tiny reference models by finite differences in both modes, sparse-vs-dense forward arithmetic, independent degree normalization, permutation-equivariant predictions and training, mask isolation, stable unclipped cross-entropy, selection vs independent prefix refits, artifacts and CLI.

A six-cycle and two disconnected triangles are different graphs, but with identical constant node features and degree 2, every normalized neighborhood produces the same feature at every layer. This model gives **identical node probabilities** on both. The counterexample is exact for this architecture and fixture; it is not a claim that all graph neural networks fail on those graphs. No graph-level classifier or universal graph-isomorphism test is implemented.

## Fixed-model input gradients

![Input-gradient locality and sum audit](https://raw.githubusercontent.com/midya8/graphlab/main/assets/input-audit.svg)

`margin_attribution` / `explain` differentiates an explicit target node's chosen class-logit margin with respect to **all supplied input coordinates**, holding weights and graph fixed. It returns full signed gradient and gradient-times-input matrices, per-node sums, the margin, sum residual and the two-hop propagation receptive field. This is not a probability derivative or graph-edge attribution.

The hand-set tiny path fixture gives node contributions `[0.181666667, 0.341907943, 0.074981603, 0, 0, 0]`, summing to margin **0.5985562126120147** with reported residual **0.0**. Node 2's first coordinate contributes **-0.0136082763**, so only showing unsigned magnitudes would change the answer. Nodes 3-5 are beyond the two-layer receptive field and have exactly zero gradient; replacing node 5's features leaves the target margin unchanged. This is an arithmetic fixture, not a learned-model quality result.

For this **bias-free, positively homogeneous ReLU model** and the all-zero feature reference, the signed `x * gradient` sum equals the margin, up to floating-point reduction error. The identity is specific to this score/model/reference and is not an independent explanation-validity certificate. The zero reference need not be realistic. ReLU's derivative at exactly zero is defined as zero.

A separate one-node counterexample has margin ReLU(x): at x=-1 the gradient and `x * gradient` are both zero, yet replacing x with +1 changes the margin from 0 to 1. Local derivatives do not measure arbitrary finite interventions, causal importance, robustness or feature interactions. No new attribution method or causal claim is made.

## Edge deletion is a different question

`edge_sensitivity` / `edges` reruns the fixed model after deleting **each single original edge separately**, recomputing all degrees and normalization. It returns every signed margin change in original edge order. Features and weights stay fixed. This is finite score sensitivity, not an edge gradient, causal importance, joint-deletion guarantee or performance metric.

| Deleted edge in the hand-set path | Node-0 class-1 minus class-0 margin | Change from baseline |
| --- | ---: | ---: |
| None | 0.598556213 | 0 |
| 0-1 | 0.742000000 | +0.143443787 |
| 1-2 | 0.720500000 | +0.121943787 |
| 2-3 | 0.615407943 | +0.016851731 |
| 3-4 | 0.598556213 | 0 |
| 4-5 | 0.598556213 | 0 |

Node 3's **input-feature derivative is zero**, yet deleting edge 2-3 changes the target margin because node 2's degree changes. Input-feature locality does not imply the same boundary for graph structure or normalization. Deletions 3-4 and 4-5 have no effect in this tiny fixture. No statement of generic edge irrelevance follows from a zero single-deletion effect.

A preflight budget requires `1 + number_of_edges` model forwards before any model call. Default cap 256, supported cap 1-8193. The five-edge demo takes exactly six forwards. No partial top-k list hides edges, and an over-budget request fails rather than silently sampling. Every perturbed graph still adds self loops, so isolated nodes remain valid. This can be expensive on larger graphs; counts are actual forward invocations, not walltime claims.

```sh
python -m graphlab edge-demo
python -m graphlab edges /tmp/model.json examples/predict.json --node 0 --positive 1 --negative 0 --max-forwards 256
```

## Scope and limits

Small, undirected, unweighted graphs only: 1-128 nodes, 1-16 features, hidden width 1-32 and 2-8 classes. No edge features, attention, graph-level pooling, minibatching, dropout, weight decay, gradient clipping, calibration or confidence guarantee. The original paper's full training recipe and citation-network benchmarks are **not** reproduced. The figure's positions use true classes for a disclosed schematic, not a learned embedding.

Inference artifacts store weights and architecture, not graph data or optimizer state. No private/customer data is used and there is no privacy guarantee. This is an educational implementation, not a production library.

## Source credit

Independent educational implementation of **Kipf and Welling (2017), [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/html/1609.02907v4)**, especially normalized propagation Eq. 2 and the two-layer model/masked cross-entropy Eq. 9-10. Source read for mathematics; no copied code, dataset or pretrained weights. Published benchmark results belong to the paper, not this project.

MIT license.

## Reproduce

```sh
python -m unittest discover -s tests -v
python -m graphlab demo > /tmp/graph-demo.json
python examples/render_demo.py /tmp/graph-demo.json --check
python -m graphlab attribution-demo > /tmp/input-audit.json
python examples/render_attribution.py /tmp/input-audit.json --check
```

The train/predict CLI accepts bounded user-supplied graphs, with no external dependencies or network calls.
