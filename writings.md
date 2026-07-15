---
layout: default
title: Other writings
permalink: /writings/
---

<h1>Other writings</h1>

<h2>Scripts for seminar talks</h2>

<ul>
{% for item in site.data.writings.seminar_scripts %}
  <li><i>{{ item.title }}</i>, script for a seminar on {{ item.topic }} organized by {% if item.organizer.url %}<a href="{{ item.organizer.url }}">{{ item.organizer.name }}</a>{% else %}{{ item.organizer.name }}{% endif %} at {{ item.institution }} ({{ item.term }}).</li>
{% endfor %}
</ul>

<h2>Other notes</h2>

<ul>
{% for item in site.data.writings.other_notes %}
  <li><i>{{ item.title }}</i>, notes for a seminar that I organized at {{ item.institution }} ({{ item.term }}).</li>
{% endfor %}
</ul>
