# Kurdistan International Sociological Association website — case study

Trilingual website (English, Sorani Kurdish right-to-left, and Kurmanji Kurdish) for KISA, an academic association for sociologists of Kurdistan and the Kurdish diaspora. Built with Next.js, TypeScript, and Tailwind, exported as static HTML and hosted on Cloudflare.

## The problem

An academic association needs a public home for its identity and its work — about the association, who governs it, who its members are, its journal and conference, news, and resources — in three languages, one of which reads right-to-left. A content-management system would mean a server to keep up, accounts to manage, and a database to back up, for a site whose content changes when someone publishes a news post or updates a page. The site is editorial content, not a transaction system, so the build treats it that way: pages are pre-rendered to plain HTML, and publishing is a file change, not a deployment event with a backend behind it.

## What it does

Every page exists in three locales — `en`, `ku` (Sorani), and `kmr` (Kurmanji) — under a single `[locale]` route tree, with each locale's `lang` and `dir` coming from one config (`src/i18n/config.ts`) and UI strings living in per-locale JSON dictionaries (`en.json`, `ku.json`, `kmr.json`). The layout sets the page's `lang` and `dir` per locale, so Sorani reads right-to-left at the layout level, not by translating strings and hoping the direction follows.

The content structure mirrors the association: About, governance (international and Kurdistan Region boards), members by category, journal, conference, news, gallery, resources, bylaw, and contact pages. News posts are Markdown files per locale, parsed with gray-matter and remark, so a post is a file with `title`, `date`, `excerpt`, and `author` frontmatter. The whole site is a static export — Next.js App Router with `output: "export"` — so every page in every language is pre-rendered to plain HTML and served from Cloudflare, and pushing to `main` redeploys it.

## Design decisions

- **Direction is layout, not translation.** Sorani Kurdish reads right-to-left, so `lang` and `dir` come from one i18n config and the locale layout sets them on the page — direction is handled where the page is built, not patched onto translated strings. A translated string can never arrive with the wrong direction, because direction was never the string's job.
- **One route tree, three locales.** Every page lives under `src/app/[locale]/`, so adding a page means adding it once and it exists in all three languages. The locale is part of the URL, not a cookie or a query parameter — a link to the Kurmanji conference page is a link, shareable and bookmarkable.
- **UI text is data, not code.** Interface strings live in per-locale JSON dictionaries, with the keys kept in sync across all three files. Changing wording never means touching a component, and a missing key is a visible gap in a data file rather than a broken render.
- **News is a file, not a form.** A news post is a Markdown file in `src/content/news/<locale>/` with frontmatter for title, date, excerpt, and author. Publishing needs no admin panel, no login, and no database write — the content is versioned with the site, reviewable in a pull request, and rendered by the same build as everything else.
- **Static because the content is editorial.** The site has no user accounts, no search index to maintain, and no per-visitor state, so it is exported to static HTML and served from Cloudflare: no server to keep up, scale, or patch. The architecture matches what the site is, not what a generic web app assumes.
- **The structure is the association.** About, governance with its two boards, members by category, journal, conference, news, gallery, resources, bylaw, contact — the page tree is the association's own shape, so a visitor finds the thing they came for where they expect it, and adding a section means adding pages, not redesigning navigation.
- **Content editing has one rule.** A news post goes in `src/content/news/<locale>/`; UI text goes in the dictionaries, with keys kept in sync across all three. There is one place for each kind of change, so an editor never has to guess where a fix belongs.
- **The build is the deploy.** `npm run build` produces the static export in `./out`, and pushing to `main` redeploys the site. There is no separate release step to forget and no manual upload — the thing that is reviewed is the thing that goes live.

## Worked example: publishing a news post

A conference announcement goes out in all three languages. The post is three files, one per locale, each with the same frontmatter shape the site already documents:

```markdown
---
title: "Annual Conference 2026 — Call for Papers"
date: 2026-11-05
excerpt: "The association invites paper proposals for its annual conference."
author: "KISA"
---

The call for papers is open...
```

The files land in `src/content/news/en/`, `src/content/news/ku/`, and `src/content/news/kmr/` — the same post, in each language's directory — and the local check is the same as any other change:

```bash
npm run dev      # http://localhost:3000 — read it in all three locales
npm run build    # static export in ./out
```

Pushing to `main` redeploys the site. No admin panel was opened, no database row was written, and no server was restarted: the announcement is a versioned file, the build renders it into every locale's static pages, and the deploy is the push itself. A post that exists in only one locale is a post in one locale — the per-locale directories make the gap visible instead of silently serving one language's news to every reader.

## What it demonstrates

A multilingual site where the hard part — right-to-left layout — is handled once, at the layout level, and everything else follows from ordinary decisions: static export for editorial content, Markdown files for news, dictionaries for UI text, and a deploy that is just a push.

## Links

- Repo: [midya8/kurdistansociology-website](https://github.com/midya8/kurdistansociology-website)
- Live: [kurdistansociology.com](https://kurdistansociology.com)
