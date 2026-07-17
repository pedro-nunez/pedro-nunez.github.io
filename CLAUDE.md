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
  and activities). Has a "PDF version" button (`.button` CSS class,
  same style as AG-in-Madrid's "Add event") linking to
  `assets/cv.pdf`, generated by `scripts/export_cv_pdf.py` (see below) —
  not wired into the Jekyll build, so it's regenerated and committed by
  hand whenever `_data/cv.yml` changes.
- **`_data/cv.yml`**: all CV content (everything the CV page, Research,
  Teaching, and the travel map draw on) was consolidated from nine
  separate top-level data files (`positions.yml`, `publications.yml`,
  `talks.yml`, `activities.yml`, `teaching.yml`, `service.yml`,
  `funding.yml`, `projects.yml`, `additional-formation.yml`) into this
  one file, under `sections:`, to have a single source of truth with no
  duplicated data. Its shape follows rendercv's own YAML schema (see
  <https://docs.rendercv.com/user_guide/yaml_input_structure/cv/>), and
  it's genuinely fed to rendercv — see `scripts/export_cv_pdf.py` below.
  Top-level `name`/`location`/`email`/`website`/`social_networks`
  mirror rendercv's own top-level `cv` fields (the website itself
  doesn't use them yet); `social_networks` is a list of
  `{network, username}` pairs using rendercv's own recognized network
  names (currently just `GitHub`), rendered as icon links on the PDF's
  header line alongside location/email/website.
  `sections.education`/`experience` use rendercv's `EducationEntry`/
  `ExperienceEntry` field names (`institution`/`degree`/`area`,
  `company`/`position`, `location`, `start_date`/`end_date`);
  `sections.publications` uses `PublicationEntry` (`title`, `authors`
  as a flat list of name strings — co-author links the site used to
  show were dropped, since rendercv's `authors` doesn't support them;
  `journal`, `doi`, `date`); `sections.languages` uses `OneLineEntry`
  (`label`/`details`); every other section (`talks`, `activities`,
  `academic_visits`, `teaching_courses`, `teaching_materials`,
  `teaching_experience`, `service`, `funding`, `projects`, `extra`)
  uses the generic `NormalEntry` (`name`/`summary`/`date`/
  `start_date`/`end_date`/`location`), since rendercv has no dedicated
  entry type for talks, service, etc. `academic_visits` was split out
  of `activities` (which used to hold both conferences/workshops/
  schools and visits, distinguished by `type: visit`) into its own
  section, mirroring the education/experience split, so it has its own
  place on the CV page and in `scripts/export_cv_pdf.py`'s section
  list, between Contributed Talks and Other Academic Activities.
  `extra` is the former `additional-formation.yml` —
  renamed now that it lives under a plain key, so
  `site.data.cv.sections.extra` works directly and no longer needs the
  bracket-notation workaround (`site.data['additional-formation']`) a
  hyphenated top-level file required. `teaching_experience` is new and
  PDF-only (see below) — the website's Teaching page still reads the
  more granular `teaching_courses`/`teaching_materials`. rendercv
  ignores extra keys it doesn't recognize, so the site's own fields
  ride alongside the standard ones on each entry: `lat`/`lon` (travel
  map pins), `status` (`current`/`past`/`future`, drives map pin color
  and the Invited/Contributed or Academic Visits/Conferences split on
  the CV page), `precision: month` (used where only month/year is
  known — see `_includes/date-range.html`), `dates: [...]` (a list of
  exact meeting days for the few NCTS minicourses that didn't meet on
  consecutive days), `display_location` (preferred over `location`
  everywhere it's shown to a human — the travel map, the PDF export,
  and the CV page's Conferences section — wherever the precise
  location isn't the best label; currently just Tour de Formosa: the
  pin sits at Jinlun, one stop along the tour, but every human-facing
  view just says "Taiwan's East Coast"; `location` remains the
  fallback for entries without an override), plus per-section extras
  like `type`, `role`, `institution`, `url`,
  `online`. rendercv's template substitution crashes on non-string
  extra values (numbers, booleans), so
  `scripts/export_cv_pdf.py` strips those before handing the data to
  rendercv — string extras are silently ignored by rendercv, so those
  are left as-is.
- **`scripts/export_cv_pdf.py`**: generates `assets/cv.pdf` from
  `_data/cv.yml` via rendercv (`pip install -r scripts/requirements.txt`,
  then `python scripts/export_cv_pdf.py`; not part of `bundle exec
  jekyll serve`/build, no Ruby↔Python bridge). `_data/cv.yml` is
  written for Jekyll, so this script does the print-specific reshaping:
  picks a fixed, hand-chosen list of sections/headings and their order
  (matching the CV Pedro used before this site existed), folds the
  "Erasmus Exchange" education entry into the Bachelor's highlights
  (present as its own entry in the data/website/map, merged only for
  print), moves `summary` into the first highlight bullet for
  Education/Experience entries (adding a trailing period if missing —
  `cv.yml`'s `summary`/`note`-derived fields often omit one, relying on
  the website's Liquid templates to append it at render time, e.g.
  `{{ pos.summary }}.` in `cv.md`; the PDF has no such template-level
  punctuation, so `ensure_period()` does the same job for every summary
  surfaced as its own line — Education/Experience highlights, Talks'
  event line, Academic Visits/Conferences Attended via
  `combine_institution_into_summary()`, and Other Academic Activities),
  builds Education's `area` as "{full
  degree} in {area}" (e.g. "PhD in Mathematics") while the degree
  column itself uses `degree_abbr` when present ("MSc"/"BSc", to fit
  its narrow width — the website and map always use the full
  `degree`), italicizes the CV owner's own name in publication
  bylines, sets `design.templates.publication_entry.main_column` to
  append a period after AUTHORS and after the JOURNAL (URL) line too
  (`**TITLE**\nSUMMARY\nAUTHORS.\nJOURNAL (URL).` — template-level
  rather than `ensure_period()`, since AUTHORS is computed by rendercv
  itself, not available as a plain string beforehand; verified
  separately that rendercv still drops "(URL)." cleanly when there's
  no doi/url), maps `arxiv` → rendercv's `url` field only for
  publications that don't have a `doi` — a `doi` and `url` can't both
  show under rendercv's default template, but that's fine here since
  it's the intended behavior, not a limitation to work around: a
  published paper's entry deliberately shows just the journal and DOI,
  with the arXiv link reserved for still-unpublished preprints (Pedro
  confirmed this on 2026-07-17 after trying the alternative — showing
  both a DOI and an arXiv link on published entries — and preferring
  what was already there), formats `dates: [...]` into the "22, 27, 29
  Apr 2026" style for minicourses with non-contiguous meeting days,
  sets a custom `design.templates.normal_entry.main_column`
  (`**NAME**\nSUMMARY\nHIGHLIGHTS\nURL`) so that `NormalEntry`-based
  sections (talks, activities, service, etc.) actually show their
  `url`, which rendercv's own default template for that entry type
  omits, and replaces `start_date`/`end_date` (or a bare `date`) with a
  precomputed, day-precise `date` string via `apply_precise_dates()`
  for Invited/Contributed Talks, Academic Visits, Other Academic
  Activities, Scholarships & Funding, Conferences Attended, and
  Additional Formation — rendercv's own `single_date`/`date_range`
  templates are global (`design.templates`, shared by every entry
  type), so there's no way to make just these sections show days while
  Work Experience/Education/Teaching Experience/Research Projects stay
  at month precision other than bypassing the template entirely with a
  literal string, which rendercv uses verbatim; collapses a repeated
  month/year rather than stating it on both ends of a range ("1 – 31
  Jul 2015", "20 Jul – 9 Aug 2014", "Jan – Jun 2013"), only falling
  back to two full dates when start and end are in different years;
  respects `precision: month` per entry (e.g. Erasmus Scholarship, the
  Android courses) by omitting the day for those specifically; a
  no-op for entries whose `date` is already a free-text term (e.g. service's
  "Summer Term 2025") rather than a real date. Also
  sets `design.typography.alignment` to
  `"justified-with-no-hyphenation"` (rendercv's default hyphenates
  when justifying, which broke long location names awkwardly
  mid-syllable in the narrow date/location column, e.g.
  "Esch-sur-Alzette, Luxembourg" as "Luxem-/bourg" — this still wraps
  at existing hyphens, e.g. within "Esch-sur-Alzette" itself, just
  won't invent new break points). Course names in
  `sections.teaching_experience`'s highlights are italicized directly
  in the `cv.yml` text (`*Course Name*`) rather than in the script,
  since it's part of the actual sentence content, not a presentational
  transform.
- **`README.md`** (previously just a title) and `scripts/export_cv_pdf.py`'s
  module docstring were both written up as standalone, human-facing
  guides — the goal being that the PDF export pipeline is usable and
  understandable without needing this CLAUDE.md file or an AI
  assistant's help. README.md covers previewing the Jekyll site
  (`bundle install && bundle exec jekyll serve`) and regenerating
  `assets/cv.pdf` (venv setup, then re-running the script whenever
  `_data/cv.yml` changes); every command in it was actually run from a
  clean state to confirm it works verbatim, not just described. The
  script's docstring gained a WHAT THIS DOES / SETUP / USAGE / WHY
  EACH TRANSFORM EXISTS structure, and previously-undocumented pieces
  (`main()`, `SECTION_BUILDERS`, `build_rendercv_document()`) got
  docstrings/comments explaining the pipeline and how to extend it
  (e.g. adding a new PDF section). `_data/cv.yml`'s header comment
  gained an explicit "run `python scripts/export_cv_pdf.py` after
  editing this file" instruction, since it previously only described
  the file's shape, not what to do after changing it.
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
  `date-range.html`. Each entry reads "Date range: Title (linked, if
  `url` is set), at Institution." (the date range leads, unparenthesized
  — a deliberate departure from `cv.md`'s "Title, Institution
  (date range)." style used everywhere else on the site). Notes on the
  page invite visitors to suggest unlisted events via the "Add event"
  button (styled via a new `.button` CSS class, linking to a GitHub
  issue form, `.github/ISSUE_TEMPLATE/add-event.yml`) or by emailing
  Pedro directly (a `mailto:` link built from `site.data.cv.email`, the
  same top-level field the PDF export uses — not otherwise shown
  anywhere else on the website); submissions land as a plain issue (not
  an automated PR) and Pedro adds them to the data file by hand — kept
  deliberately simple, with fully automated issue-to-PR as a possible
  future step. Its date ranges use `date-range.html`'s new `smart`
  parameter (see below) to collapse repeated months/years, e.g.
  "21 – 25 Sep 2026", "29 Jun – 3 Jul 2026".
- **`_includes/date-range.html`** gained an optional `smart` parameter,
  off by default (so existing call sites — `cv.md`, `travel-map.md` —
  keep showing full dates on both ends of a range, unchanged) and
  currently opted into only by `algebraic-geometry-in-madrid.md`. When
  on, it collapses a repeated month/year rather than stating it on both
  ends — "1 - 31 Jul 2015", "20 Jul - 9 Aug 2014", "Jan - Jun 2013"
  with `precision: month` — falling back to two full dates when start
  and end are in different years. This mirrors
  `scripts/export_cv_pdf.py`'s `format_date_range()` for the PDF, but
  is a separate, independent implementation in Liquid rather than
  shared code — there's no mechanism for the Jekyll site and the Python
  export script to share logic, so the same date-formatting rule is
  deliberately duplicated in both places.

No known gaps remain open. (A previous revision of this file described
published papers losing their arXiv link in the PDF as a gap to fix —
see the `scripts/export_cv_pdf.py` bullet above: that's actually the
intended behavior, confirmed with Pedro, not a limitation.) All local
commits have been pushed to `origin/master`.

To resume this work in a new session, just say "continue where we left
off" — this section has the full context.
