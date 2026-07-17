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
- **Blog**: superseded by the "Algebraic Geometry in Madrid" events page
  (see Progress below) — a data-driven list rather than Jekyll posts,
  since the actual need was a curated events list, not individual
  articles.
- External profile links: MathSciNet, ORCID, Mathematics Genealogy
  Project, GitHub, LaTeX templates repository. (Done — see Progress.)

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
  `_data/cv.yml` (`site.data.cv.sections.publications`); a compact
  Papers list also on Home.
- Teaching page (`teaching.md`) reading from `_data/cv.yml`
  (`site.data.cv.sections.teaching_courses` for previous teaching and
  `.teaching_materials` for e.g. the Lean Algebra Exercises) —
  mirroring the multi-list pattern still used in `writings.yml`.
- Other writings page (`writings.md`) reading from `_data/writings.yml`
  (not CV content, so it stayed out of the `cv.yml` consolidation
  below).
- CV page (`cv.md`, at `/cv/`, linked in the nav): renders the full CV
  — work experience, research projects, publications, teaching,
  education, languages, invited/contributed talks, academic visits,
  other academic activities, funding, conferences/workshops/schools/
  courses attended, and "Additional Formation" (non-academic training
  and activities). Has a "Download PDF" button linking to
  `assets/cv.pdf`, which **does not exist yet** — Pedro needs to export
  and add that file for the link to work.
- **`_data/cv.yml`**: all CV content (everything the CV page, Research,
  Teaching, and the travel map draw on) was consolidated from nine
  separate top-level data files (`positions.yml`, `publications.yml`,
  `talks.yml`, `activities.yml`, `teaching.yml`, `service.yml`,
  `funding.yml`, `projects.yml`, `additional-formation.yml`) into this
  one file, under `sections:`, to have a single source of truth with no
  duplicated data. Its shape follows rendercv's own YAML schema (see
  <https://docs.rendercv.com/user_guide/yaml_input_structure/cv/>) —
  `sections.education`/`experience` use rendercv's `EducationEntry`/
  `ExperienceEntry` field names (`institution`/`degree`/`area`,
  `company`/`position`, `location`, `start_date`/`end_date`);
  `sections.publications` uses `PublicationEntry` (`title`, `authors`
  as a flat list of name strings — co-author links the site used to
  show were dropped, since rendercv's `authors` doesn't support them;
  `journal`, `doi`, `date`); every other section (`talks`, `activities`,
  `teaching_courses`, `teaching_materials`, `service`, `funding`,
  `projects`, `extra`) uses the generic `NormalEntry`
  (`name`/`summary`/`date`/`start_date`/`end_date`/`location`), since
  rendercv has no dedicated entry type for talks, service, etc. `extra`
  is the former `additional-formation.yml` — renamed now that it lives
  under a plain key, so `site.data.cv.sections.extra` works directly
  and no longer needs the bracket-notation workaround
  (`site.data['additional-formation']`) a hyphenated top-level file
  required. rendercv ignores extra keys it doesn't recognize, so the
  site's own fields ride alongside the standard ones on each entry:
  `lat`/`lon` (travel map pins), `status` (`current`/`past`/`future`,
  drives map pin color and the Invited/Contributed or Academic
  Visits/Conferences split on the CV page), `precision: month` (used
  where only month/year is known — see `_includes/date-range.html`),
  plus per-section extras like `type`, `role`, `institution`, `url`,
  `online`. This file isn't fed to rendercv yet (no PDF is generated
  from it) — schema alignment is preparatory, in case that becomes the
  way `assets/cv.pdf` gets produced later.
- Travel map (`travel-map.md`): interactive Leaflet map with one pin
  per unique location, built from `_data/cv.yml`'s `education`,
  `experience`, `talks`, and `activities` sections (grouped by lat/lon;
  each pin's popup lists everything that happened there). Custom SVG
  pin icons (see `pinIcon()` in `travel-map.md`): a classic
  circle-and-point marker shape (a circle with two tangent lines down
  to a tip, giving a sharp "shoulder" rather than a smooth teardrop),
  with a subtle gradient fill, a same-color border on both the pin and
  its inner white circle, and no drop shadow, sized at 75% of the pin's
  initial redesign. 4-category color legend (current affiliation / past
  affiliation / past trip / upcoming trip), with a priority order
  (upcoming, then current affiliation, then past affiliation, then past
  trip) used both to pick a pin's color when a location has several
  categories, and to keep higher-priority pins on top when they
  visually overlap. Leaflet is loaded conditionally via
  `page.extra_head == "leaflet"` in `_layouts/default.html`.
  Current/past affiliation coordinates in `_data/cv.yml`'s `education`/
  `experience` sections point at the precise department building (NTU,
  Freiburg, Bonn, LMU Munich, UCM), not just the city center; other
  trip locations still use approximate coordinates.
- Miscellanea page (`miscellanea.md`, at `/miscellanea/`, linked in the
  nav): a "Links" subsection with external profile links (MathSciNet,
  ORCID, Mathematics Genealogy Project, GitHub, LaTeX templates repo).
  The home page's "CV (coming soon)" placeholder link was removed now
  that the CV page exists and is in the nav.
- "Algebraic Geometry in Madrid" events page
  (`algebraic-geometry-in-madrid.md`, at `/algebraic-geometry-in-madrid/`,
  linked in the nav as "AG in Madrid"): a curated list of AG conferences,
  workshops, and seminars in Madrid, grouped into Upcoming/Past sections,
  backed by `_data/madrid-events.yml` (fields: `title`, `institution`,
  `start`/`end`, `status: future|past`, optional `url`), reusing
  `date-range.html`. Notes on the page clarify the list isn't guaranteed
  complete and that "algebraic geometry" is understood broadly. An "Add
  event" button (styled via a new `.button` CSS class) links to a GitHub
  issue form (`.github/ISSUE_TEMPLATE/add-event.yml`) so others can
  submit events; submissions land as a plain issue (not an automated
  PR) and Pedro adds them to the data file by hand — kept deliberately
  simple, with fully automated issue-to-PR as a possible future step.

Not yet started: `assets/cv.pdf` itself. All local commits have been
pushed to `origin/master`.

To resume this work in a new session, just say "continue where we left
off" — this section has the full context.
