---
layout: default
title: Teaching
permalink: /teaching/
---

<h1>Teaching</h1>

<h2>Previous teaching</h2>

<ul>
{% for course in site.data.cv.sections.teaching_courses %}
  <li>{{ course.position }} for <i>{% if course.url %}<a href="{{ course.url }}">{{ course.summary }}</a>{% else %}{{ course.summary }}{% endif %}</i>{% if course.note %} {{ course.note }}{% endif %} during the {{ course.date }} at {{ course.company }}.</li>
{% endfor %}
</ul>

<h2>Teaching materials</h2>

<ul>
{% for item in site.data.cv.sections.teaching_materials %}
  <li><i><a href="{{ item.url }}">{{ item.name }}</a></i>{% if item.summary %}, {{ item.summary }}{% endif %}, written during the {{ item.date }} at {{ item.institution }}.</li>
{% endfor %}
</ul>

<p>Here is my <a href="{{ '/assets/pdfs/teaching-statement.pdf' | relative_url }}" title="My teaching statement">teaching statement</a>.</p>
