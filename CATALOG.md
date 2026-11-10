# Project discovery catalog

This is an index of the existing public case studies in `projects/*.md`. `README.md` and `CONTINUED.md` are aggregate navigation and release histories, so they are not counted again. No existing case study or release evidence is moved, deleted or rewritten.

## Build and reproduce

```sh
python tools/build_catalog.py
python tools/build_catalog.py --check
python -m unittest discover -s tests -v
node --test --test-concurrency=1 tests/test_search.cjs tests/test_browser.cjs
python -m http.server 8000 --directory docs
```

Python uses only the standard library. Browser tests need Node 22+ and Chrome (`CHROME_BIN` can select it). The page itself has no runtime packages, external fonts, analytics, accounts, API calls or paid services. Open `docs/index.html` directly or serve `docs/` as static files.

## Source contract

The deterministic generator reads every eligible project Markdown file in filename order. It ignores fenced examples when finding titles, section headings and prose. It keeps the first heading, an opening prose excerpt, all noncode section headings and a deduplicated alphabetic/numeric term set from noncode source prose. A sentence boundary is preferred when an excerpt needs shortening; otherwise an ellipsis marks the shortened text. This is a small documented parser, not a full CommonMark implementation. It does not interpret arbitrary HTML or execute Markdown.

Every record carries the exact source path, source URL, UTF-8 byte count and SHA-256 digest. These hashes detect content changes relative to a checked-out source tree; they are not signatures, identity proof or evidence that claims in a case study are true. `catalog.json` is a manifest of numbered JSON shards. The matching JavaScript shards carry the same project records. Shards keep individual files bounded without dropping projects. The static HTML includes every card and link, even with JavaScript disabled or a data script unavailable. If data and card membership disagree, filtering stays hidden rather than presenting an incomplete list.

Search is local, case-insensitive and accent-insensitive. Whitespace-separated query words must all occur as literal substrings in the project's ID, title, excerpt, section headings or source-prose term set. Matching is not stemming, semantic search, a benchmark or a quality ranking. Terms can match prose beyond the displayed excerpt. Results remain in source filename order. The URL stores the query for bookmarking; typing replaces the current history entry and browser navigation restores a bookmarked query. Queries are capped at 256 characters.

## What the index does not claim

An excerpt is not a fresh reproduction, test result, endorsement or current product-status report. The generator does not add test totals, infer categories, rank quality, verify every repository's present availability, or turn synthetic development controls into held-out results. Follow the source case study for its evidence, dates, assumptions and limits. The catalog does not replace that evidence.

## Checks

Python tests check source completeness, deterministic generation, digest sensitivity, exact static card/link membership, fenced examples, bold openings, navigation-only blocks, escaping and missing-source refusal. A separate JavaScript matching oracle checks literal query semantics, source order, Unicode normalization and empty queries. Actual Chrome compares every card's source link, query result sets at 320/390/1280 widths, mobile containment, 44-pixel controls, bookmarked-query restoration, trusted text entry and Clear input, and the no-JavaScript fallback. Failed content assertions are not retried; only initial debugger readiness waits.

Pages publishing is separate from catalog generation. CI checks that generated files match committed source before deployment. Updating an existing case study requires rebuilding the catalog. Adding a new case study automatically changes the manifest, shards and static cards on the next build.
