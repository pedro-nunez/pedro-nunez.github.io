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

<script>
  // The three data files below carry lat/lon for every entry that should
  // appear on the map (see the comments at the top of each _data file).
  var positions = {{ site.data.positions | jsonify }};
  var talks = {{ site.data.talks | jsonify }};
  var activities = {{ site.data.activities | jsonify }};

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
  var priority = ["current-affiliation", "past-affiliation", "upcoming", "past-trip"];

  var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  // Builds a teardrop-shaped pin icon (like Google Maps) in the given
  // color, as an inline SVG. iconAnchor points at the pin's tip, so it
  // lines up with the actual coordinates instead of its center.
  function pinIcon(color) {
    var svg = '<svg xmlns="http://www.w3.org/2000/svg" width="13" height="19" viewBox="0 0 26 38">' +
      '<path d="M13 0C5.8 0 0 5.8 0 13c0 9.5 13 25 13 25s13-15.5 13-25C26 5.8 20.2 0 13 0z" ' +
      'fill="' + color + '" stroke="#333" stroke-width="1"/>' +
      '<circle cx="13" cy="13" r="5.5" fill="#fff"/></svg>';
    return L.divIcon({
      html: svg,
      className: "map-pin",
      iconSize: [13, 19],
      iconAnchor: [6.5, 19],
      popupAnchor: [0, -17]
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

  positions.forEach(function (p) {
    if (!p.lat || !p.lon) return;
    points.push({
      lat: p.lat,
      lon: p.lon,
      city: p.city,
      title: p.role + ", " + p.institution,
      url: null,
      date: formatRange(p.start, p.end, "month"),
      sortKey: p.start,
      category: p.status === "current" ? "current-affiliation" : "past-affiliation"
    });
  });

  talks.forEach(function (t) {
    if (!t.lat || !t.lon) return;
    points.push({
      lat: t.lat,
      lon: t.lon,
      city: t.city,
      title: t.title + " — " + t.event,
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
      city: a.city,
      title: a.title,
      url: a.url || null,
      date: formatRange(a.start, a.end, a.precision),
      sortKey: a.start,
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
      var label = it.url ? '<a href="' + it.url + '">' + it.title + "</a>" : it.title;
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
