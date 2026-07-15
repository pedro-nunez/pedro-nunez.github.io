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

## Progress so far

Built, committed, step by step (see git log for the full sequence):

- Minimal Jekyll scaffold, default layout, header/nav include, basic CSS
  (default theme disabled).
- Home/About page (`index.md`) with bio, photo, research interests.
- Research/Publications page (`research.md`) reading from
  `_data/publications.yml`; a compact Papers list also on Home.
- Teaching page (`teaching.md`) reading from `_data/teaching.yml`.
- Other writings page (`writings.md`) reading from `_data/writings.yml`.
- Travel map page (`travel-map.md`): bare Leaflet map (OSM tile layer,
  centered `[20, 10]` zoom 2) with **no markers yet** — this is where we
  paused to change plans (see below). Leaflet is loaded conditionally via
  `page.extra_head == "leaflet"` in `_layouts/default.html`.

Not yet started: Blog (Jekyll posts), external profile links
(MathSciNet, ORCID, Math Genealogy, GitHub, LaTeX templates repo).
Local commits are ahead of `origin/master` and have not been pushed yet.

## In-progress plan: data-driven CV page + travel map reuse

Decided (2026-07-15): instead of just linking a static CV PDF, the CV
will be a Jekyll page rendered from data files, same pattern as
Research/Teaching/Writings. Key decisions made together:

- **PDF download**: keep a manually-exported static PDF asset (e.g.
  `assets/cv.pdf`) that gets re-uploaded whenever the CV changes
  meaningfully; the CV page just links/buttons to it. Rejected:
  print-stylesheet/`window.print()` and automated GitHub Actions PDF
  generation (both add complexity not worth it right now).
- **Data layout**: one small YAML file per CV section, matching the
  existing one-file-per-section convention — new files
  `_data/positions.yml`, `_data/talks.yml`, `_data/education.yml` — the
  CV page also reuses the *existing* `_data/publications.yml` and
  `_data/teaching.yml` rather than duplicating them.
- **Map data reuse**: `_data/positions.yml` and `_data/talks.yml`
  entries include `lat`/`lon` fields (even though the CV page itself
  won't display them). The travel map reads markers straight out of
  those two files instead of a separate `_data/locations.yml`, so
  location data is entered once. Entries without `lat`/`lon` are simply
  skipped by the map. Legend/marker styling should distinguish
  category (affiliation vs. talk/conference) and status (current/past,
  and future for talks).

### Next steps, in order

1. Create `_data/positions.yml` (one entry per academic position: role,
   note, institution, city, lat, lon, start, end, status
   current/past, url). A first draft was proposed (NTU postdoc,
   Freiburg PhD, Bonn — dates/roles need Pedro to confirm/fill in) but
   was **not yet saved** when we paused — recreate and fill it in first.
2. Create `_data/talks.yml` (conferences/talks, same idea, with
   `lat`/`lon`, and a status of past/future).
3. Create `_data/education.yml` if needed for CV entries not covered by
   positions (e.g. degrees without a lat/lon-worthy "position").
4. Build the CV page (e.g. `cv.md`) that reads positions, education,
   talks, and reuses publications/teaching data; add the "Download PDF"
   button linking to the static asset.
5. Wire up `travel-map.md`: loop over `site.data.positions` and
   `site.data.talks`, add markers with popups, and a legend (current
   affiliation / past affiliation / past talk / future talk).

To resume this work in a new session, just say "continue where we left
off" — this section has the full context.
