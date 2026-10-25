---
layout: default
---

![Photo of Pedro Núñez]({{ '/assets/images/profile.jpg' | relative_url }}){: .profile-photo }

<h1>Pedro Núñez</h1>

I am a *Profesor Ayudante Doctor* at the Polytechnic University of Madrid, School of Computer Systems Engineering. I work on algebraic geometry, mostly on birational geometry and derived categories.

Previously, I was a postdoc in the group of
<a href="https://www.math.ntu.edu.tw/~jkchen/" class="person-link">Jungkai Alfred Chen</a>
at National Taiwan University. Before that, I was a PhD student of
<a href="https://cplx.vm.uni-freiburg.de/" class="person-link">Stefan Kebekus</a> at the
University of Freiburg.

<h2>Papers</h2>

<ul class="papers-list">
{% for pub in site.data.cv.sections.publications %}
  {% assign coauthors = pub.authors | where_exp: "a", "a.name != site.data.cv.name" %}
  <li>
    <a href="{% if pub.doi %}https://doi.org/{{ pub.doi }}{% else %}https://arxiv.org/abs/{{ pub.arxiv }}{% endif %}" class="paper-title">{{ pub.title }}</a>{% if coauthors.size > 0 %} (with {% include author-list.html authors=coauthors link_class="person-link" %}){% endif %}, {% if pub.journal %}in {{ pub.journal }} ({{ pub.date }}){% else %}available on arXiv ({{ pub.date }}){% endif %}.
  </li>
{% endfor %}
</ul>

<h2>Current teaching</h2>

{% assign current_courses = site.data.cv.sections.teaching_courses | where_exp: "course", "course.status == 'current'" %}

<ul>
{% for course in current_courses %}
  <li>
    {{ course.position }} for
    <i>{% if course.url %}<a href="{{ course.url }}" class="teaching-course-link">{{ course.summary }}</a>{% else %}{{ course.summary }}{% endif %}</i>{% if course.note %} {{ course.note }}{% endif %}
    during the {{ course.date }} at {{ course.company }}.
  </li>
{% endfor %}
</ul>
