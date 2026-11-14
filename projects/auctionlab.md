# AuctionLab

AuctionLab enumerates combinatorial allocations, Vickrey-Clarke-Groves (VCG) prices, report-independent bundle menus and seller-coalition core deficits. Synthetic private values, no actual auctions or money.

[Live inspector](https://midya8.github.io/auctionlab/) · [Source](https://github.com/midya8/auctionlab)

## Questions the report separates

- Which allocations maximize reported welfare, including every tie?
- What externality does each winner pay, and what utility does truthful reporting attain?
- Can a seller-inclusive coalition generate more value than its current combined payoff?
- What happens under each explicitly supplied unilateral report?

A coalition deficit is a transferable-utility witness, not a collusion plan. Checking selected reports is not a proof over every possible valuation.

## Bundle-versus-singletons control

The developed default has two items and three complete value rows, indexed by empty, A, B, AB:

| Bidder | Empty | A | B | AB |
|---|---:|---:|---:|---:|
| B1 | 0 | 0 | 0 | 10 |
| B2 | 0 | 6 | 0 | 6 |
| B3 | 0 | 0 | 6 | 6 |

Giving A to B2 and B to B3 creates welfare **12**. Remove either winner and the remaining bidders can create **10**. The other winner contributes **6** in the chosen allocation. Each winner pays the externality **10 - 6 = 4**, giving revenue **8** and truthful utilities **[0,2,2]**.

The seller with B1 could produce **10**, but their current combined payoff is only **8**. This seller-inclusive coalition has a cooperative-core deficit of **2**. It is a mathematical blocking witness, not an actual collusion strategy, equilibrium or market recommendation. This numerical profile varies the classical bundle-versus-singletons pattern credited to the existing literature; the phenomenon is not new.

Changing only B1's row to `[0,5,5,10]` leaves welfare at 12, raises revenue to 10 and eliminates the deficit in this developed control. This numerical comparison does not establish a general causal claim about valuation classes.

## Report-independent bundle menus

For every bidder and every bundle, reserve that bundle and optimize everyone else on the remaining goods. Subtract that remaining-goods optimum from the optimum without the bidder. This defines a bundle-price menu using only the other reports.

The explorer retains every remaining-goods optimum witness, each true bundle value, price, utility and maximizing bundle. At the default, B3 can get bundle B for price 4 and utility 2; bundle AB costs 10 and yields utility -4. Every efficient truthful allocation chooses a best menu bundle.

The complete finite menu makes the externality visible. The general truthfulness result remains classical VCG theory, not a theorem proved by trying a few reports.

## Efficient ties and supplied reports

Generation enumerates every item owner, including seller-retained items, in lexicographic order. Every welfare-maximizing allocation is retained. On the tied single-good control, both winning allocations survive: payment vectors are `[7,0]` and `[0,7]`, while utilities remain `[0,0]` and revenue 7.

For supplied alternative reports, change one bidder's reported values while keeping its true values and all other reports fixed. Retain every reported-optimal tie and evaluate true utility after payment. The zero-report one-bidder control includes every tie, with true utility gains spanning -9 to 0. It is not prefiltered to show only favorable outcomes.

## Certificate replay

Python generation uses ownership vectors; the separate certificate verifier enumerates disjoint bundle products, derives ownership IDs and independently reconstructs the entire report. It never imports the generator. Strict recursive comparison rejects missing, duplicated, reordered, extra and mistyped evidence.

The browser offers strict JSON input, allocation/menu/coalition/report selectors, complete witness tables and native input/certificate downloads. Input edits clear stale evidence and disable downloads until a new valid report is generated. Mobile tables have explicit sideways-scroll hints and keyboard-focusable regions.

Browser generation and replay change census representation but share evidence construction. This is disclosed: the browser is not a second independent mechanism implementation. Cross-language equality supplements the separately implemented Python replay. A self-consistent certificate establishes arithmetic relative to its included input, not the economic truth or provenance of a bidder's values.

## Bounded reproduction evidence

| Check | Observed result |
|---|---|
| Python suite | 24 tests |
| Full cross-language corpus | 52 profiles; 1,997 allocations; 163 efficient outcomes; 272 coalition rows; 752 menu entries |
| Selected reports in that corpus | 349 reports; 1,394 reported-optimal outcomes |
| Primitive report tampering | 1,204 forgeries rejected per engine |
| Exhaustive small-type audit | All 196 two-bidder profiles over 14 monotone two-good value rows with entries 0..2; all 14 reports per bidder; 5,488 reports and 12,348 reported-optimal outcomes |
| Input-built HiGHS reference | 1,024 binary integer solves; 5,530 constraint rows; zero objective error at 1e-8 tolerance, SciPy 1.15.3 |
| Installed wheel | Six module origins; 16 developed controls; two entrypoints; 32 CLI forgeries |
| Actual Chrome | 48 responsive views; 1,581 allocation selections; 636 menu entries; 312 coalition rows; 3,441 deviation outcomes |
| Native downloads | All 16 inputs and 16 certificates; downloaded certificates replayed by Python |

The HiGHS reference is constructed from input bidder/bundle variables and bidder/item constraints. It separately recomputes all coalition welfare and remaining-goods menu optima, checks integrality and feasibility, and does not encode expected answers. It is optional, not a production runtime dependency.

The 16 controls are developed teaching fixtures, not held out. The 52-profile corpus includes 36 seeded profiles across 1..4 items and 1..3 bidders. The 196-profile report-type exhaustion covers an explicitly bounded universe, not all possible valuations. No performance, learned-generalization or real-market claim follows from these counts.

## Earlier release checks

The earlier source PR1 merged after all six latest feature/PR jobs passed. Merged main `16ab4f8efa912f118b87323027170d8167ee9a39` retains the initial commit and feature history. All 47 public files matched the checked local source. [Merged-main checks](https://github.com/midya8/auctionlab/actions/runs/42897526338) and [Pages deployment](https://github.com/midya8/auctionlab/actions/runs/42897526146) passed. At that release, every one of the five deployed assets matched merged source byte for byte. The full real-Chrome workflow passed against the deployed site, including native download replay; all 30 unmasked deployed captures exactly match the inspected local pixels. Desktop live hero and mobile allocation pixels were also inspected directly. These are commit-specific earlier release checks, not a claim that an unchecked later deployment passed. They do not establish the truth of supplied values or suitability for a real market.

## Scope and prior work

At most four items and three bidders. Complete nonnegative monotone integer valuations 0..100 with empty-bundle value 0, free disposal, zero seller reserve and quasilinear private values. At most six supplied alternative reports per bidder. No learned valuations, budgets, common values, false names, collusion audit, core-selecting price rule, market advice or large-scale winner-determination claim.

The VCG rule, menu interpretation and cooperative-core formulation are established theory. [Roughgarden's lecture notes](https://theory.stanford.edu/~tim/f05/ca.pdf), [Ausubel and Milgrom's chapter](https://milgrom.people.stanford.edu/wp-content/uploads/2005/12/Lovely-but-Lonely-Vickrey-Auction-072404a.pdf) and [Conitzer and Sandholm's paper](https://www.cs.cmu.edu/~conitzer/vcgfailuresAAMAS06.pdf) ground the definitions and limitations. [Existing formal verification](https://isa-afp.org/entries/Vickrey_Clarke_Groves.html) and [existing Rust software](https://docs.rs/vcg-auction/latest/src/vcg_auction/vcg.rs.html) are acknowledged. The contribution is this bounded implementation, synthetic teaching controls, evidence format, independent replay and inspectable UI, not a new theorem or first verified implementation.
