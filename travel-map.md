---
layout: default
title: Travel Map
permalink: /travel-map/
extra_head: leaflet
---

<h1>Travel Map</h1>

<div id="map"></div>

<script>
  var map = L.map('map').setView([20, 10], 2);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
</script>
