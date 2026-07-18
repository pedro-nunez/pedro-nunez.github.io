---
layout: default
---

![Photo of Pedro Núñez]({{ '/assets/images/profile.jpg' | relative_url }}){: .profile-photo }

# Pedro Núñez

<a href="mailto:pnunez@ntu.edu.tw" class="mailto-link">pnunez [at] ntu.edu.tw</a>

I am a postdoc working in algebraic geometry in the group of
<a href="https://www.math.ntu.edu.tw/~jkchen/" class="person-link">Jungkai Alfred Chen</a>
at National Taiwan University. Before that, I was a PhD student of
<a href="https://cplx.vm.uni-freiburg.de/" class="person-link">Stefan Kebekus</a> at the
University of Freiburg.

My research interests are birational geometry and derived categories
of algebraic varieties.

## Papers

<ul class="papers-list">
{% for pub in site.data.cv.sections.publications %}
  {% assign coauthors = pub.authors | where_exp: "a", "a.name != site.data.cv.name" %}
  <li>
    <a href="{% if pub.doi %}https://doi.org/{{ pub.doi }}{% else %}https://arxiv.org/abs/{{ pub.arxiv }}{% endif %}" class="paper-title">{{ pub.title }}</a>{% if coauthors.size > 0 %} (with {% include author-list.html authors=coauthors link_class="person-link" %}){% endif %},<br>{% if pub.journal %}in {{ pub.journal }} ({{ pub.date }}){% else %}available on arXiv ({{ pub.date }}) and submitted for publication{% endif %}.
  </li>
{% endfor %}
</ul>
