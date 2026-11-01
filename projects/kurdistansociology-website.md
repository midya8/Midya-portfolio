# Kurdistan International Sociological Association website — case study

A trilingual website for the Kurdistan International Sociological Association, built with Next.js, TypeScript, and Tailwind CSS, exported as static HTML and hosted on Cloudflare.

- Live: [kurdistansociology.com](https://kurdistansociology.com)
- Repo: [midya8/kurdistansociology-website](https://github.com/midya8/kurdistansociology-website)

## The constraint that shaped the build

The site serves readers in three languages: English, Sorani Kurdish, and Kurmanji Kurdish. Sorani Kurdish is written right-to-left, so multilingual support here is not just translated strings — it is a layout problem. Direction, text alignment, and navigation order all have to flip correctly, and the design has to look deliberate in both directions rather than mirrored as an afterthought.

## Decisions

- **Static export over a running server.** The content is editorial, not transactional, so the site is exported to plain HTML at build time. That keeps hosting simple and the pages fast: there is no server to keep up, scale, or patch, and Cloudflare serves the result globally.
- **Next.js for structure, not for dynamism.** Next.js provides the routing and build pipeline, but the output is static. The framework works for the project instead of the project working around the framework.
- **Right-to-left as a first-class layout concern.** Direction is handled at the layout level so that switching languages switches the reading experience, not just the words.
- **Tailwind for consistency across scripts.** A utility-first approach keeps spacing, type, and components consistent whether the page is set in Latin or Arabic script.

## What it demonstrates

Building for more than one language and more than one writing direction, and choosing the simplest architecture that meets the actual requirements: static output, no backend to maintain, and a reading experience that respects each language's direction.
