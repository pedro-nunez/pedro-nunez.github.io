---
layout: default
title: Research
permalink: /research/
---

<h1>Research</h1>

<h2>Research interests</h2>

<p>Birational classification of algebraic varieties and derived categories
of algebraic varieties. More specifically:</p>

<ul>
  <li>Semiorthogonal decompositions and their relation to the minimal model program.</li>
  <li>Campana's birational classification program and differential forms therein.</li>
</ul>

<h2>Publications and preprints</h2>

<ol reversed>
{% for pub in site.data.cv.sections.publications %}
  <li>
    <i>{{ pub.title }}</i>.
    {% assign coauthors = pub.authors | where_exp: "a", "a.name != site.data.cv.name" %}
    {% if coauthors.size > 0 %}
    <br>with {% include author-list.html authors=coauthors link_class="person-link" %}.
    {% endif %}
    {% if pub.journal %}
    <br>{{ pub.journal }} ({{ pub.date }}).
    {% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}" class="paper-link">DOI:{{ pub.doi }}</a>.{% endif %}
    {% else %}
    <br>(Submitted.)
    {% endif %}
    {% if pub.arxiv %}
    <br>Preprint: <a href="https://arxiv.org/abs/{{ pub.arxiv }}" class="paper-link">arXiv:{{ pub.arxiv }}</a>.
    {% endif %}
  </li>
{% endfor %}
</ol>

<h2>PhD, master's and bachelor's theses</h2>

<ul>
  <li><i><a href="{{ '/assets/pdfs/phd-thesis.pdf' | relative_url }}" class="pdf-link">Categorical aspects of Campana orbifolds</a></i>, PhD thesis written under the supervision of <a href="https://cplx.vm.uni-freiburg.de" class="person-link">Stefan Kebekus</a> at the University of Freiburg (2023).</li>
  <li><i><a href="{{ '/assets/pdfs/master-thesis.pdf' | relative_url }}" class="pdf-link">Derived categories of Fano fibrations</a></i>, master's thesis written under the supervision of <a href="https://sites.google.com/site/lucatasin" class="person-link">Luca Tasin</a> and <a href="https://pbelmans.ncag.info" class="person-link">Pieter Belmans</a> at the University of Bonn (2019).</li>
  <li><i><a href="{{ '/assets/pdfs/bachelor-thesis.pdf' | relative_url }}" class="pdf-link">Blow-ups in algebraic geometry</a></i>, bachelor's thesis written under the supervision of <a href="https://www.math.lmu.de/~geldhauser/" class="person-link">Nikita Geldhauser</a> at the Ludwig-Maximilians-University of Munich (2017).</li>
</ul>
