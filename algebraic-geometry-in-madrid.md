---
layout: default
title: Algebraic Geometry in Madrid
permalink: /algebraic-geometry-in-madrid/
---

# Algebraic Geometry in Madrid

A list of algebraic geometry conferences, workshops, and seminars taking
place in Madrid.

The list may be incomplete. If you know of any unlisted events, you can
suggest them through the button below or by sending me an
[email](mailto:{{ site.data.cv.email }}){: .mailto-link }. Thanks!

[Add event](https://github.com/pedro-nunez/pedro-nunez.github.io/issues/new?template=add-event.yml){: .button }

{% assign upcoming = site.data['madrid-events'] | where: "status", "future" | sort: "start" %}
{% assign past = site.data['madrid-events'] | where: "status", "past" | sort: "start" | reverse %}

## Upcoming

<ul>
{% for event in upcoming %}
  <li>
    {% include date-range.html start=event.start end=event.end precision=event.precision smart=true %}:
    {% if event.url %}<a href="{{ event.url }}" class="event-link">{{ event.title }}</a>{% else %}{{ event.title }}{% endif %},
    at {{ event.institution }}.
  </li>
{% endfor %}
</ul>

## Past

<ul>
{% for event in past %}
  <li>
    {% include date-range.html start=event.start end=event.end precision=event.precision smart=true %}:
    {% if event.url %}<a href="{{ event.url }}" class="event-link">{{ event.title }}</a>{% else %}{{ event.title }}{% endif %},
    at {{ event.institution }}.
  </li>
{% endfor %}
</ul>
