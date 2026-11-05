# Personal site — midya.ca — case study

Personal site, live at [midya.ca](https://midya.ca). Built with React, TypeScript, Vite, and Three.js, deployed as a static build on DigitalOcean App Platform. The background is a procedural galaxy rendered in WebGL — nothing is loaded from outside the code: the stars, spiral galaxy, dust, constellation lines, and nebula haze are all generated at runtime.

## The problem

A personal site has one job: present the person clearly, on any device, without getting in its own way. A heavy visual background is the obvious risk — a galaxy rendered in WebGL can be beautiful on a desktop and a battery drain on a phone, a slideshow of motion for someone who asked for less of it, or a blank page where WebGL is unavailable. The site has to carry a distinctive visual identity without ever making the visitor pay for it in performance, motion, or a failed render.

## What it does

The background is a procedural WebGL scene ([`GalaxyBackground.tsx`](https://github.com/midya8/midya.ca/blob/main/src/components/GalaxyBackground.tsx)): particle layers for the stars, the spiral galaxy, and the dust, constellation lines, and a noise-shader nebula, finished with bloom post-processing. Nothing is an image asset — every element of the scene is generated at runtime.

Rendering adapts to the device instead of assuming it. A low, mid, or high profile is chosen from viewport size, device memory, CPU cores, and pixel ratio, and the profile sets the particle budgets, the bloom strength, and a 40/55/60 fps frame cap. A visitor who prefers reduced motion gets a single static frame; rendering pauses while the tab is hidden; and if WebGL is unavailable at all, a CSS gradient takes over so the page still reads. On unmount, the geometries, materials, the post-processing composer, and the WebGL context are all disposed.

All of the site's copy lives in one file, [`src/data/profile.ts`](https://github.com/midya8/midya.ca/blob/main/src/data/profile.ts). The stack is React 19, TypeScript, Vite, Three.js, and Motion, with a static build (`npm run build` produces `dist/`) deployed on DigitalOcean App Platform.

## Design decisions

- **The scene is generated, not shipped.** The stars, spiral galaxy, dust, constellation lines, and nebula haze are all produced at runtime by the code — there is no image asset to download, version, or serve, and the background can never be a broken link or a stale file.
- **Quality is a profile, chosen from the device.** Low, mid, or high is decided from viewport size, device memory, CPU cores, and pixel ratio, and the profile sets particle budgets, bloom strength, and a 40/55/60 fps frame cap. The site does not ask the visitor to find a quality setting; it reads the device and fits itself to it.
- **Reduced motion is a first-class render.** `prefers-reduced-motion` gets a single static frame of the galaxy — the identity stays, the motion goes. Accessibility here is not a toggle added later; it is one of the render paths the component was written with.
- **The page survives its own environment.** Rendering pauses while the tab is hidden, so a background tab costs nothing, and a CSS gradient takes over if WebGL is unavailable. The site degrades to something readable instead of failing to something blank.
- **Teardown is part of the feature.** Geometries, materials, the post-processing composer, and the WebGL context are disposed on unmount. A background that leaks GPU resources on every navigation is a bug, not a visual flourish, and this one is written not to have it.
- **One content file.** All copy lives in `src/data/profile.ts`, separate from the scene and the components. Updating what the site says never means touching how it renders, and the content is reviewable in one place.
- **Typed and checked before it ships.** TypeScript with `npm run typecheck` and a Vite production build mean the site is verified before it is deployed, and the static build on DigitalOcean App Platform means there is no server to keep up for a personal page.

## Worked example: updating the site's copy

Something changes — a new line of work, a rewritten introduction. The change is a text edit in one file, `src/data/profile.ts`, and the local check is the same as any other change:

```bash
npm run dev        # local dev server — read it against the live galaxy
npm run typecheck  # the copy is typed, so a mistake is a compile error, not a live typo
npm run build      # production build in dist/
```

No component was opened, no scene code was touched, and no asset was regenerated: the copy is data, the galaxy is code, and the two change on different schedules. The same separation is what makes the adaptive rendering safe to keep — the scene can be tuned for a low-end phone without ever risking the words on top of it.

## What it demonstrates

A personal site where the distinctive part — a procedural galaxy — is engineered like infrastructure: generated rather than shipped, profiled to the device rather than fixed, respectful of reduced motion, resilient when WebGL is missing, and cleaned up when it unmounts. The visual identity is the engineering, not a layer on top of it.

## Links

- Repo: [midya8/midya.ca](https://github.com/midya8/midya.ca)
- Live: [midya.ca](https://midya.ca)
