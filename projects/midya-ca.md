# Personal site — midya.ca — case study

A personal site set against a procedurally generated Three.js galaxy. Built with React, TypeScript, and Vite.

- Live: [midya.ca](https://midya.ca)
- Repo: [midya8/midya.ca](https://github.com/midya8/midya.ca)

## The constraint that shaped the build

A visual centerpiece like a galaxy is easy to overdo: it can dominate the page, drain a weaker device, or ignore the visitor entirely. The goal here was a site that looks alive without getting in the way of reading it — striking on a capable machine, restrained everywhere else, and respectful of visitors who prefer less motion.

## Decisions

- **Procedural, not pre-rendered.** The galaxy is generated in code with Three.js rather than baked into an image or video. That keeps it lightweight to ship and lets it respond to the device it runs on instead of playing back the same heavy asset for everyone.
- **Rendering quality that adapts to the device.** The scene scales its rendering effort to what the hardware can comfortably handle, so the experience stays smooth rather than stuttering on modest machines or wasting power on strong ones.
- **Reduced-motion awareness.** Visitors who have asked their system for reduced motion get a calmer presentation. Motion is a preference, not a requirement, and the site treats it that way.
- **Vite for a fast, simple build.** React and TypeScript provide the structure; Vite keeps the build quick and the output static, so there is no server to maintain behind a personal site.

## What it demonstrates

Building a visually ambitious page that still respects its constraints: performance that adapts to the device, motion that respects the visitor's settings, and a static build with nothing to keep running.
