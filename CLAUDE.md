# CLAUDE.md

## What this project is

The personal academic website of Pedro Núñez, a mathematician working in
algebraic geometry (currently a postdoc at National Taiwan University).
The repository starts empty; the goal is to build the site from scratch,
step by step. It replaces an old hand-written single-page site, whose
content (bio, publications, teaching, travel map locations) Pedro will
provide as each section is built.

## Tech stack and hosting

- **Jekyll**, deployed on **GitHub Pages** (let GitHub build the site;
  keep the setup compatible with GitHub Pages' build environment).
- Content in **Markdown**, templates in **Liquid**, styling in plain
  **CSS/SCSS**. Keep JavaScript to a minimum — the only planned JS
  feature is the Leaflet travel map.
- Keep dependencies minimal. Prefer a small amount of custom code over
  pulling in plugins or frameworks, unless a plugin is clearly the
  standard solution and is supported by GitHub Pages.
- This is a GitHub Pages *user site* (`username.github.io`), served at
  the domain root, so `baseurl` in `_config.yml` stays empty.

## The most important rule: this is a learning project

I have **no prior experience with Jekyll** and limited experience with web
development. The primary goal is that I understand and can maintain every
part of this site myself. Therefore:

- Work **bottom-up and step by step**. One small, self-contained step at
  a time: propose the step, explain what we are about to do and why,
  make the change, then show me how to see the result locally.
- **Never produce large amounts of code in one go.** If a feature needs a
  lot of code, split it into small increments and check in with me
  between them.
- When a Jekyll concept appears for the first time (front matter,
  layouts, includes, `_config.yml`, collections, data files, Liquid tags,
  posts vs pages, ...), pause and explain it briefly before using it.
- Prefer the simplest solution I can understand over the cleverest one.
- After each step, remind me how to preview the site
  (`bundle exec jekyll serve`) and suggest a commit with a descriptive
  message, so the git history documents the construction.
- Ask before making design decisions with lasting consequences; offer me
  options with trade-offs instead of picking silently.

## Design direction

Clean, sober academic style, taking inspiration from a mix of:
- **Astrofy** (https://github.com/manuelernestog/astrofy): modern look,
  profile/sidebar presentation.
- **academicpages** (https://github.com/academicpages/academicpages.github.io):
  classic academic structure and content organization.

We take *inspiration* from these; we are not forking them. The site must
be responsive and readable on mobile. Language: English.

## Planned structure and content

- **Home / About**: short bio (postdoc in Jungkai Alfred Chen's group at
  NTU; previously PhD with Stefan Kebekus in Freiburg), profile photo,
  link to CV (PDF), research interests (birational geometry, derived
  categories).
- **Research / Publications**: list of publications and preprints with
  arXiv and DOI links. Store these as structured data
  (e.g. `_data/publications.yml`) rather than hard-coded HTML, so adding
  a paper means editing one data file. Pedro will provide the list.
- **Teaching**: courses and seminars (content provided by Pedro).
- **Other writings**: notes and expository texts (content provided by
  Pedro).
- **Travel map**: an interactive Leaflet map of affiliations and
  conferences (current/previous affiliations, past/future events, with a
  legend), like the old site had. Locations should live in a data file
  (e.g. `_data/locations.yml`), not inside the JavaScript.
- **Blog**: announcements of algebraic geometry events in Madrid, using
  Jekyll posts.
- External profile links: MathSciNet, ORCID, Mathematics Genealogy
  Project, GitHub, LaTeX templates repository.

## Conventions

- Commit early and often; one logical step per commit.
- Comment non-obvious code, especially Liquid templates and the map JS.
- Keep file and directory names lowercase with hyphens.
