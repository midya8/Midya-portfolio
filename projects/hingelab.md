# HingeLab: exact scalar-network robustness

HingeLab computes every affine region of a supplied small rational ReLU network. It separates three questions: whether one reference is robust at a requested radius, which references are robust at that radius, and how robust interval length changes over every radius in [0,32].

[One-reference inspector](https://midya8.github.io/hingelab/) · [Every-reference inspector](https://midya8.github.io/hingelab/reference.html) · [Every-radius inspector](https://midya8.github.io/hingelab/radius.html) · [Source](https://github.com/midya8/hingelab)

## A distance need not be attained

Fix class 1 at margin ≥ 0 and class 0 otherwise. For margin(x) = x on [-2,2], the opposite-class set from reference x = 1 is [-2,0). Its distance has infimum 1, but no opposite-class point attains it. A closed ball of radius 1 is robust. From x = -1, the tie x = 0 is an actual opposite-class point, so the same radius is not robust. The label convention and endpoint ownership are part of the answer.

An isolated tie makes this visible: margin(x) = -|x| has class 1 only at x = 0. A sampled grid can miss that entire class. HingeLab keeps the singleton, hidden activation kinks and exact open/closed endpoints rather than smoothing them away.

## Run and audit

Python 3.10+, no runtime dependencies. Node 22+ and Chrome for browser tests.

```sh
python -m unittest discover -s tests -v
python -c 'import json; print(json.dumps(json.load(open("docs/controls.json"))[0]["input"]))' > /tmp/request.json
python -m hingelab atlas /tmp/request.json > /tmp/report.json
python -m hingelab verify /tmp/report.json
python -m hingelab reference /tmp/request.json > /tmp/reference.json
python -m hingelab reference-verify /tmp/reference.json
npm test
bash tools/check_wheel.sh
python -m http.server 8000 --directory docs
```

The installed wheel exposes module and console commands outside the checkout. All three report families have separate generator and verification commands. The exact contracts describe the input grammar, reproduction and finite-check arguments:
[one reference](https://github.com/midya8/hingelab/blob/main/CONTRACT.md),
[every reference](https://github.com/midya8/hingelab/blob/main/REFERENCE.md),
[every radius](https://github.com/midya8/hingelab/blob/main/RADIUS.md).

## Three exact reports

- **One reference:** forward affine-interval splitting, canonical open-interior activation masks, per-cell zero witnesses, opposite-class intervals, distance infimum, attainment and an actual witness inside the requested ball when one exists. The exact domain Lipschitz constant is the largest absolute output slope.
- **Every reference:** erode each exact class component by the requested closed ball, clipped to the declared domain. At radius 1 for margin x on [-2,2], class-0 robust references are [-2,-1), while class-1 references are [1,2]. A domain edge is not an invented adversary.
- **Every radius:** sum the domain-edge-aware piecewise-affine length profiles, preserve strict/closed existence intervals, and solve the first radius at most a requested domain-length fraction. For margin x, length is max(4-2r,0). At radius 2 the length is zero, but the class-1 singleton {2} still exists. Class 0 vanishes at 2; class 1 vanishes only above 2. A constant class may never reach a target below one.

Python uses `Fraction`; the browser independently uses normalized `BigInt` fractions. Only SVG coordinates and tick labels are rounded. Inspect regions/components, affine length pieces, class-specific existence sets, inverse targets and downloadable JSON. Edits and invalid input clear stale results.

## Why the checks are separate

The base checker enumerates at most 64 hidden activation masks, intersects rational phase inequalities, reconstructs coverage/formulas, then checks boundary/root atoms and intervening open intervals. It imports neither forward generator nor its set-construction function.

The reference checker shifts all mask-derived class boundaries by ±radius and checks exact opposite-class intersection on every critical point and open interval. It imports no reference generator or erosion/union routine.

The radius checker partitions at differences and half-differences between boundary/root points. In each open radius cell, exact closed-ball intersection reconstructs affine length; endpoints and existence are checked separately. It imports no forward profile, reference generator or erosion/union routine. Parsing, direct evaluation and the independent base mask enumerator are shared explicitly. The finite-ordering argument, rather than a sampled grid, covers all radius atoms. A browser report becomes independently checked only after Python accepts its JSON.

## Evidence and limits

Fresh public-source reproduction passes 26 Python tests and ten Node/actual-Chrome tests. The retained suites cover 200 base and 160 reference seeded networks; radius tests add 40 seeded profile networks. Complete cross-language comparisons cover 144 base, 200 reference and 104 radius reports. Generator-disabled checks, forged report fields/types, exact singleton/strict-endpoint cases and installed-wheel reproduction remain covered. Both installed entrypoints reproduce eight controls for each of the three report families and reject forged evidence.

Live Chrome checks the base workflow's 54 region selections/24 reports, the reference workflow's 47 component selections/28 reports, and 28 radius reports across 320/390/1280 pixels. Download, stale clearing and invalid-input behavior pass. All 13 deployed assets match main. Full phone and desktop workflows were visually inspected. The documentation review preserved every one of the 42 non-document source files.

The contract is deliberately small: one scalar input, one scalar output margin, one or two hidden layers of width 1..3, at most six hidden neurons. Input rational absolute values are at most 32 with reduced denominator at most 1,024; the domain is a nonempty closed interval. Radius horizon [0,32], target fraction [0,1]. Robust fraction is interval length divided by domain length, not accuracy or probability. Zero length is not absence. The critical-radius checker uses O(P^4) intersection checks for P mask-derived boundary/root points, plus mask enumeration, evaluation and sorting; rational bit cost is not constant.

Established piecewise-affine line restrictions and morphological erosion, not a new verification algorithm, theorem implementation from the cited papers, trained/imported model, high-dimensional certificate, benchmark or scaling claim. No paid API or private data. The [source ledger](https://github.com/midya8/hingelab/blob/main/SOURCES.md) distinguishes neural-network background from the erosion definition; relative-domain closed balls differ explicitly from Pegden's open-ball convention. Historical citations were preserved, not freshly revalidated. MIT license.
