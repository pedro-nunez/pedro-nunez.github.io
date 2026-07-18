---
layout: default
title: Travel Map
permalink: /travel-map/
extra_head: leaflet
---

<h1>Travel Map</h1>

<div id="map"></div>

<ul id="map-legend">
  <li><span class="dot" style="background:#2ca02c"></span> Current affiliation</li>
  <li><span class="dot" style="background:#d62728"></span> Past affiliation</li>
  <li><span class="dot" style="background:#1f77b4"></span> Past trip</li>
  <li><span class="dot" style="background:#f1c40f"></span> Upcoming trip</li>
</ul>

<p>Thanks to <a href="https://juliaschneider.pages.math.cnrs.fr/home/index.html" class="person-link">Julia Schneider</a> for giving me this idea, and thanks to <a href="https://claude.ai" class="person-link">Claude</a> for helping me implement it.</p>

<script>
  // The data below carries lat/lon for every entry that should appear on
  // the map (see the comments at the top of each source).
  var education = {{ site.data.cv.sections.education | jsonify }};
  var experience = {{ site.data.cv.sections.experience | jsonify }};
  var talks = {{ site.data.cv.sections.talks | jsonify }};
  var activities = {{ site.data.cv.sections.activities | jsonify }}.concat(
    {{ site.data.cv.sections.academic_visits | jsonify }}
  );

  // Colors per category, also used in the legend above.
  var colors = {
    "current-affiliation": "#2ca02c",
    "past-affiliation": "#d62728",
    "past-trip": "#1f77b4",
    "upcoming": "#f1c40f"
  };
  // If a location has entries in several categories, the marker uses the
  // color of whichever category comes first in this list, and categories
  // earlier in the list are drawn on top when pins visually overlap.
  var priority = ["upcoming", "current-affiliation", "past-affiliation", "past-trip"];

  var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  // Lightens (positive percent) or darkens (negative percent) a "#rrggbb"
  // color, used to derive the pin's gradient and border shades from its
  // base category color.
  function shadeColor(hex, percent) {
    var num = parseInt(hex.slice(1), 16);
    var amt = Math.round(2.55 * percent);
    var r = Math.min(255, Math.max(0, (num >> 16) + amt));
    var g = Math.min(255, Math.max(0, ((num >> 8) & 0x00ff) + amt));
    var b = Math.min(255, Math.max(0, (num & 0x0000ff) + amt));
    return "#" + (0x1000000 + r * 0x10000 + g * 0x100 + b).toString(16).slice(1);
  }

  // Builds a classic map-pin icon (circle sitting on a point, like the old
  // Leaflet color markers) in the given color, as an inline SVG. The path
  // is a circle with two tangent lines running down to a tip, which is
  // what gives the pin its sharp "shoulder" instead of a smooth teardrop
  // curve. iconAnchor points at that tip, so it lines up with the actual
  // coordinates instead of the icon's center.
  var pinIconCounter = 0;
  function pinIcon(color) {
    pinIconCounter++;
    var gradId = "pin-gradient-" + pinIconCounter;
    var light = shadeColor(color, 25);
    var dark = shadeColor(color, -20);
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="19.5" height="30.75" viewBox="0 0 26 41">' +
      '<defs>' +
        '<linearGradient id="' + gradId + '" x1="0" y1="0" x2="1" y2="1">' +
          '<stop offset="0" stop-color="' + light + '"/>' +
          '<stop offset="1" stop-color="' + color + '"/>' +
        '</linearGradient>' +
      '</defs>' +
      '<path d="M24.08 18.79A12.5 12.5 0 1 0 1.92 18.79L13 40Z" ' +
        'fill="url(#' + gradId + ')" stroke="' + dark + '" stroke-width="1"/>' +
      '<circle cx="13" cy="13" r="5.5" fill="#fff" stroke="' + dark + '" stroke-width="1"/>' +
      '</svg>';
    return L.divIcon({
      html: svg,
      className: "map-pin",
      iconSize: [19.5, 30.75],
      iconAnchor: [9.75, 30],
      popupAnchor: [0, -27]
    });
  }

  // Formats an ISO date string ("2023-09-01") without going through
  // JavaScript's Date object, which would shift the day depending on the
  // visitor's timezone.
  function formatDate(iso, precision) {
    var parts = iso.split("-");
    var year = parts[0];
    var month = months[parseInt(parts[1], 10) - 1];
    if (precision === "month") {
      return month + " " + year;
    }
    return parseInt(parts[2], 10) + " " + month + " " + year;
  }

  function formatRange(start, end, precision) {
    if (!end) {
      return formatDate(start, precision) + "–Present";
    }
    if (start === end) {
      return formatDate(start, precision);
    }
    return formatDate(start, precision) + "–" + formatDate(end, precision);
  }

  // Build one flat list of "points" out of the three data sources, each
  // with a category used for marker color and a sortKey used to order
  // entries within a location's popup.
  var points = [];

  education.forEach(function (p) {
    if (!p.lat || !p.lon) return;
    points.push({
      lat: p.lat,
      lon: p.lon,
      city: p.location,
      title: p.degree + " in " + p.area + ", " + p.institution,
      url: null,
      date: formatRange(p.start_date, p.end_date, "month"),
      sortKey: p.start_date,
      category: p.status === "current" ? "current-affiliation" : "past-affiliation"
    });
  });

  experience.forEach(function (p) {
    if (!p.lat || !p.lon) return;
    points.push({
      lat: p.lat,
      lon: p.lon,
      city: p.location,
      title: p.position + ", " + p.company,
      url: null,
      date: formatRange(p.start_date, p.end_date, "month"),
      sortKey: p.start_date,
      category: p.status === "current" ? "current-affiliation" : "past-affiliation"
    });
  });

  talks.forEach(function (t) {
    if (!t.lat || !t.lon) return;
    points.push({
      lat: t.lat,
      lon: t.lon,
      city: t.location,
      title: t.name + " — " + t.summary,
      url: null,
      date: formatDate(t.date),
      sortKey: t.date,
      category: t.status === "future" ? "upcoming" : "past-trip"
    });
  });

  activities.forEach(function (a) {
    if (!a.lat || !a.lon) return;
    points.push({
      lat: a.lat,
      lon: a.lon,
      city: a.display_location || a.location,
      title: a.name,
      url: a.url || null,
      date: formatRange(a.start_date, a.end_date, a.precision),
      sortKey: a.start_date,
      category: a.status === "future" ? "upcoming" : "past-trip"
    });
  });

  // Group points by location so that a city with many events (talks,
  // conferences, an affiliation, ...) gets a single marker instead of a
  // pile of overlapping ones.
  var groups = {};
  points.forEach(function (pt) {
    var key = pt.lat + "," + pt.lon;
    if (!groups[key]) {
      groups[key] = { lat: pt.lat, lon: pt.lon, city: pt.city, items: [] };
    }
    groups[key].items.push(pt);
  });

  var map = L.map('map');

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var bounds = [];

  Object.keys(groups).forEach(function (key) {
    var group = groups[key];
    group.items.sort(function (a, b) { return b.sortKey.localeCompare(a.sortKey); });

    var category = priority.filter(function (cat) {
      return group.items.some(function (it) { return it.category === cat; });
    })[0];

    var popupHtml = "<strong>" + group.city + "</strong><ul>";
    group.items.forEach(function (it) {
      var label = it.url ? '<a href="' + it.url + '" class="event-link">' + it.title + "</a>" : it.title;
      popupHtml += "<li>" + label + " (" + it.date + ")</li>";
    });
    popupHtml += "</ul>";

    // Earlier entries in `priority` get a higher zIndexOffset, so their
    // pin is drawn on top when it visually overlaps a lower-priority one.
    var zIndexOffset = (priority.length - priority.indexOf(category)) * 100;

    L.marker([group.lat, group.lon], { icon: pinIcon(colors[category]), zIndexOffset: zIndexOffset })
      .addTo(map)
      .bindPopup(popupHtml);

    bounds.push([group.lat, group.lon]);
  });

  map.fitBounds(bounds, { padding: [20, 20] });
</script>
