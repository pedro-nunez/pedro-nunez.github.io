---
layout: default
---

![Photo of Pedro Núñez]({{ '/assets/images/profile.jpg' | relative_url }}){: .profile-photo }

# Pedro Núñez

I am a postdoc working in algebraic geometry in the group of Jungkai
Alfred Chen at National Taiwan University. Before that, I was a PhD
student of Stefan Kebekus at the University of Freiburg.

My research interests are birational geometry and derived categories
of algebraic varieties.

[CV (coming soon)](#)

## Papers

<ul>
{% for pub in site.data.publications %}
  <li>
    <a href="{% if pub.doi %}https://doi.org/{{ pub.doi }}{% else %}https://arxiv.org/abs/{{ pub.arxiv }}{% endif %}" class="paper-title">{{ pub.title }}</a>{% if pub.authors.size > 0 %} (with {% include author-list.html authors=pub.authors %}){% endif %}, {% if pub.venue %}in {{ pub.venue }}{% else %}submitted{% endif %}.
  </li>
{% endfor %}
</ul>
