---
layout: default
title: Other Writings
permalink: /writings/
---

<h1>Other Writings</h1>

<h2>Scripts for seminar talks</h2>

<ul>
{% for item in site.data.writings.seminar_scripts %}
  <li><i>{% if item.url %}<a href="{{ item.url | relative_url }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}</i>, script for a seminar on {{ item.topic }} organized by {% if item.organizer.url %}<a href="{{ item.organizer.url }}" class="person-link">{{ item.organizer.name }}</a>{% else %}{{ item.organizer.name }}{% endif %} at {{ item.institution }} ({{ item.term }}).</li>
{% endfor %}
</ul>

<h2>Other notes</h2>

<ul>
{% for item in site.data.writings.other_notes %}
  <li><i>{% if item.url %}<a href="{{ item.url | relative_url }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}</i>, notes for a seminar that I organized at {{ item.institution }} ({{ item.term }}){% if item.programme_url %}, <a href="{{ item.programme_url | relative_url }}">programme</a>{% endif %}.</li>
{% endfor %}
</ul>
