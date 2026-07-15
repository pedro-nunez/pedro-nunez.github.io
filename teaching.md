---
layout: default
title: Teaching
permalink: /teaching/
---

<h1>Teaching</h1>

<h2>Previous teaching</h2>

<ul>
{% for course in site.data.teaching %}
  <li>{{ course.role }} for <i>{% if course.url %}<a href="{{ course.url }}">{{ course.course }}</a>{% else %}{{ course.course }}{% endif %}</i>{% if course.note %} {{ course.note }}{% endif %} during the {{ course.term }} at {{ course.institution }}.</li>
{% endfor %}
</ul>

<p>Here is my <a href="#" title="My teaching statement">teaching statement</a> (coming soon).</p>
