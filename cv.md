---
layout: default
title: CV
permalink: /cv/
---

<h1>Curriculum Vitae</h1>

<p><a href="{{ '/assets/pdfs/cv.pdf' | relative_url }}" class="button">PDF version</a></p>

<h2>Work Experience</h2>

<ul>
{% for pos in site.data.cv.sections.experience %}
  <li>
    <strong>{{ pos.position }}</strong>, {{ pos.company }} ({{ pos.location }})<br>
    {% include date-range.html start=pos.start_date end=pos.end_date precision="month" %}
    {% if pos.summary %}<br>{{ pos.summary | replace: "Jungkai Alfred Chen", '<a href="https://www.math.ntu.edu.tw/~jkchen/">Jungkai Alfred Chen</a>' | replace: "Stefan Kebekus", '<a href="https://cplx.vm.uni-freiburg.de/">Stefan Kebekus</a>' }}.{% endif %}
    {% if pos.highlights %}
    <ul>
      {% for h in pos.highlights %}<li>{{ h }}</li>{% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ul>

<h2>Participation in Research Projects</h2>

<ul>
{% for proj in site.data.cv.sections.projects %}
  <li>
    <strong>{{ proj.name }}</strong>, {{ proj.institution }} ({{ proj.location }})<br>
    {% include date-range.html start=proj.start_date end=proj.end_date precision="month" %}
    {% if proj.summary %}<br>{{ proj.summary | replace: "Jungkai Alfred Chen", '<a href="https://www.math.ntu.edu.tw/~jkchen/">Jungkai Alfred Chen</a>' | replace: "Stefan Kebekus", '<a href="https://cplx.vm.uni-freiburg.de/">Stefan Kebekus</a>' }}{% endif %}
  </li>
{% endfor %}
</ul>

<h2>Publications</h2>

<ol reversed>
{% for pub in site.data.cv.sections.publications %}
  <li>
    <i>{{ pub.title }}</i>.
    {% assign coauthors = pub.authors | where_exp: "a", "a.name != site.data.cv.name" %}
    {% if coauthors.size > 0 %}
    <br>with {% include author-list.html authors=coauthors %}.
    {% endif %}
    {% if pub.journal %}
    <br>{{ pub.journal }} ({{ pub.date }}).
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
{% for course in site.data.cv.sections.teaching_courses %}
  <li>{{ course.position }} for <i>{% if course.url %}<a href="{{ course.url }}">{{ course.summary }}</a>{% else %}{{ course.summary }}{% endif %}</i>{% if course.note %} {{ course.note }}{% endif %} during the {{ course.date }} at {{ course.company }}.</li>
{% endfor %}
</ul>

<h2>Education</h2>

<ul>
{% for pos in site.data.cv.sections.education %}
  <li>
    <strong>{{ pos.degree }} in {{ pos.area }}</strong>, {{ pos.institution }} ({{ pos.location }})<br>
    {% include date-range.html start=pos.start_date end=pos.end_date precision="month" %}
    {% if pos.summary %}<br>{{ pos.summary | replace: "Jungkai Alfred Chen", '<a href="https://www.math.ntu.edu.tw/~jkchen/">Jungkai Alfred Chen</a>' | replace: "Stefan Kebekus", '<a href="https://cplx.vm.uni-freiburg.de/">Stefan Kebekus</a>' }}.{% endif %}
    {% if pos.highlights %}
    <ul>
      {% for h in pos.highlights %}<li>{{ h }}</li>{% endfor %}
    </ul>
    {% endif %}
  </li>
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
{% for talk in site.data.cv.sections.talks %}
  {% if talk.type == "invited" %}
  <li>
    <i>{{ talk.name }}</i>, {{ talk.summary }}{% if talk.online %} (online){% endif %}
    ({{ talk.date | date: "%-d %b %Y" }}), {{ talk.location }}.
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Contributed Talks</h2>

<ul>
{% for talk in site.data.cv.sections.talks %}
  {% if talk.type == "contributed" %}
  <li>
    <i>{{ talk.name }}</i>, {{ talk.summary }} ({{ talk.date | date: "%-d %b %Y" }}), {{ talk.location }}.
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Academic Visits</h2>

<ul>
{% for item in site.data.cv.sections.academic_visits %}
  <li>
    {{ item.name }}{% if item.institution %}, {{ item.institution }}{% endif %}, {{ item.location }}
    ({% include date-range.html start=item.start_date end=item.end_date %}).
    {% if item.summary %}{{ item.summary | replace: "Meng Chen", '<a href="https://faculty.fudan.edu.cn/chenmeng/zh_CN/index/107651/list/index.htm">Meng Chen</a>' }}.{% endif %}
  </li>
{% endfor %}
</ul>

<h2>Other Academic Activities</h2>

<ul>
{% for item in site.data.cv.sections.service %}
  <li>
    {{ item.name }}{% if item.role %} ({{ item.role }}){% endif %}{% if item.institution %}, {{ item.institution }}{% endif %}, {{ item.location }}
    ({% if item.date %}{{ item.date }}{% else %}{% include date-range.html start=item.start_date end=item.end_date %}{% endif %}).
    {% if item.summary %}{{ item.summary | replace: "Flora Poon", '<a href="https://sites.google.com/view/florapoon">Flora Poon</a>' | replace: "Hsueh-Yung Lin", '<a href="https://homepage.ntu.edu.tw/~hsuehyunglin">Hsueh-Yung Lin</a>' }}.{% endif %}
  </li>
{% endfor %}
</ul>

<h2>Scholarships &amp; Funding Received</h2>

<ul>
{% for item in site.data.cv.sections.funding %}
  <li>
    {{ item.name }}, {{ item.location }}
    ({% include date-range.html start=item.start_date end=item.end_date precision=item.precision %}).
    {{ item.summary }}
  </li>
{% endfor %}
</ul>

<h2>Conferences, Workshops, Schools and Courses Attended</h2>

<ul>
{% for item in site.data.cv.sections.activities %}
  <li>
    {% if item.url %}<a href="{{ item.url }}">{{ item.name }}</a>{% else %}{{ item.name }}{% endif %} ({{ item.type }}){% if item.institution %}, {{ item.institution }}{% endif %}, {{ item.display_location | default: item.location }}
    ({% include date-range.html start=item.start_date end=item.end_date %}{% if item.online %}, online{% endif %}).
    {% if item.summary %}{{ item.summary }}.{% endif %}
  </li>
{% endfor %}
</ul>

<h2>Additional Formation</h2>

<ul>
{% for item in site.data.cv.sections.extra %}
  <li>
    {% if item.url %}<a href="{{ item.url }}">{{ item.name }}</a>{% else %}{{ item.name }}{% endif %} ({{ item.type }}), {{ item.location }}
    ({% include date-range.html start=item.start_date end=item.end_date precision=item.precision %}).
    {{ item.summary }}
  </li>
{% endfor %}
</ul>
