---
layout: default
title: Algebraic Geometry in Madrid
permalink: /algebraic-geometry-in-madrid/
---

# Algebraic Geometry in Madrid

A list of algebraic geometry conferences, workshops, and seminars taking
place in Madrid. Algebraic geometry is understood here in a broad sense,
and this list is not guaranteed to be complete.

[Add event](https://github.com/pedro-nunez/pedro-nunez.github.io/issues/new?template=add-event.yml){: .button }

{% assign upcoming = site.data['madrid-events'] | where: "status", "future" | sort: "start" %}
{% assign past = site.data['madrid-events'] | where: "status", "past" | sort: "start" | reverse %}

## Upcoming

<ul>
{% for event in upcoming %}
  <li>
    {% if event.url %}<a href="{{ event.url }}">{{ event.title }}</a>{% else %}{{ event.title }}{% endif %},
    {{ event.institution }}
    ({% include date-range.html start=event.start end=event.end precision=event.precision %}).
  </li>
{% endfor %}
</ul>

## Past

<ul>
{% for event in past %}
  <li>
    {% if event.url %}<a href="{{ event.url }}">{{ event.title }}</a>{% else %}{{ event.title }}{% endif %},
    {{ event.institution }}
    ({% include date-range.html start=event.start end=event.end precision=event.precision %}).
  </li>
{% endfor %}
</ul>
