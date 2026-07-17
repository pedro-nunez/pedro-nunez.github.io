#!/usr/bin/env python3
"""Export _data/cv.yml to assets/cv.pdf via rendercv.

_data/cv.yml is written primarily for the Jekyll site (see CLAUDE.md), so
this script does the presentation work needed to turn it into the printed
CV: picking which sections appear, in what order, under what heading, and
a few section-specific reshapes (e.g. merging service + visit entries into
one "Other Academic Activities" section) so the result matches the layout
of the old hand-written LaTeX resume.

Requires: pip install -r scripts/requirements.txt
          (a virtualenv is recommended: python -m venv .venv && source
          .venv/bin/activate before installing)
Usage:    python scripts/export_cv_pdf.py
"""

import datetime
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CV_YAML = REPO_ROOT / "_data" / "cv.yml"
BUILD_DIR = REPO_ROOT / "rendercv_build"
OUTPUT_PDF = REPO_ROOT / "assets" / "cv.pdf"

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def clean_extra_fields(value):
    """Drop non-string extra fields (numbers, booleans) that crash
    rendercv's template substitution; e.g. lat/lon, online. Standard
    rendercv fields are never numeric/boolean, so this only ever touches
    our own extras."""
    if isinstance(value, dict):
        return {k: clean_extra_fields(v) for k, v in value.items() if not isinstance(v, (bool, float))}
    if isinstance(value, list):
        return [clean_extra_fields(v) for v in value]
    return value


def ensure_period(text):
    """Many summary/note fields in cv.yml omit a trailing period, relying
    on the website's Liquid templates to add one at render time (see
    cv.md). The PDF has no such template-level punctuation, so callers
    that surface a summary as its own line/bullet apply this explicitly.
    Doesn't touch text already ending in sentence-final punctuation."""
    if not text:
        return text
    text = text.rstrip()
    return text if text[-1] in ".!?:" else text + "."


def promote_summary_to_highlight(entries):
    """EducationEntry/ExperienceEntry: move summary into the first
    highlight, matching the old resume's style of treating the thesis/
    role blurb as a bullet rather than a separate description line."""
    result = []
    for e in entries:
        e = dict(e)
        summary = e.pop("summary", None)
        if summary:
            e["highlights"] = [ensure_period(summary)] + list(e.get("highlights", []))
        result.append(e)
    return result


def combine_institution_into_summary(e):
    """NormalEntry has no distinct 'institution' field, so an unrecognized
    institution extra is otherwise silently dropped. Fold it into summary
    as '{institution}. {summary}'."""
    e = dict(e)
    institution = e.pop("institution", None)
    summary = e.get("summary")
    if institution and summary:
        combined = f"{institution}. {summary}"
    else:
        combined = institution or summary
    if combined:
        e["summary"] = ensure_period(combined)
    return e


def format_multi_dates(dates):
    """Format a list of date.date objects the way the old resume shows
    non-contiguous minicourse meeting days: '22, 27, 29 Apr 2026' or,
    spanning months, '24, 26 Nov, 1 Dec 2025' (year/month shown once,
    on the last date in each run)."""
    groups = []
    for d in sorted(dates):
        if groups and groups[-1][0] == d.month and groups[-1][1] == d.year:
            groups[-1][2].append(d.day)
        else:
            groups.append((d.month, d.year, [d.day]))
    parts = []
    for i, (month, year, days) in enumerate(groups):
        day_str = ", ".join(str(d) for d in days)
        if i == len(groups) - 1:
            parts.append(f"{day_str} {MONTHS[month - 1]} {year}")
        else:
            parts.append(f"{day_str} {MONTHS[month - 1]}")
    return ", ".join(parts)


def format_single_date(d, month_only=False):
    """rendercv's own single_date template only shows month/year; several
    sections (talks, funding, conferences, ...) actually know the exact
    day, so this formats a precise 'D Mon YYYY' as a literal date string
    fed through rendercv's 'date' field (which is used verbatim, not
    reformatted). month_only handles the couple of entries flagged
    precision: month, where the day genuinely isn't known."""
    if month_only:
        return f"{MONTHS[d.month - 1]} {d.year}"
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def format_date_range(start, end, month_only=False):
    """Precise equivalent of rendercv's date_range template, mirroring
    _includes/date-range.html but additionally collapsing a repeated
    month/year rather than stating it on both ends: '1 – 31 Jul 2015',
    '20 Jul – 9 Aug 2014', 'Jan – Jun 2013' (month_only), and only
    falling back to two full dates when start and end are in different
    years. 'Present' for an open end date; a single formatted date if
    start and end are the same (down to month, if month_only)."""
    if not end:
        return f"{format_single_date(start, month_only)} – Present"
    same_year = start.year == end.year
    same_month = same_year and start.month == end.month
    if month_only:
        if same_month:
            return format_single_date(start, True)
        if same_year:
            return f"{MONTHS[start.month - 1]} – {MONTHS[end.month - 1]} {end.year}"
        return f"{format_single_date(start, True)} – {format_single_date(end, True)}"
    if start == end:
        return format_single_date(start)
    if same_month:
        return f"{start.day} – {end.day} {MONTHS[end.month - 1]} {end.year}"
    if same_year:
        return f"{start.day} {MONTHS[start.month - 1]} – {end.day} {MONTHS[end.month - 1]} {end.year}"
    return f"{format_single_date(start)} – {format_single_date(end)}"


def apply_precise_dates(e):
    """Replace start_date/end_date (or a bare date) with a precomputed
    'date' string carrying full day precision, since rendercv's own
    single_date/date_range templates are global (month/year only) and
    can't be set per-section. No-op for entries whose 'date' is already
    a free-text term (e.g. service's "Summer Term 2025") rather than a
    real date — there's no extra precision to add there."""
    e = dict(e)
    month_only = e.pop("precision", None) == "month"
    if "start_date" in e:
        e["date"] = format_date_range(e.pop("start_date"), e.pop("end_date", None), month_only)
    elif isinstance(e.get("date"), datetime.date):
        e["date"] = format_single_date(e["date"], month_only)
    return e


def build_work_experience(data):
    return promote_summary_to_highlight(data["sections"]["experience"])


def build_research_projects(data):
    # NormalEntry drops the unrecognized 'institution' extra by default,
    # which is what we want here: the old resume shows only the funding
    # note for these, not the host institution.
    return data["sections"]["projects"]


def build_publications(data):
    result = []
    for e in data["sections"]["publications"]:
        e = dict(e)
        arxiv = e.pop("arxiv", None)
        # rendercv's default PublicationEntry template shows only one of
        # doi/url when both are set, so only recover the arXiv link where
        # there's no doi to conflict with (unpublished/preprint entries).
        # Published entries keep just the doi — matching both there needs
        # a custom template, deferred as cosmetic work.
        if arxiv and not e.get("doi"):
            e["url"] = f"https://arxiv.org/abs/{arxiv}"
        # No journal means still unpublished; label it explicitly rather
        # than leaving the "JOURNAL (URL)" line blank before the link.
        e.setdefault("journal", "Preprint")
        # Italicize the CV owner's own name in the byline (rendercv's
        # convention for emphasizing an author, e.g. "*H. Tom*" in its
        # docs) so it stands out among any co-authors.
        e["authors"] = [f"*{a}*" if a == data["name"] else a for a in e["authors"]]
        result.append(e)
    return result


def build_teaching_experience(data):
    return data["sections"]["teaching_experience"]


def build_education(data):
    entries = [dict(e) for e in data["sections"]["education"]]
    erasmus = next((e for e in entries if e.get("degree") == "Erasmus Exchange"), None)
    if erasmus:
        entries = [e for e in entries if e is not erasmus]
        bachelor = next((e for e in entries if e.get("degree") == "Bachelor"), None)
        if bachelor:
            bachelor.setdefault("highlights", [])
            bachelor["highlights"].insert(
                1,
                "Erasmus exchange at LMU Munich during the course 2016/2017.",
            )
    # "area" becomes "{full degree} in {area}" (e.g. "PhD in
    # Mathematics"), matching the old resume's headings. The PDF's
    # degree column is narrow (designed for "PhD"-length strings), so
    # that column still uses the abbreviated form; the website and
    # travel map always show the full degree from cv.yml directly.
    for e in entries:
        e["area"] = f"{e['degree']} in {e['area']}"
        if "degree_abbr" in e:
            e["degree"] = e.pop("degree_abbr")
    return promote_summary_to_highlight(entries)


def build_languages(data):
    return data["sections"]["languages"]


def build_talks(data, talk_type):
    result = []
    for e in data["sections"]["talks"]:
        if e.get("type") != talk_type:
            continue
        e = dict(e)
        if e.pop("online", False):
            e["summary"] = f"{e.get('summary', '')} (online)"
        if e.get("summary"):
            e["summary"] = ensure_period(e["summary"])
        result.append(apply_precise_dates(e))
    return result


def build_academic_visits(data):
    return [apply_precise_dates(combine_institution_into_summary(e)) for e in data["sections"]["academic_visits"]]


def build_other_academic_activities(data):
    result = []
    for e in data["sections"]["service"]:
        e = dict(e)
        if e.get("summary"):
            e["summary"] = ensure_period(e["summary"])
        result.append(apply_precise_dates(e))
    return result


def build_funding(data):
    return [apply_precise_dates(e) for e in data["sections"]["funding"]]


def build_conferences_attended(data):
    result = []
    for e in data["sections"]["activities"]:
        e = combine_institution_into_summary(dict(e))
        display_location = e.pop("display_location", None)
        if display_location:
            e["location"] = display_location
        dates_list = e.pop("dates", None)
        if e.pop("online", False):
            e["name"] = f"{e['name']} (online)"
        if dates_list:
            e["date"] = format_multi_dates(dates_list)
            e.pop("start_date", None)
            e.pop("end_date", None)
        else:
            e = apply_precise_dates(e)
        result.append(e)
    return result


def build_additional_formation(data):
    return [apply_precise_dates(e) for e in data["sections"]["extra"]]


SECTION_BUILDERS = [
    ("Work Experience", build_work_experience),
    ("Participation in Research Projects", build_research_projects),
    ("Publications", build_publications),
    ("Teaching Experience", build_teaching_experience),
    ("Education", build_education),
    ("Languages", build_languages),
    ("Invited Talks", lambda data: build_talks(data, "invited")),
    ("Contributed Talks", lambda data: build_talks(data, "contributed")),
    ("Academic Visits", build_academic_visits),
    ("Other Academic Activities", build_other_academic_activities),
    ("Scholarships & Funding received", build_funding),
    ("Conferences, Workshops and Schools Attended", build_conferences_attended),
    ("Additional Formation", build_additional_formation),
]


def build_rendercv_document(data):
    sections = {title: clean_extra_fields(builder(data)) for title, builder in SECTION_BUILDERS}
    return {
        "cv": {
            "name": data["name"],
            "location": data["location"],
            "email": data["email"],
            "website": data["website"],
            "social_networks": data.get("social_networks", []),
            "sections": sections,
        },
        "design": {
            "theme": "classic",
            "templates": {
                # rendercv's default NormalEntry template
                # ("**NAME**\nSUMMARY\nHIGHLIGHTS") doesn't include URL, so
                # entries with a url (e.g. conference/workshop pages) would
                # otherwise silently lose that link.
                "normal_entry": {"main_column": "**NAME**\nSUMMARY\nHIGHLIGHTS\nURL"},
                # Default is "URL (JOURNAL)"; swapped so the journal/preprint
                # label reads first with the DOI/arXiv link in parentheses,
                # e.g. "Geometriae Dedicata 216, 20 (10.1007/...)." or
                # "Preprint (arxiv.org/...)." — trailing periods added after
                # AUTHORS and (URL) for consistency with the rest of the CV;
                # verified separately that rendercv drops "(URL)." cleanly
                # along with the parens when there's no doi/url, though that
                # case doesn't come up in our actual data (every entry has
                # one or the other).
                "publication_entry": {"main_column": "**TITLE**\nSUMMARY\nAUTHORS.\nJOURNAL (URL)."},
            },
            # rendercv's default hyphenates when justifying, which can break
            # words awkwardly mid-syllable in the narrow date/location column
            # (e.g. "Esch-sur-Alzette, Luxembourg" as "Luxem-/bourg"). This
            # still wraps at existing hyphens (e.g. within "Esch-sur-Alzette"
            # itself) — it just won't invent new break points.
            "typography": {"alignment": "justified-with-no-hyphenation"},
        },
    }


def main():
    if shutil.which("rendercv") is None:
        sys.exit("rendercv not found on PATH. Install with: pip install -r scripts/requirements.txt")

    data = yaml.safe_load(CV_YAML.read_text(encoding="utf-8"))
    document = build_rendercv_document(data)

    BUILD_DIR.mkdir(exist_ok=True)
    input_path = BUILD_DIR / "cv.yaml"
    input_path.write_text(yaml.safe_dump(document, allow_unicode=True, sort_keys=False), encoding="utf-8")

    subprocess.run(
        [
            "rendercv",
            "render",
            str(input_path),
            "--pdf-path",
            "cv.pdf",
            "--dont-generate-markdown",
            "--dont-generate-png",
        ],
        cwd=BUILD_DIR,
        check=True,
    )

    OUTPUT_PDF.parent.mkdir(exist_ok=True)
    shutil.copyfile(BUILD_DIR / "cv.pdf", OUTPUT_PDF)
    print(f"wrote {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
