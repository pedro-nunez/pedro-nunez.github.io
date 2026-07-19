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
  **CSS/SCSS**. Keep JavaScript to a minimum — besides the Leaflet
  travel map, the only other JS is the small light/dark theme toggle
  and (planned) the mobile nav hamburger menu (see Progress below).
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
  articles. That page has since moved out to its own repository
  (`pedro-nunez/ag-in-madrid`, see Progress), so this site's own nav
  just links to it externally now.
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
- Home/About page (`index.md`) with bio, photo, research interests, and
  the email link right under the name (same obfuscated-display style
  as the Contact page: `pnunez [at] ntu.edu.tw`, hardcoded rather than
  read from `_data/cv.yml`, matching how Contact does it too). The bio
  prose links Jungkai Alfred Chen and Stefan Kebekus to their
  homepages directly (plain HTML `<a>`, since this text is hardcoded
  here, not sourced from `cv.yml`).
- **Linking specific people's names mentioned in `_data/cv.yml`'s free
  text** (advisors, hosts, co-organizers, PIs — as opposed to
  publication co-authors or `writings.yml` organizers, which already
  have their own structured `{name, url}` fields): done via Liquid's
  `replace` filter directly in `cv.md`'s template
  (`{{ item.summary | replace: "Name", '<a href="...">Name</a>' }}`),
  never by editing the `cv.yml` string itself. The same `summary`
  fields feed `scripts/export_cv_pdf.py`, which has no equivalent
  replace step, so the PDF always shows these names as plain text —
  matching Pedro's preference (confirmed twice: co-author links, then
  these) that people-links belong on the website only, never the PDF.
  A `replace` is a no-op when its target string isn't present, so it's
  safe to chain onto every relevant section's summary output rather
  than conditioning on which specific entry contains the name. Currently
  linked this way: Jungkai Alfred Chen and Stefan Kebekus (Work
  Experience, Research Projects, Education), Meng Chen (Academic
  Visits), Flora Poon and Hsueh-Yung Lin (Other Academic Activities).
  Explicitly left unlinked at Pedro's request: Yujiro Kawamata and
  Keiji Oguiso (NCTS minicourse lecturers, in Conferences Attended).
- Research/Publications page (`research.md`) reading from
  `_data/cv.yml` (`site.data.cv.sections.publications`); a compact
  Papers list also on Home. Its "PhD, master's and bachelor's theses"
  section is hardcoded HTML (not data-driven, unlike the rest of the
  page) with each thesis title now linking its PDF under
  `assets/pdfs/`.
- Teaching page (`teaching.md`) reading from `_data/cv.yml`
  (`site.data.cv.sections.teaching_courses` for previous teaching and
  `.teaching_materials` for e.g. the Lean Algebra Exercises) —
  mirroring the multi-list pattern still used in `writings.yml`. Its
  "teaching statement" link (previously a "coming soon" placeholder)
  now points at `assets/pdfs/teaching-statement.pdf`.
- Other writings page (`writings.md`) reading from `_data/writings.yml`
  (not CV content, so it stayed out of the `cv.yml` consolidation
  below). Each `seminar_scripts`/`other_notes` entry has a `url`
  linking its own PDF under `assets/pdfs/`; the one `other_notes`
  entry ("Enumerative Geometry") additionally has `programme_url` for
  a second, separate PDF (the seminar's programme) — the only entry
  with two documents, so this got its own field rather than a general
  "list of PDFs per entry" mechanism nothing else currently needs.
- **`assets/pdfs/`**: holds every PDF on the site (theses, seminar
  scripts/notes, the teaching statement, and `cv.pdf`) — a
  subdirectory alongside the pre-existing `assets/css/`/`assets/images/`
  convention. `cv.pdf` briefly stayed directly under `assets/` (from
  before this convention existed, when moving it would have been a
  gratuitous unrelated change) but was folded in once Pedro asked for
  it explicitly; `scripts/export_cv_pdf.py`'s `OUTPUT_PDF` constant
  and `cv.md`'s "PDF version" button both point at
  `assets/pdfs/cv.pdf` now.
- CV page (`cv.md`, at `/cv/`, linked in the nav): renders the full CV
  — work experience, research projects, publications, teaching,
  education, languages, invited/contributed talks, academic visits,
  other academic activities, funding, conferences/workshops/schools/
  courses attended, and "Additional Formation" (non-academic training
  and activities). Has a "PDF version" button (`.button` CSS class,
  same style as AG-in-Madrid's "Add event") linking to
  `assets/pdfs/cv.pdf`, generated by `scripts/export_cv_pdf.py` (see
  below) — not wired into the Jekyll build, so it's regenerated and
  committed by hand whenever `_data/cv.yml` changes.
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
  as a list of `{name, url}` objects rather than rendercv's own flat
  list-of-strings shape — `url` is optional and lets the website link
  each co-author to their homepage (`_includes/author-list.html`);
  rendercv's own `authors` field doesn't support per-author links, so
  `scripts/export_cv_pdf.py` reduces each entry to just its `name` for
  the PDF, which was in fact the reason this was flattened to plain
  strings in an earlier revision of `cv.yml`, before Pedro asked for
  the links back on the website specifically; `journal`, `doi`,
  `date`); `sections.languages` uses `OneLineEntry`
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
- **`scripts/export_cv_pdf.py`**: generates `assets/pdfs/cv.pdf` from
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
  `assets/pdfs/cv.pdf` (venv setup, then re-running the script whenever
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
  trip locations still use approximate coordinates. An attribution
  note (crediting Julia Schneider for the idea and Claude for helping
  implement it) appears once, right below the legend.
- Miscellanea page (`miscellanea.md`, at `/miscellanea/`, linked in the
  nav): two plain Markdown-list sections, in order — "Workflow" (the
  LaTeX templates repo) and "Links" (external profile links:
  MathSciNet, ORCID, Mathematics Genealogy Project, GitHub). LaTeX
  templates used to live under Links before Workflow was split out. A
  "Lean" section briefly existed too (for the Lean Algebra Exercises
  repo) but was removed as redundant with `cv.yml`'s
  `teaching_materials`, which already lists it (shown on the Teaching
  and CV pages).
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
- Contact page (`contact.md`, at `/contact/`, linked in the nav as the
  last item): plain HTML content (matching `teaching.md`'s
  `<h1>`/`<h2>` style rather than Markdown `#`/`##`, since that's the
  more common pattern across the site's pages) with three sections —
  Email (a `mailto:` link, display text obfuscated as "pnunez [at]
  ntu.edu.tw" to deter scrapers), Address, and Office — hardcoded
  directly in the page rather than sourced from `_data/cv.yml`, since
  none of this (a physical mailing address, an office room number)
  belongs in a rendered CV.
- **First step of the "distinguish link types with CSS classes" idea**
  (see below): two classes so far, `cv-page-link` and `person-link`,
  both currently styled identically (plain text, underline only on
  hover — the shared `.cv-page-link, .person-link` rule in
  `assets/css/main.css`). `cv-page-link` is page-scoped, not
  link-kind-scoped: it goes on *every* in-text link on `cv.md`
  (person names via the `replace` filter, institution/talk/funding/
  activity URLs, DOI/arXiv links, the teaching course link), except
  the "PDF version" button, which keeps only its existing `.button`
  class (a UI action, not a content link) — confirmed with Pedro, who
  also confirmed the nav bar's `/cv/` entry in `header.html` stays
  unclassed, since `cv-page-link` is about links living in the CV
  page's content, not links pointing at it. `person-link` is the
  complementary link-kind class for links to a person's homepage
  everywhere *other* than `cv.md`: the bio prose on `index.md`
  (Jungkai Alfred Chen, Stefan Kebekus), the thesis supervisors on
  `research.md`, the seminar organizer on `writings.md`, and the
  Julia Schneider *and* Claude credits on `travel-map.md` (Claude
  started out classed as `external-link` when this class was first
  introduced, on the reasoning that it isn't a person's homepage, but
  Pedro later asked for it to be `person-link` too, alongside Julia
  Schneider).
  `_includes/author-list.html` (paper co-author links, shared by
  `cv.md`, `research.md`, and `index.md`) gained an optional
  `link_class` include parameter so each call site can pass the right
  class (`cv-page-link` on `cv.md`, `person-link` on the other two).
  This also let `main.css`'s old `.papers-list a:not(.paper-title)`
  rule (index.md's co-author links specifically) be folded into the
  new shared `person-link` rule instead of duplicating it.
- **Rest of the link-CSS-classes idea's class-adding phase**: six more
  classes added across the site, HTML/Liquid only and deliberately with
  no CSS yet — Pedro is writing the actual per-class styles himself.
  `mailto-link`: `index.md`, `contact.md`, and the "email" link on
  `algebraic-geometry-in-madrid.md` (the latter via kramdown's
  `{: .mailto-link }` inline attribute list syntax, the same mechanism
  already used for `{: .profile-photo }` on index.md's photo, since
  that link is written as Markdown, not raw HTML). `paper-link`: a
  new class, deliberately kept separate from the pre-existing
  `paper-title` (which stays exactly as it was — still only
  `index.md`'s italicized paper-title links, still styled the same
  way); `paper-link` instead tags the plain "DOI:.../arXiv:..." text
  links on `research.md` — same underlying purpose (a link to one of
  Pedro's own papers) but a visually different pattern, so two classes
  rather than one. `pdf-link`: links to Pedro's own PDFs under
  `assets/pdfs/` outside `cv.md` — the thesis titles on `research.md`,
  the teaching statement on `teaching.md`, and every
  `writings.yml` entry's `url`/`programme_url` on `writings.md`.
  `event-link`: links to a conference/workshop/seminar's own external
  homepage outside `cv.md` — `algebraic-geometry-in-madrid.md`'s
  `event.url` entries, and the activity `url` built into
  `travel-map.md`'s JS-generated popups (the "activity-link" vs.
  "event-link" naming question from the candidate list was resolved
  by merging into just `event-link`, since no second distinct kind of
  link was actually found in the code). `teaching-course-link`:
  `teaching.md`'s `course.url` and `teaching_materials` `url` (course/
  material homepage links; `cv.md`'s own version of these is already
  `cv-page-link`). `external-link`: catch-all for the rest —
  `miscellanea.md`'s four profile/workflow links. Deliberately left
  out of this pass: the nav bar
  (`header.html`), since Pedro wants to handle it as part of the
  future "general aesthetic pass" rather than this content-link
  classification, and Leaflet's OpenStreetMap attribution link on
  `travel-map.md`, left unstyled as third-party boilerplate.
- **Actual styling for all the link classes above**, a homogeneous
  two-color scheme Pedro specified directly (not delegated): a shared
  rule in `main.css` gives `mailto-link`, `paper-title`, `paper-link`,
  `pdf-link`, `event-link`, `teaching-course-link`, and `external-link`
  the same maroon (`#7b1e3a`, the color already used for `paper-title`
  and `.button`), underlined only on hover; `paper-title` keeps its own
  separate italic rule on top, since that's specific to it, not shared
  by the other six. `cv-page-link`/`person-link` keep their
  pre-existing inherited-color, underline-only-on-hover rule, unchanged.
  So exactly two visual treatments cover every classified link on the
  site right now, one per class group. Every one of these classes (plus
  `.button`) also gained an explicit `:visited` rule repeating the same
  color, so a link's look never changes just because it's been clicked
  — relying on the ordinary cascade (an author stylesheet already beats
  the browser's default blue/purple `:link`/`:visited` colors) would
  have worked too, but Pedro asked for this to be explicit in the CSS
  rather than implicit.
- **Claude credit on `travel-map.md` reclassified from `external-link`
  to `person-link`** (see the `person-link` bullet above) — a small
  correction after seeing it rendered.
- **`writings.md`'s "Enumerative Geometry" entry** (the one
  `other_notes` entry with a `programme_url`) now reads as two
  sentences instead of one: "*Enumerative Geometry*, notes for a
  seminar that I organized at the University of Freiburg (WS 20/21).
  See programme." — the main sentence always ends with its own period
  now, and, only when `programme_url` is set, a second sentence ("See
  programme.", with "programme" linked as `pdf-link`) follows. Entries
  without a `programme_url` are unaffected (still just the one
  sentence).
- **Light/dark theme system** (first step of the "general aesthetic
  pass" idea below — nav layout is the second step, in progress):
  every color in `main.css` is now a CSS custom property on `:root`
  (`--bg-color`, `--text-color`, `--accent-color`,
  `--accent-color-hover`, `--button-text-color`), so light vs. dark is
  just two blocks overriding those variables rather than two copies of
  every rule. Light (the default, unchanged from before): white
  background, black text, the same maroon accent as always. Dark (new):
  `#1a1a1a` background, off-white `#e8e8e8` text, and goldenrod
  `#daa520` replacing maroon as the accent everywhere it was used
  (link classes, `.button`), with `.button`'s text switching to dark
  (`#1a1a1a`) instead of white to keep it readable against the lighter
  goldenrod background; `cv-page-link`/`person-link` need no dark-mode
  change since they already use `color: inherit`. Which theme applies,
  in priority order: a manual choice stored in `localStorage` (via
  a `data-theme="light"`/`"dark"` attribute Pedro's browser sets on
  `<html>`) beats the OS/browser's `prefers-color-scheme`, which beats
  the light defaults if neither of the above says otherwise. A tiny
  inline script in `_layouts/default.html`'s `<head>` (must stay
  inline, not moved to a file, so it runs before first paint) applies
  any stored choice immediately, preventing a flash of the wrong theme
  on repeat visits; `assets/js/theme-toggle.js` (new — first
  hand-written JS on the site besides the travel map) handles clicking
  the toggle button and keeps its icon (🌙 in light mode, ☀️ in dark —
  always showing the theme a click would switch *to*) in sync. The
  toggle button itself (`#theme-toggle` in `header.html`) is a
  placeholder in its current spot for now; the nav-layout step below
  will move it to its real position (top-right on desktop, top bar on
  mobile).
- **Responsive nav layout** (second step of the "general aesthetic
  pass," and the toggle button's permanent home): `header.html` now
  has three pieces — a `.topbar` div (hamburger button + site name,
  mobile-only), the always-visible `#theme-toggle` button (now
  `position: fixed; top; right`, so it stays in the same page corner
  whether or not `.topbar` is shown), and, as a sibling outside
  `<header>`, `#site-nav` (the actual link list) plus `#nav-backdrop`
  (an overlay, only relevant on mobile). Desktop (the default; no
  media query needed): `#site-nav` is a persistent `position: fixed`
  left sidebar (nav links only, per Pedro's call earlier — no name or
  photo), and `body` gets `margin-left: 12rem` to make room for it;
  `.topbar` stays `display: none`, so no hamburger or centered name
  appear. Below the `768px` breakpoint (`@media (max-width: 768px)`,
  chosen as an ordinary phone/small-tablet cutoff, easy to adjust):
  `.topbar` becomes a `position: fixed` full-width bar at the very top
  (hamburger absolutely-positioned at its left so it doesn't disturb
  the centering, site name centered via the topbar's own
  `justify-content: center` since the hamburger is out of flow);
  `#site-nav` becomes an off-canvas drawer (`transform: translateX(-100%)`
  by default, slid in via a `.open` class) instead of a persistent
  sidebar, and `body` swaps back to `margin-left: 0` with extra
  `padding-top` to clear the fixed topbar. `assets/js/nav-toggle.js`
  (new) wires the hamburger click to add/remove `.open` on `#site-nav`
  and show/hide `#nav-backdrop`; clicking the backdrop or pressing
  Escape also closes the drawer. Verified in a real browser: desktop
  sidebar, light/dark toggle in both layouts, and the mobile topbar +
  drawer open/close/backdrop-close mechanics — the last of these
  was checked by temporarily forcing the mobile CSS rules on
  (window-resize automation wasn't available in that session), not by
  an actual narrow-viewport resize, so Pedro should still give the real
  breakpoint a look on an actual phone or by resizing a desktop browser
  window. Confirmed working on Pedro's own phone afterward.
- **Font/size/alignment pass** (third and, per Pedro, final step of the
  "general aesthetic pass" — sizes themselves needed no changes).
  Typeface: **Source Sans 3**, matching `scripts/export_cv_pdf.py`'s
  PDF export, which already uses it as rendercv's default body font
  without overriding it — so the website and the PDF CV now share a
  typeface without either file referencing the other. Loaded via a
  Google Fonts `<link>` in `_layouts/default.html`'s `<head>`
  (preconnect hints + the stylesheet link), applied as
  `"Source Sans 3", sans-serif` on `body` in `main.css` (the
  `sans-serif` fallback covers the rare case the Google Fonts request
  fails). Alignment: a new global `h1 { text-align: center; }` rule
  centers every page's title (all pages use exactly one `<h1>` for
  this, so one rule covers the whole site); `.profile-photo` gained
  `display: block; margin: 0 auto;` to center the home page's photo
  the same way its `<h1>` name is now centered. Everything else
  (body text, `<h2>`s, lists) stays left-aligned, per Pedro's
  instruction that "the rest of the text can remain how it is now."
  Margins/centering: introduced a `.page-wrap`/`.page-content` wrapper
  around `{{ content }}` in `default.html` (previously these box-model
  concerns — padding, `max-width`, the sidebar-clearing margin — all
  lived directly on `body`, which also carries the background/text
  color/font and can't simultaneously be centered *within* the space
  right of the fixed sidebar using plain margins). `.page-wrap` clears
  the sidebar (`margin-left: 12rem` on desktop, `0` + `padding-top` for
  the fixed topbar on mobile, mirroring the breakpoint logic `body`
  used to carry) and is a flex row with `justify-content: center`;
  `.page-content` is the actual `max-width: 60rem` box with more
  generous padding (`2rem 3rem` desktop, `1.5rem 1.25rem` mobile) than
  the old flat `1rem`. The net effect: on desktop the textbox is
  centered in the space to the *right* of the sidebar, not in the full
  browser window (which would look off-center relative to the
  sidebar) — exactly what Pedro asked for.

- **Sidebar/page background contrast**: introduced a new
  `--sidebar-bg-color` CSS variable, distinct from `--bg-color`, so
  `.site-nav` and the mobile `.topbar` can differ from the page
  background instead of matching it exactly (previously both used
  `--bg-color`). Light theme: page `#f0f0f1` (a light gray, replacing
  the original plain white), sidebar/topbar `#e4e4e6` (a shade darker)
  — matching a reference screenshot Pedro provided. Dark theme:
  sidebar/topbar `#262626`, a shade *lighter* than the page's
  `#1a1a1a` — the opposite direction from light mode, since a sidebar
  needs to visually separate itself by going darker on a light page
  but lighter on a dark one.
- **Fixed the travel map covering the mobile nav drawer**: Leaflet's
  own internal panes and controls use `z-index` values up to 1000, far
  above the mobile drawer's `z-index: 25`, and `#map` had no stacking
  context of its own, so those Leaflet elements could escape above the
  open drawer instead of sitting behind it. Fixed by giving `#map`
  `position: relative; z-index: 0`, which contains all of Leaflet's
  internal z-indices regardless of what the library uses internally.
  Verified by reproducing the bug (injecting a test element at the
  drawer's own z-index and confirming the map covered it) before the
  fix and confirming the reverse after — real mobile-viewport testing
  wasn't available in this session (see below), so this was the
  substitute verification method.
- **Base font size**: `body` had no `font-size` of its own, so text
  rendered at the browser default (16px). Bumped to `1.125rem` (18px),
  matching Astrofy's own body-copy size (its `text-lg` utility class)
  — confirmed by reading Astrofy's own source
  (`src/pages/index.astro`, `src/components/SideBarMenu.astro`) rather
  than guessing. `.site-nav` has no `font-size` rule of its own
  either, so nav links already inherited this new size too; kept
  deliberately equal to the body text rather than mirroring Astrofy's
  own choice of a slightly smaller nav (`text-base`, 16px) — Pedro
  considered the gap and preferred equal sizing.
- **Text column width**: `.page-content`'s `max-width` (introduced in
  the font/size/alignment pass above at `60rem`) was reduced to
  `45rem` (720px) — it read too wide on a full-size desktop window;
  the new value was chosen to be close to how the column already
  looked on a half-screen-sized window.
- **Theme toggle redesign**: replaced the 🌙/☀️ emoji (fixed-color,
  always a yellow sun regardless of theme) with inline SVG icons — a
  solid circle-with-rays sun and a solid crescent moon, both drawn
  with `fill="currentColor"` so they pick up the button's own color
  instead of emoji's built-in one. Button color is an explicit muted
  gray (`#888`, same in both themes, not tied to `--text-color` or
  `--accent-color`), and the button's `border` was dropped for a
  plainer look. Icon size went through one iteration: `18px` read too
  small, settled on `24px`. Also added a hover tooltip: `title` (and
  `aria-label`, previously a static, mismatched "Toggle dark mode")
  now reads "Switch to light theme"/"Switch to dark theme" depending
  on which way a click would go, mirroring the icon's own logic — the
  native browser tooltip positions itself near the cursor
  automatically, the same mechanism Chrome's own UI tooltips use, so
  no custom positioning code was needed.
- **Mobile theme-toggle alignment fix**: it used a hardcoded
  `top: 0.55rem` guess instead of true vertical centering, so it sat
  slightly off from `.nav-toggle` (the hamburger), which centers
  itself properly via `top: 50%` + `transform: translateY(-50%)`
  against the `.topbar`'s `3rem` height. Applied the same technique —
  since `.theme-toggle` is a *sibling* of `.topbar`, not a child, and
  is itself `position: fixed` (so a plain `top: 50%` would resolve
  against the full viewport, not the topbar), the fix instead
  hardcodes `top: 1.5rem` (half of the topbar's own `3rem` height)
  plus `transform: translateY(-50%)`. Horizontal spacing needed no
  change — both buttons already sit `0.75rem` from their respective
  screen edge. This fix lives inside the existing
  `@media (max-width: 768px)` block, so — like the rest of the mobile
  layout — it's scoped to viewport width, not to actual phone
  hardware; shrinking a desktop browser window below `768px` hits the
  identical rule, which is how it was actually tested in this session:
  real mobile-viewport screenshots aren't available in this
  environment (window-resize calls don't reliably affect the
  screenshot tool's capture viewport), so a narrowed dev-server browser
  window stood in, later confirmed for real by Pedro on his phone.
- **Section title spacing**: added `h2 { margin-top: 2.5rem; }` for
  clearer visual separation between a page's sections. This followed a
  design discussion where Pedro asked about also centering `<h2>`s (to
  match the already-centered `<h1>`); the recommendation was to keep
  section titles left-aligned (matching the left-aligned body
  text/lists under them, and preserving the `<h1>` as each page's one
  deliberate focal point) and reach for spacing instead — Pedro
  agreed.
- **Nav link hover/active shading**: `.site-nav` links now get a
  background shade on hover, and a subtler one permanently on
  whichever link matches the current page — mirroring Astrofy's own
  sidebar menu behavior (which uses DaisyUI's `bg-base-300`-style
  active class, applied by matching an element ID in a small
  client-side script). Implemented instead as two new CSS variables,
  `--nav-active-bg`/`--nav-hover-bg`, layered on top of
  `--sidebar-bg-color`: a black overlay in light mode
  (`rgba(0,0,0,...)`, darkens) and a white one in dark mode
  (`rgba(255,255,255,...)`, lightens), since a light sidebar needs to
  shade darker but an already-dark one needs to shade lighter.
  Active-page detection itself was done directly in `header.html` via
  Liquid (`{% if page.url == '...' %}` per nav link) rather than
  Astrofy's client-side script, since Jekyll already knows the current
  page at build time — keeping with the project's "minimal JS"
  preference. This replaced the previous underline-on-hover behavior
  specifically for `.site-nav a` (every other link-kind class
  elsewhere on the site is untouched). `.site-nav a` also gained
  `padding: 0.4rem 0.6rem` and `border-radius: 0.3rem` so the shaded
  rectangle reads as an intentional pill/bar rather than hugging the
  link text tightly.
- **Research page**: swapped the order of the two research-interest
  bullets (semiorthogonal decompositions now listed first, then
  Campana's program) — content-only change, doesn't touch
  `index.md`'s separate, general "birational geometry and derived
  categories" prose sentence.

- **`_config.yml` now excludes `CLAUDE.md` from the Jekyll build.**
  GitHub Pages' `jekyll-optional-front-matter` plugin runs *every*
  Markdown file through Liquid regardless of whether it has front
  matter, so the previous CLAUDE.md update — which documented a
  Liquid snippet from `header.html` in plain prose
  (`` `{% if page.url == '/' %}` ``) — broke the live build: the
  snippet isn't real template code and isn't balanced/closed, and
  Jekyll's Liquid parser doesn't know that. GitHub Pages kept serving
  the last successful deploy, so nothing was actually down, but no
  further pushes would have deployed until this was fixed. Setting
  `exclude` in `_config.yml` *replaces* Jekyll's own default exclude
  list rather than merging with it — confirmed locally that omitting
  the defaults makes Jekyll try to read the Ruby gems under
  `vendor/bundle/` as site content — so the usual defaults (`Gemfile`,
  `vendor/bundle/`, etc.) are listed alongside `CLAUDE.md` explicitly.
  Caught by actually building locally (`bundle exec jekyll build`)
  after the CLAUDE.md edit, then confirmed against the real failure
  via `gh run list`/`gh run view --log-failed` — worth doing both
  after any CLAUDE.md edit that quotes Liquid syntax, and worth
  checking `gh run list` after any push in general, since GitHub Pages
  silently keeps serving the last good build on failure rather than
  erroring visibly anywhere else.
- **Travel map**: `#map-legend` gained `justify-content: center` (it
  was already a flex row, just left-aligned), and its font-size was
  set explicitly — tried `12px` first, too small per Pedro, settled on
  `14px` — with the legend dots switched from `rem` to `em` units so
  they keep scaling proportionally with whatever the legend's own
  font-size ends up being, rather than staying a fixed absolute size
  next to shrinking text.
- **Fixed the travel map showing gray bands above/below on mobile**:
  `fitBounds` has to zoom out far to fit the wide Mexico-to-Taiwan
  longitude spread into a narrow mobile width, and at zoom 0 or 1 the
  world map's rendered height (256/512px) can end up shorter than
  `#map`'s fixed 400px height — Mercator doesn't wrap vertically, so
  that shows as gray. Worse than the total-height math alone suggests,
  because the marker cluster's latitude centroid sits off-center (all
  points are north of the equator), so even zoom 1 could still clip
  the top specifically. Fixed by flooring the zoom at 2
  (`L.map('map', { minZoom: 2 })`) on screens `<=768px` (mirroring the
  breakpoint the nav already uses) — left alone on wider screens,
  where `fitBounds` already picks a high enough zoom on its own and
  flooring it there would just needlessly crop pins (confirmed via
  `map.getBoundsZoom()`: natural zoom is already 1 at a 600–700px
  desktop-ish width, 2 at 800px+). Verified by forcing the map's
  container width down via JS (`document.getElementById('map').style
  .width = ...` + `map.invalidateSize()`) and reading
  `map.getZoom()`/`map.getSize()` directly, since real narrow-viewport
  browser testing isn't reliably available in this environment (see
  below).
- **Mobile top spacing above page titles**, tightened in two passes.
  First: `h1`'s own default browser `margin-top` (~24px, from its
  ~36px font-size) was redundant on top of `.page-content`'s own
  top padding, so zeroed it out on mobile specifically — cut the
  topbar-to-title gap from 64px to 40px. Second pass, after Pedro
  asked for still more: `.page-wrap`'s extra clearance above the
  topbar (`padding-top: 4rem`, vs the topbar's own `3rem`) trimmed to
  `3.5rem`, and `.page-content`'s top/bottom padding from `1.5rem` to
  `1rem` — down to 24px. Both passes measured the same way: since real
  narrow-viewport reloads aren't reliably available in this
  environment (`resize_window` doesn't reliably narrow the tab's
  actual rendered viewport here — `window.innerWidth` stays at the
  desktop value even after a resize call reports success), the mobile
  `@media (max-width: 768px)` rules were injected unconditionally via
  a temporary `<style>` tag (copied verbatim from `main.css`, not
  hand-picked properties — an early attempt that cherry-picked just
  `.topbar`'s `display` missed its `height`/`position` and gave a
  bogus measurement), then `getBoundingClientRect()` read directly on
  `.topbar` and `h1` to compute the real pixel gap.
- **Mobile body font-size** dropped from 18px (the size chosen for
  desktop) back to 16px, scoped inside the same mobile media query —
  reads better at typical phone viewing distance/density than the
  size chosen for desktop.
- **Persistent name header atop the desktop sidebar**, added after
  Pedro asked for *some* way to keep his name visible on wide screens
  while browsing any page, not just Home (the sidebar was nav-links
  only, no name/photo, per his own earlier call — see the responsive
  nav layout bullet above). Astrofy's own sidebar was checked directly
  for inspiration (`SideBar.astro`): it has a circular profile photo
  linking home above its nav menu, but no name text. Landed on a
  text-only header after Pedro picked it over a photo+name variant or
  a full-width top bar, from three options offered. Went through two
  more rounds of revision from there, both from direct visual
  feedback rather than getting it right the first time:
  1. First cut: the name was a clickable link (reusing `.site-name`),
     right-aligned by default, with the divider below it living on
     the link's own `border-bottom` + `padding-bottom`. Pedro found
     the divider "too obvious/disruptive" (it read as part of the
     button's own box) and asked for centering.
  2. Second cut: centered the text (`text-align: center`), and pulled
     the divider out into its own standalone `<hr class="sidebar-
     divider">` between the name and the nav links, so the line sits
     between two elements rather than inside either one's clickable
     box/hover-highlight — this also meant the name's own `.site-nav
     a` padding/border-radius overrides no longer needed the extra
     `.site-nav` prefix for specificity (nothing left to out-specify).
     Pedro then asked to go further: make the name link *replace* the
     "Home" nav entry entirely, since both went to the same place.
     Implemented via a `{% if page.url == '/' %}` active class
     directly on the name link, `<hr>` hidden on mobile at matching
     specificity (`.sidebar-name`/`.sidebar-divider { display: none }`
     — the *first* mobile-hide attempt used `.site-nav .sidebar-name`
     to out-specify the old always-linked desktop rule, but once the
     desktop rule stopped needing that extra specificity, the mobile
     rule had to drop it too or it would win by specificity regardless
     of source order and the hide would silently never apply).
  3. Third cut, after Pedro reconsidered: not convinced by a clickable
     name replacing Home after all. Reverted to a plain, non-clickable
     `<div>` (not an `<a>`) for the name, and restored "Home" as its
     own regular nav link below the divider. Landed here: `.sidebar-
     name` is inert text, centered, `.sidebar-divider` a subtle
     standalone rule (`border-top: 1px solid var(--nav-hover-bg)`,
     reusing the nav-shading overlay variable rather than a solid
     `var(--text-color)` line, which read as too heavy), Home restored
     as a normal link. Both hidden on mobile, where `.topbar` already
     shows the name.
- **Home page**: dropped the email `mailto:` link entirely (Contact
  page still has its own, unaffected — this was scoped to Home only).
  AG in Madrid page: dropped its own `mailto:` link too, but restored
  "or by sending me an email" immediately after as Pedro asked for the
  phrase back with "email" left as plain, unlinked text — a content
  preference, not an oversight to fix.
- **`.button` (the "PDF version"/"Add event" buttons)**: centered
  first (`display: block; width: fit-content; margin: 0 auto` on the
  class itself, rather than adding a wrapper class to both
  `cv.md`/`algebraic-geometry-in-madrid.md`, since `.button` is only
  ever the sole content of its own paragraph in both places), then
  redesigned from solid-fill to outline style after Pedro found the
  solid block "too intrusive": transparent background, accent-colored
  border and text (matching the site's other links) instead of a
  solid `--accent-color` fill with `--button-text-color` text, filling
  solid only on hover (reusing `--accent-color-hover` for the hover
  fill, so that variable stayed in use rather than going orphaned).
  Also shrunk twice at Pedro's request — padding, border-radius, and
  font-size (`0.9em`) all reduced — after a first smaller pass still
  read as too large.

- **Info popup on the AG in Madrid page's title**: a small circled-i
  (`&#9432;`) button next to the `<h1>`, styled like the info icons
  Google Sites shows, revealing the page's explanatory text (previously
  always-visible prose above the "Add event" button) in a click-to-open
  popup instead — kept the title area more compact while "Add event"
  stays visible underneath. `.info-toggle-wrap`/`.info-toggle`/
  `.info-popup` in `main.css` (theme-aware, matching the site's existing
  light/dark variables) plus a new `assets/js/info-toggle.js` (toggles
  the popup, closes on outside click or Escape — same pattern as
  `nav-toggle.js`). Short-lived in this repo: superseded almost
  immediately by the full page migration below, which took this feature
  with it.
- **"Algebraic Geometry in Madrid" moved to its own repository**,
  `pedro-nunez/ag-in-madrid` (completing the "To do" item that used to
  be listed here), deployed as its own GitHub Pages *project* site at
  `pedro-nunez.github.io/ag-in-madrid/` (`baseurl: "/ag-in-madrid"` in
  its own `_config.yml`, unlike this repo's user site with an empty
  `baseurl`). The new repo is a standalone Jekyll site with no shared
  build step with this one, so everything it needs was copied rather
  than referenced: `_data/madrid-events.yml`, `_includes/date-range.html`,
  the `.github/ISSUE_TEMPLATE/add-event.yml` issue form (now pointing
  "Add event" at `pedro-nunez/ag-in-madrid`'s own issue tracker instead
  of this repo's), and a *trimmed* copy of `main.css` (and
  `theme-toggle.js`/`info-toggle.js` verbatim) — same color
  variables/light-dark logic, fonts, and sizes, but only the rules that
  single page actually uses, since it has no sidebar/nav of its own.
  Its `_layouts/default.html` replaces this site's nav entirely with two
  fixed corner elements: a "Pedro Núñez" link (top-left, plain text
  styled like `.site-name`, linking back to
  `https://pedro-nunez.github.io/`) and the same theme-toggle button
  (top-right) — no hamburger/drawer needed since there's no nav menu to
  toggle, so none of this site's responsive nav-layout CSS/JS had to be
  ported over. Both sites share an origin, so a theme choice made on
  either one carries over to the other via `localStorage` automatically,
  with no extra code. Back in this repo: the internal page
  (`algebraic-geometry-in-madrid.md`), its data file, its issue
  template, `assets/js/info-toggle.js`, and the `.info-toggle`/
  `.info-popup` CSS rules were all deleted (the page's content and that
  feature only exist in the new repo now); `header.html`'s "AG in
  Madrid" nav link now points straight at
  `https://pedro-nunez.github.io/ag-in-madrid/` instead of an internal
  permalink, dropping the now-meaningless "active page" check along with
  it (an external link can't match `page.url`). `.event-link` stayed in
  this repo's `main.css`, unlike the other AG-in-Madrid-specific
  classes, since the travel map's JS-generated popups also use it.

- **"Last updated" bar**, resolving the corresponding To-do item below:
  a fixed, non-interactive label pinned to the bottom of every page,
  reading "Last updated in {month} {year}" from `site.time` (build
  time, not the file's own git history — the simpler of the two
  options the To-do item had left open). Sits behind a gradient fade
  (`linear-gradient(to bottom, transparent, var(--bg-color) 65%)`)
  rather than a solid bar, so it reads as floating over the page
  rather than a hard-edged strip; `pointer-events: none` and a low
  `z-index: 5` keep it from blocking clicks on real content, since it
  visually overlaps the very bottom of the page. Lives once in
  `_layouts/default.html` (not per-page), so it applies to every page
  automatically. `.page-content` gained extra bottom padding so real
  content never sits directly behind the label. On desktop `left:
  12rem` clears the fixed sidebar (matching `.page-wrap`'s own
  `margin-left`); the mobile media query resets it to `left: 0`, where
  there's no sidebar to clear.

No known gaps remain open. (A previous revision of this file described
published papers losing their arXiv link in the PDF as a gap to fix —
see the `scripts/export_cv_pdf.py` bullet above: that's actually the
intended behavior, confirmed with Pedro, not a limitation.) All local
commits have been pushed to `origin/master`.

## To do

Confirmed as actual tasks (not just musings) — Pedro considers the
homepage itself finished otherwise:

- **Reformat the CV page** to be more tabular-style/readable — currently
  a sequence of prose-like entries per section (see the CV page bullet
  in Progress above); Pedro wants it more scannable, roughly table-like,
  though the exact layout isn't decided yet.
- **Add a Claude Code mascot icon somewhere** (tentatively also at the
  bottom of the sidebar) that, when clicked, shows a message along the
  lines of "Website developed from scratch with Claude Code's
  assistance." Exact placement, icon asset, and click-interaction style
  (popup vs. tooltip vs. something else) not decided yet.

## Ideas for the future

Not started, not confirmed as to-dos either — background context so
it isn't lost between sessions:

- **Aesthetic polish is ongoing, not a one-time pass.** The original
  three-step "general aesthetic pass" (theme system, responsive nav
  layout, font/size/alignment — see Progress above) turned out not to
  be the end of it: Pedro has kept sending small, ad hoc polish
  requests since (sidebar/page background contrast, theme-toggle icon
  redesign, section spacing, nav hover/active shading, text column
  width — also in Progress above), each its own one-off rather than a
  planned batch. Treat this as open-ended; nothing else specific is
  queued right now beyond the To do items above, but expect more small
  requests like these to keep coming.

To resume this work in a new session, just say "continue where we left
off" — this section has the full context.
