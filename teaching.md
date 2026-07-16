---
layout: default
title: Teaching
permalink: /teaching/
---

<h1>Teaching</h1>

<h2>Previous teaching</h2>

<ul>
{% for course in site.data.teaching.courses %}
  <li>{{ course.role }} for <i>{% if course.url %}<a href="{{ course.url }}">{{ course.course }}</a>{% else %}{{ course.course }}{% endif %}</i>{% if course.note %} {{ course.note }}{% endif %} during the {{ course.term }} at {{ course.institution }}.</li>
{% endfor %}
</ul>

<h2>Teaching materials</h2>

<ul>
{% for item in site.data.teaching.materials %}
  <li><i><a href="{{ item.url }}">{{ item.title }}</a></i>{% if item.note %}, {{ item.note }}{% endif %}, written during the {{ item.term }} at {{ item.institution }}.</li>
{% endfor %}
</ul>

<p>Here is my <a href="#" title="My teaching statement">teaching statement</a> (coming soon).</p>
