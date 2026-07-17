---
layout: default
title: CV
permalink: /cv/
---

<h1>Curriculum Vitae</h1>

<p><a href="{{ '/assets/cv.pdf' | relative_url }}">Download as PDF</a></p>

<h2>Work Experience</h2>

<ul>
{% for pos in site.data.positions %}
  {% if pos.category == "work" %}
  <li>
    <strong>{{ pos.role }}</strong>, {{ pos.institution }} ({{ pos.city }})<br>
    {% include date-range.html start=pos.start end=pos.end precision="month" %}
    {% if pos.note %}<br>{{ pos.note }}.{% endif %}
    {% if pos.highlights %}
    <ul>
      {% for h in pos.highlights %}<li>{{ h }}</li>{% endfor %}
    </ul>
    {% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Participation in Research Projects</h2>

<ul>
{% for proj in site.data.projects %}
  <li>
    <strong>{{ proj.title }}</strong>, {{ proj.institution }} ({{ proj.city }})<br>
    {% include date-range.html start=proj.start end=proj.end precision="month" %}
    {% if proj.note %}<br>{{ proj.note }}{% endif %}
  </li>
{% endfor %}
</ul>

<h2>Publications</h2>

<ol reversed>
{% for pub in site.data.publications %}
  <li>
    <i>{{ pub.title }}</i>.
    {% if pub.authors.size > 0 %}
    <br>with {% include author-list.html authors=pub.authors %}.
    {% endif %}
    {% if pub.venue %}
    <br>{{ pub.venue }} ({{ pub.year }}).
    {% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">DOI:{{ pub.doi }}</a>.{% endif %}
    {% else %}
    <br>(Submitted.)
    {% endif %}
    {% if pub.arxiv %}
    <br>Preprint: <a href="https://arxiv.org/abs/{{ pub.arxiv }}">arXiv:{{ pub.arxiv }}</a>.
    {% endif %}
  </li>
{% endfor %}
</ol>

<h2>Teaching Experience</h2>

<ul>
{% for course in site.data.teaching.courses %}
  <li>{{ course.role }} for <i>{% if course.url %}<a href="{{ course.url }}">{{ course.course }}</a>{% else %}{{ course.course }}{% endif %}</i>{% if course.note %} {{ course.note }}{% endif %} during the {{ course.term }} at {{ course.institution }}.</li>
{% endfor %}
</ul>

<h2>Education</h2>

<ul>
{% for pos in site.data.positions %}
  {% if pos.category == "education" %}
  <li>
    <strong>{{ pos.role }}</strong>, {{ pos.institution }} ({{ pos.city }})<br>
    {% include date-range.html start=pos.start end=pos.end precision="month" %}
    {% if pos.note %}<br>{{ pos.note }}.{% endif %}
    {% if pos.highlights %}
    <ul>
      {% for h in pos.highlights %}<li>{{ h }}</li>{% endfor %}
    </ul>
    {% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Languages</h2>

<ul>
  <li><strong>Spanish</strong>: native speaker.</li>
  <li><strong>English</strong>: C1 level (IELTS with score 8).</li>
  <li><strong>German</strong>: C1 level (Goethe-Zertifikat C1).</li>
  <li><strong>Chinese</strong>: B1 level (HSK3 + HSKK Basic).</li>
</ul>

<h2>Invited Talks</h2>

<ul>
{% for talk in site.data.talks %}
  {% if talk.type == "invited" %}
  <li>
    <i>{{ talk.title }}</i>, {{ talk.event }}{% if talk.online %} (online){% endif %}
    ({{ talk.date | date: "%-d %b %Y" }}), {{ talk.city }}.
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Contributed Talks</h2>

<ul>
{% for talk in site.data.talks %}
  {% if talk.type == "contributed" %}
  <li>
    <i>{{ talk.title }}</i>, {{ talk.event }} ({{ talk.date | date: "%-d %b %Y" }}), {{ talk.city }}.
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Academic Visits</h2>

<ul>
{% for item in site.data.activities %}
  {% if item.type == "visit" %}
  <li>
    {{ item.title }}{% if item.institution %}, {{ item.institution }}{% endif %}, {{ item.city }}
    ({% include date-range.html start=item.start end=item.end %}).
    {% if item.note %}{{ item.note }}.{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Other Academic Activities</h2>

<ul>
{% for item in site.data.service %}
  <li>
    {{ item.title }}{% if item.role %} ({{ item.role }}){% endif %}{% if item.institution %}, {{ item.institution }}{% endif %}, {{ item.city }}
    ({% if item.term %}{{ item.term }}{% else %}{% include date-range.html start=item.start end=item.end %}{% endif %}).
    {% if item.note %}{{ item.note }}.{% endif %}
  </li>
{% endfor %}
</ul>

<h2>Scholarships &amp; Funding Received</h2>

<ul>
{% for item in site.data.funding %}
  <li>
    {{ item.title }}, {{ item.city }}
    ({% include date-range.html start=item.start end=item.end precision=item.precision %}).
    {{ item.note }}
  </li>
{% endfor %}
</ul>

<h2>Conferences, Workshops, Schools and Courses Attended</h2>

<ul>
{% for item in site.data.activities %}
  {% if item.type != "visit" %}
  <li>
    {% if item.url %}<a href="{{ item.url }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %} ({{ item.type }}){% if item.institution %}, {{ item.institution }}{% endif %}, {{ item.city }}
    ({% include date-range.html start=item.start end=item.end %}{% if item.online %}, online{% endif %}).
    {% if item.note %}{{ item.note }}.{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Additional Formation</h2>

<ul>
{% for item in site.data['additional-formation'] %}
  <li>
    {% if item.url %}<a href="{{ item.url }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %} ({{ item.type }}), {{ item.city }}
    ({% include date-range.html start=item.start end=item.end precision=item.precision %}).
    {{ item.note }}
  </li>
{% endfor %}
</ul>
